from django.db import models

#* Models where this model is a foreign key:
#* Player_On_Game
#* Extension

class Player(models.Model):
    PlayerID = models.AutoField(primary_key=True)
    PlayerName = models.CharField(max_length=50)
    PlayerScore = models.IntegerField(default=0)
    Birthday = models.DateField()
    Mail = models.EmailField(blank=False)  # Mandatory mail

    def __str__(self):
        return str(
            self.PlayerID
            + " "
            + self.PlayerName
            + " with "
            + self.PlayerScore
            + " points"
        )
