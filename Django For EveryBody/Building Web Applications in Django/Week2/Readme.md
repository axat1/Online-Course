# Django Tutorial 03
For this assignment work through Part 3 of the Django tutorial at [https://docs.djangoproject.com/en/3.0/intro/tutorial03/](https://docs.djangoproject.com/en/3.0/intro/tutorial03/).

If you need to run this grading program on an application that is running on your laptop or desktop computer with a URL like http://localhost... you will need to install and use the NGrok or [LocalTunnel](http://www.dj4e.com/md/) application to get a temporary Internet-accessible URL that can be used with this application. 
Make sure to use Django's port 8000 and not port 8888 as is used in the above documentation.


Add the following to your mysite/polls/views.py with the required information above.
        def owner(request):
            return HttpResponse("Hello, world. xyz is the polls index.")

Make sure to check the file mysite/polls/urls.py to insure that the the path to the owner view is properly routed:
```
urlpatterns = [
    path('', views.index, name='index'),
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
You should already have created a question with this text from the previous assignment:

    Answer to the Ultimate Question
