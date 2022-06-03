from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from first_lab.forms import RegisterForm
from bot_directory.start_bot import send_message_to_admin
from django.http import Http404
from .models import BlogModel, CommentModel
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect


def index(request):
    data = {'title': 'CityForum'}
    return render(request, "first_lab/index.html", context=data)


def info(request):
    data = {'title': 'About Us'}
    return render(request, "first_lab/info.html", context=data)


def register(request):
    data = {'title': 'Register'}
    return render(request, "first_lab/register.html", context=data)

def LocalStorage1(request):
    data = {'title': 'LocalStorage1'}
    return render(request, "first_lab/page-1.html", context=data)

def LocalStorage2(request):
    data = {'title': 'LocalStorage2'}
    return render(request, "first_lab/page-2.html", context=data)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'first_lab/register.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user_email = form.cleaned_data.get("email")
            send_message_to_admin(f"Добавлена запись о новом пользователе\n"
                                  f"Логин: {username}\n"
                                  f"Почта: {user_email}")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def contact_form(request):
    form = ContactForm()
    if request.method == "POST" and is_ajax(request=request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "first_lab/contact.html", {"form": form})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def test(request):
    return render(request, "first_lab/recipe_book.html")

def BlogListView(request):
    dataset = BlogModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogModel.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, 'first_lab/listview.html', context)


def BlogDetailView(request, _id):
    try:
        data = BlogModel.objects.get(id=_id)
        comments = CommentModel.objects.filter(blog=data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name=form.cleaned_data['your_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   blog=data)
            Comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'first_lab/detailview.html', context)