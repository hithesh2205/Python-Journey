import random

def assign_teams(names):
    # Shuffle the list of names randomly
    random.shuffle(names)
    
    # Split the names into two teams
    mid = len(names) // 2  # Find the middle index
    team1 = names[:mid]    # First half goes to team 1
    team2 = names[mid:]    # Second half goes to team 2
    
    return team1, team2

def main():
    # Input list of names
    names = input("Enter names separated by commas: ").split(',')
    
    # Strip whitespace and ensure the list is clean
    names = [name.strip() for name in names]
    
    # Ensure there are at least two names
    if len(names) < 2:
        print("Please enter at least two names.")
        return
    
    # Assign names to two teams
    team1, team2 = assign_teams(names)
    
    # Output the results
    print(f"\nTeam 1: {', '.join(team1)}")
    print(f"Team 2: {', '.join(team2)}")

# Run the program
main()
