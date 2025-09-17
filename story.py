def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print()
    print("The sword pulses with ancient power. An inscription reads:")
    print("\"Only the worthy may wield me.\"")
    print()
    
    # Heroic choices
    print("What do you do?")
    print("1. Attempt to pull the sword from the stone")
    print("2. Examine the sword more carefully") 
    print("3. Leave the sword and continue your journey")
    print("4. Call out to see if anyone owns the sword")
    
    choice = input("Choose your action (1-4): ").strip()
    
    if choice == "1":
        print("\nYou grasp the hilt with both hands...")
        print("A surge of energy flows through you!")
        print("The stone cracks and the sword slides free effortlessly! ⚔️")
        print("You are worthy! The Sword of Light is now yours!")
        print("+100 Hero Points! You feel empowered to face any challenge!")
        
    elif choice == "2":
        print("\nYou notice ancient runes along the blade:")
        print("\"Courage honors the heart, not the strength of arm.\"")
        print("You realize true worth comes from within.")
        print("The sword glows brighter and rises to meet your hand! ✨")
        print("You have gained the Sword of Wisdom!")
        print("+80 Wisdom Points!")
        
    elif choice == "3":
        print("\nYou decide to leave the sword for a more worthy hero.")
        print("As you turn to leave, a beam of light surrounds you!")
        print("The sword recognizes your humility and follows you! 🌟")
        print("You have gained a loyal magical companion!")
        print("+90 Humility Points!")
        
    elif choice == "4":
        print("\nYou call out: \"Is anyone there?\"")
        print("An ancient forest spirit appears before you!")
        print("\"Your respect for ownership shows great character,\" it says.")
        print("The spirit blesses you with the sword's power! 🧚")
        print("You gain the Spirit's Protection!")
        print("+85 Honor Points!")
        
    else:
        print("\nYou hesitate too long...")
        print("The sword's glow fades and vanishes into the stone.")
        print("A voice echoes: \"Indecision is the enemy of destiny.\"")
        print("You continue your journey empty-handed. 😔")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()