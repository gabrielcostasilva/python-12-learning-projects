someone = input("Enter a famous name: ").strip().title()
place = input("Enter a place: ").strip().lower()

weekday = ""
while weekday not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    weekday = input("Enter a weekday: ").strip().lower()

adjective = input("Enter an adjective: ").strip().lower()

print(f"{someone} cycled to the {place} on {weekday} morning with an unidentifiable, and therefore {adjective} emotion.")