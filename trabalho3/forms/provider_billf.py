from django import forms
from trabalho3.models.provider_bill import ProviderBill


class ProviderBillForm(forms.ModelForm):
    class Meta:
        model = ProviderBill
        fields = "__all__"
