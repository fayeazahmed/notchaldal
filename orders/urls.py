from django.urls import path
from .views import CreateOrderView, RetrieveOrderView

urlpatterns = [
    path('create', CreateOrderView.as_view()),
    path('retrieve', RetrieveOrderView.as_view()),
]
