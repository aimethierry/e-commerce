from django.conf.urls import  url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
 ProductDetailView,
 ProductListView,
 VariationListView,
)


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name="product_list"),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'), # /tweet/1/update/
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
]
