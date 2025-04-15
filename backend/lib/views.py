from rest_framework import viewsets, status
from rest_framework.response import Response

class BaseView(viewsets.ModelViewSet):
    model = None
    queryset = None
    filter_backends = []
    view_serializer = {
        'list': None,  # To be defined in each ViewSet as needed
        'create': None,  # To be defined in each ViewSet as needed
        'update': None,  # To be defined in each ViewSet as needed
        'partial_update': None,  # To be defined in each ViewSet as needed
        'view': None,  # To be defined in each ViewSet as needed
    }
    http_method_names = ['get', 'post']

    def get_serializer_context(self):
        pass

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on the action.
        """
        # If the action exists in the view_serializer dictionary, use that
        if self.action in self.view_serializer and self.view_serializer[self.action]:
            return self.view_serializer[self.action]

        # If no specific serializer for the action, return the default serializer
        return super().get_serializer_class()

    def handle_exception(self, exc):
        # Customize exception handling if needed
        return super().handle_exception(exc)

    def perform_create(self, serializer):
        """
        Save the object and return the response.
        Override this method to perform custom actions before saving.
        """

        serializer.save()

    def perform_update(self, serializer):
        """
        Save the object and return the response.
        Override this method to perform custom actions before saving.
        """
        serializer.save()