from tagme.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from tagme.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    model = Forum
    template_name = "tagme/list.html"

class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = "tagme/detail.html"
    def get(self, request, pk) :
        x = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'forum' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text', 'tags']
    template_name = "tagme/form.html"

class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text', 'tags']
    template_name = "tagme/form.html"

class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "tagme/delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Forum, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('tagme:tagme_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "tagme/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse('tagme:tagme_detail', args=[forum.id])


