from django import forms
from trabalho3.models.provider import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = "__all__"
