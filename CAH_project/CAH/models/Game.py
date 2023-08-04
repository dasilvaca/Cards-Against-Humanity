from django.db import models

#* Models where this model is a foreign key:
#* Extension_On_Game
#* Asked_Card
#* Player_On_Game


class Game(models.Model):
    GameID = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Password = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(
            self.GameID + " " + ("is Active" if self.Active else "is not Active")
        )