"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def sleep(**data):
    """"""
    from time import sleep  # noqa

    t = data.get("wait_time", 0.5)
    sleep(t)
    return


@generate_flow_definition
class SleepTool(GladierBaseTool):
    """Sleep Gladier tool"""

    compute_functions = [sleep]
    required_input = ["compute_endpoint"]
