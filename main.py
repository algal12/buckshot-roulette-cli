import random

print("💀 Buckshot Roulette — You vs Dealer!")
print("One bullet in the 6-chamber revolver.")
print("Survive 3 rounds to win.\n")

bullet_position = random.randint(0, 5)
current_chamber = 0
rounds_survived = 0

while rounds_survived < 3:
    print("\nRound", rounds_survived + 1)
    print("Choose who to shoot:")
    print("1. Shoot Yourself")
    print("2. Shoot the Dealer")
    choice = input("Enter 1 or 2: ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        continue

    print("You pull the trigger...")

    # Your shot
    if current_chamber == bullet_position:
        if choice == "1":
            print("💥 BOOM! You shot yourself. Game over.")
        else:
            print("💥 BOOM! You shot the dealer. You win!")
        break
    else:
        print("🔫 Click... No bullet fired.")
        current_chamber = (current_chamber + 1) % 6

        if choice == "2":
            # Dealer's turn to shoot you
            print("\nDealer decides to shoot you...")
            print("Dealer pulls the trigger...")

            if current_chamber == bullet_position:
                print("💥 BOOM! Dealer shot you. Game over.")
                break
            else:
                print("🔫 Click... Dealer missed.")
                current_chamber = (current_chamber + 1) % 6
                rounds_survived += 1
        else:
            # You shot yourself and missed, so next round
            rounds_survived += 1

if rounds_survived == 3:
    print("\n🎉 You survived all rounds! You win.")
