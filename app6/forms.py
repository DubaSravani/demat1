from django import forms

class EdubridgeForm(forms.Form):
    name=forms.CharField(max_length=100)
