from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs=({"placeholder": "Логин", "class": "input-field", "id": "username"})))
    email = forms.EmailField(
        widget=forms.TextInput(attrs=({"class": "input-field", "placeholder": "Почта", "id": "e-mail"})))
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs=({"placeholder": "Пароль", "class": "input-field", "id": "password", "type": "password"})))
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs=(
            {"placeholder": "Повторите пароль", "class": "input-field", "id": "repeat-password", "type": "password"})))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(forms.Form):
    your_name = forms.CharField(max_length=20)
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)