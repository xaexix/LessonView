from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView

from .models import Stock
from .forms import StockForm


class HomePageView(TemplateView):
    template_name = 'base.html'


class StockListView(ListView):

    model = Stock


class DetailStockView(DetailView):

    model = Stock


class StockFormView(FormView):
    template_name = 'app/stock_form.html'
    form_class = StockForm
    success_url = reverse_lazy('stock_list')

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
