"""Example of a simple function"""

from gladier import GladierBaseTool, generate_flow_definition


def sleep(**data):
    ''''''
    import sleep # noqa
    t = data.get('wait_time',0.5)
    sleep.sleep(t)
    return




@generate_flow_definition
class SimpleTool(GladierBaseTool):
    """Simple Gladier tool"""

    compute_functions = [sleep]
    required_input = ["compute_endpoint"]
