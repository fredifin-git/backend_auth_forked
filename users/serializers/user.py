from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CustomUser, StudentProfile
from django.db import transaction
# from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(ModelSerializer):
    # teacher_name =
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'last_login', 'date_joined', 'is_staff', 'role', 'phone', 'first_name', 'last_name')


class StudentProfileSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(required=True)

    class Meta:
        model = StudentProfile
        fields = ('user', 'student_class',)


class CustomRegisterSerializer(RegisterSerializer):
    # role = serializers.role = serializers.CharField(max_length=10, default='Student')
    phone = serializers.CharField(max_length=30)
    birthdate = serializers.DateField()

    # class Meta:
    #     model = CustomUser
    #     fields = ('birthdate', 'classname', 'email', 'phone', 'role', 'teacher')

    # def get_cleaned_data(self):
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password1': self.validated_data.get('password1', ''),
    #         'password2': self.validated_data.get('password2', ''),
    #         'email': self.validated_data.get('email', ''),
    #         'role': self.validated_data.get('role', ''),
    #         'birthday': self.validated_data.get('birthday', ''),
    #         'classname': self.validated_data.get('classname', ''),
    #         'teacher': self.validated_data.get('teacher', ''),
    #     }
    # @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone = self.data.get('phone')
        user.birthdate = self.data.get('birthdate')
        user.save()
        return user

# class CustomRegisterSerializer(RegisterSerializer):
#     role = serializers.role = serializers.CharField(max_length=10, default='Student')
#
#     class Meta:
#         model = CustomUser
#         fields = ('birthdate', 'classname', 'email', 'phone', 'role', 'teacher')
#
#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'password2': self.validated_data.get('password2', ''),
#             'email': self.validated_data.get('email', ''),
#             'role': self.validated_data.get('role', ''),
#             'birthday': self.validated_data.get('birthday', ''),
#             'classname': self.validated_data.get('classname', ''),
#             'teacher': self.validated_data.get('teacher', ''),
#         }
#     def save(self, request):
#         adapter = get_adapter
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         user.save()
#         adapter.save_user(request, user, self)
#         return user
