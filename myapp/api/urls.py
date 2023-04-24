from django.urls import path
from myapp.api.views import (CategoryCreateAPIView,
                             CategoryCreateAPIView2,
                             CategoryUpdateAPIView,
                             CategoryUpdateAPIView2,
                             BlogListCreateAPIView,
                             CategoryListAPIView,
                             BlogUpdateDeleteAPIView,
                             BlogListWithCategoryAPIView,
                             BlogRetrievAPIView,
CommentListAPIView,
CommentListWithBlogAPIView,
CommentRetrievAPIView,
CommentCreateAPIView,
CommentDeleteUpdteAPIView,
                            )

urlpatterns = [
    #category
    path('category-list/', CategoryListAPIView.as_view(), name='category_list_api_view'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category_create_api_view'),
    path('category-create2/', CategoryCreateAPIView2.as_view(), name='category_create_api_view2'),
    path('category-update/<int:pk>', CategoryUpdateAPIView.as_view(), name='category_update_api_view'),
    path('category-update2/<int:pk>', CategoryUpdateAPIView2.as_view(), name='category_update_api_view2'),
    #blog
    path('blog/<int:pk>', BlogRetrievAPIView.as_view(), name='blog_view'),
    path('blog-filter-category/<int:pk>', BlogListWithCategoryAPIView.as_view(), name='blog_filter_category_view'),
    path('blog-list-create/', BlogListCreateAPIView.as_view(), name='blog_list_create_view'),
    path('blog-delete-update/<int:pk>', BlogUpdateDeleteAPIView.as_view(), name='blog_delete_update_view'),
    # Comment
    path('comment-list/', CommentListAPIView.as_view(), name='comment_list_view'),
    path('comment/', CommentRetrievAPIView.as_view(), name='comment_list_view'),
    path('comment-list-blog/<int:id>', CommentListWithBlogAPIView.as_view(), name='comment_filter_blog_view'),
    path('comment-list-create/', CommentCreateAPIView.as_view(), name='comment_create_view'),
    path('comment-delete-update/<int:pk>', CommentDeleteUpdteAPIView.as_view(), name='comment_update_delete_view'),
]