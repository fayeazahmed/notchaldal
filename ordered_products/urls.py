from django.urls import path
from .views import RetrieveOrderedProductsView

urlpatterns = [
    path('retrieveorder', RetrieveOrderedProductsView.as_view()),
]
