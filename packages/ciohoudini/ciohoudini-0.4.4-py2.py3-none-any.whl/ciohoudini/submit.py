"""Handle button presses to submit and test jobs.

preview: Open a window displaying the structure of the submission and
the JSON objects that will be sent to Conductor.

submit: Send jobs to Conductor
"""
import os
import traceback

import hou

from ciohoudini import payload
from contextlib import contextmanager
from ciocore import conductor_submit
from ciohoudini.submission_dialog import SubmissionDialog
SUCCESS_CODES = [201, 204]


@contextmanager
def saved_scene(node=None):
    """Do stuff in the context of a saved scene.
    
    If scene is modified, or always-autosave is on, or user wants to embed HDAs, then save the scene.
    Otherwise there's no need to save. 
    Always yield a fiulename.
    """
    current_scene_name = hou.hipFile.name()
    always_use_autosave = node and node.parm("use_autosave").eval()
    modified = hou.hipFile.hasUnsavedChanges()
    should_embed_hdas = node and node.parm("embed_hdas").eval()
    orig_embed_hdas_val =_get_save_op_defs()

    try:
        fn = None 
        
        if modified or always_use_autosave or should_embed_hdas:
            if should_embed_hdas:
                _set_save_op_defs(True)
            fn = node.parm("autosave_scene").eval()
            hou.hipFile.save(file_name=fn, save_to_recent_files=False)
        else:
            fn = hou.hipFile.path()
            # findFile will raise if the current file was deleted or something
            hou.findFile(fn)
        yield fn
    finally:
        _set_save_op_defs(orig_embed_hdas_val)
        hou.hipFile.setName(current_scene_name)


def _get_save_op_defs():
    """GETTER: embed_hdas is a global setting and only available through hscript AFAICT."""
    otconfig =  hou.hscript("otconfig")
    result = next(f for f in otconfig[0].split("\n") if f.startswith("Save Operator Definitions"))
    result = result.split(":")[1].strip()
    return True if result == "true" else False

def _set_save_op_defs(state):
    """SETTER: embed_hdas."""
    val = 1 if state else 0
    hou.hscript("otconfig -s {}".format(val))

def invoke_submission_dialog(*nodes, **kwargs):
    """
    Execute the modal submission dialog givebn nodes.
    """

    submission_dialog = SubmissionDialog(nodes)
    hou.session.conductor_validation = submission_dialog
    result = submission_dialog.exec_()
    
# If there is more than one node, don't provide any nodes to the save function, thereby ignoring autosave.
def run(*nodes):
    """Submit the given node."""
    
    result = []
    if not nodes:
        return result
    first_node = nodes[0]
    with saved_scene(first_node) as fn:
        if not fn:
            return result

        # Now we know all nodes are valid and the scene has been saved 
        return [ submit_one(node) for node in nodes ]


def get_submission_payload(node):
    """Get the submission payload for the given node."""
    kwargs = {}
    kwargs["do_asset_scan"] = True
    kwargs["task_limit"] = -1
    submission_payload = payload.resolve_payload(node, **kwargs)
    return submission_payload

def submit_one(node):
    try:
        payload = get_submission_payload(node)
        remote_job = conductor_submit.Submit(payload)
        response, response_code = remote_job.main()
    except:
        response = traceback.format_exc()
        response_code = 500
    return {"response": response, "response_code": response_code, "node": node}
 