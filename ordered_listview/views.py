from collections import OrderedDict

from django.views.generic import ListView


class OrderedListView(ListView):
    allowed_order_by = tuple()
    default_order_by = None
    order_by_attr = 'by'

    def get(self, request, *args, **kwargs):
        by = request.GET.get(self.order_by_attr)
        self.allowed_order_by_dict = OrderedDict(self.allowed_order_by)
        self.order_by = by if by and by.lstrip('-') in self.allowed_order_by_dict else self.default_order_by
        return super(OrderedListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(OrderedListView, self).get_queryset()
        return qs.order_by(self.order_by)

    def get_context_data(self, **kwargs):
        c = super(OrderedListView, self).get_context_data(**kwargs)
        c['order_by_field'] = self.order_by
        c['order_by_fields'] = self.allowed_order_by_dict
        c['order_by_attr'] = self.order_by_attr
        return c
