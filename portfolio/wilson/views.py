from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib import request


from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def index(request):
     return render(request, "wilson/index.html")

def landing(request):
     return render(request, "wilson/landing.html")

def about(request):
     return render(request, "wilson/about.html")

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# # 			}
# 			message = "\n".join(body.values())

			# try:
			# 	send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			# except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			# return redirect ("main:homepage")
      
	# form = ContactForm()
	# return render(request, "main/contact.html", {'form':form})
def contact(request):
     # CONTACT FORM
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          message = request.POST.get('message')
          form_data = {
               'name':name,
               'email':email,
               'phone':phone,
               'message':message,
          }
          message = '''
          From:\n\t\t{}\n
          Message:\n\t\t{}\n
          Email:\n\t\t{}\n
          Phone:\n\t\t{}\n
          '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
          # send_mail('You got a mail!', message, '', ['wilsonabdiel000@gmail.com']) # TODO: enter your email address
          
          try:
               # send_mail( message, email, ['wilsonabdiel000@gmail.com']) 
               send_mail('You got a mail!', message, '', ['wilsonabdiel000@gmail.com'])
          except BadHeaderError:
               return HttpResponse('Invalid header found.')
          return render(request,"wilson/index.html")
     else:
        
          
      return render(request,"wilson/contact.html")