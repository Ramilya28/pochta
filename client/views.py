# from django.shortcuts import render, redirect
# from django.views import View
# from .models import Client

# class ClientListView(View):
#     def get(self, request):
#         clients = Client.objects.all()
#         return render(request, 'client_list.html', {'clients': clients})

# class ClientDetailView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_detail.html', {'client': client})

# class ClientCreateView(View):
#     def get(self, request):
#         return render(request, 'client_create_form.html')

#     def post(self, request):
#         # Обработка данных формы для создания клиента
#         return redirect('client_list')

# class ClientUpdateView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_update_form.html', {'client': client})

#     def post(self, request, pk):
#         # Обработка данных формы для обновления клиента
#         return redirect('client_list')

# class ClientDeleteView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_delete_confirm.html', {'client': client})

#     def post(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         client.delete()
#         return redirect('client_list')

from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'users/signup.html'
    
    form_class = UserCreationForm

    success_url = reverse_lazy('photo:list')


    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        login(self.request, user)

        return to_return
    
class CustomLoginView(LoginView):
    
    template_name = 'users/login.html'