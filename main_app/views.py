from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import DeleteView

# Create your views here.

def home(request):
    widget_list = Widget.objects.all()
    # instanciate WidgetForm
    widget_form = WidgetForm() 
    return render(request, 'home.html', {
        # render the widget_list and widget_form input in browser via dictionary
        'widget_list': widget_list,
        'widget_form': widget_form
    })

def create_widget(request):
    w_form = WidgetForm(request.POST)
    # save the WidgetForm after validating the form
    if w_form.is_valid():
        w_form.save()
    return redirect('home')

class RemoveWidget(DeleteView):
    model = Widget
    success_url = '/'