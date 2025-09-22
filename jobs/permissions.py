from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins or superusers to edit objects.
    """
    def has_permission(self, request, view):
        # Allow read-only access for any request (GET, HEAD, OPTIONS).
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to authenticated users who are either admins or superusers.
        return request.user and request.user.is_authenticated and (request.user.role == 'admin' or request.user.is_superuser)