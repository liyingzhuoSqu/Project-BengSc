from django.db import models

# Create your models here.
class QMusic(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    song_name = models.CharField(max_length=20, verbose_name='歌曲')
    singer_name = models.CharField(max_length=20, verbose_name='歌手')
    times = models.CharField(max_length=10, verbose_name='时长')

class WMusic(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    song_name = models.CharField(max_length=20, verbose_name='歌曲')
    singer_name = models.CharField(max_length=20, verbose_name='歌手')
    times = models.CharField(max_length=10, verbose_name='时长')

class KMusic(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    song_name = models.CharField(max_length=20, verbose_name='歌曲')
    singer_name = models.CharField(max_length=20, verbose_name='歌手')
    times = models.CharField(max_length=10, verbose_name='时长')