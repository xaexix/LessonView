from django.urls import path

from .views import HomePageView, StockListView, DetailStockView, StockFormView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('stock-list/', StockListView.as_view(), name='stock_list'),
    path('stock/<int:pk>', DetailStockView.as_view(), name='stock_detail'),
    path('add-stock/', StockFormView.as_view(), name='add_stock')
]
