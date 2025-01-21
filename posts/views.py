from django.shortcuts import render, get_object_or_404, redirect
from catalogs.models import Catalog
from tags.models import Tag
from .models import Post, Comment


def home(request):
    posts = Post.objects.all()
    catalogs = Catalog.objects.all()
    tags = Tag.objects.all()
    ctx = {'posts': posts, 'catalogs': catalogs, 'tags': tags}
    return render(request, 'index.html', ctx)

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             created_at__year=year,
                             created_at__month=month,
                             created_at__day=day,
                             )
    comments = post.comments.all()
    return render(request, 'post/post-detail.html', {'post': post, 'comments': comments})

def filter_results(request):
    category = request.GET.getlist('category')
    sort_by = request.GET.get('sort')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    hashtags = request.GET.getlist('hashtag')

    results = []
    if category or sort_by or start_date or end_date or hashtags:
        results = Post.objects.all()

        if category:
            results = results.filter(catalog__in=category)
        if sort_by:
            if sort_by == 'latest':
                results = results.order_by('-created_at')
            elif sort_by == 'oldest':
                results = results.order_by('created_at')
        if start_date and end_date:
            results = results.filter(created_at__range=[start_date, end_date])
        if hashtags:
            results = results.filter(tags__id__in=hashtags).distinct()
    catalogs = Catalog.objects.all()
    tags = Tag.objects.all()
    ctx = {'results': results, 'catalogs': catalogs, 'tags': tags}
    return render(request, 'post/filter_results.html', ctx)

def post_search(request):
    catalogs = Catalog.objects.all()
    tags = Tag.objects.all()
    search = request.GET.get('search')
    if search:
        results = Post.objects.filter(title__icontains=search)
    else:
        results = Post.objects.none()
    ctx = {'results': results, 'catalogs': catalogs, 'tags': tags}
    return render(request, 'post/search_results.html', ctx)


def post_comment(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             created_at__year=year,
                             created_at__month=month,
                             created_at__day=day,
                             )

    if request.method == 'POST':
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if author and email and comment:
            Comment.objects.create(
                post=post,
                author=author,
                email=email,
                comment=comment
            )
            return redirect('posts:detail', slug=slug, year=year, month=month, day=day)
    comments = post.comments.all()
    return render(request, 'post/post-detail.html', {'post': post, 'comments': comments})
