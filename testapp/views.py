from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from testapp.models import Department,Employee
from testapp.serializers import DepartmentSerializer,EmployeeSerializer

class HelloworldView(APIView):
    
    def get(self, request):
        return Response({'message': 'Hello, world!'})
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

