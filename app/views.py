from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import TodoItem
from .forms import TodoForm

class LoginRequiredMixin(LoginRequiredMixin):
    login_url = "/auth/login"

@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'app/home.html')


class ItemsView(LoginRequiredMixin, ListView):
    template_name = 'app/item-list.html'
    context_object_name = 'items'

    # queryset = TodoItem.objects.filter(archived=False, author_id=request.user).order_by("-id")

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user, archived=False).order_by("-id")

# class CreateItemView(CreateView):
#     model = TodoItem
#     form_class = TodoForm
#     template_name = 'app/item-list.html'
#     fields = ('title', 'text', )
#     context_object_name = 'create_form'

def create_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
    else:
        form = TodoForm()
    items = TodoItem.objects.filter(author=request.user, archived=False).order_by('-id')
    return render(request, 'app/list_elem.html', {"create_form": form, "items": items})


class DeleteItemView(DeleteView):
    model = TodoItem
    template_name = 'app/item-list.html'
    success_url = 'app/list_elem.html'

def delete_item(request, pk):
    item = TodoItem.objects.get(id=pk)
    item.archived = True
    item.save()
    items = TodoItem.objects.filter(author=request.user, archived=False).order_by('-id')
    return render(request, 'app/list_elem.html', {'items': items})

def mark_done(request, pk):
    item = TodoItem.objects.get(id=pk)
    item.done = True
    item.save()
    items = TodoItem.objects.filter(author=request.user, archived=False).order_by('-id')
    return render(request, 'app/list_elem.html', {'items': items})

def archived_list(request):
    items = TodoItem.objects.filter(author=request.user, archived=True).order_by('-id')

    return render(request, 'app/archive.html', {'items': items})
