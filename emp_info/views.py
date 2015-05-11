from django.shortcuts import render_to_response,redirect,RequestContext
from .forms import RegForm,EditForm,LoginForm,ChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

#Home Page
def home_view(request):
   return render_to_response('home.html', context_instance=RequestContext(request))

#Registration Page
def index(request):
	if request.method == 'POST':
		form = RegForm(data=request.POST)
		username = request.POST['username']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password =request.POST['password']
		if form.is_valid():
			user = User.objects.create_user(username,email,password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
      			return HttpResponseRedirect('/home/')
 	else:
   		form = RegForm()
	return render_to_response('registration_form.html', {'form': form}, context_instance=RequestContext(request))

#Login Page
def login_view(request):
	if request.user and request.user.is_authenticated():
		b = User.objects.get(username=request.user)
		return render_to_response("edit.html",{'b':b},context_instance=RequestContext(request))
	else:
	        if request.method=='POST':
			form = LoginForm(request.POST)
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			print user
			b = User.objects.get(username=request.POST['username'])
			if user is not None:
		    		if user.is_active:
		        		login(request,user)
		        		return render_to_response("edit.html",{'b':b},context_instance=RequestContext(request))
		form = LoginForm()
		return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

#Edit Page

def edit_view(request,id):
	if request.user and request.user.is_authenticated():
		b = User.objects.get(id=id)
		if request.method=='POST':				
			b.first_name = request.POST['first_name']
			b.last_name = request.POST['last_name']
			b.email = request.POST['email']
			b.save()
			return render_to_response('edit.html',{'b':b},context_instance=RequestContext(request))				
		else:
	    		form = EditForm()

	else:
		return redirect('login')

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/home/')

#Change Password Page

def changep_view(request,id):
	if request.user and request.user.is_authenticated():
		if request.method=='POST':
			b = User.objects.get(id=id)	
			form = ChangeForm(request.POST)
			if form.is_valid():
				b.set_password(request.POST['password'])					
				b.save()
				return render_to_response("changep.html",{'form': form},context_instance=RequestContext(request))
		else:
			form = ChangeForm()
	else:
		return HttpResponseRedirect('/home/')

	return render_to_response("changep.html",{'form':form},context_instance=RequestContext(request))


