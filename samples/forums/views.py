from forums.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render

from forums.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    model = Forum
    template_name = "forum_list.html"

class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = "forum_detail.html"

class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forum_form.html"

class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forum_form.html"

class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forum_delete.html"

