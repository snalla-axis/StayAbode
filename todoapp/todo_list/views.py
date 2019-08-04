from django.core import serializers

# Create your views here.
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView

from todo_list.forms import TodosForm
from todo_list.models import Todos


class Index(TemplateView):
    template_name = 'index.html'


class CreateTodo(CreateView):
    model = Todos
    form_class = TodosForm
    template_name = 'todo_create.html'
    # success_url = reverse_lazy("todo_list:list")


class ListTodo(ListView):
    model = Todos
    template_name = 'todo_listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Todos().get_undeleted_tasks()
        return context


class DetailsTodo(DetailView):
    model = Todos
    context_object_name = 'task'
    template_name = 'todo_detail.html'


class UpdateTodo(UpdateView):
    model = Todos
    form_class = TodosForm
    template_name = 'todo_create.html'


class DeleteTodo(DeleteView):
    model = Todos
    template_name = 'todo_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy("todo_list:list")

    def delete(self, request, *args, **kwargs):
        """
        Call the save method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ListAllOrOne(View):
    def __init__(self):
        super().__init__()

    def get(self, requets):
        id = requets.GET.get('id', None)
        queryset = Todos.objects.all()
        fields=('title','description', 'todo_date_time','status','created_at', 'modified_at', 'is_deleted')
        if id:
            todo_one_json = serializers.serialize("json", queryset.filter(id=id), fields=fields)
            return JsonResponse({"data":todo_one_json}, content_type="application/json")
        todo_json = serializers.serialize("json", queryset, fields=fields)
        return JsonResponse({"data":todo_json}, content_type="application/json")

