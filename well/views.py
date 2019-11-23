from django.shortcuts import render
from well.models import Post
from django.views import View

class PostListView(View):
    model = Post
    template_name = "well/list.html"

    def get(self, request) :
        post_list = Post.objects.all()
        ctx = {'post_list' : post_list}
        return render(request, self.template_name, ctx)

