from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import StudentSerializer, StudentOtherSerializer, RandomUserSerializer
from api.models import Student, RandomUser
from django.views.generic import TemplateView
from api.forms import StudentForm
from django.shortcuts import redirect
# Create your views here.


class StudentView(APIView):
    def get(self, request, format=None):
        students = Student.student_object.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentOtherSerializer(data=request.data)
        if serializer.is_valid():
            student = Student(**serializer.data)
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentUi(TemplateView):
    template_name = 'student/studentfile.html'
    form_class = StudentForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('student')
        return super(StudentUi,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Student.student_object.filter(name__contains='emre')

    def get_context_data(self, *args, **kwargs):
        context = super(StudentUi, self).get_context_data(*args, **kwargs)
        context['test'] = self.get_queryset()
        context['data'] = self.form_class()
        return context


class RandomUserView(APIView):

    def get(self, request, format=None):

        users = RandomUser.user_obj.all()
        serializer = RandomUserSerializer(users, many=True)
        return Response(serializer.data)
