from django import forms
from django.db import transaction

from .models import Order
from products.models import Product
from users.models import User


class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        res = super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        label="수량", error_messages={"required": "수량을 입력해 주세요"}
    )

    product = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product_id = cleaned_data.get("product")
        user_email = self.request.session.get("user")
        if not (quantity and product_id):
            self.add_error("quantity", "값이 없습니다.")
            self.add_error("product_id", "값이 없습니다.")
