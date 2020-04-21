from django.db import models
from django.contrib.auth.models import User


class MinesweeperUser(models.Model):
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=70, unique=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(MinesweeperUser, self).save(*args, **kwargs)
        if is_new:
            authuser = User(username=self.username, email=self.email,
                            first_name=self.first_name, last_name=self.last_name)
            authuser.set_password(self.username)
            authuser.save()

    class Meta:
        ordering = ['id']


class MinesweeperGame(models.Model):
    user = models.ForeignKey('MinesweeperUser', on_delete=models.CASCADE)
    game_won = models.BooleanField(default=False)
    game_time = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(default='easy', max_length=45)

    def __str__(self):
        return str(self.user) + " : " + self.difficulty + ' : ' + str(self.game_time) + ' : '+ str(self.game_won)  

    class Meta:
        ordering = ['user', 'game_won', 'game_time']


class MultiplayerGame(models.Model):
    player_one = models.ForeignKey('MinesweeperUser', on_delete=models.CASCADE, related_name="player1")
    player_two = models.ForeignKey('MinesweeperUser', on_delete=models.CASCADE, related_name="player2")
    difficulty = models.CharField(default='easy', max_length=45) 
    gameover = models.BooleanField(default=False)
    game_winner = models.ForeignKey('MinesweeperUser', on_delete=models.CASCADE, related_name="game_winner")
    date = models.DateTimeField(auto_now=True)
    game_code = models.CharField(default='WRONG', max_length=45, unique=True)

    def __str__(self):
        return str(self.player_one) + " : " + str(self.player_two) + ' : ' + str(self.date)

    class Meta:
        ordering = ['player_one', 'player_two', 'date']
