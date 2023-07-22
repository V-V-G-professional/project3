from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', AnimalsHome.as_view(), name='home'),
    path('category', AnimalsCategory.as_view(), name='сategory'),
    path('about/', About.as_view(), name='about'),
    path('addpage/', AnimalsAddPage.as_view(), name='addpage'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', AnimalsShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AnimalsShowCategory.as_view(), name='category'),


]