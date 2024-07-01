from gladier import GladierBaseTool



class Diaspora_Consume_Event(GladierBaseTool):
    """"""

    flow_definition = {
    'Comment': 'Consume and wait messages to Diaspora Event Fabric',
    'StartAt': 'ConsumeMessages',
    'States': {
        'ConsumeMessages': {
            'Comment': 'reads messages to a specified topic in Diaspora',
            'Type': 'Action',
            'ActionUrl': 'https://diaspora-action-provider.ml22sevubfnks.us-east-1.cs.amazonlightsail.com/',
            'Parameters': {
                'action': 'consume',
                'topic.$': '$.input.topic',
                'keys.$': '$.input.keys',
                'filters.$': '$.input.filters',
            },
            'ResultPath': '$.ConsumeMessages',
            'End': True,
        },
    },
}

    required_input = [
        'topic'
    ]

    flow_input = {

    }
