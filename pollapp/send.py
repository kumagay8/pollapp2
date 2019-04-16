from django.core.management.base import BaseCommand, CommandError
import sched, time
import smtplib
from datetime import datetime
#from django.core.mail import BadHeaderError, send_mail, EmailMessage
from email.mime.text import MIMEText
from pollapp.pollapp.models import Guest

#import django
#django.setup()


class Command(BaseCommand):

	def mailsend():

		account = "event.message.for.guests@gmail.com"
		password = "0880kum@g@i"

		to_email =[to.email for to in Guest.email.all()]
		from_email = "event.message.for.guests@gmail.com"

		subject = "Subject here"
		message = "message_test"
		msg = MIMEText(message, "html")
		msg["Subject"] = subject
		msg["To"] = to_email
		msg["From"] =from_email
		#	from_email = "event.message.for.guests@gmail.com"
		#	to = ["event.message.for.guests@gmail.com"]
		#	bcc = [temp_email]

		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(account, password)
		server.send_message(msg)
		server.quit()
		#	email=EmailMessage(subject, message, from_email, to)
		#	email.send()

	s = sched.scheduler(time.time, time.sleep)
	start_time = datetime.strptime("2019/4/8 22:20", '%Y/%m/%d %H:%M')
	time_second = (start_time -datetime.now()).seconds
	s = sched.scheduler(time.time, time.sleep)
	s.enter(time_second, 1, mailsend)
	s.run()

