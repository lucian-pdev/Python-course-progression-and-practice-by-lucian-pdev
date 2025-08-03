print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

time_event_start_in_min = hour * 60 + mins                                                              # convert to min for common value with duration
time_event_end_in_min = time_event_start_in_min + dura                                                  # add duration in min
time_event_end_readable_hour = (time_event_end_in_min // 60) % 24                                       # obtain floor divided integer of hour then divide by 24 (1 day) and keep the remainder (the hour value)
time_event_end_readable_min = time_event_end_in_min % 60                                                # modulo division by 60 (1 hour) leaves the remainder as the value of minutes

print("The closing time is ", time_event_end_readable_hour, ":", time_event_end_readable_min, sep="")   # separator set to null, and manually added spaces to not leave spaces inside hour:min format.
print("The closing time is",str(time_event_end_readable_hour)+":"+str(time_event_end_readable_min))     # converted numbers to strings to use concatenation (+), keeping standard separator
