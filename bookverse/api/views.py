from rest_framework import generics, mixins, permissions

from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        """
        Define different permissions for GET and POST requests.
        - Allow anyone for GET (no authentication required).
        - Require authentication for POST (creating an author).
        """
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]  # Auth required for POST
        return []  # No auth required for GET

    def get(self, request, *args, **kwargs):
        # Handle GET request (List Authors)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle POST request (Create an Author)
        return self.create(request, *args, **kwargs)


class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "id"

    def get_permissions(self):
        """
        Define different permissions for GET and POST requests.
        - Allow anyone for GET (no authentication required).
        - Require authentication for POST (creating an author).
        """
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return []  # No auth required for GET
