from django import forms
from trabalho3.models.bill import Bill


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"
