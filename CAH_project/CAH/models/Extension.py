from django.db import models

# * Models where foreign keys are from:
# * from .Language import Language
# * from .Player import Player


# * Models where this model is a foreign key:
# * Extension_On_Game
# * Answer_Card
# * Question_Card


class Extension(models.Model):
    ExtensionID = models.AutoField(primary_key=True)
    ExtensionName = models.CharField(max_length=20)
    LanguageID = models.ForeignKey("Language", on_delete=models.CASCADE)
    CreatorID = models.ForeignKey("Player", on_delete=models.CASCADE)

    def __str__(self):
        return str(
            self.ExtensionID
            + " "
            + self.ExtensionName
            + " in "
            + self.LanguageID
            + " by "
            + self.CreatorID
        )
