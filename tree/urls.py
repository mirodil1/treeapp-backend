from django.urls import path

from .views import TreeListApiView, TreeDetailApiView

urlpatterns = [
    path("trees/", TreeListApiView.as_view()),
    path("tree/<int:id>", TreeDetailApiView.as_view()),
]
