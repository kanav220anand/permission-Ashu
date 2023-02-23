from django.contrib import admin
from django.urls import include, path
# from user.views import IndexPageView

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('user.urls'), name='user'),
    
    path('login/', views.loginPage,name = 'login'),
    path('register/', views.register,name = 'register'),
    path('logout/', views.logoutUser,name = 'logout'),

    path('products/', views.ProductPageView.as_view(), name = 'products'),
    path('page2/', views.Page2PageView.as_view(),name = 'page2'),
    path('page3/', views.Page3PageView.as_view(),name = 'page3'),
    path('page4/', views.Page4PageView.as_view(),name = 'page4'),
    path('page5/', views.Page5PageView.as_view(),name = 'page5'),

    path('', views.IndexPageView.as_view(), name='home'),
]
