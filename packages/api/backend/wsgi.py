# -*- coding: utf-8 -*-

from backend.event import register_availables
from eve import Eve


# instantiate main application object
app = Eve()

# apply event hooks to the app
register_availables(app)
