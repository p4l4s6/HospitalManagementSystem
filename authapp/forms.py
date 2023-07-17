from django import forms

from authapp.models import Slot


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'
