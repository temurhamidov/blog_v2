from django.urls import path

from .views import HomeView, \
    BlogCreateView, \
    CategoryBlogView, \
    BlogDetailView, \
    CategoryListView, \
    AddCategoryUserView, \
    BlogUpdateView,\
    BlogDeleteView, CommentCreateView, TagBlogView, UsersListView, MyBlogView, search_blogs
app_name = 'myapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-create/', BlogCreateView.as_view(), name='blog_create'),
    path('category/<slug:slug>', CategoryBlogView.as_view(), name='category_blog'),
    path('tag/<slug:slug>', TagBlogView.as_view(), name='tag_blog'),
    path('blog-detail/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
    path('category-add-user/<slug:slug>', AddCategoryUserView.as_view(), name='category_add_user'),
    path('blog-update/<slug:slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog-delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog-comment/<slug:slug>', CommentCreateView.as_view(), name='comment_create'),
    path('user-list/', UsersListView.as_view(), name='users_list'),
    path('my-blog/', MyBlogView.as_view(), name='my_blogs'),
    path('search/', search_blogs, name='search_blogs'),
]