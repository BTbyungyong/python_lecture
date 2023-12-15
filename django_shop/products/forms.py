from django import forms
from .models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=64, label="상품명", error_messages={"required": "상품명을 입력해 주세요"}
    )
    price = forms.IntegerField(
        label="상품가격", error_messages={"required": "상품가격을 입력해 주세요"}
    )
    description = forms.CharField(
        max_length=64, label="상품설명", error_messages={"required": "상품설명을 입력해 주세요"}
    )
    stock = forms.IntegerField(label="재고", error_messages={"required": "재고을 입력해 주세요"})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        price = cleaned_data.get("price")
        description = cleaned_data.get("description")
        stock = cleaned_data.get("stock")

        if not (name and price and description and stock):
            self.add_error("name", "값이 없습니다.")
            self.add_error("price", "값이 없습니다.")
