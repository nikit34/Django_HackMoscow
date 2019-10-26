from django.shortcuts import render

# Create your views here.

from .models import Task, Child, TaskInstance#, Subject

from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    num_tasks = Task.objects.count()
    num_instances = TaskInstance.objects.all().count()
    num_instances_available = TaskInstance.objects.filter(status__exact='a').count()
    num_childs = Child.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={
        'num_tasks': num_tasks,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_childs':num_childs,
        'num_visits': num_visits},
    )


from django.views import generic


class CompanyListView(generic.ListView):
    model = Task
    paginate_by = 5

class CompanyDetailView(generic.DetailView):
    model = Task


from django.contrib.auth.mixins import LoginRequiredMixin


class CompanyListView(generic.ListView):
    model = Task
    paginate_by = 5


class CompanyDetailView(generic.DetailView):
    model = Task


class OwnerListView(generic.ListView):
    model = Child
    paginate_by = 5


class OwnerDetailView(generic.DetailView):
    model = Child


from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedCompanysByUserListView(LoginRequiredMixin, generic.ListView):
    model = TaskInstance
    template_name = 'catalog/taskinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return TaskInstance.objects.filter(borrower=self.request.user).filter(status__exact='d').order_by('due_back')


from django.contrib.auth.mixins import PermissionRequiredMixin


class LoanedCompanysAllListView(PermissionRequiredMixin, generic.ListView):
    model = TaskInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/taskinstance_list_borrowed_all.html'
    paginate_by = 5

    def get_queryset(self):
        return TaskInstance.objects.filter(status__exact='d').order_by('due_back')


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from .forms import RenewCompanyForm


@permission_required('catalog.can_mark_returned')
def renew_task_librarian(request, pk):
    task_instance = get_object_or_404(TaskInstance, pk=pk)

    if request.method == 'POST':
        form = RenewCompanyForm(request.POST)
        if form.is_valid():
            task_instance.due_back = form.cleaned_data['renewal_date']
            task_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewCompanyForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'task_instance': task_instance,
    }

    return render(request, 'catalog/task_renew_librarian.html', context)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Child


class OwnerCreate(PermissionRequiredMixin, CreateView):
    model = Child
    fields = '__all__'
    initial = {'group': '1a'}
    permission_required = 'catalog.can_mark_returned'


class OwnerUpdate(PermissionRequiredMixin, UpdateView):
    model = Child
    fields = ['first_name', 'last_name', 'date_of_birth', 'group']
    permission_required = 'catalog.can_mark_returned'


class OwnerDelete(PermissionRequiredMixin, DeleteView):
    model = Child
    success_url = reverse_lazy('childs')
    permission_required = 'catalog.can_mark_returned'


class CompanyCreate(PermissionRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class CompanyUpdate(PermissionRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class CompanyDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    permission_required = 'catalog.can_mark_returned'


def graph_1(request):
    datasplit = ChartData_1()
    name_child = []
    grade = []
    for i in range(len(datasplit.get(request).data)):
        name_child.append(str(datasplit.get(request).data[i][0]))
        grade.append(datasplit.get(request).data[i][1])
    dict_data = {'name_child': name_child, 'grade': grade}
    return render(request, 'graph_1.html', context=dict_data)


class ChartData_1(APIView):
    def get(self, request, format=None):
        articles = dict()
        for task in Task.objects.all():
            articles[task.child] = task.grade
        articles = sorted(articles.items(), key=lambda x: x[1])
        return Response(articles)


def graph_2(request):
    datasplit = ChartData_2()
    subject = []
    cost = []
    for i in range(len(datasplit.get(request).data)):
        subject.append(datasplit.get(request).data[i][0])
        cost.append(datasplit.get(request).data[i][1])
    dict_data = {'sub': subject, 'cost': cost}
    return render(request, 'graph_2.html', context=dict_data)


class ChartData_2(APIView):
    def get(self, request, format=None):
        articles = dict()
        for task in Task.objects.all():
            articles[task.title] = task.cost
        articles = sorted(articles.items(), key=lambda x: x[1])
        return Response(articles)


def graph_3(request):
    datasplit = ChartData_3()
    task = []
    due_back = []
    for i in range(len(datasplit.get(request).data)):
        task.append(datasplit.get(request).data[i][0])
        due_back.append(datetime.datetime.strptime(str(datasplit.get(request).data[i][1]), "%Y-%m-%d"))
    dict_data = {'task': task, 'due_back': due_back}
    return render(request, 'graph_3.html', context=dict_data)


class ChartData_3(APIView):
    def get(self, request, format=None):
        articles = dict()
        for t in TaskInstance.objects.all():
            articles[t.task] = t.due_back
        articles = sorted(articles.items(), key=lambda x: x[1])
        return Response(articles)


from .algorithm import ml_alg

def info_graph(request):
    datasplit = InfoChartData()
    subject = []
    grade = []
    for i in range(len(datasplit.get(request).data)):
        subject.append(datasplit.get(request).data[i][0])
        grade.append(datasplit.get(request).data[i][1])
    dict_data = {'subject': subject, 'grade': grade}
    coord_data = ml_alg(dict_data)

    first =[]
    second = []
    third = []
    for i in range(len(coord_data)):
        first.append(coord_data[i][0])
        second.append(coord_data[i][1])
        third.append(coord_data[i][2])
    return render(request, 'info_graph.html', context={'x1': first, 'y1': second, 'z1': third})


class InfoChartData(APIView):
    def get(self, request, format=None):
        articles = dict()
        for task in Task.objects.all():
            articles[task.title] = task.grade
        articles = sorted(articles.items(), key=lambda x: x[1])
        return Response(articles)
