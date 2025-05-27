import time  # To use sleep and time functions

# Step 1: Input time in seconds
seconds = int(input("Enter time in seconds: "))

# Step 2: Countdown loop
while seconds > 0:
    mins, secs = (seconds//60,seconds%60)
    timer = f'{mins:02d}:{secs:02d}'  # Format as MM:SS
    print(timer, end='\r')  # '\r' keeps it on the same line
    time.sleep(1)
    seconds =seconds-1