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
                "InputPath": "$.Getsysteminfo.details.result[0]",
                "ResultPath": "$.input.msgs[0].sys_info",
                "Next": "GatherFlowInfo",
            },
            "GatherFlowInfo":{
                "Type": "Pass",
                "InputPath": "$._context.run_id",
                "ResultPath": "$.input.msgs[0].flow_run_id",
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
