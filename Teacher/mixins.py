from django.contrib.auth.mixins import AccessMixin
from Admin.models import Admin_Web

class AdminRequiredMixin(AccessMixin):
    """
    Mixin to restrict access to admin users only.
    Ensures that the logged-in user exists in the Admin_Web model.
    """
    
    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is in the Admin_Web table.
        If the user is not an admin, it redirects them to the no-permission page.
        """
        if not Admin_Web.objects.filter(username=request.user.username).exists():
            return self.handle_no_permission()  # Redirects to login or error page
        
        return super().dispatch(request, *args, **kwargs)