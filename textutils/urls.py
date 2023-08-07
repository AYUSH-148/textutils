"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# The single dot is a convention for the current directory.
'''Path function is contained within the django.urls module.
It helps in routing URLs to the appropriate view function within a Django project.
Now, let's discuss the arguments passed in the path function.

    1. about/: It is the endpoint of the URL. 

         Example: Let's suppose a user tries to access https://www.codewithharry.com/blog/. In this URL, 'blog' is the endpoint. 

    2. views.about: It is the function defined in the views.py file. Here, we pass the function that should be executed 
       whenever someone tries to access our website's 'about' page. 

    3. name='about': It is the name of the path. Naming a path will help us to access it from anywhere in our project. 
    In the future, we will see how to access a path from templates.'''

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name="index"),
#     path('next/',views.about,name="about")
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.rasen,name="index"),
    path('analyze',views.analyze,name="analyze"),
    path('navbar',views.navbar,name="navbar")

    # path('capitalise-first',views.capfirst,name="capfirst"),
    #
    # # GO TO THE FIRST PAGE OF THIS DJANGO WEBSITE
    # path('direct home',views.direct,name='hg')

    # go to second one

]
