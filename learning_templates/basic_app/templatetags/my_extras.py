from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')


#register.filter('cut',cut)#1st argument in filter() is the string and 2nd argument is function name
