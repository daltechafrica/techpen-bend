from django.db import models
import uuid

# Create your models here.
class Blog(models.Model):
    # author =
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(  default=uuid.uuid4, unique=True, 
                            primary_key=True, editable=False    )    
    # image = 

    def __str__(self) -> str:
        return self.title

class Review(models.Model):

    VOTE_TYPE = (
        ('5 ⭐', '⭐⭐⭐⭐⭐ 5'),
        ('4 ⭐', '⭐⭐⭐⭐ 4'),
        ('3 ⭐', '⭐⭐⭐ 3'),
        ('2 ⭐', '⭐⭐ 2'),
        ('1 ⭐', '⭐ 1',),
        ('down',   '👎 thumbs-down',)
    )

    #owner = 
    blog = models.ForeignKey( Blog, on_delete= models.CASCADE, null= True, blank= True )
    # above is the one project to many reviews. One to many
    body = models.TextField(null=True, blank=True)
    rate = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
