from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=50,verbose_name="名字")
    qq = models.CharField(max_length=10)
    addr = models.TextField(verbose_name="地址")
    email = models.EmailField()
    class Meta:
      verbose_name = '作者'
      verbose_name_plural = '作者'
 
    def __str__(self):
        return self.name
 
 
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,verbose_name="作者") #引用时候以1,2,3代表
    content = models.TextField(verbose_name="内容")
    score = models.IntegerField(verbose_name="打分")  # 文章的打分
    tags = models.ManyToManyField('Tag',verbose_name="标记")
    class Meta:
       verbose_name = '文章'
       verbose_name_plural = '文章'
 
    def __str__(self):
        return self.title
 
 
class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name="名称")
    class Meta:
        verbose_name = '标记'
        verbose_name_plural = '标记'
 
    def __str__(self):
        return self.name
