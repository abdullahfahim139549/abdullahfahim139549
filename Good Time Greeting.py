import datetime
now = datetime.datetime.now()
hour = now.hour
if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = " Good Afternoon"
else:
    greeting = "Good Evening"
print(f"{greeting}!")