from django.db import models

# * Models where foreign keys are from:
# * from .Question_Card import Question_Card
# * from .Game import Game


class Asked_Card(models.Model):
    QuestionCardID = models.ForeignKey("Question_Card", on_delete=models.CASCADE)
    GameID = models.ForeignKey("Game", on_delete=models.CASCADE)
