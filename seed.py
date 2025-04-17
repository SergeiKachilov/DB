from models import *

TABLES = [Genre, CountOfPlayers, Game]

with db:
    db.drop_tables(TABLES)
    GamePlayers = Game.genre_id.get_through_model()
    db.create_tables(TABLES)

    p1 = CountOfPlayers.create(name="Однопользовательская")
    p2 = CountOfPlayers.create(name="Многопользовательская")
    p3 = CountOfPlayers.create(name="Кооперативная")

    g1 = Genre.create(name="Хоррор")
    g2 = Genre.create(name="Приключение")

    game = Game.create(name="Call of Cthulhu", genre_id=g1)
    g2.games.add(game)