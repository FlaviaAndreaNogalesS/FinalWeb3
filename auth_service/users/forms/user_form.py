from django import forms
from users.models.user import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }