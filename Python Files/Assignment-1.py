# Q1: ATM PIN Verification


correct_pin = 1234
entered_pins = [1111, 2222, 1234]

# --- FOR LOOP VERSION ---
print("--- Q1: FOR LOOP ---")
attempts = 3
granted = False

for i in range(min(len(entered_pins), attempts)):
    if entered_pins[i] == correct_pin:
        print("Access Granted")
        granted = True
        break
    else:
        tries_left = attempts - (i + 1)
        if tries_left > 0:
            print(f"Wrong PIN, {tries_left} tries left")

if not granted and len(entered_pins) >= attempts:
    print("Card Locked")


# --- WHILE LOOP VERSION ---
print("\n--- Q1: WHILE LOOP ---")
attempts = 3
i = 0
granted = False

while i < attempts and i < len(entered_pins):
    if entered_pins[i] == correct_pin:
        print("Access Granted")
        granted = True
        break
    else:
        tries_left = attempts - (i + 1)
        if tries_left > 0:
            print(f"Wrong PIN, {tries_left} tries left")
    i += 1

if not granted:
    print("Card Locked")

 
# Q2: Grocery Checkout Total


item_prices = [200, 300, 250, 400, 150]

# --- FOR LOOP VERSION ---
print("\n--- Q2: FOR LOOP ---")
total = 0
discount_applied = False

for price in item_prices:
    if total > 1000:
        discount_applied = True
    
    if discount_applied:
        total += price * 0.9
    else:
        total += price

print(f"Final total: {total}")


# --- WHILE LOOP VERSION ---
print("\n--- Q2: WHILE LOOP ---")
total = 0
discount_applied = False
i = 0

while i < len(item_prices):
    price = item_prices[i]
    
    if total > 1000:
        discount_applied = True
    
    if discount_applied:
        total += price * 0.9
    else:
        total += price
    
    i += 1

print(f"Final total: {total}")


# ============================================
# Q3: Number Guessing Game
# ============================================

secret_number = 42
guesses = [10, 60, 35, 50, 42]

# --- FOR LOOP VERSION ---
print("\n--- Q3: FOR LOOP ---")
for i, guess in enumerate(guesses):
    if guess == secret_number:
        print(f"Correct, took {i + 1} guesses")
        break
    elif guess > secret_number:
        print("Too High")
    else:
        print("Too Low")


# --- WHILE LOOP VERSION ---
print("\n--- Q3: WHILE LOOP ---")
i = 0
while i < len(guesses):
    guess = guesses[i]
    if guess == secret_number:
        print(f"Correct, took {i + 1} guesses")
        break
    elif guess > secret_number:
        print("Too High")
    else:
        print("Too Low")
    i += 1


# ============================================
# Q4: Movie Ticket Booking
# ============================================

total_seats = 100
booking_requests = [20, 30, 25, 40, 10]

# --- FOR LOOP VERSION ---
print("\n--- Q4: FOR LOOP ---")
seats_remaining = total_seats

for request in booking_requests:
    if request > seats_remaining:
        print("Not enough seats")
        break
    else:
        seats_remaining -= request

print(f"Seats remaining: {seats_remaining}")


# --- WHILE LOOP VERSION ---
print("\n--- Q4: WHILE LOOP ---")
seats_remaining = total_seats
i = 0

while i < len(booking_requests):
    request = booking_requests[i]
    if request > seats_remaining:
        print("Not enough seats")
        break
    else:
        seats_remaining -= request
    i += 1

print(f"Seats remaining: {seats_remaining}")


# ============================================
# Q5: Study Streak Tracker
# ============================================

scores = [70, 65, 80, 90, 55, 75]

# --- FOR LOOP VERSION ---
print("\n--- Q5: FOR LOOP ---")
streak = 0

for score in scores:
    if score >= 60:
        streak += 1
    else:
        print("Streak broken")
        break

print(f"Final streak length: {streak}")


# --- WHILE LOOP VERSION ---
print("\n--- Q5: WHILE LOOP ---")
streak = 0
i = 0

while i < len(scores):
    score = scores[i]
    if score >= 60:
        streak += 1
    else:
        print("Streak broken")
        break
    i += 1

print(f"Final streak length: {streak}")