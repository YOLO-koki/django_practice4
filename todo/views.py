from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.models import Todo

# Create your views here.
# ListView・・・モデルを単純に利用した表示を行う
class TodoList(ListView):
    model = Todo
    # ↓HTMLで表示する時に使う変数名(tasks)
    context_object_name = 'tasks'
    
    # template_name: str = 'todo_list.html'

# DetailView・・・オブジェクトの詳細ページを表示する
class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'


# CreateView・・・
# CreateViewでは、入力する項目をfieldsで設定する必要がある。
class TodoCreate(CreateView):
    model = Todo
    # 「__all__」・・・カラム全てを選択
    fields = '__all__'
    # reverse_lazy('list')・・・createが完了したら「reverse_lazy」を使って「list」という名前がついたページに遷移
    success_url = reverse_lazy('list')
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('list')