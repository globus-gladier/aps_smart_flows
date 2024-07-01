#!/usr/bin/env python

"""Simple Example for Smart Flows"""

import argparse
from pprint import pprint
import uuid
from gladier import FlowsManager, GladierBaseClient, generate_flow_definition
from tools.produce_event import Diaspora_Produce_Event
from tools.consume_event import Diaspora_Consume_Event 
from tools.sys_info_tool import SysInfoTool

@generate_flow_definition()
class ProduceClient(GladierBaseClient):
    """"""
    gladier_tools = [SysInfoTool, Diaspora_Produce_Event]

@generate_flow_definition()
class ConsumeClient(GladierBaseClient):
    """"""
    gladier_tools = [Diaspora_Consume_Event]

def generate_unique_key():
    """"""
    return str(uuid.uuid4())

def run_flow(**kwargs):
    """"""
    ClientFlow1 = ProduceClient()
    pprint(ClientFlow1.get_flow_definition())
    ClientFlowConsumer = ConsumeClient()

    new_key = generate_unique_key()
    flow_input = {"input": {
        "topic": "topic7b385f033313",
        "msgs": [],
        "keys": [new_key],
        "filters": [
            {'Pattern': {'key': new_key}}
        ],
        "compute_endpoint":"36d0b3c2-47a8-4465-8742-8296dc266b0b"
        }
    }

    print("Created payload.")
    pprint(flow_input)
    print("")

    flow_run = ClientFlow1.run_flow(flow_input=flow_input, label="Smart Flows Trigger")
    print("https://app.globus.org/runs/" + flow_run["action_id"])

    flow_run = ClientFlowConsumer.run_flow(flow_input=flow_input, label="Smart Flows Consumer")
    print("https://app.globus.org/runs/" + flow_run["action_id"])


##  Arguments for the execution of this file as a stand-alone client
def arg_parse():
    """Argument Parser for Smart Flows"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="User Name", default="Bob")
    return parser.parse_args()


## Main execution of this "file" as a Standalone client
if __name__ == "__main__":
    args = arg_parse()
    run_flow(name=args.name)
