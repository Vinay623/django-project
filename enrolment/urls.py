from django.urls import path
from .views import (
    DashboardView,
    StudentListView,
    CourseListView,
    EnrolmentListView,
    EnrolmentCreateView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("enrolments/", EnrolmentListView.as_view(), name="enrolment-list"),
    path("enrolments/new/", EnrolmentCreateView.as_view(), name="enrolment-create"),
]