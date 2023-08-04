from django.db import models

# * Models where foreign keys are from:
# * from .Game import Game
# * from .Player import Player

#* Models where this model is a foreign key:
#* Answer_Card_Of_Player_On_Game



class Player_On_Game(models.Model):
    PlayerOnGameID = models.AutoField(primary_key=True)
    GameID = models.ForeignKey("Game", on_delete=models.CASCADE)
    PlayerID = models.ForeignKey("Player", on_delete=models.CASCADE)
    IsCzar = models.BooleanField(default=False)
    PlayerOnGameScore = models.IntegerField(default=0)

    def __str__(self):
        return str(
            self.PlayerOnGameID
            + " "
            + self.PlayerID
            + " in "
            + self.GameID
            + " with "
            + self.PlayerOnGameScore
            + " points"
        )
