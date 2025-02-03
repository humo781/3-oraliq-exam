from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from authors.baseModel import BaseModel
from authors.models import Author
from catalogs.models import Catalog
from tags.models import Tag

class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('posts:post_comments', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return self.title

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
