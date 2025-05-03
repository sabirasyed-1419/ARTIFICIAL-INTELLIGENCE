# Simple Vacuum Cleaner Problem (2-room world)

# Environment definition
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Agent location
location = "A"

# Simple reflex agent function
def vacuum_cleaner(location, env):
    if env[location] == "Dirty":
        print(f"Cleaning {location}")
        env[location] = "Clean"
    else:
        print(f"{location} is already clean")
    
    # Move to the next room
    next_location = "B" if location == "A" else "A"
    return next_location

# Run the agent
for _ in range(2):  # Clean both rooms
    location = vacuum_cleaner(location, environment)

print("Final Environment State:", environment)
