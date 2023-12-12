correct_pin = "0805"

attempts = 0

while attempts < 3:
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("PIN code correct. Access granted.")
        break
    else:
        print("Incorrect...")
        attempts += 1

if attempts == 3:
    print("Sorry, your payment card has been blocked.")


