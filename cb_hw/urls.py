from django.urls import path

from . import views

app_name = 'cb_hw'
urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('list-books/', views.BookListView.as_view(), name='list'),
    path('list-authors/', views.AuthorListView.as_view(), name='list'),
    path('detail-author/<int:pk>', views.AuthorDetailView.as_view(), name='detail'),
    path('detail-store/<int:pk>', views.StoreDetailView.as_view(), name='detail'),
    path('list-stores/', views.StoreListView.as_view(), name='list'),
    path('detail-publisher/<int:pk>', views.PublisherDetailView.as_view(), name='detail'),
    path('list-publishers/', views.PublisherListView.as_view(), name='list'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete'),

]
