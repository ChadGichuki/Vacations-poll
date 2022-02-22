response = {}

while True:
    name = input("What is your name: ")
    vacation = input(
        "If you could visit one place in the world, where would it be? ")

    response[name] = vacation

    question = input("Would you like someone else to take the poll? yes/no ")

    if question == 'no':
        break

print("\n********Poll Results*********")

for name, vacation in response.items():
    print(f"{name} would love to visit {vacation}")
