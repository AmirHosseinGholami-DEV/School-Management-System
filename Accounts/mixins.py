from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from Admin.models import Admin_Web

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is an admin user."""
    
    def dispatch(self, request, *args, **kwargs):
        """
        Check if the user exists in the Admin_Web table.
        If not, redirect to the no-permission handler.
        """
        if not Admin_Web.objects.filter(username=request.user.username).exists():
            return self.handle_no_permission()
        
        return super().dispatch(request, *args, **kwargs)
