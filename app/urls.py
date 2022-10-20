# ******* STEP-3 *******
# HERE WE HAVE CREATED NEW URLS.PY FILE IN OUR APPLICATION FOLDER


from django.urls import path,include

# HERE WE ARE IMPORTING VIEWS
from . import views

urlpatterns = [
    path("",views.SignUpPage,name="signuppage"),
    path("signup/",views.SignUpRequest,name="signup"),
    path("login/",views.Loginpage,name="login"),
    path("loginuser/",views.Loginuser,name="loginuser"),
    path("home/",views.Homepage,name="homepage"),
    path("contact/",views.Contactus,name="contact"),
]   