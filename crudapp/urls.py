from django.urls import path

from . import views

urlpatterns = [
    path('emp', views.emp),
    path('', views.boot),
    path('show/',views.show, name = 'show'),
    path('signup', views.register_user),
    path('login/', views.login_user, name = 'login'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('logout/', views.logout_user, name='logout'),

]