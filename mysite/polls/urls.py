from django.urls import path
from . import views

app_name = 'polls'
# 汎用ビュー(クラスビュー)
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_name'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
# 関数ビュー
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail_name'),
#     path('<int:question_id>/results', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]
