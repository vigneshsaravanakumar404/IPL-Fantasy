# Imports
from Functions import format_batter_table, format_bowler_table, clear
from requests import get

# Variables
BATTING_DATA_SOURCE = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/indian-premier-league-2023-15129"
BOWLING_DATA_SOURCE = "https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/indian-premier-league-2023-15129"

#* Main
clear()
print("\033[91mIPL Fantasy Points Calculator:\033[0m\n")

#! Batting Calculations
print("\033[92mBatting Calculations...\033[0m")
print("\033[90mRuns, Strike Rate, 0s, 50s, 100s, NOs\033[0m")

response = get(BATTING_DATA_SOURCE)
batting_data = format_batter_table(response.text)

print("\n")

#! Bowling Calculations
print("\033[92mBowling Calculations...\033[0m")
print("\033[90mWickets, Maidens, Hat-Tricks, 4+ Wickets, 5+ Wickets, 6+ Wickets, Economy Rate\033[0m")

response = get(BOWLING_DATA_SOURCE)
bowling_data = format_bowler_table(response.text)

print("\n")

#* Results
print("\033[92mResults\033[0m")
print(batting_data)
print(bowling_data)
