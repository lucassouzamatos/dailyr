#####################################################
#          Configuratin for dailyr Rest API         #
#####################################################

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

testing = {
    'item_title': 'test',

    # index, store
    'resource_methods': ['GET', 'POST'],

    'schema': {
        'name': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 255,
            'required': True,
        },
        'email': {
            'type': 'string',
            'required': True,
            'unique': True,
        }
    }
}

DOMAIN = {
    'testing': testing
}