from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

class Login(TemplateView):
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=email, password=password)
        if user is not None:
            print("sdfsd")
            request.session["user_id"] = user.id
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('login')

    template_name = "social/login.html"

class Register(TemplateView):
    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        return HttpResponseRedirect('login')	

class Home(View):
    def get(self, request):
        if "user_id" not in request.session:
            return HttpResponseRedirect('login')

        # Get all users list except self , render it
        # Get all the post of followed users
        
        return HttpResponse("asdfsd")

class Logout(View):
    def get(self, request):
        try:
            del request.session["user_id"]
            return HttpResponseRedirect("login")
        except KeyError:
            pass
        return HttpResponseRedirect("")
# class CreateView(View):
# 	def get(self, request):
# 		s = "{'key':'value'}"
# 		url = pyqrcode.create(s)
# 		buffer = io.BytesIO()
# 		url.svg(buffer, scale=10)
# 		return HttpResponse(buffer.getvalue())

# class ScanView(TemplateView):
# 	def post(self, request, *args, **kwargs):
# 		return HttpResponse(f"{request.POST['fname']} {request.POST['lname']}")


# 	template_name = "attendance/index.html"

