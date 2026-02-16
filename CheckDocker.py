import subprocess
import platform #Lego brick
my_os = platform.system()
if my_os =="Windows":
    print("Checking Windows enviroment...") 
    #login for windows goes here
    result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
elif my_os == "Linux":
    print("Checkinhg Ubuntu/Linux enviroment...")
    #logic for Linux goes here
    result = subprocess.run(["docker", "--version"], capture_output=True, text=True)

#The logic
if result.returncode ==0:
    print(f"status: Success on {my_os}!")
    print(f"Output: {result.stdout}")
else:
    print("Docker not found.")