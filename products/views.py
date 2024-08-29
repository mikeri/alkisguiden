from alcoprice.settings import MEDIA_ROOT, MEDIA_URL
from django.views.generic import ListView
from products import models
from random import choice
import os


class OverviewView(ListView):
    model = models.Product
    paginate_by = 100
    ordering = "alcohol_litre_price"

    def get_context_data(self, *args, **kwargs):
        self.request.session["sort"] = "alcohol_litre_price"
        self.request.session["types"] = "all"
        logo_dir = MEDIA_ROOT + "/logos"
        logos = [img for img in os.listdir(logo_dir) if img.endswith(".webp")]
        logo_url = MEDIA_URL  + "logos/" + choice(logos)
        context = super().get_context_data(*args, **kwargs)
        context["logo_url"] = logo_url
        context["subtitle"] = choice(models.Slogan.objects.all())
        context["product_types"] = models.ProductType.objects.all().order_by("name")
        return context


class TableView(ListView):
    template_name = "products/product_table.html"
    model = models.Product
    paginate_by = 100

    def handle_attr(self, attr, default):
        if attr == "types":
            selected_types = filter(lambda p: p.startswith("type-"), self.request.GET.keys())
            query_val = []
            for _type in selected_types:
                query_val.append(int(_type[5:]))
            if not query_val:
                return None
        else:
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
        types = self.handle_attr("types", None)
        queryset = models.Product.objects.all()
        if types:
            queryset = queryset.filter(type_id__in=types)
        return queryset.order_by(ordering)
