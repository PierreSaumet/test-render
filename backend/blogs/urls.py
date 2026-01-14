from django.urls import include, path
from rest_framework import routers

# import everything from views
from blogs.views import BlogsViewSet

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'blogs', BlogsViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls))
]