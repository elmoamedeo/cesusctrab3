from django import forms
from trabalho3.models.provider_bill import ProviderBill


class ProviderBillForm(forms.ModelForm):
    class Meta:
        model = ProviderBill
        fields = "__all__"

    def clean(self):
        cleaned_data = super(ProviderBillForm, self).clean()
        self.instance.field = 'quantity'
        return cleaned_data
