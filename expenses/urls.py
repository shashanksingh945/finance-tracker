from django.urls import path
from .views import home,add_expense,delete_expense,register_view,login_view,logout_view,home,edit_expense,export_csv

urlpatterns=[
    path('',home,name='home'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('add/',add_expense,name='add_expense'),
    path('delete/<int:id>/',delete_expense,name='delete_expense'),
    path('edit/<int:id>/',edit_expense,name='edit_expense'),
    path('export/',export_csv,name='export_csv'),
]