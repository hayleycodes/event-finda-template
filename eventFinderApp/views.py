from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()
    
    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related()
        )

    def get_context_data(self, **kwargs):  # WIP
        context = super().get_context_data(**kwargs)
        for index,event in enumerate(self.object_list):
            context[index] = [
                event.categories.all()[:3]
            ]
        # for i in context:
        #     print(context[i])
        return context


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


class AddEventView(generic.CreateView):
    # using the create view we can just give it the variables 
    # as the functionaity is already built in!
    form_class = EventForm
    context_object_name = 'eventform'
    template_name = 'eventFinderApp/createEvent.html'
    success_url = reverse_lazy('eventFinderApp:index')
    # we have to use reverse_lazy so that urls.py can load our class
    # and not get stuck in a recursive loop 


def account(request):
    return render(request, 'eventFinderApp/account.html')



