from django.contrib import admin
from django.urls import path
from loginlogout import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignUp,name="signup"),
    path('login/',views.Login,name="login"),
    path('home/',views.HomePage,name="home"),
    path('forgotPassword/',views.forgot_password,name="forgot_password")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)