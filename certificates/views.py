from django.shortcuts import render
from .forms import CertificateForm
from .models import Certificate, Teacher, Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

def generate_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)
    return str(refresh), str(access)


def generate_certificate(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            teacher = form.cleaned_data['teacher']
            student = form.cleaned_data['student']
            certificate = Certificate.objects.create(teacher=teacher, student=student)

            certificate.jwt_token_refresh, certificate.jwt_token_access = generate_jwt_token(request.user)
            certificate.save()

            return render(request, 'certificate_generated.html', {'certificate': certificate})
    else:
        form = CertificateForm()
    context = {
        'form': form,
        'teachers': teachers,
        'students': students,
    }

    return render(request, 'generate_certificate.html', context)

@api_view(['POST'])
def verify_certificate(request):
    jwt_token_access = request.data.get('jwt_token_acess')

    if not jwt_token_access:
        return Response({'error': 'JWT token is required for verification.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        access_token = AccessToken(jwt_token_access)
        certificate = Certificate.objects.filter(
            jwt_token_access = access_token
        ).first()

        if certificate:
            return Response({'message': 'Certificate is valid.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Certificate not found or not valid.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
