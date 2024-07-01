"""Gather Metadata for publish tool"""

from gladier import GladierBaseTool, generate_flow_definition


def gather_metadata(wfile=None, text=None, **data):
    """python function for gather metadata"""
    import os

    if "~" in wfile:
        wfile = os.path.expanduser(wfile)

    with open(wfile, "w+") as file1:
        file1.writelines(text)

    return wfile


@generate_flow_definition
class GatherMetadata(GladierBaseTool):
    """gladier Tool for gather metadata"""

    compute_functions = [gather_metadata]
    required_input = ["wfile", "name", "compute_endpoint"]
