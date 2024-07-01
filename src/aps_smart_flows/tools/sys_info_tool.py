"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def getSystemInfo(**data):
    ''''''
    import platform,socket,re,uuid,json,psutil,logging # noqa
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    except Exception as e:
        logging.exception(e)
    return [{"content":info}]
    content =[]
    for key in info.keys():
        content.append({'content':info[key]})
    return content

@generate_flow_definition
class SysInfoTool(GladierBaseTool):
    """Simple Gladier tool"""

    compute_functions = [getSystemInfo]
    required_input = ["compute_endpoint"]
