# Django Tutorial 04
For this assignment work through Part 4 of the Django tutorial at [https://docs.djangoproject.com/en/3.0/intro/tutorial04/](https://docs.djangoproject.com/en/3.0/intro/tutorial04/).

If you need to run this grading program on an application that is running on your laptop or desktop computer with a URL like http://localhost... you will need to install and use the NGrok or LocalTunnel application to get a temporary Internet-accessible URL that can be used with this application. Make sure to use Django's port 8000 and not port 8888 as is used in the above documentation.

Even though this exercise refactors three of your views as generic views, you can keep the "owner" view as an old-style view in your mysite/polls/views.py.
    ```
    def owner(request):
        return HttpResponse("Hello, world. xyz is the polls owner.")
    ```

You can mix function and class views in your mysite/polls/urls.py file as shown below:
```
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]```

You should already have a question with this text with one answer that is '42' from the previous assignment:

    Answer to the Ultimate Question
