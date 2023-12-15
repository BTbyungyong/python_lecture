from django.db import models


class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, verbose_name="상품"
    )
    quantity = models.IntegerField(verbose_name="수량")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")

    def __str__(self):
        return str(self.user) + " " + str(self.product)

    class Meta:
        db_table = "order"
        verbose_name = "주문"
        verbose_name_plural = "주문"
