from django import template
from django.utils.http import urlencode


register = template.Library()


@register.inclusion_tag('ordered_listview/field.html', takes_context=True)
def order_field(context, field):
    ctx = dict(context=context)
    order_by = field
    if field == context['order_by_field'].lstrip('-'):
        ctx['desc'] = context['order_by_field'].startswith('-')
        ctx['asc'] = not ctx['desc']
        order_by = ("-" if ctx['asc'] else "") + field
    attrs = dict(context['request'].GET.items() + [(context['order_by_attr'], order_by)])
    ctx['url'] = "?" + urlencode(attrs)
    ctx['name'] = context['order_by_fields'][field]
    return ctx
