from django.db import models
from django.utils import timezone
from django.urls import reverse


# we will be creating the models that will be useful through
# out our project that will help to keep the track of the records
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ Method to save the published date """
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        """ Method to approve the comment"""
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        """
        This is defined to use the absolute url
        """
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        """ To return the string represenation of the model in python"""
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        """
        Method to approve the comment that is added by the random user
        """
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        """
        This is defined to use the absolute url
        """
        return reverse("post_list")

    def __str__(self):
        return self.text()
