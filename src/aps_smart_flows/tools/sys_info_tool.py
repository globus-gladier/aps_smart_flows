"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def getSystemInfo(**data):
    """"""
    import platform, socket, re, uuid, psutil  # noqa
    from copy import deepcopy

    new_data = deepcopy(data)
    new_data["msgs"][0]["platform"] = platform.system()
    new_data["msgs"][0]["platform-release"] = platform.release()
    new_data["msgs"][0]["platform-version"] = platform.version()
    new_data["msgs"][0]["architecture"] = platform.machine()
    new_data["msgs"][0]["hostname"] = socket.gethostname()
    new_data["msgs"][0]["ip-address"] = socket.gethostbyname(socket.gethostname())
    new_data["msgs"][0]["mac-address"] = ":".join(
        re.findall("..", "%012x" % uuid.getnode())
    )
    new_data["msgs"][0]["processor"] = platform.processor()
    new_data["msgs"][0]["ram"] = (
        str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    )

    return new_data


@generate_flow_definition
class SysInfoTool(GladierBaseTool):
    """Simple Gladier tool"""

    compute_functions = [getSystemInfo]
    required_input = ["compute_endpoint"]
