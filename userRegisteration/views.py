from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from userRegisteration.models import Users

def registeration(request):
    return render(request, 'registration.html')

def save_receipt(request):
	if request.POST.get('isAgree') == 'on':
		user = Users(
			first_name = request.POST.get('firstName',''),
			last_name = request.POST.get('lastName',''),
			email = request.POST.get('email',''),
			isAgree = True,
		)
		user.save();
		return render_to_response('save_receipt.html',{
								'sequence':user.id, 
								'firstName':user.first_name,
								'lastName':user.last_name,
								'email':user.email
								})



