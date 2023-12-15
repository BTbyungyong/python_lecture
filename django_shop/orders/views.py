from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.db import transaction

from .forms import OrderForm
from .models import Order
from products.models import Product
from users.decorator import login_required
from users.models import User


@method_decorator(login_required, name="dispatch")
class OrderCreateView(FormView):
    form_class = OrderForm
    success_url = "/products/"

    def form_valid(self, form):
        with transaction.atomic():
            product = Product.objects.get(pk=form.data.get("product_id"))
            order = Order(
                quantity=form.data.get("quantity"),
                product=product,
                user=User.objects.get(email=self.request.session.get("user_email")),
            )
            order.save()
            product.stock -= int(form.data.get("quantity"))
            product.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect("/products/detail/" + str(form.data.get("product")) + "/")

    # def get_form_kwargs(self,**kwargs):
    #     kw = super().get_form_kwargs(**kwargs)
    #     kw.update({
    #         'request':self.request
    #     })
    #     return kw


@method_decorator(login_required, name="dispatch")
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = "orders"

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get("user"))
        return queryset
