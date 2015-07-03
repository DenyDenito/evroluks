from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'email', 'name', 'date_execution', 'address', 'message']
        widgets = {
            'phone': forms.TextInput(attrs={"class": "form-control", 'placeholder': u'Номер телефона...'}),
            'email': forms.TextInput(
                attrs={"class": "form-control", "placeholder": u'Адрес электронной почты...'}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": u'Фамилия Имя Отчество...'}),
            'date_execution': forms.DateTimeInput(attrs={"class": "form-control", "placeholder": u'Удобное время...'}),
            'address': forms.TextInput(
                attrs={"class": "form-control textsend", "placeholder": u'Адрес...'}),
            'message': forms.Textarea(attrs={"class": "form-control", "placeholder": u'Объект чистки...'}),
        }
