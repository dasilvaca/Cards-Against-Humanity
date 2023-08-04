from django.db import models

# * Models where foreign keys are from:
# * from .Player_On_Game import Player_On_Game
# * from .Answer_Card import Answer_Card


class Answer_Card_Of_Player_On_Game(models.Model):
    PlayerOnGameID = models.ForeignKey("Player_On_Game", on_delete=models.CASCADE)
    AnswerCardID = models.ForeignKey("Answer_Card", on_delete=models.CASCADE)
    OnHold = models.BooleanField(default=True)
    TemporalPosition = models.IntegerField(default=0)
