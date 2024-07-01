#!/usr/bin/env python

"""Simple Example for Smart Flows"""

import argparse
from pprint import pprint

from gladier import FlowsManager, GladierBaseClient, generate_flow_definition
from tools.produce_event import Diaspora_Produce_Event
from tools.consume_event import Diaspora_Consume_Event 

@generate_flow_definition()
class Diaspora_Example_Client(GladierBaseClient):
    """"""

    gladier_tools = [Diaspora_Produce_Event]



def run_flow(**kwargs):
    """"""
    exampleClient = Diaspora_Example_Client()
    exampleClient.get_flow_id()
    exampleClient.login()

    flow_input = {"input": {"topic": "potato", "msgs": "baked"}}
    print("Created payload.")
    pprint(flow_input)
    print("")

    client_run_label = "Smart Flows Example"
    flow_run = exampleClient.run_flow(flow_input=flow_input, label=client_run_label)

    print("Run started with ID: " + flow_run["action_id"])
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
