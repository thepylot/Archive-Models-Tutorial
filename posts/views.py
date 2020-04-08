from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostArchive

def posts_view(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts.html', {'posts':posts})

def archive_post(request, id):
    post = get_object_or_404(Post, id=id)
    archive_post = PostArchive()
    for field in post._meta.fields:
        setattr(archive_post, field.name, getattr(post, field.name))
    archive_post.pk = None
    archive_post.save()
    return redirect('posts')

def archive_post_view(request):
    archive_posts = PostArchive.objects.all().order_by('-id')
    return render(request, 'archive.html', {'archive_posts':archive_posts})


