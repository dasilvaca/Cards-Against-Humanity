from django.db import models

# Create your models here.

class Game(models.Model):
    GameID = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Password = models.CharField(max_length=20, blank=True)

class Extension_On_Game(models.Model):
    GameID = models.ForeignKey(Game, on_delete=models.CASCADE)
    ExtensionName = models.CharField(max_length=20)
    ExtensionID = models.ForeignKey('Extension', on_delete=models.CASCADE)

class Player(models.Model):
    PlayerID = models.AutoField(primary_key=True)
    PlayerName = models.CharField(max_length=50)
    PlayerScore = models.IntegerField(default=0)
    Birthday = models.DateField()
    Mail = models.EmailField(blank=False) # Mandatory mail

class Language(models.Model):
    LanguageID = models.AutoField(primary_key=True)
    LanguageName = models.CharField(max_length=20)

class Extension(models.Model):
    ExtensionID = models.AutoField(primary_key=True)
    ExtensionName = models.CharField(max_length=20)
    LanguageID = models.ForeignKey(Language, on_delete=models.CASCADE)
    CreatorID = models.ForeignKey(Player, on_delete=models.CASCADE)

class Player_On_Game(models.Model):
    PlayerOnGameID = models.AutoField(primary_key=True)
    GameID = models.ForeignKey(Game, on_delete=models.CASCADE)
    PlayerID = models.ForeignKey(Player, on_delete=models.CASCADE)
    IsCzar = models.BooleanField(default=False)
    PlayerOnGameScore = models.IntegerField(default=0)

class Answer_Card(models.Model):
    AnserCardID = models.AutoField(primary_key=True)
    AnserCardDescription = models.CharField(max_length=100)
    ExtensionID = models.ForeignKey(Extension, on_delete=models.CASCADE)

class Answer_Card_Of_Player_On_Game(models.Model):
    PlayerOnGameID = models.ForeignKey(Player_On_Game, on_delete=models.CASCADE)
    AnswerCardID = models.ForeignKey(Answer_Card, on_delete=models.CASCADE)
    OnHold = models.BooleanField(default=True)

class Question_Card(models.Model):
    QuestionCardID = models.AutoField(primary_key=True)
    ExtensionID = models.ForeignKey(Extension, on_delete=models.CASCADE)
    QuestionCardDescription = models.CharField(max_length=100)
    ExpectedAnswers = models.IntegerField(default=1)

class Asked_Card(models.Model):
    QuestionCardID = models.ForeignKey(Question_Card, on_delete=models.CASCADE)
    GameID = models.ForeignKey(Game, on_delete=models.CASCADE)


class Extension_On_Game(models.Model):
    GameID = models.ForeignKey(Game, on_delete=models.CASCADE)
    ExtensionID = models.ForeignKey('Extension', on_delete=models.CASCADE)