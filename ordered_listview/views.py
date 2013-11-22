from django.db.models import Count
from django.views.generic import ListView

from collections import OrderedDict


class OrderedListView(ListView):
    allowed_order_by = tuple()
    default_order_by = None
    order_by_attr = 'by'
    null_ignore_fields = []

    def get(self, request, *args, **kwargs):
        by = request.GET.get(self.order_by_attr)
        self.allowed_order_by_dict = OrderedDict(self.allowed_order_by)
        self.order_by = by if by and by.lstrip('-') in self.allowed_order_by_dict else self.default_order_by
        return super(OrderedListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(OrderedListView, self).get_queryset()
        field_name = self.order_by.lstrip("-")
        if self.null_ignore_fields == "*" or field_name in self.null_ignore_fields:
            null_field_name = 'null_%s' % field_name
            return qs.annotate(**{null_field_name: Count(field_name)}).order_by("-%s" % null_field_name, self.order_by)
        return qs.order_by(self.order_by)

    def get_context_data(self, **kwargs):
        c = super(OrderedListView, self).get_context_data(**kwargs)
        c['order_by_field'] = self.order_by
        c['order_by_fields'] = self.allowed_order_by_dict
        c['order_by_attr'] = self.order_by_attr
        return c
