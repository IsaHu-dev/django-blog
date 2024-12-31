from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Include the admin path
    path("", include("blog.urls"), name="blog-urls"),  # Include the blog app URLs
]