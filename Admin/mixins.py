from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from Admin.models import Admin_Web

class AdminRequiredMixin(AccessMixin):
    """
    A mixin to ensure that the current user is an admin user.

    This class checks if the user is in the Admin_Web table.
    If the user is not found, they will be redirected to a permission error page.
    """
    def dispatch(self, request, *args, **kwargs):
        """
        The dispatch method checks whether the current user is an admin.

        Args:
            request: The HTTP request object.
            *args: Any additional arguments.
            **kwargs: Any keyword arguments.

        Returns:
            A redirect response if the user is not an admin.
            Otherwise, it calls the parent dispatch method to proceed with the normal request handling.
        """
        try:
            # Attempt to retrieve the admin user from the Admin_Web table using their username
            Admin_Web.objects.get(username=request.user.username)
        except Admin_Web.DoesNotExist:
            # If the user is not found, handle the permission error
            return self.handle_no_permission()

        # If the user is found as an admin, proceed with the request
        return super().dispatch(request, *args, **kwargs)
