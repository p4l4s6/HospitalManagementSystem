from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview.as_view(), name='home'),
    path('slot/', views.SlotListView.as_view(), name='slot-list'),
    path('slot/add/', views.SlotAddView.as_view(), name='slot-add'),
    path('slot/update/<int:pk>/', views.SlotUpdateView.as_view(), name='slot-update'),
    path('slot/delete/<int:object_id>/', views.SlotDeleteView.as_view(), name='slot-delete'),
]
