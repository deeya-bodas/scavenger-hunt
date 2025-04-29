import hashlib

with open("my_info.txt", "r") as file:
    # Remove whitespace around the netid!
    net_id = file.readline().strip()

hashed_value = hashlib.sha256(net_id.encode()).hexdigest()

# Print the hashed result to their CLI
print("Treasure Code:", hashed_value[:5])