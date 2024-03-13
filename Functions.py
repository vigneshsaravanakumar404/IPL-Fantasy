from bs4 import BeautifulSoup
from os import system, name

def format_batter_table(html_data):
    # Parse HTML data
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the table body
    table_body = soup.find('tbody')

    # Extract table rows
    player_data = {}
    for row in table_body.find_all('tr'):
        player_info = [cell.text.strip() for cell in row.find_all('td')]
        player_name = player_info[0].split('(')[0].strip()  # Extracting player name from the first cell
        player_data[player_name] = {
            "Span": player_info[1],
            "Mat": int(player_info[2]) if player_info[2] != '-' else player_info[2],
            "Inns": int(player_info[3]) if player_info[3] != '-' else player_info[3],
            "NO": int(player_info[4]) if player_info[4] != '-' else player_info[4],
            "Runs": int(player_info[5]) if player_info[5] != '-' else player_info[5],
            "HS": player_info[6],
            "Ave": float(player_info[7]) if player_info[7] != '-' else player_info[7],
            "BF": int(player_info[8]) if player_info[8] != '-' else player_info[8],
            "SR": float(player_info[9]) if player_info[9] != '-' else player_info[9],
            "100": int(player_info[10]) if player_info[10] != '-' else player_info[10],
            "50": int(player_info[11]) if player_info[11] != '-' else player_info[11],
            "0": int(player_info[12]) if player_info[12] != '-' else player_info[12],
            "4s": int(player_info[13]) if player_info[13] != '-' else player_info[13],
            "6s": int(player_info[14]) if player_info[14] != '-' else player_info[14]
        }

    return player_data

def format_bowler_table(html_data):
    return None

def clear():
    system('cls' if name == 'nt' else 'clear')