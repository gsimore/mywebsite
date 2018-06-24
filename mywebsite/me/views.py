from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import Person, Resume


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        gabby = Person.objects.get(first_name='Gabrielle')
        context['gabby'] = gabby
        resume = Resume.objects.get(person=gabby)
        context['experiences'] = resume.experiences.order_by('start_date')

        return context
