1. ```
   django-admin startproject blogproject
   '''
   blogproject\
       manage.py
       blogproject\
           __init__.py
           settings.py
           urls.py
           wsgi.py
   '''
   settings.py
   LANGUAGE_CODE = 'zh-hans'
   TIME_ZONE = 'Asia/Shanghai'
   ```

2. ```
   python manage.py startapp blog
   '''
   blog\
       __init__.py
       admin.py
       apps.py
       migrations\
           __init__.py
       models.py
       tests.py
       views.py
   '''

   INSTALLED_APPS = [
     ...
     'blog',
   ]
   ```

3. ```
   from django.db import models
   class Post(models.Model):
   	title = models.CharField(max_length=70)
   	body = models.TextField()
   	created_time = models.DateTimeField()
   	excerpt = models.CharField(max_length=200, blank=True)
   	category = models.Foreignkey(Category)
   	tags = models.ManyToManyField(Tag, blank=True)
   	author = models.ForeignKey(User)
   	
   python manage.py makemigrations
   python manage.py migrate

   c = Category(name="python")
   c.save()
   user = User.objects.get(username="myuser")
   posts = Post.objects.all()

   p = Post.objects.get(title="Forever")
   p.delete()
   ```

4. ```
   #blog/urls.py
   from django.conf.urls import url
   from . import views
   urlpatterns = [
     url(r'', views.index, name='index')
   ]
   #blog/views.py
   from django.http import HttpResponse
   def index(request):
   	return HttpResponse("Welcome")
   #urls.py
   from django.conf.urls import url, include
   urlpatterns = [
     url(r'', include('blog.urls'))
   ]
   ```

5. ```
   #项目根目录下建立templates/blog/index.html
   #settings.py
   TEMPLATES = [
     ...
     'DIRS': [os.path.join(BASE_DIR, 'templates')]
   ]
   #
   def index(request):
   	return render(request, 'blog/index.html', context=[
         			'title': 'Blog',
   			])
   ```

6. ```

   ```

7. ```

   ```

8. ```

   ```

9. ```

   ```

10. ​