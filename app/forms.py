from django.forms.models import ModelForm

from .models import Stock


class StockForm(ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'
