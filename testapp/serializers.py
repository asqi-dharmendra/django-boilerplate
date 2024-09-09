from rest_framework import serializers
from .models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    
    class Meta:
        model=Employee
        fields = ['id', 'name', 'address', 'department', 'department_name']