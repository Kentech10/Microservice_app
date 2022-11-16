from django.db import models

# creating a TalentPlus Models


class TalentPlus(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()


    def __str__(self):
        return self.title 