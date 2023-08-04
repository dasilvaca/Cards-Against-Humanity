from django.db import models

# * Models where foreign keys are from:
# * from .Game import Game
# * from .Extension import Extension


class Extension_On_Game(models.Model):
    GameID = models.ForeignKey("Game", on_delete=models.CASCADE)
    ExtensionID = models.ForeignKey("Extension", on_delete=models.CASCADE)

    def __str__(self):
        return str(
            self.GameID
            + " has the "
            + self.ExtensionName
            + " extension identified with "
            + self.ExtensionID
        )
