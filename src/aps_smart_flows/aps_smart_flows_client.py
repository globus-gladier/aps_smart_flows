#!/usr/bin/env python

"""Simple Example for Smart Flows"""

import uuid
from pprint import pprint

from gladier import GladierBaseClient, generate_flow_definition
from tools.consume_event import Diaspora_Consume_Event
from tools.produce_event import Diaspora_Produce_Event
from tools.sleep_tool import SleepTool
from tools.sys_info_tool import SysInfoTool


@generate_flow_definition(
    #output of  sysinfo >> input of diaspora
)
class ProduceClient(GladierBaseClient):
    """"""

    gladier_tools = [SysInfoTool, Diaspora_Produce_Event]


@generate_flow_definition()
class ConsumeClient(GladierBaseClient):
    """"""

    gladier_tools = [SleepTool, Diaspora_Consume_Event]


def generate_unique_key():
    """"""
    return str(uuid.uuid4())

def create_new_topic():
    """"""
    pass

def create_flow_control_topic():
    """"""
    pass

def run_flow(**kwargs):
    """"""
    ClientFlow1 = ProduceClient()
    ClientFlowConsumer = ConsumeClient()

    new_key = generate_unique_key()
    flow_input = {
        "input": {
            ##compute bits
            "compute_endpoint": "36d0b3c2-47a8-4465-8742-8296dc266b0b",
            "wait_time": 15,
            ##Diaspora bits
            # better way to increase support
            #events = [topic+value+keys] or single
            "topic": "topic7b385f033313",
            "msgs": [{"smartkey": new_key}],
            "filters": [
                {"Pattern": {"value": {"smartkey": [{"prefix": str(new_key[0:5])}]}}},
            ],  ##bug here but it works
            ##
        }
    }

    print("Created payload.")
    pprint(flow_input)
    print("")

    ###Trigger flow
    flow_run = ClientFlow1.run_flow(
        flow_input=flow_input, label="Smart Flows Trigger: " + new_key[0:5]
    )
    print("https://app.globus.org/runs/" + flow_run["action_id"] + "/logs")

    ##Gather list of "trigger flows" for wait
    trigger_id = flow_run["action_id"]

    ##This flow will wait for all the flows on trigger flows
    flow_run = ClientFlowConsumer.run_flow(
        flow_input=flow_input, label="Smart Flows Consumer: " + new_key[0:5]
    )
    print("https://app.globus.org/runs/" + flow_run["action_id"] + "/logs")


## Main execution of this "file" as a Standalone client
if __name__ == "__main__":
    run_flow()
