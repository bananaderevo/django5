from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Book, Publisher, Store


def main(request):
    return render(request, 'cb_hw/main.html')


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate', 'comment']
    template_name = 'cb_hw/create_book.html'
    success_url = '/list/'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'cb_hw/detail_book.html'
    context_object_name = 'book'


class BookListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Book
    fields = ['name', 'authors']
    template_name = 'cb_hw/list_book.html'

    login_url = '/'
    redirect_field_name = 'redirect_to'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = BookCreateView.fields
    template_name = 'cb_hw/create_book.html'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/list-books/'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(BookDeleteView, self).post(request, *args, **kwargs)


class AuthorListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Author
    fields = ['name', 'age']
    template_name = 'cb_hw/list_author.html'


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'cb_hw/detail_author.html'
    context_object_name = 'model'


class StoreDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'cb_hw/detail_store.html'
    context_object_name = 'model'


class StoreListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Store
    fields = ['name', 'books']
    template_name = 'cb_hw/list_store.html'


class PublisherDetailView(LoginRequiredMixin, DetailView):
    model = Publisher
    template_name = 'cb_hw/detail_publisher.html'
    context_object_name = 'model'


class PublisherListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Publisher
    fields = ['name']
    template_name = 'cb_hw/list_publisher.html'
