from django.urls import path
from .views import TokoList, Sample, Map, TokoCreate, CourseList, CourseCreate

urlpatterns = [
    path('all_list/<int:c>/', TokoList.as_view(), name='all_list'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('create/<int:c>/', TokoCreate.as_view(), name='create'),
    path('courses/create/', CourseCreate.as_view(), name='courses_create'),
    path('sample/', Sample.as_view()),
    path('', Map.as_view(), name='map'),
]