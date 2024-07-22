"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def getSystemInfo(**data):
    """"""
    import platform
    result = {"info": list(platform.uname())}
    return result


@generate_flow_definition
class SysInfoTool(GladierBaseTool):
    """Simple Gladier tool"""

    compute_functions = [getSystemInfo]
    required_input = ["compute_endpoint"]
