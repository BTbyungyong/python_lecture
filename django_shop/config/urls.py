from django.contrib import admin
from django.urls import path, include

from users import views as user_view
from products import views as product_view
from orders import views as order_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", user_view.index),
    path("register/", user_view.RegisterView.as_view()),
    path("login/", user_view.LoginView.as_view()),
    path("logout/", user_view.logout),
    path("products/", product_view.ProductListView.as_view()),
    path("products/create/", product_view.ProductCreateView.as_view()),
    path("products/detail/<int:pk>/", product_view.ProductDetailView.as_view()),
    path("order/", order_view.OrderList.as_view()),
    path("order/create/", order_view.OrderCreateView.as_view()),
    path("api/product/", product_view.ProductListApi.as_view()),
    path("api/product/<int:pk>/", product_view.ProductDetailApi.as_view()),
]
