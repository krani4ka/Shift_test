from django import forms


class UploadFileForm(forms.Form):
    file = forms.ImageField()
    HEX = forms.CharField()
    HEX.required = False
