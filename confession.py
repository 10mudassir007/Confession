def calculate_total_time(reading_time, writing_time):
    return reading_time + writing_time

def roast_feedback(total_time):
    if total_time >= 120:
        print("Oh bhai, 2 ghante confessions mein laga diye?! Kya NASA mein job lagne wali hai is se? Acha hota yehi time kisi kaam ki cheez pe lagate. Zindagi mein kuch bara karna hai ya bas yahan hi phasna hai?")
    elif total_time >= 60:
        print("Vah, lagta hai aj sirf confession scroll karne ka irada tha. 1 se 2 ghante waste karke samajhte ho tumhari life set ho jayegi? Thora focus apne real goals pe bhi rakho, shayad kuch ban jao.")
    else:
        print("Chalo, kam az kam tumne apni zindagi ke 1 ghante se kam hi barbaad kiye. Isi tarah control mein raho aur asli zindagi mein bhi kuch kar dikhane ka irada rakho!")

reading_time = []
writing_time = []
weekly_total_time = 0

for day in range(7):
    reading = int(input(f"Day {day + 1} - Enter time spent reading confessions (in minutes): "))
    writing = int(input(f"Day {day + 1} - Enter time spent writing confessions (in minutes): "))

    reading_time.append(reading)
    writing_time.append(writing)

    daily_total_time = calculate_total_time(reading, writing)
    weekly_total_time += daily_total_time

    roast_feedback(daily_total_time)
    print()

print("Weekly Summary:")
if weekly_total_time > 600:
    print("Kya baat hai, 10 ghante se zyada confessions mein ghusa hua hai? Jawan admi ho ya waqt barbaad karne ki machine? Kuch productive cheez socho, warna ye confessions tumhari CV mein nahi likhe jayenge!")
else:
    print("Wah bhai, lagta hai thoda waqt manage karna seekh rahe ho! Isi tarah apne goals par focus karo, warna ye confession wali duniya tumhe kabhi aagay nahi le jaayegi. Shabash, sahi raho!")