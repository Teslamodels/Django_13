from django.urls import path
from .views import Id, name, name2, age

urlpatterns = [
    path('', Id, name='id'),
    path("Id/<int:id>", Id, name='Id2'),
    path('name/', name, name='name'), 
    path("name/<str:name>/", name, name='name2'), 
    path('name2/', name2, name='name3'), 
    path('name2/<str:name>/', name2, name='name4'),
    path('age/', age, name='age'),
    path('age/<int:age>/', age, name='age2'),
]
