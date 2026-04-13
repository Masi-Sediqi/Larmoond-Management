from django import forms

from .models import Domain, Server


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = [
            'domain_name',
            'client',
            'price',
            'status',
            'start_date',
            'end_date',
            'registrar',
            'dns_provider',
            'notes',
        ]
    
        widgets = {
            'domain_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'registrar': forms.TextInput(attrs={'class': 'form-control'}),
            'dns_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError("End date cannot be earlier than start date.")
        return cleaned_data


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = [
            'server_name',
            'status',
            'price',
            'start_date',
            'end_date',
            'cpu_cores',
            'ram_gb',
            'storage_gb',
            'bandwidth_tb',
            'ip_address',
            'provider',
            'operating_system',
            'notes',
        ]
        widgets = {
            'server_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cpu_cores': forms.NumberInput(attrs={'class': 'form-control'}),
            'ram_gb': forms.NumberInput(attrs={'class': 'form-control'}),
            'storage_gb': forms.NumberInput(attrs={'class': 'form-control'}),
            'bandwidth_tb': forms.NumberInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'provider': forms.TextInput(attrs={'class': 'form-control'}),
            'operating_system': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError("End date cannot be earlier than start date.")
        return cleaned_data