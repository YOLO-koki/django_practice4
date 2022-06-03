from django.db import models

# Create your models here.
class Todo(models.Model):
    # CharField・・・入力値：文字列
    #               入力項目：テキストボックス
    title = models.CharField('タスク名', max_length=30)
    # TextField・・・入力項目：テキストエリア
    description = models.TextField('詳細', blank=True)
    # DateField・・・日付
    deadline = models.DateField('締切')
    
    def __str__(self) -> str:
        return self.title