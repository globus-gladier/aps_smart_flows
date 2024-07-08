"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def getSystemInfo(**data):
    """"""
    import platform, socket, re, uuid, psutil  # noqa
    from copy import deepcopy

    new_data = {}
    new_data["platform"] = platform.system()
    new_data["platform-release"] = platform.release()
    new_data["platform-version"] = platform.version()
    new_data["architecture"] = platform.machine()
    new_data["hostname"] = socket.gethostname()
    new_data["ip-address"] = socket.gethostbyname(socket.gethostname())
    new_data["mac-address"] = ":".join(
        re.findall("..", "%012x" % uuid.getnode())
    )
    new_data["processor"] = platform.processor()
    new_data["ram"] = (
        str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    )

    return new_data


@generate_flow_definition
class SysInfoTool(GladierBaseTool):
    """Simple Gladier tool"""

    compute_functions = [getSystemInfo]
    required_input = ["compute_endpoint"]
