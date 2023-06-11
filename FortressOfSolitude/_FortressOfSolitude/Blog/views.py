"""
DBA 1337_TECH, AUSTIN TEXAS © MAY 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

from _FortressOfSolitude.core.utils import UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (ArchiveIndexView, CreateView, DeleteView, DetailView, MonthArchiveView,
                                  YearArchiveView)

from .decorators import require_authenticated_permission
from .forms import PostForm, SecurePostForm, PublicSecurePostForm
from .models import Post, SecureDataAtRestPost, SecureDataAtRestPostPublic
from .utils import (
    AllowFuturePermissionMixin, DateObjectMixin,
    PostFormValidMixin, PostGetMixin, SecurePostGetMixin)


# Create your views here.
def greeting(request):
    return HttpResponse('Welcome to 1337_Tech Blog')


@require_authenticated_permission(
    'Blog.view_post')
class PostDetail(PostGetMixin, DetailView):
    model = Post


@require_authenticated_permission(
    'Blog.add_post')
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post


@require_authenticated_permission(
    'Blog.add_post')
class SecurePostUpdate(PostFormValidMixin, UpdateView):
    form_class = SecurePostForm
    model = SecureDataAtRestPost
    template_name = 'Blog/secureNote_form_update.html'

@require_authenticated_permission(
    'Blog.add_post')
class PublicSecurePostUpdate(PostFormValidMixin, UpdateView):
    form_class = PublicSecurePostForm
    model = SecureDataAtRestPostPublic
    context_object_name = "blog_securepost_public_update"
    template_name = 'Blog/public_secureNote_form_update.html'


@require_authenticated_permission(
    'Blog.delete_post')
class PostDelete(PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')


@require_authenticated_permission(
    'Blog.delete_post')
class SecurePostDelete(SecurePostGetMixin, DeleteView):
    date_field = 'pub_date'
    model = SecureDataAtRestPost
    # template_name = 'blog/secureNote_confirm_delete.html'
    queryset = (
        SecureDataAtRestPost.objects
        .select_related('author')
        # .prefetch_related('startups')
        .prefetch_related('tags')
    )
    success_url = reverse_lazy('blog_securepost_list')

@require_authenticated_permission(
    'Blog.delete_post')
class PublicSecurePostDelete(SecurePostGetMixin, DeleteView):
    date_field = 'pub_date'
    context_object_name = "blog_securepost_public_delete"
    model = SecureDataAtRestPostPublic
    template_name = 'blog/public_secureNote_confirm_delete.html'
    queryset = (
        SecureDataAtRestPost.objects
        .select_related('author')
        # .prefetch_related('startups')
        .prefetch_related('tags')
    )
    success_url = reverse_lazy('blog_securepost_public_list')


@require_authenticated_permission(
    'Blog.add_post')
class PostCreate(PostFormValidMixin, CreateView):
    form_class = PostForm
    model = Post


@require_authenticated_permission(
    'Blog.add_post')
class SecurePostCreate(PostFormValidMixin, CreateView):
    form_class = SecurePostForm
    model = SecureDataAtRestPost
    template_name = 'Blog/securenote_form.html'

@require_authenticated_permission(
    'Blog.add_post')
class PublicSecurePostCreate(PostFormValidMixin, CreateView):
    form_class = PublicSecurePostForm
    model = SecureDataAtRestPostPublic
    context_object_name = 'blog_securepost_public_create'
    template_name = 'Blog/secureNote_public_form.html'


@require_authenticated_permission(
    'Blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    date_field = 'pub_date'
    model = Post
    success_url = reverse_lazy('blog_post_list')


@require_authenticated_permission(
    'Blog.view_post')
class PostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    queryset = (
        Post.objects
        .select_related('author')
        # .prefetch_related('startups')
        .prefetch_related('tags')
    )


@require_authenticated_permission(
    'Blog.view_post')
class SecurePostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    queryset = (
        SecureDataAtRestPost.objects
        .select_related('author')
        # .prefetch_related('startups')
        .prefetch_related('tags')
    )

    context_object_name = 'secureNote_detail'
    template_name = 'Blog/securedataatrestpost_detail.html'


class PublicSecurePostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    queryset = (
        SecureDataAtRestPostPublic.objects
        .select_related('author')
        .prefetch_related('tags')
    )

    context_object_name = 'secureNote_public_detail'
    template_name = 'Blog/public_secureNote_detail.html'


@require_authenticated_permission(
    'Blog.view_post')
class PostList(
    AllowFuturePermissionMixin,
    ArchiveIndexView):
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'Blog/post_list.html'


@require_authenticated_permission(
    'Blog.view_post')
class SecurePostList(
    AllowFuturePermissionMixin,
    ArchiveIndexView):
    allow_empty = True
    context_object_name = 'securepost_list'
    date_field = 'pub_date'
    make_object_list = True
    model = SecureDataAtRestPost
    paginate_by = 5
    template_name = 'Blog/secureNote_list.html'

class PublicSecurePostList(
    AllowFuturePermissionMixin,
    ArchiveIndexView):
    allow_empty = True
    context_object_name = 'blog_securepost_public_list'
    date_field = 'pub_date'
    make_object_list = True
    model = SecureDataAtRestPostPublic
    paginate_by = 5
    template_name = 'Blog/public_secureNote_list.html'


# @require_authenticated_permission(
#   'Blog.change_post')
class PostUpdate(
    PostFormValidMixin,
    DateObjectMixin,
    UpdateView):
    date_field = 'pub_date'
    form_class = PostForm
    model = Post


@require_authenticated_permission(
    'Blog.view_post')
class PostArchiveMonth(
    AllowFuturePermissionMixin,
    MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


@require_authenticated_permission(
    'Blog.view_post')
class PostArchiveYear(
    AllowFuturePermissionMixin,
    YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


@require_authenticated_permission(
    'Blog.view_post')
class SecurePostArchiveYear(
    AllowFuturePermissionMixin,
    YearArchiveView):
    allow_empty = True
    context_object_name = 'securepost_archive_year'
    date_field = 'pub_date'
    make_object_list = True
    model = SecureDataAtRestPost
    paginate_by = 5
    template_name = 'Blog/secureNote_archive_year.html'


class PublicSecurePostArchiveYear(
    AllowFuturePermissionMixin,
    YearArchiveView):
    allow_empty = True
    context_object_name = 'blog_securepost_public_archive_year'
    date_field = 'pub_date'
    make_object_list = True
    model = SecureDataAtRestPostPublic
    paginate_by = 5
    template_name = 'Blog/public_secureNote_archive_year.html'


@require_authenticated_permission(
    'Blog.view_post')
class SecurePostArchiveMonth(
    AllowFuturePermissionMixin,
    MonthArchiveView):
    model = SecureDataAtRestPost
    make_object_list = True
    date_field = 'pub_date'
    month_format = '%m'
    paginate_by = 5
    context_object_name = 'securepost_archive_month'
    template_name = 'Blog/secureNote_archive_month.html'

class PublicSecurePostArchiveMonth(
    AllowFuturePermissionMixin,
    MonthArchiveView):
    model = SecureDataAtRestPostPublic
    make_object_list = True
    date_field = 'pub_date'
    month_format = '%m'
    paginate_by = 5
    context_object_name = 'blog_securepost_public_archive_month'
    template_name = 'Blog/public_secureNote_archive_month.html'
