from django.conf.urls import  url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
 CategoryListView,
 CategoryDetailView
 
)


urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name="category_list"),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    # url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'), # /tweet/1/update/
    # url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
]
