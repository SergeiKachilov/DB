from peewee import Model, AutoField, CharField, ForeignKeyField, SqliteDatabase, ManyToManyField

db = SqliteDatabase("Games.db")

class Genre(Model):
    id = AutoField()
    name = CharField(50)
    class Meta:
        database = db
        db_table = "genres"

class CountOfPlayers(Model):
    id = AutoField()
    name = CharField()
    class Meta:
        database = db
        db_table = "players"

class Game(Model):
    id = AutoField()
    name = CharField()
    genre_id = ManyToManyField(Genre, backref="games")
    count_of_players_id = ForeignKeyField(CountOfPlayers)
    class Meta:
        database = db
        db_table = "games"

