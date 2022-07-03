from django.db import models

# Create your models here.
CATEGORY = (('business', 'ビジネス'), ('life', 'ライフ'), ('other', 'その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title