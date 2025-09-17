from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'نام خود را وارد کنید'})
                                , max_length=30,
                                 required=True,
                                 help_text='Optional.' ,
                                 label='name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" , 'palecholder' : 'نام خانوادگی خود را وارد کنید'}),
                                max_length=30,
                                required=True,
                                label='last name')
    email =forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control" }),
                                max_length=30,
                                required=True,
                                label='email')
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" , 'palecholder' : 'نام کاربری مخصوص خود را وارد کنید'}),
                                max_length=30,
                                required=True,
                                label='username')
    # password1 = forms.CharField(label='password 1' , widget=forms.PasswordInput(
    #     attrs= {
    #         'class':"form-control" ,
    #         "name":"password",
    #         'type':'password',
    #         'placeholder':'رمز خود را وارد کنید ',
    #     }))
    # password2 = forms.CharField(label='password 2', widget=forms.PasswordInput(
    #     attrs={
    #         'class': "form-control",
    #         "name": "password",
    #         'type': 'password',
    #         'placeholder': 'رمز خود را وارد کنید '
    #     }
    #     ))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


