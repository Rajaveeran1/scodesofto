from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date as d
from datetime import time as t
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Enquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'cyberneticr@gmail.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("index")
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})
	#return render(request, "index.html", {'form':form})


def portfolio(request):
    return render(request,'portfolio_details1.html',{})

def portfolio_2(request):
    return render(request,'portfolio_details2.html',{})


def portfolio_3(request):
    return render(request,'portfolio_details3.html',{})


def portfolio_4(request):
    return render(request,'portfolio_details4.html',{})


def portfolio_5(request):
    return render(request,'portfolio_details5.html',{})


def portfolio_6(request):
    return render(request,'portfolio_details6.html',{})
	

