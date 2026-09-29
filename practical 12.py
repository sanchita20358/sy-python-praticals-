location=(13.83,75.453)

print("GPS location",location)

print("LATITUDE:",location[0])
print("longitude:",location[1])

print("Number of location:",len(location))

print("last coordinates:",location[-1])

print("Is latitude is present:", 13.83 in location)

print("Coordinates using slicing:",location[0:2])

extra=("Pune",)
new_location=location+extra

print("Location with city:",new_location)

print("Repeated co ordinates:",location*2)


