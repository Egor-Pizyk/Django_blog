from django.template.defaulttags import register


@register.simple_tag
def get_avg(*args):
    rate_values = [item['value'] for item in args[0]]
    return sum(rate_values) / len(rate_values)
