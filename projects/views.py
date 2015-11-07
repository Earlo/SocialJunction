from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse

from .models import Project

def index(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('projects/index.html')
#    context = RequestContext(request, {
#        'latest_project_list': latest_project_list,
#    })
#    return HttpResponse(template.render(context))

    context = {'latest_project_list': latest_project_list}
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'projects/detail.html', {'project': project})
