from django import forms
from .models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone No'}))
    user_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User_type'}))
    hostel_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hostel ID'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone',
            'user_type',
            'hostel_id',
        ]
