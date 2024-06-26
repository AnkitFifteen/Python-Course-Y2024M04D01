"""
URL configuration for StudentsManagementProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from StudentsManagementApp.views import ViewStudents, RegisterStudent, UpdateStudent, DeleteStudent


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ViewStudents.as_view(), name = "ViewStudents"),
    path("show-students/", ViewStudents.as_view(), name = "ViewStudents"),
    path("register-student/", RegisterStudent.as_view(), name = "RegisterStudent"),
    path("update-student/<int:pk>/", UpdateStudent.as_view(), name = "UpdateStudent"),
    path("delete-student/<int:pk>/", DeleteStudent.as_view(), name = "DeleteStudent"),
]
