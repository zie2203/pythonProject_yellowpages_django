from django.contrib.auth.models import User
from django.db import models

class category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class yellowm(models.Model):
    business_name = models.CharField(max_length=100)
    business_shortname=models.SlugField(max_length=255,unique=True)
    business_category = models.ForeignKey(category,default=1,related_name='business_category', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    is_enable = models.BooleanField(default=False)

    def __str__(self):
        return self.business_name
class Reviews(models.Model):

    STARS = (
        (1,'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'),
    )
    title=models.CharField(max_length=255)
    description=models.TextField()
    review_author=models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255,blank=True)
    rating = models.PositiveSmallIntegerField(choices=STARS, default=1)
    yellowm = models.ForeignKey(yellowm, related_name='reviewofbusiness' ,default=1, on_delete=models.CASCADE)

    def __str__(self):
          return self.title