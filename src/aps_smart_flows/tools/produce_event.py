from gladier import GladierBaseTool



class Diaspora_Produce_Event(GladierBaseTool):
    """"""

    flow_definition = {
    'Comment': 'Publish messages to Diaspora Event Fabric',
    'StartAt': 'PublishMessages',
    'States': {
        'PublishMessages': {
            'Comment': 'Send messages to a specified topic in Diaspora',
            'Type': 'Action',
            'ActionUrl': 'https://diaspora-action-provider.ml22sevubfnks.us-east-1.cs.amazonlightsail.com/',
            'Parameters': {
                'action': 'produce',
                'topic.$': '$.input.topic',
                'keys.$': '$.input.keys',
                'msgs.$': '$.Getsysteminfo.details.result[0]',
            },
            'ResultPath': '$.PublishMessages',
            'End': True,
        },
    },
}

    required_input = [
        'topic',
        'msgs'
    ]

    flow_input = {

    }
