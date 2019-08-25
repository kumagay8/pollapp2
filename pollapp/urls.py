from django.urls import path
from django.contrib import admin
from . import views
from pollapp.views import  GuestListView , CSVExportView
from django.conf import settings
from django.conf.urls.static import static
#, GuestFormView , GuestConfirmView , GuestRegisterView , GuestReplyView 

app_name = 'pollapp'
urlpatterns = [
	path('admin/', admin.site.urls),
#主催者の確認ページ
#	path('1/guestlist/', GuestListView.as_view(), name='list'),
	path('2/guestlist/', GuestListView, name='guestlist'),


#ゲストユーザ登録の為の入力フォーム
	path('2/guestform/', views.GuestFormView, name='guestform'),	

#ゲストユーザの情報をCSVで出力するページ
	path('2/csvexport/', CSVExportView, name='csvexport'),

#テストページ
	path('2/testpage/', views.testpage, name='testpage'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
