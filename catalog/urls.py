from django.urls import path, include
from django.conf import settings
from .views import index, CompanyListView, CompanyDetailView, OwnerListView, OwnerDetailView, info_graph, graph_1, graph_2, graph_3, LoanedCompanysByUserListView, LoanedCompanysAllListView, renew_task_librarian, OwnerCreate, OwnerUpdate, OwnerDelete, CompanyCreate, CompanyUpdate, CompanyDelete, ChartData_1, ChartData_2, ChartData_3, InfoChartData

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', CompanyListView.as_view(), name='tasks'),
    path('task/<int:pk>', CompanyDetailView.as_view(), name='task-detail'),
    path('childs/', OwnerListView.as_view(), name='childs'),
    path('child/<int:pk>', OwnerDetailView.as_view(), name='child-detail'),

    path('graph/1', graph_1, name='graph_1'),
    path('catalog/graph/1', ChartData_1.as_view(), name='api-chart-data'),
    path('graph/2', graph_2, name='graph_2'),
    path('catalog/graph/2', ChartData_2.as_view(), name='api-chart-data'),
    path('graph/3', graph_3, name='graph_3'),
    path('catalog/graph/3', ChartData_3.as_view(), name='api-chart-data'),

    path('info_graph/', info_graph, name='info_graph'),
    path('catalog/info_graph/', InfoChartData.as_view(), name='api-chart-data'),
]


urlpatterns += [
    path('mytasks/', LoanedCompanysByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', LoanedCompanysAllListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    path('task/<uuid:pk>/renew/', renew_task_librarian, name='renew-task-librarian'),
]


urlpatterns += [
    path('child/create/', OwnerCreate.as_view(), name='child_create'),
    path('child/<int:pk>/update/', OwnerUpdate.as_view(), name='child_update'),
    path('child/<int:pk>/delete/', OwnerDelete.as_view(), name='child_delete'),
]


urlpatterns += [
    path('task/create/', CompanyCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', CompanyUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', CompanyDelete.as_view(), name='task_delete'),
]

urlpatterns += [
    path('child/create/', OwnerCreate.as_view(), name=''),]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
