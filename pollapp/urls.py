from django.urls import path
from django.contrib import admin
from . import views
from pollapp.views import  GuestListView , CSVExportView
#, GuestFormView , GuestConfirmView , GuestRegisterView , GuestReplyView 

app_name = 'pollapp'
urlpatterns = [
	path('admin/', admin.site.urls),
#主催者の確認ページ
#	path('1/guestlist/', GuestListView.as_view(), name='list'),
	path('1/guestlist/', GuestListView, name='guestlist'),


#ゲストユーザ登録の為の入力フォーム
	path('1/guestform/', views.GuestFormView, name='guestform'),	

#ゲストユーザの情報をCSVで出力するページ
	path('1/csvexport/', CSVExportView, name='csvexport'),

#テストページ
	path('1/testpage/', views.testpage, name='testpage')
]
