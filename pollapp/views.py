import time
import sched
import csv
import io
from datetime import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import GuestsForm
from .models import Guest
from django.views.decorators.http import require_POST
from django.core.mail import BadHeaderError, send_mail, EmailMessage



def GuestListView(request):
	form = GuestsForm(request.POST or None)
	if request.method == 'POST':
		form.cleaned_data

	d = {
		'Guests': Guest.objects.all(),
	}
	return render(request,'1/guestlist.html',d)


def GuestFormView(request):
	form = GuestsForm(request.POST or None)

	context = {
		'form': form,
	}
	return render(request,'1/guestform.html', context )


def testpage(request):
	form = GuestsForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			Guest.objects.create(**form.cleaned_data)

	temp_email = request.POST['email']
	temp_name = request.POST['name']
	temp_furi = request.POST['furi']
	temp_memo = request.POST['memo']

	if 'email' in request.POST:
		subject = "登録確認のお知らせ"
		message = "以下のように登録しました。//n 名前：%s //n フリガナ：%s //n メールアドレス：%s //n 備考：%s //n 当日を待ちしております。" %(temp_name ,temp_furi ,temp_email ,temp_memo)
		from_email = "event.message.for.guests@gmail.com"
		to = ["event.message.for.guests@gmail.com"]
		bcc = [temp_email]
	email=EmailMessage(subject, message, from_email, to, bcc)
	email.send()

	context = {
			'form': form,
			}
	return render(request, '1/testpage.html', context)

"""
def mailsend():

	subject = "Subject here"
	message = "message_test"
	from_email = "event.message.for.guests@gmail.com"
	to = ["event.message.for.guests@gmail.com"]
#	bcc = [temp_email]

	email=EmailMessage(subject, message, from_email, to, bcc)
	email.send()
"""

def CSVExportView(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="guest.csv"'
	writer = csv.writer(response)
	for guest in Guest.objects.all():
		writer.writerow([guest.name, guest.furi, guest.memo])
	return response

# Create your views here.

