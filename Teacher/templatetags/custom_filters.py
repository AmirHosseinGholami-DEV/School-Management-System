from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """ Get an item from dictionary safely (handle None values). """
    if dictionary is not None and key is not None:
        return dictionary.get(key, None) 
    return None
