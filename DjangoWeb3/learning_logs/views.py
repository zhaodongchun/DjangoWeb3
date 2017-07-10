from django.shortcuts import render
# from learning_logs.models import *
from . models import Topic
# from django.shortcuts import render_to_response

# Create your views here.

def index(request):
  
  #  return render_to_response('index.html')
  return render(request,'learning_logs/index.html')

def topics(request):
    topics=Topic.objects.order_by('date_added')
    content={'topics':topics}
    return render(request,'learning_logs/topics.html',content)