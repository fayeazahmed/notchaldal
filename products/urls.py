from django.urls import path
from .views import GetProductsView

urlpatterns = [
    path('<category>', GetProductsView.as_view()),
]
