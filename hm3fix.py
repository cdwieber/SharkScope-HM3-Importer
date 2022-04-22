import csv
import sqlite3
import sys

db_file = 'C:\HM3 Files\Databases\MyHM3Database.hmdb'
player_name = 'coolsage'
# id for wpn
site_id = 24


def get_hm3_tourneys():
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM tournaments'):
        print(row)


def do_update():
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Get the ID for the player we wanna edit
    player_sql = (
        "SELECT player_id FROM players WHERE playername = '{}' AND pokersite_id = {}".format(player_name, site_id))
    cur.execute(player_sql)
    player_id = cur.fetchone()[0]

    tourneys = parse_csv()
    for tourney in tourneys:
        game_id = tourney[" Game ID"]
        entrants = tourney[" Entrants"]
        buyin = int(float(tourney[" Stake"]) * 100)
        rake = int(float(tourney[" Rake"]) * 100)
        rebuy = buyin
        position = int(tourney[" Position"])
        num_rebuys = int(tourney[" ReEntries/Rebuys"]) if tourney[" ReEntries/Rebuys"] != '' else 0
        result = float(tourney[" Result"])

        winnings = 0
        if (result > 0):
            winnings = buyin + (rebuy * num_rebuys) + (result * 100)

        # get the tournament id we're working with
        cur.execute("SELECT tournament_id FROM tournaments WHERE tournament_number = {}".format(game_id))
        data = cur.fetchone()
        if data is None:
            continue
        tourney_id = data[0]


        tourney_sql = ("UPDATE tournaments SET "
                       "number_of_entrants = {}, "
                       "buyin_in_cents = {}, "
                       "rake_in_cents = {}, "
                       "rebuy_in_cents = {} "
                       "WHERE tournament_number = {}".format(entrants, buyin, rake, rebuy, game_id))
        result_sql = ("UPDATE tournament_players SET "
                      "finish_position = {}, "
                      "winnings_in_cents = {}, "
                      "number_of_rebuys = {} "
                      "WHERE tournament_id = {} AND player_id = {}".format(position, int(winnings), num_rebuys, tourney_id, player_id))

        cur.execute(tourney_sql)
        cur.execute(result_sql)
        con.commit()
        print("Updated " + game_id)


def parse_csv():
    results = []
    with open('tourneys.csv') as csvfile:
        tourneys = csv.DictReader(csvfile)
        for row in tourneys:
            results.append(row)
    return results


do_update()
