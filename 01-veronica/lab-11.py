hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

duration_in_min = mins + dura
final_hours = (hour + duration_in_min//60)%24
final_mins = duration_in_min % 60

# the final hours % 24 is used because for big values in mins the response will
# be higher than 24 hours and when the results hit 24 hours need to because zero and start again
# 24%24 is zero equal to midnight

print(final_hours, final_mins, sep = ":")
