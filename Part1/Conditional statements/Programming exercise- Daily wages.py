hr = float(input(f"Hourly wage: "))
work = int(input(f"Hours worked: "))
day = input(f"Day of the week: ").strip() .lower()
dw = hr * work #daily work!!
#wage sunday!
ws = (hr * 2) * work

if day in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday"):
    print(f"Daily wages: {dw:.1f} euros")
elif day == "sunday":
    print(f"Daily wages: {ws:.1f} euros")
else:
    print("Invalid day of the week.")
