from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.indexPage, name = 'index'),
    path('results/', views.resultsPage, name = 'results'),
    path('book/<str:bk_isbn>/', views.bookPage, name = 'book'),
    path('mostsellers/', views.mostSellersPage, name = 'mostsellers'),
    path('forkids/', views.forKidsPage, name = 'forkids'),
    path('foradults/', views.forAdultsPage, name = 'foradults'),
    path('login/', views.loginPage, name = 'login'),
    path('signup/', views.signupPage, name = 'signup'),
    path('logout/', views.logoutPage, name = 'logout'),
]