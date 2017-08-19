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

6. ```1
   静态文件
   blog应用下建立static/blog
   {% load staticfiles %}
   <link rel="stylesheet "href="{% static 'blog/css/pace.css' %}">
   ```

7. ```python
   python manage.py createsuperuser
   #admin.py
   from django.contrib import admin
   from .models import Post
   class PostAdmin(admin.ModelAdmin):
   	list_display = ['title', 'created_time', 'category']
   admin.site.register(Post, PostAdmin)

   ```

8. ```
   urlpatterns = [
     url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
   ]

   class Post():
   	def get_absolute_url(self):
   		return reverse('blog:detal', kwargs={'pk': self.pk})
   		
   def detail(request, pk):
   	post = get_object_or_404(Post, pk=pk)
   	return render(request, 'blog/detail.html', context={'post': post})

   <h1 class=''>
   	<a href="{{ post.get_absolute.url }}">{{ post.title }}</a>
   </h1>
   ```

9. ```
   #markdown
   #pip install markdown
   import markdown
   def detail(request, pk):
   	post = get_object_or_404(Post, pk=pk)
   	post.body = markdown.markdown(post.body,
   								  extensions=[
                                       'markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.toc',
   								  ])
   	return render(request, 'blog/detail.html', context={'post': post})
   	
   #代码高亮
   #pip install Pygments
   <link rel="stylesheet" href="{% static 'blog/css/highlights/github.css' %}">
   ```

10. ```
    #使用自定义模板标签
    1)blog应用下建立templatetags，创建__init__.py，blog_tags.py
    2)blog.tags.py
    from ..models import Post
    from django import template

    register = template.Library()
    @register.simple_tag
    def get_recent_posts(num=5):
    	return Post.objects.all().order_by('-created_time')[:num]
    	
    3)base.html
    {% get_recent_posts as recent_post_list %} 
    {% for post in recent_post_list %}
    {% endfor %}
    ```

11. ```
    def category(request, pk):
    	cate = get_object_or_404(Category, pk=pk)
    	post_list = Post.objects.filter(Category=cate).order_by('-created_time')
    	return render(request, 'blog/index.html', context={'post_list': post_list})
    	
    urlpatterns = [
      url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    ]

    {% for category in category_list %}
    <li>
    	<a href="{% url 'blog:category' category.pk %}">{{ category.name }}</a>
    </li>
    {% endfor %}
    ```

12. ```
    #表单
    1) 
    class CommentForm(forms.ModelForm):
    	class Meta:
    		model = Comment
    		fields = ['name', 'email', 'url', 'text']
    2)
    def post_comment(request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

                # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
                # 然后重定向到 get_absolute_url 方法返回的 URL。
                return redirect(post)
            else:
                comment_list = post.comment_set.all()
                context = {'post': post,
                           'form': form,
                           'comment_list': comment_list
                           }
                return render(request, 'blog/detail.html', context=context)
        return redirect(post)
    3)url
    4)
    def detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.body = markdown.markdown(...)
        form = CommentForm()
        comment_list = post.comment_set.all()
        context = {'post': post,
                   'form': form,
                   'comment_list': comment_list
                   }
        return render(request, 'blog/detail.html', context=context)
     5)
     <form action="{% url 'comments:post_comment' post.pk %}" method="post" class="comment-form">
      {% csrf_token %}
      <div class="row">
        <div class="col-md-4">
          <label for="{{ form.name.id_for_label }}">名字：</label>
          {{ form.name }}
          {{ form.name.errors }}
        </div>
        <div class="col-md-4">
          <label for="{{ form.email.id_for_label }}">邮箱：</label>
          {{ form.email }}
          {{ form.email.errors }}
        </div>
        <div class="col-md-4">
          <label for="{{ form.url.id_for_label }}">URL：</label>
          {{ form.url }}
          {{ form.url.errors }}
        </div>
        <div class="col-md-12">
          <label for="{{ form.text.id_for_label }}">评论：</label>
          {{ form.text }}
          {{ form.text.errors }}
          <button type="submit" class="comment-btn">发表</button>
        </div>
      </div>    <!-- row -->
    </form>
    ```

13. ```

    ```

14. ```

    ```

15. ```

    ```

16. ```

    ```

17. ​