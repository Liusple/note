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
    class Post(models.Model):
    	class Meta:
    		ordering = ["-created_time"]
    ```

14. ```
    #Ngnix/Fabric
    ```

15. ```
    #生成摘要
    复写save
    class Post(models.Model):
    	excerpt = models.CharField(max_length=200, blank=True)
    	
    	def save(self, *args, **kwargs):
    		if not self.excerpt:
    			md = ...
    			self.excerpt = strip_tags(md.convert(self.body))[:54]
    		super(Post, self).save(*args, **kwargs)
    ```

16. ```
    #基于类的通用视图ListView,DetailView
    from django.views.generic import ListView
    class IndexView(ListView):
    	model = Post
    	template_name = 'blog/index.html'
    	context_object_name = 'post_list'
    	
    urlpatterns = [
      url(r'^$', views.IndexView.as_view(), name="index"),
    ]

    class PostDetailView(DetailView):
    	model = Post
    	template_name = 'blog/detail.html'
    	context_object_name = 'post'
    	
    	def get(self, request, *args, **kwargs):
    		response = super(PostDetailView, self).get(request, *args, **kwargs)
    		self.object.increase_views()
    		return response
    		
    	def get_object(self, queryset=None):
    		post = super(PostDetailView, self).get_object(queryset=None)
    		post.body = markdown....
    		return post
            
    	def get_context_data(self, **kwargs):
    		context = super(PostDetailView, self).get_context_data(**kwargs)
    		form = CommentForm()
    		comment_list = self.object.comment_set.all()
    		context.update({
              'form': form,
              'comment_list': comment_list
    		})
    		return context
    ```

17. ```
    #分页
    1)
    class IndexView(ListView):
    	paginate_by = 10
    	...
    2)
    templates/blog/index.html
    {% if is_paginated %}
    <div class="pagination-simple">
      <!-- 如果当前页还有上一页，显示一个上一页的按钮 -->
      {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">上一页</a>
      {% endif %}
      <!-- 显示当前页面信息 -->
      <span class="current">第 {{ page_obj.number }} 页 / 共 {{ paginator.num_pages }} 页</span>
      <!-- 如果当前页还有下一页，显示一个下一页的按钮 -->
      {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">下一页</a>
      {% endif %}
    </div>
    {% endif %}
    ```

18. ```
    #聚合
    from django.db.model.aggregates import Count

    @register.simple_tag
    def get_categories():
    	return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    ```

19. ```
    #目录
    class PostDetailView(DetailView):
    	model = Post
    	template_name = 'blog/detail.html'
    	...
    	def get_object(self, queryset=None):
    		...
    		md = markdown.Markdown(
    			extensions=['markdown.extensions.extra',
    						'markdown.extensions.codehilite',
    						 TocExtension(slugify=slugify),
    		)]
    		post.body = md.convert(post.body)
    		post.toc = md.toc
    		return post
    		
    <h3 class="">
    	{{ post.toc | safe }}
    </h3>
    ```

20. ```
    #全文搜索
    1）pip install whoosh django-haystack jieba
    2）
    blogproject/settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        # 其它 app...
        'haystack',
        'blog',
        'comments',
    ]
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
            'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        },
    }
    HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

    3）
    from haystack import indexes
    from .models import Post
    class PostIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.CharField(document=True, use_template=True)
        def get_model(self):
            return Post
        def index_queryset(self, using=None):
            return self.get_model().objects.all()
    4）
    templates/search/indexes/blog/post_text.txt
    {{ object.title }}
    {{ object.body }}
    5）
    blogproject/urls.py

    urlpatterns = [
        # 其它...
        url(r'^search/', include('haystack.urls')),
    ]
    6）
    <form role="search" method="get" id="searchform" action="{% url 'haystack_search' %}">
      <input type="search" name="q" placeholder="搜索" required>
      <button type="submit"><span class="ion-ios-search-strong"></span></button>
    </form>
    7）search.html
    8）支持高亮搜索
    base.html

    <head>
        <title>Black &amp; White</title>
        ...
        <style>
            span.highlighted {
                color: red;
            }
        </style>
        ...
    </head>
    9)支持中文搜索
    from jieba.analyse import ChineseAnalyzer
    ...
    #注意先找到这个再修改，而不是直接添加  
    schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer(),field_boost=field_class.boost, sortable=True)
    10）建立索引
    python manage.py rebuild_index
    ```

21. ```

    ```

22. ​