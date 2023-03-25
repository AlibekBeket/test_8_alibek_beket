from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from accounts.forms import LoginForm, CustomUserCreationForm, UserNameForm

from feedback.models import Review


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('products_list')


def logout_view(request):
    logout(request)
    return redirect('products_list')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = '/'
    template_name = 'update_password.html'


class UserDetailView(ListView):
    template_name = 'user_detail.html'
    model = Review
    context_object_name = 'reviews'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = get_object_or_404(User, pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=get_object_or_404(User, pk=self.kwargs['pk']))
        return queryset


class UserUpdateView(UpdateView):
    form_class = UserNameForm
    model = User
    success_url = '/'
    template_name = 'update_user.html'
    context_object_name = 'user'
