import json
import turtle
import urllib.request
import time
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

# Open the file using the default application on macOS
subprocess.run(["open", "iss.txt"])

# Set up the world map in turtle module
screen = turtle.Screen()
screen.setup(1309,720)
screen.setworldcoordinates(-180,-90,180,90)  # Set world coordinates to longitude/latitude bounds

# Load the world map image
screen.bgpic("world-map.gif")
screen.register_shape("iss-icon.gif")
iss = turtle.Turtle()
iss.shape("iss-icon.gif")
iss.setheading(45)
iss.penup()

while True:
    # Load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    # Output long and lat to the terminal
    print("\nLatitude:" + str(lat))
    print("Longitude:" + str(lon))

    # Update ISS location on the map, correcting for turtle screen coordinates
    iss.goto(lon, lat)

    # Refresh every 5 seconds
    time.sleep(5)
