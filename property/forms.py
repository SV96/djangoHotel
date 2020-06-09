from django import forms

from .models import Reserver,Property


class ReserverForm(forms.ModelForm):
    class Meta:
        model = Reserver
        fields = '__all__'
    property = forms.ModelChoiceField(queryset=Property.objects.all())
