from eve import Eve


def on_post_testing_res(request, response):
    """
    Called before sending the response back.

    Generally not a good idea to change the response here, just
    react to it.

    :param request: a :class:`~werkzeug.local.LocalProxy`
    :param response: a :class:`~flask.wrappers.Response` 
    """

    data = response.json
    content = data.get('_items', data)
    print(f'we are sending this: {content}')


def update_testing_name(response: dict):
    """
    Called after some data was fetched from database and it is
    going to build a Response.

    Good place to make customizations.

    :param response: a raw response
    """

    items = response['_items']
    for item in items:
        item['name'] += '_ULALA'


def update_specific_item(item: dict):
    """
    Called after one item was fetched from database.

    Good place to make customizations.

    :param item: the item fecthed
    """

    item['name'] += '_SPECIFIC'


def change_item_before_its_created(items: list):
    """
    Called before some items are going to be persisted.
    It is always a list, even if you are inserting just one.

    Good place to make customizations.

    :param items: list of items to be created
    """

    for item in items:
        item['email'] += '@mysuperemail.net'


def notice_a_creation(items: list):
    """
    Called after some items were persisted.

    Changes here are useless, as this is not going
    to be returned to the client.

    :param items: list of items created
    """

    print(f'this items were be created: {items}')


app = Eve()

# hooks
app.on_post_GET_testing += on_post_testing_res

app.on_fetched_resource_testing += update_testing_name
app.on_fetched_item_testing += update_specific_item

app.on_insert_testing += change_item_before_its_created
app.on_inserted_testing += notice_a_creation 
