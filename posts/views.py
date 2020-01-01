from django.shortcuts import redirect, render, get_object_or_404,HttpResponse
from .models import Post
from .forms import PostModelForm,AuthorModelForm
from django.contrib import messages
#>>>>>>>>>>>>>>>>>>>>>>>>>VIEW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def post_list(request):
    all_posts = Post.objects.all()
    return render(request,'postlist.html',{'all_posts':all_posts})

#>>>>>>>>>>>>>>>>>>>>>>>>>UNIQUE-POST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def posts_slug(request,slug):
    unique_post= get_object_or_404(Post, slug=slug)
    return render(request,'PostDetail.html',{'post':unique_post})

#>>>>>>>>>>>>>>>>>>>>>>>>>CREATE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def posts_create(request):
    c_post = PostModelForm(request.POST or None, request.FILES or None)
    if c_post.is_valid():
        c_post.save()
        print('/nUSER CREATED')
        messages.info(request, 'You Posted Succesfully!')
        return redirect('/posts/')
    else:
        messages.info(request, 'Please fill all the information!')
        redirect('/posts/CreatePost/')
    return render(request,'form.html',{'post':c_post})

def authors_create(request):
    authorform = AuthorModelForm(request.POST or None, request.FILES or None)
    if authorform.is_valid():
        authorform.save()
        messages.info(request, 'Author is created Succesfully!')
        return redirect('/posts/CreatePost/')
    else:
        messages.info(request, 'Please fill all the information!')
    return render(request,'form.html',{'author':authorform})     

#>>>>>>>>>>>>>>>>>>>>>>>>>UPDATE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def posts_update(request,slug):
    slug_post = get_object_or_404(Post,slug=slug)
    update_form = PostModelForm(request.POST or None,request.FILES or None,instance=slug_post)
    if update_form.is_valid():
        update_form.save()
        messages.info(request,'Post is Updated Successfully!')
        return redirect('/posts/')
    return render(request,'form.html',{'post':update_form})

#>>>>>>>>>>>>>>>>>>>>>>>>>DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def posts_delete(request,slug):
    slug_post = Post.objects.get(slug=slug)
    slug_post.delete()
    messages.info(request,'Post is Deleted Successfully!')
    return redirect('/posts/')
