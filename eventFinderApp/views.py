from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.template import RequestContext
from .models import Event


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for index,event in enumerate(self.object_list):
            context[index] = [
                event.categories.all()[:3]
            ]
        for i in context:
            print(context[i])
        return context


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


def account(request):
    return render(request, 'eventFinderApp/account.html')

def createNewEvent(request):
    if request.method == 'POST':
        form = request.POST
        new_event = Event(
            title=form['title'],
            location=form['location'],
            start_time=form['starttime'],
            end_time=form['endtime']
        )
        new_event.save()
        print(new_event.title)
        # return ShowAppsView.as_view()(self.request)
    return render(request, 'eventFinderApp/createEvent.html')