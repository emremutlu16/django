from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    mobile_number = forms.IntegerField()
