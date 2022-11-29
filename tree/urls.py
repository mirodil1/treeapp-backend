from django.urls import path

from .views import (
    TreeListApiView, TreeDetailApiView,
    UsersTree
)

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("trees/", TreeListApiView.as_view()),
    path("tree/<int:id>/", TreeDetailApiView.as_view()),
    path("user/trees/", UsersTree.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)