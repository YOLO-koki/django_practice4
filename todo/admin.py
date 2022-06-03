from django.contrib import admin
from .models import Todo
# Register your models here.
#　作成したテーブルを管理画面に表示できるようにする
admin.site.register(Todo)