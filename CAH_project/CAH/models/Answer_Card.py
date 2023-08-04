from django.db import models

# * Models where foreign keys are from:
# * from .Extension import Extension

#* Models where this model is a foreign key:
#* Answer_Card


class Answer_Card(models.Model):
    AnserCardID = models.AutoField(primary_key=True)
    AnserCardDescription = models.CharField(max_length=100)
    ExtensionID = models.ForeignKey("Extension", on_delete=models.CASCADE)

    def __str__(self):
        return str(
            self.AnserCardID
            + " "
            + self.AnserCardDescription
            + " in "
            + self.ExtensionID
        )
