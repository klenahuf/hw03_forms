from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User
from .forms import PostForm
from .utils import get_paginator_helper
SYMBOLS_QUANTITY: int = 30


def index(request):
    paginator_obj = get_paginator_helper(request)
    context = {
        'title': 'Последние обновления на сайте',
        'page_obj': paginator_obj['page_obj']
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    paginator_obj = get_paginator_helper(request, filter_name='group',
                                         filter_value=group)
    title = group.title
    text = group.description
    context = {
        'text': text,
        'title': title,
        'page_obj': paginator_obj['page_obj'],
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    paginator_obj = get_paginator_helper(request, filter_name='author',
                                         filter_value=author)
    context = {
        'title': f'Профайл пользователя {author.get_full_name()}',
        'author': author,
        'page_obj': paginator_obj['page_obj'],
        'post_total': paginator_obj['count_post']
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    post_list = Post.objects.filter(author=author)
    count_posts = post_list.count()
    title = f"Пост {post.text[:SYMBOLS_QUANTITY]}"
    context = {
        "title": title,
        "post": post,
        "count_posts": count_posts,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect("posts:profile", request.user)


@login_required
def post_edit(request, post_id):
    post_edit_flag = True
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        if request.user != post.author:
            return redirect('posts:profile', request.user)
        form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:post_detail', post.id)

    return render(request, 'posts/create_post.html', {'form': form,
                                                      'post': post,
                                                      'post_edit_flag': post_edit_flag
                                                      })
