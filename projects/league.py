matches = [
    # (home, away, home_goals, away_goals)
    ("Gor Mahia", "Tusker", 2, 1),
    ("AFC Leopards", "KCB", 0, 0),
    ("Kariobangi Sharks", "Gor Mahia", 1, 3),
    ("Tusker", "AFC Leopards", 2, 2),
    ("KCB", "Kariobangi Sharks", 1, 0),
    ("Gor Mahia", "KCB", 4, 1),
    ("AFC Leopards", "Tusker", 1, 3),
    ("Kariobangi Sharks", "AFC Leopards", 2, 2),
]

teams = ["Gor Mahia", "AFC Leopards", "Kariobangi Sharks", "Tusker", "KCB"]

def get_result(home_goals,away_goals):
 
    if home_goals > away_goals :
        return "home"
    elif away_goals > home_goals:
        return "away"
    else:
        return "draw"



for home,away , home_goals , away_goals in matches:
    
    result = get_result(home_goals,away_goals)
    
    print(f"{home} {home_goals} vs {away_goals} {away}")
    print(f"Result: {result}")
    print("--------------------")
    
    
