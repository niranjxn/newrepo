
# Loops (For and While)

# Movie Ticket Booking Example

print("Checking available movie tickets:")

available_seats = ["A1", "A2", "A3", "A4", "A5"]
for seat in available_seats:
    print(f"Seat {seat} is available")

print("\nBooking seats until full:")
booked = 0
while booked < len(available_seats):
    print(f"Booking seat {available_seats[booked]}")
    booked += 1

print("All seats booked!")

print("\nSeat check (skip reserved, stop if sold out):")
for seat in ["A1", "Reserved", "A2", "Sold Out", "A3"]:
    if seat == "Reserved":
        continue
    if seat == "Sold Out":
        break
    print(f"Seat {seat} is open for booking")
