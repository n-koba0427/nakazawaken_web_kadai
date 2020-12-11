from django.db import models


class TokoModel(models.Model):
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField('科目', max_length=50)

    def __str__(self):
        return self.name

class TokoModel2(models.Model):
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    course = models.ForeignKey(
                    Course,
                    verbose_name='カテゴリー',
                    on_delete=models.PROTECT
               )