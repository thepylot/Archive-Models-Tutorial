from django.db import models

class BasePostModel(models.Model):

    class Meta:
        abstract=True
    
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Post(BasePostModel):
    pass

class PostArchive(BasePostModel):
    pass
