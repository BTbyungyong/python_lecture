from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="상품명")
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "상품"
        verbose_name_plural = "상품"