from tagme.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime

from tagme.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    template_name = "tagme/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            query.add(Q(tags__name__in=[strval]), Q.OR)
            objects = Forum.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]
        else :
            objects = Forum.objects.all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'forum_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        return retval

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


