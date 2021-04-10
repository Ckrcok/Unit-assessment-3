from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WidgetForm
from .models import Widget
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    widget_form = WidgetForm()
    total = 0
    widgets = Widget.objects.all()
    for widget in widgets:
        total += widget.quantity
    return render(request, 'index.html', {
        'wacky_form': widget_form,
        'widget_list': widgets,
        'total': total
        })
class WidgetCreate(CreateView):
    model = Widget
    fields = ['description', 'quantity']
    success_url = '/'

def DeleteWidget(request, pk):
  widget = Widget.objects.get(id=pk)
  widget.delete()
  return redirect('home')
