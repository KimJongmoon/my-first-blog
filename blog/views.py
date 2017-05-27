from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_list(request, pk):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts':posts})
    post = Post.objects.get(pk=pk)

    messages = (
        '<p>사진입니다</p>'
        '<p><img src="{url}" /></p>'.format(url = post.image.url),
    )
    return HttpResponse('\n'.join(messages))

def create(request):
    if request.method == "GET":
        form = PostForm()
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)
