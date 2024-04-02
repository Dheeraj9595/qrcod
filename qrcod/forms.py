# forms.py

from django import forms

class QRCodeForm(forms.Form):
    data = forms.CharField(label='Data', max_length=1000)
    body = forms.ChoiceField(label='Body', choices=[('square', 'Square'), ('circle', 'Circle')])
    size = forms.IntegerField(label='Size')
    download = forms.BooleanField(label='Download', required=False)
    file = forms.ChoiceField(label='File Type', choices=[('png', 'PNG'), ('svg', 'SVG')])