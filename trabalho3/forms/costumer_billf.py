from django import forms
from trabalho3.models.costumer_bill import CostumerBill


class CostumerBillForm(forms.ModelForm):
    class Meta:
        model = CostumerBill
        fields = "__all__"

    def clean(self):
        cleaned_data = super(CostumerBillForm, self).clean()
        self.instance.field = 'quantity'
        return cleaned_data
