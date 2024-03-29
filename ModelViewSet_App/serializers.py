from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['empid','empname','email','salary']