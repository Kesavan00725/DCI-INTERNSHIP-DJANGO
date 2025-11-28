from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Mithul part – Home page: list all posts
def home(request):
    data = BlogPost.objects.order_by('-created_at')
    return render(request, "home.html", {"post": data})


# Kishore part – Detail page
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'post_detail.html', {'post': post})


# Member 3 – Create, Edit, Delete

# Create a new post
def create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})


# Edit an existing post
def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


# Delete an existing post (with confirm page)
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    # GET → show confirmation page
    return render(request, 'confirm_delete.html', {'post': post})
