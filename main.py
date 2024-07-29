import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder
import subprocess


# URL for the API providing information about people in space
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Open a file to write the information
with open("iss.txt", "w") as file:
    file.write("There are currently " + str(result["number"]) + " astronauts on the ISS:\n\n")
    people = result["people"]

    # Loop through each person in space and write their information to the file
    for p in people:
        file.write(p["name"] + " - on board\n")
    
    # Get the current latitude and longitude using geocoder
    g = geocoder.ip('me')
    file.write("\nYour current lat/long is: " + str(g.latlng) + "\n")

# The file is automatically closed when the 'with' block ends

# Open the file using the default application on macOS
subprocess.run(["open", "iss.txt"])
