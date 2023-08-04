from django.db import models

# * Models where foreign keys are from:
# * from .Extension import Extension

# * Models where this model is a foreign key:
# * Asked_Card


class Question_Card(models.Model):
    QuestionCardID = models.AutoField(primary_key=True)
    ExtensionID = models.ForeignKey("Extension", on_delete=models.CASCADE)
    QuestionCardDescription = models.CharField(max_length=100)
    ExpectedAnswers = models.IntegerField(default=1)
