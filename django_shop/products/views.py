from typing import Any
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .models import Product
from .forms import RegisterForm
from .serializer import ProductSerializer
from orders.forms import OrderForm
from users.decorator import admin_required


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


@method_decorator(admin_required, name="dispatch")
class ProductCreateView(FormView):
    form_class = RegisterForm
    template_name = "register_product.html"
    success_url = "/products/"

    def form_valid(self, form: Any) -> HttpResponse:
        product = Product(
            name=form.data.get("name"),
            price=form.data.get("price"),
            description=form.data.get("description"),
            stock=form.data.get("stock"),
        )
        product.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    template_name = "products_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = OrderForm(self.request)
        return context


class ProductListApi(GenericAPIView, ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetailApi(GenericAPIView, RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
