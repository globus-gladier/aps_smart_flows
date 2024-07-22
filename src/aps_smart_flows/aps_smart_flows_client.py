#!/usr/bin/env python

"""Simple Example for Smart Flows"""

import uuid
from pprint import pprint

from diaspora_event_sdk import Client as DiasporaGlobusClient
from gladier import GladierBaseClient, generate_flow_definition
from tools.consume_event import Diaspora_Consume_Event
from tools.produce_event import Diaspora_Produce_Event
from tools.sleep_tool import SleepTool
from tools.sys_info_tool import SysInfoTool

##EDIT HERE
TOPIC_NAME = "aps_smart_flow"
GLOBUS_GROUP = "0bbe98ef-de8f-11eb-9e93-3db9c47b68ba"
LOCAL_COMPUTE = "36d0b3c2-47a8-4465-8742-8296dc266b0b"
##
@generate_flow_definition()
class ProduceClient(GladierBaseClient):
    """"""

    globus_group = GLOBUS_GROUP
    gladier_tools = [SysInfoTool, Diaspora_Produce_Event]


@generate_flow_definition()
class ConsumeClient(GladierBaseClient):
    """"""

    globus_group = GLOBUS_GROUP
    gladier_tools = [SleepTool, Diaspora_Consume_Event]


def generate_unique_key():
    """"""
    return str(uuid.uuid4())


def run_flow(**kwargs):
    """"""
    ClientFlow1 = ProduceClient()
    ClientFlowConsumer = ConsumeClient()
    ClientDiaspora = DiasporaGlobusClient()
    print(ClientDiaspora.register_topic(TOPIC_NAME))
    print(ClientDiaspora.list_topics())
    print("Topic to produce/consume:", TOPIC_NAME)

    new_key = generate_unique_key()
    flow_input = {
        "input": {
            ##compute bits
            "compute_endpoint": LOCAL_COMPUTE,
            "wait_time": 15,
            "topic": TOPIC_NAME,
            "msgs": [{"smartkey": new_key}],
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
    flow_input["input"]["filters"] = [
        {"Pattern": {"value": {"flow_run_id": [{"prefix": str(trigger_id[0:5])}]}}},
    ]

    ##This flow will wait for all the flows on trigger flows
    flow_run = ClientFlowConsumer.run_flow(
        flow_input=flow_input, label="Smart Flows Consumer: " + new_key[0:5]
    )
    print("https://app.globus.org/runs/" + flow_run["action_id"] + "/logs")


## Main execution of this "file" as a Standalone client
if __name__ == "__main__":
    run_flow()
