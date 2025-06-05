correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Voer je wachtwoord in: ")
    if user_input == correct_password:
        print("Toegang verleend!")
        break
    else:
        attempts += 1
        print(f"Onjuist wachtwoord! Poging {attempts} / {max_attempts}")

if attempts == max_attempts:
    print("Toegang geweigerd.")