# Generated by Django 4.2.3 on 2023-08-04 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Card',
            fields=[
                ('AnserCardID', models.AutoField(primary_key=True, serialize=False)),
                ('AnserCardDescription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('ExtensionID', models.AutoField(primary_key=True, serialize=False)),
                ('ExtensionName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('GameID', models.AutoField(primary_key=True, serialize=False)),
                ('Active', models.BooleanField(default=True)),
                ('Password', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('LanguageID', models.AutoField(primary_key=True, serialize=False)),
                ('LanguageName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PlayerID', models.AutoField(primary_key=True, serialize=False)),
                ('PlayerName', models.CharField(max_length=50)),
                ('PlayerScore', models.IntegerField(default=0)),
                ('Birthday', models.DateField()),
                ('Mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Card',
            fields=[
                ('QuestionCardID', models.AutoField(primary_key=True, serialize=False)),
                ('QuestionCardDescription', models.CharField(max_length=100)),
                ('ExpectedAnswers', models.IntegerField(default=1)),
                ('ExtensionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.extension')),
            ],
        ),
        migrations.CreateModel(
            name='Player_On_Game',
            fields=[
                ('PlayerOnGameID', models.AutoField(primary_key=True, serialize=False)),
                ('IsCzar', models.BooleanField(default=False)),
                ('PlayerOnGameScore', models.IntegerField(default=0)),
                ('GameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.game')),
                ('PlayerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.player')),
            ],
        ),
        migrations.CreateModel(
            name='Extension_On_Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExtensionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.extension')),
                ('GameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.game')),
            ],
        ),
        migrations.AddField(
            model_name='extension',
            name='CreatorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.player'),
        ),
        migrations.AddField(
            model_name='extension',
            name='LanguageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.language'),
        ),
        migrations.CreateModel(
            name='Asked_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.game')),
                ('QuestionCardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.question_card')),
            ],
        ),
        migrations.CreateModel(
            name='Answer_Card_Of_Player_On_Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OnHold', models.BooleanField(default=True)),
                ('TemporalPosition', models.IntegerField(default=0)),
                ('AnswerCardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.answer_card')),
                ('PlayerOnGameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.player_on_game')),
            ],
        ),
        migrations.AddField(
            model_name='answer_card',
            name='ExtensionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAH.extension'),
        ),
    ]
