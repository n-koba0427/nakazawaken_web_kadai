from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import TokoModel, TokoModel2, Course
from django.urls import reverse_lazy, reverse
from django.db.models import Q

class CourseList(ListView):
    template_name = 'courses.html'
    model = Course
    def get_queryset(self):
        q_word = self.request.GET.get('s')
 
        if q_word:
            object_list = Course.objects.filter(
                Q(name__icontains=q_word) | Q(id__icontains=q_word))
        else:
            object_list = Course.objects.all()
        return object_list

class CourseCreate(CreateView):
    template_name = 'course_create.html'
    model = Course
    fields = ('name',)
    success_url = reverse_lazy('courses')

class TokoList(ListView):
    template_name = 'all_list.html'
    model = TokoModel2

    def get(self, request, *args, **kwargs):
        c = self.kwargs['c']
        if c:
            object_list = self.model.objects.filter(
                Q(course__id__icontains=c))
        else:
            object_list = self.model.objects.all()

        context = locals()
        context = {
            'key': c,
            'object_list': object_list
            }
        return render(request, self.template_name, context)

class TokoCreate(CreateView):
    template_name = 'create.html'
    model = TokoModel2
    fields = ('content','course',)
    def get_form(self):
        form = super(TokoCreate, self).get_form()
        key = self.kwargs['c'] or '1'
        form.initial['course']= key
        return form
    def get_success_url(self):
        return reverse('all_list', kwargs={'c': self.kwargs['c']})

class Sample(ListView):
    template_name = 'sample.html'
    model = TokoModel

class Map(ListView):
    template_name = 'map.html'
    model = TokoModel