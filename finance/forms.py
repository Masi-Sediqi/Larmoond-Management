from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django import forms
from .models import Income, Expense
from django import forms
from .models import Income


class IncomeForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = Income
        fields = ["title", "source", "amount", "currency", "date", "note"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": ""
        })
        self.fields["source"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["amount"].widget.attrs.update({
            "class": "form-control",
            "step": "0.01"
        })
        self.fields["currency"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["note"].widget.attrs.update({
            "class": "form-control",
            "rows": "3"
        })


class ExpenceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = Expense
        fields = ["title", "category", "amount", "currency", "date", "note"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": ""
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["amount"].widget.attrs.update({
            "class": "form-control",
            "step": "0.01"
        })
        self.fields["currency"].widget.attrs.update({
            "class": "form-select"
        })
        self.fields["note"].widget.attrs.update({
            "class": "form-control",
            "rows": "3"
        })