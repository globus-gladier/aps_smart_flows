"""Produce Diaspora Event gladier tool"""

from gladier import GladierBaseTool


class Diaspora_Produce_Event(GladierBaseTool):
    """"""

    flow_definition = {
        "Comment": "Publish messages to Diaspora Event Fabric",
        "StartAt": "MergeResult",
        "States": {
            "MergeResult":{
                "Comment": "This adds custom result to the message",
                "Type": "Pass",
                "Result" : {
                    "sys_info": "$.Getsysteminfo.details.result[0]",
                },
                "ResultPath": "$.msgs[0]",
                "Next": "GatherFlowInfo",
            },
            "GatherFlowInfo":{
                "Type": "Pass",
                "Result": {
                    "flow_run_id": "$._context.run_id"
                },
                "ResultPath": "$.msgs[0]",
                "Next": "PublishMessages",
            },
            "PublishMessages": {
                "Comment": "Send messages to a specified topic in Diaspora",
                "Type": "Action",
                "ActionUrl": "https://diaspora-action-provider.ml22sevubfnks.us-east-1.cs.amazonlightsail.com/",
                "Parameters": {
                    "action": "produce",
                    "topic.$": "$.input.topic",
                    "msgs.$": "$.input.msgs",
                },
                "ResultPath": "$.PublishMessages",
                "End": True,
            },
        },
    }

    required_input = ["topic", "msgs"]

    flow_input = {}
