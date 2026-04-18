from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Student, Course, Enrolment
from .forms import EnrolmentForm


class DashboardView(TemplateView):
    template_name = "enrolment/dashboard.html"


class StudentListView(ListView):
    model = Student
    template_name = "enrolment/student_list.html"
    context_object_name = "students"


class CourseListView(ListView):
    model = Course
    template_name = "enrolment/course_list.html"
    context_object_name = "courses"


class EnrolmentListView(ListView):
    model = Enrolment
    template_name = "enrolment/enrolment_list.html"
    context_object_name = "enrolments"


class EnrolmentCreateView(CreateView):
    model = Enrolment
    form_class = EnrolmentForm
    template_name = "enrolment/enrolment_form.html"
    success_url = reverse_lazy("enrolment-list")