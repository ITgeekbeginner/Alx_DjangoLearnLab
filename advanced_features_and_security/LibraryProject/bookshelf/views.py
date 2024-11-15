from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from .forms import PostForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, book_id):
    post = get_object_or_404(Post, id=book_id)
    return render(request, 'book_detail.html', {'book': post})

@permission_required('bookshelf.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Post, id=book_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = PostForm(instance=book)
    return render(request, 'post_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def post_delete(request, book_id):
    book = get_object_or_404(Post, id=book_id)
    book.delete()
    return redirect('book_list')

# Create your views here.