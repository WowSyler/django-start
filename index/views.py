from django.shortcuts import render
from django.utils import timezone
from .models import Story
from .models import StoryDetail
from .models import Answers


def get_story(request):
    storys = Story.objects.all()
    return render(request,'index/home.html',{'storys':storys})


def start_story(request, id):
    story = StoryDetail.objects.get(story_id=id, fisrt=True)
    answers = Answers.objects.filter(storydetail=story)
    return render(request,'index/startstory.html',{
        'story':story,
        'answers':answers
    })

def story(request, id):
    story = StoryDetail.objects.get(id=id, fisrt=False)
    answers = Answers.objects.filter(storydetail=story)
    return render(request,'index/storydetail.html',{
        'story':story,
        'answers':answers
    })