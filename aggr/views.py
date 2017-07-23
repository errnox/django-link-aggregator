from django.template import Context, loader
from aggr.models import Post
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_posts_list = Post.objects.all().order_by('-created')[:20]
    t = loader.get_template('aggr/index.html')
    c = Context({
            'latest_posts_list': latest_posts_list,
            })
    return HttpResponse(t.render(c))
    # Simple way
    # output = ', '.join([p.question for p in latest_posts_list])
    # return HttpResponse(output)

def detail(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render_to_response('aggr/detail.html', {'post': p})
    # Long version
    # c = Context({
    #         'latest_posts_list': latest_posts_list,
    #         })
    # return HttpResponse(t.render(c))

