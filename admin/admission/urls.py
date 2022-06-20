from . import views
from django.urls import path 


urlpatterns = [

    path('',views.index,name="index"),
    path('add/' , views.addData , name="addData"),
    path('show/' , views.showData , name="showData"),
    path('edit/<int:id>' , views.editData , name="editData"),
    path('delete/<int:id>' , views.deleteData , name="deleteData"),
    path('update/<int:id>' , views.updateData , name="updateData"),
]