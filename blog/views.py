from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        'post_list' : qs
    })

def post_detail(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_Detail.html', {
        'post': qs
    })