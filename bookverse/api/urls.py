from django.urls import path

from . import views

urlpatterns = [
    path("authors/", views.AuthorListCreateView.as_view(), name="authors-list-create"),
    path(
        "authors/<int:id>/",
        views.AuthorRetrieveUpdateDeleteView.as_view(),
        name="author-detail-update-delete",
    ),
]
