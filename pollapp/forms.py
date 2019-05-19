from django import forms
from .models import Guest
from django.core.exceptions import ValidationError

class GuestsForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = ('name','furi','email','memo')
		label = {
			'name': '名前' ,
			'furi': 'フリガナ' ,
			'email': 'メールアドレス' ,
			'memo': 'メモ',
					}
		widgets ={
			'name':forms.TextInput(attrs={'size':42}),
			'furi':forms.TextInput(attrs={'size':42}),
			'email':forms.EmailInput(attrs={'size':42}),
			'memo':forms.Textarea(attrs={'cols':40, 'rows':2}),
		}
		requireds = {
			'name': True ,
			'furi': True ,
			'email': True ,
			'memo': None,
					}
		# requiredsはTrueかNone/’’を必ず入れる







