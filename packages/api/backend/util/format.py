# -*- coding: utf-8 -*-


def msg_from_list(title: str,
                  items: list,
                  template: str = ' {index}. {item}') -> str:
    """
    Build a nice formatted message from a list of items.

    :param title: main text in the message
    :param items: list of messages
    :template: default template applied to each item
    """

    message_list = [title]
    for index, item in enumerate(items):
        item_msg = template.format(index=index + 1, item=item)
        message_list.append(item_msg)
    return '\n'.join(message_list)
