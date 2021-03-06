# Generated by Django 2.1.7 on 2019-03-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_mood_music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=300)),
                ('age', models.IntegerField(default=0)),
                ('emotion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_mood_music.Emotion')),
            ],
        ),
    ]
