from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from . import forms

from authapp.models import Slot


# Create your views here.

class Homeview(TemplateView):
    template_name = 'dashboard.html'


class SlotListView(ListView):
    queryset = Slot.objects.all()
    template_name = 'slot_list.html'


class SlotAddView(CreateView):
    queryset = Slot.objects.all()
    template_name = 'add_slot.html'
    form_class = forms.SlotForm
    success_url = '/auth/slot/'


class SlotUpdateView(UpdateView):
    queryset = Slot.objects.all()
    template_name = 'add_slot.html'
    form_class = forms.SlotForm
    success_url = '/auth/slot/'


class SlotDeleteView(View):

    def get(self, request, object_id):
        slot = Slot.objects.get(id=object_id)
        slot.delete()
        return redirect('/auth/slot/')
