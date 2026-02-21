import psutil
import platform

# TASK 1: Create a variable to store your OS name using the skills from the video
# Hint: Use platform.system() like we did earlier
my_os = platform.system()

def monitor_my_server():
    # This line is the "Magic"—it grabs the CPU number for you
    cpu = psutil.cpu_percent(interval=1)
    
    # TASK 2: Use an F-STRING (from 27:17 in the video) to print the status
    # It should look like: "Checking [OS Name]... Current CPU: [cpu]%"
    print(f"Checking{my_os} Current CPU:{cpu}")

    # TASK 3: Use a COMPARISON (from the cheat sheet) 
    # If cpu is greater than 80, print "WARNING: High Usage!"
    if cpu > 80:
        print("WARNING: High Usage!")

# This starts the function
monitor_my_server()