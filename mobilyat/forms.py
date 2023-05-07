from django import forms
from django_select2.forms import Select2Widget
from .models import SaleInvoice


class SaleInvoiceForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = '__all__'
        widgets = {
            'customer_name': Select2Widget,
        }
