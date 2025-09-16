from rest_framework import viewsets
from .models import Category, Job
from .serializers import CategorySerializer, JobSerializer, JobCreateUpdateSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    
 
    def get_queryset(self):
        queryset = super().get_queryset()
        
        
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__iexact=category)

        
        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)
            
        return queryset

    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return JobCreateUpdateSerializer
        return JobSerializer