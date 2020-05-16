from django import forms
from trabalho3.models.costumer import Costumer


class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = "__all__"
