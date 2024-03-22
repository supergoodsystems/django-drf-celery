import requests
import urllib3
from celery import shared_task
from celery.contrib import rdb
from polls.models import Question


@shared_task
def add(x, y):
    resp = urllib3.request("GET", "http://httpbin.org/robots.txt")
    print(resp.read())
    resp2 = requests.get("http://ip-api.com/json")
    print(resp2.json())
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def xsumip():
    resp = urllib3.request("GET", "http://ip-api.com/json")
    myip = resp.json()["query"]
    nums = [int(x) for x in myip.split(".")]
    return sum(nums)


@shared_task
def count_questions():
    return Question.objects.count()


@shared_task
def update_question(question_id, text):
    q = Question.objects.get(pk=question_id)
    q.question_text = text
    q.save()
