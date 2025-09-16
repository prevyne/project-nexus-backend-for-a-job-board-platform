from rest_framework import serializers
from .models import Category, Job

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class JobSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company', 'description', 'location', 
            'job_type', 'category', 'posted_at'
        ]

class JobCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title', 'company', 'description', 'location', 
            'job_type', 'category'
        ]