from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'<int:ifsc>', views.BranchDetailView)

urlpatterns = [
    path('<ifsc>/', views.BranchDetailView.as_view(), name='branch-detail'),
    path('<bank>/<city>/', views.BranchListView.as_view(), name='branch-lists')
]
