from django.conf import settings
from django.db import models

class Guest(models.Model):
	name = models.CharField(
		max_length=30,
		#verbose_name='名前',
		help_text='名前を入力して下さい',
		)				#デフォルトwidget(TextInput)、通常A stringを使用(Max_Min_lengthがある場合、Max_length/Min_lengthを使用)

	furi = models.CharField(
		max_length=30,
		#verbose_name='フリガナ',
		help_text='名前のフリガナを入力してください',
		)

	email = models.EmailField(
		unique=True,
		default='',
		null=False,
		max_length=255,
		#verbose_name='メールアドレス',
		help_text='メールアドレスを入力してください',
		)				#デフォルトのwidget(EmailFields)/EmailValidatorを使用

	memo = models.TextField(
		blank=True,
		#verbose_name='メモ',
		help_text='参加人数が複数の場合や遅れて参加の場合は記入してください',
		) 				#blank:空欄を許容する


	def __str__(self): 										#モデル内部の情報を文字列で表現(特殊メソッド)
		return u"{0}:{1}...".format(self.id, self.name, self.furi, self.email, self.memo)
															#返り値はu(中身：format({0}=id,{1}=name,....と続いていく)

class Maildata(models.Model):
	datetime = models.DateTimeField('連絡日・時間')
	mail_to = models.EmailField(Guest) #verbose_name='To')

	def __str__(self):
		message = '{0} {1}'
		return message.format(self.mail_to)



# Create your models here.
#