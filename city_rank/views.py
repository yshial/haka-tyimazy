from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import (CityParams,
                     City,
                     Task,
                     Person,
                     Event,
                     Token,
                     ExternalUser,
                     ExternalQuery)

from .forms import (EventCreateForm,
                    TaskCreateForm)


class CityListView(ListView):
    model = City
    context_object_name = "cities"
    template_name = 'main/main.html'

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     if self.request.user.is_authenticated:
    #         print("user is authenticated")
    #     print(self.request.user)

class CityDetailView(DetailView):
    model = City
    context_object_name = 'city'
    template_name = 'main/main_detail.html'


class EventCreateView(CreateView):
    model = Event
    template_name = 'create/event_create.html'
    form_class = EventCreateForm


class TaskCreateView(CreateView):
    model = Task
    template_name = 'create/task_create.html'
    form_class = TaskCreateForm


# class CityCreateView(CreateView):
#     context_object_name = 'city'
#     model = City
#     template_name = 'create/city_create.html'
#     form_class = CityCreateForm

