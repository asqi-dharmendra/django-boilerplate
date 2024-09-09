from django.urls import path,include
from .views import DepartmentViewSet, HelloworldView,EmployeeViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'departments',DepartmentViewSet)
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    path('hello/', HelloworldView.as_view(), name='hello'),
    path('api/',include(router.urls)),
]