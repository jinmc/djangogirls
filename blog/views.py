from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Post, Job_Heykorean, Job_Jobkorea
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def base(request):
    return render(request, 'blog/base.html', {})

def jobkorea_jobs(request):
    qs = Job_Jobkorea.objects.all()
    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # qs = qs.order_by('-published_date')
    # return render(request, 'blog/jobkorea_jobs.html', {
    #     'jk_jobs' : qs
    # })
    return render(request, 'blog/jobkorea_jobs.html', {
        'page_obj' : page_obj
    })

def heykorean_jobs(request):
    qs = Job_Heykorean.objects.all()
    qs = qs.order_by('-published_date')
    return render(request, 'blog/heykorean_jobs.html', {
        'h_jobs' : qs
    })

def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        'post_list' : qs
    })

def post_detail(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': qs
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})