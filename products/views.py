from django.views.generic import ListView
from products import models
from random import choice


class OverviewView(ListView):
    model = models.Product
    paginate_by = 100
    ordering = "alcohol_litre_price"

    def get_context_data(self, *args, **kwargs):
        self.request.session["sort"] = "alcohol_litre_price"
        self.request.session["types"] = "all"
        context = super().get_context_data(*args, **kwargs)
        context["subtitle"] = choice(models.Slogan.objects.all())
        context["product_types"] = models.ProductType.objects.all().order_by("name")
        return context


class TableView(ListView):
    template_name = "products/product_table.html"
    model = models.Product
    paginate_by = 100

    def handle_attr(self, attr, default):
        query_val = self.request.GET.get(attr)
        session_val = self.request.session.get(attr)
        if attr == "sort" and query_val == session_val is not None:
            query_val = "-" + query_val
        if query_val:
            self.request.session[attr] = query_val
            return query_val
        if session_val:
            return session_val
        return default

    def get_queryset(self):
        ordering = self.handle_attr("sort", "alcohol_litre_price")
        types_query = self.handle_attr("types", None)
        queryset = models.Product.objects.all()
        if types_query and types_query != "all":
            types = types_query.split(",")
            types.remove("")
            queryset = queryset.filter(type_id__in=types)
        return queryset.order_by(ordering)
