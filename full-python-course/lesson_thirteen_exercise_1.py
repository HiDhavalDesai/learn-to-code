# Count Down Timer
import time

# time.sleep()
# This will create a delay, therefore after x number of seconds, the next line of code will run. print("Time's Up")

my_time = int(input("Enter the time in Seconds: "))


# Another way to do this is
for x in range (my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up")



# This is the way I was doing it, it's correct, but there is a better way of doing it.
#  for secs in reversed(range(0, my_time)):
#     seconds = secs % 60
#     print(f"00:00:{seconds:02}")
#     time.sleep(1)
# print("Time's Up")