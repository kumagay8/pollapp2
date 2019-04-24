from django.core.management.base import BaseCommand, CommandError
import sched, time
import smtplib
from datetime import datetime
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from email.mime.text import MIMEText
from pollapp.models import Guest

#import django
#django.setup()

def mailsend():
	account = "event.message.for.guests@gmail.com"
	password = "0880kum@g@i"

	maildata_list = Guest.objects.all()
	recipient_list = [(maildata.email) for maildata in maildata_list ]
	from_email = "event.message.for.guests@gmail.com"

	subject = "Subject here"
	message = "message_test"
	email=EmailMessage(subject, message, from_email, recipient_list)
	email.send()
	return mailsend


class Command(BaseCommand):
	def handle(self, *args, **options):
		s = sched.scheduler(time.time, time.sleep)
		start_time = datetime.strptime("2019/4/25 07:00", '%Y/%m/%d %H:%M')
		time_second = (start_time - datetime.now()).seconds
		s = sched.scheduler(time.time, time.sleep)
		s.enter(time_second, 1, mailsend())
		s.run()
"""
def mailsend(): #難しい方
	account = "event.message.for.guests@gmail.com"
	password = "0880kum@g@i"
	#recipient_list = [to.email for to in maildata.mail_to.all() ]
	#recipient_list = "event.message.for.guests@gmail.com"
	maildata_list = Guest.objects.all()
	recipient_list = [(maildata.email) for maildata in maildata_list ]
	print(recipient_list)
	from_email = "event.message.for.guests@gmail.com"
	subject = "Subject here"
	message = "message_test"
	#msg = MIMEText(message, "html")
	#msg["Subject"] = subject
	#msg["To"] = recipient_list
	#msg["From"] =from_email
	#from_email = "event.message.for.guests@gmail.com"
	#to = ["event.message.for.guests@gmail.com"]
	#bcc = [temp_email]

	#server = smtplib.SMTP("smtp.gmail.com", 587)
	#server.starttls()
	#server.login(account, password)
	#server.send_message(msg)
	email=EmailMessage(subject, message, from_email, recipient_list)
	email.send()
	#server.quit()
"""


