# Dependencies
import sys
import subprocess
import os
import webbrowser

# Clear the terminal
os.system('cls' if os.name=='nt' else 'clear')

# Define the command to be executed
command = ['streamlit', 'run', '/Users/robertzygmuntlehr/Desktop/DataScience/BootCamp/Challenges/project1/Streamlit_Test_1.py']

# Execute the command using subprocess
subprocess.run(command)
