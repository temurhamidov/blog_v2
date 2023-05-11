from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from .forms import BlogForm, CommentForm
from .models import Blog, Category, Comment, Tag
from user.models import User
from .mixins import LoginRequrmentMixins
# Create your views here.

# class BaseMixin:
#     @property
#     def categories(self):
#         categories = Category.objects.all()
#         return categories
#
#     @property
#     def tags(self):
#         tags = Tag.objects.all()
#         return tags


class HomeView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 2)

        current_page = request.GET.get('page')
        obj = paginator.get_page(current_page)
        nums = "a" * obj.paginator.num_pages
        context = {
            'blogs' : obj,
            'nums': nums,
        }
        return render(request, 'myapp/home.html', context)



class BlogCreateView(LoginRequrmentMixins, View):
    def get(self, request):
        context = {}
        context['form'] = BlogForm
        return render(request, 'myapp/blog_create.html', context)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_ = form.save(commit=False)
            form_.author = request.user
            form_.save()
            return redirect('myapp:home')
        context = {
            'form': form
        }
        return render(request, 'myapp/blog_create.html', context)


class CategoryBlogView(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        blogs = Blog.objects.filter(category__slug=slug)
        context = {
            'blogs': blogs,
        }
        return render(request, 'myapp/home.html', context)


class TagBlogView(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        blogs = Blog.objects.filter(tags__slug=slug)
        context = {
            'blogs': blogs,
        }
        return render(request, 'myapp/home.html', context)



## Detail View orqali blog detailni chiqarish
# class BlogDetailView(BaseMixin, DetailView):
#     queryset = Blog.objects.all()
#     template_name = 'myapp/blog_detail.html'
#     context_object_name = 'blog'
#
#     def get_object(self, queryset=None):
#         obj = super().get_object()
#         obj.view += 1
#         obj.save()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['categories'] = self.categories
#         return context


class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(Blog, slug=slug)
        form = CommentForm()
        blog.view += 1
        blog.save()
        context = {
            'blog' : blog,
            'form' : form,
        }
        return render(request, 'myapp/blog_detail.html', context)
#
#     def post(self, request, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         blog = get_object_or_404(Blog, slug=slug)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = self.request.user
#             comment.blog = blog
#             comment.save()
#             return redirect('myapp:blog_detail', blog.slug)


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'myapp/category_list.html'

    # def get_queryset(self):  # new
    #     search = self.request.GET.get('search')
    #     category_list = Category.objects.filter(
    #         Q(name__icontains=search) | Q(state__icontains=search)
    #     )
    #     return category_list


class AddCategoryUserView(LoginRequrmentMixins, View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        user = request.user
        if user not in category.users.all():
            category.users.add(user)
            return redirect('myapp:category_list')
        else:
            category.users.remove(user)
            return redirect('myapp:category_list')


class BlogUpdateView(LoginRequrmentMixins, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'myapp/blog_update.html'
    success_url = reverse_lazy('myapp:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get_form(self, *args, **kwargs):
        user = self.request.user
        form = super(BlogUpdateView, self).get_form(*args, *kwargs)
        form.fields['category'].queryset = user.category_set.all()
        return form

    ## Bazaga save qimasda o'zgarishlar kiritish
    # def form_valid(self, form):
    #     blog = form.save(commit=False)
    #     blog.title = blog.title + 'Form Valid'
    #     blog.save()
    #     return super().form_valid(form)

    # def get_initial(self):
    #     user = self.request.user
    #     initial = super().get_initial()
    #     initial['category'] = self.object.filter(users=user)
    #     return initial


class BlogDeleteView(LoginRequrmentMixins, DeleteView):
    model = Blog
    template_name = 'myapp/blog_delete.html'

    def get_success_url(self):
        return reverse('myapp:home')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(Blog, slug=slug)
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blog = blog
        comment.save()
        return redirect('myapp:blog_detail', blog.slug)

    def form_invalid(self, form):
        return redirect('myapp:home')


class UsersListView(LoginRequrmentMixins, ListView):
    queryset = User.objects.all()
    context_object_name = 'users'
    template_name = 'myapp/users_list.html'


class MyBlogView(LoginRequrmentMixins, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        blogs = Blog.objects.filter(author=user)
        paginator = Paginator(blogs, 2)
        current_page = request.GET.get('page')
        obj = paginator.get_page(current_page)
        context = {
            'blogs': obj,
        }
        return render(request, 'myapp/home.html', context)

def search_blogs(request):
    if request.method == 'POST':
        search = request.POST['search']
        blogs = Blog.objects.filter(title__contains=search)
        context = {
            'blogs': blogs,
        }
        return render(request, 'myapp/home.html', context)
    else:
        return redirect('myapp:home')




def error_403(request, exception):
    return render(request, '403.html')

def error_404(request, exception):
    return render(request, '404.html')




