from django import forms
from .models import UserForm
class UserFormModel(forms.ModelForm):
    class Meta:
        model=UserForm
        fields=['name','email','phone','profile']