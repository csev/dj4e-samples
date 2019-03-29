from forums.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from forums.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    model = Forum
    template_name = "forum_list.html"

class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = "forum_detail.html"
    def get(self, request, pk) :
        forum = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=forum).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'forum' : forum, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


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

class CommentCreateView(View):
    def post(self, request, pk) :
        f = get_object_or_404(Forum, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse_lazy('forum_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse_lazy('forum_detail', args=[forum.id])


