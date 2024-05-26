# from django.urls import path
# from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView


# urlpatterns = [
#     path('clients/', ClientListView.as_view(), name='client_list'),
#     path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
#     path('clients/create/', ClientCreateView.as_view(), name='client_create'),
#     path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
#     path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
# ]
from django.urls import path

from django.contrib.auth.views import LogoutView

from .views import SignUpView, CustomLoginView 

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]