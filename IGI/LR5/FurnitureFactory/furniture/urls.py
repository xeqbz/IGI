from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PromoCodeListView,
    PromoCodeCreateView,
    PromoCodeUpdateView,
    PromoCodeDeleteView
)

urlpatterns = [
    path('furniture/', views.index, name='home'),
    path('about/', views.about),
    path('news/', views.news),
    path('dictionary/', views.dictionary),
    path('contacts/', views.contacts),
    re_path(r'^privacy_policy/$', views.privacy_policy),
    path('vacancies/', views.vacancies),
    #path('promo_codes/', views.promo_codes),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_view, name='login'),
    path('reviews/', views.review_list, name='review_list'),
    path('products_list/', views.products_list, name='products_list'),
    #path('profile/', views.profile, name='profile'),
    path('superuser_profile/', views.superuser_profile, name='superuser_profile'),
    path('employee_profile/', views.employee_profile, name='employee_profile'),
    path('client_form/', views.client_form, name='client_form'),
    path('client_profile/', views.client_profile, name='client_profile'),
    path('promo_codes/', PromoCodeListView.as_view(), name='promo_codes'),
    path('promo_codes/new/', PromoCodeCreateView.as_view(), name='promo_code_new'),
    path('promo_codes/<int:pk>/edit/', PromoCodeUpdateView.as_view(), name='promo_code_edit'),
    path('promo_codes/<int:pk>/delete/', PromoCodeDeleteView.as_view(), name='promo_code_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

