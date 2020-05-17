from django import forms
from trabalho3.models.costumer_bill import CostumerBill


class CostumerBillForm(forms.ModelForm):
    class Meta:
        model = CostumerBill
        fields = "__all__"
