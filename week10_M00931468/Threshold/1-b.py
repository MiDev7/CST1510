cast = {"Cardinal Ximenez" : "Michael Palin", "Cardinal Biggles" : "Terry Jones", "Cardinal Fang" : "Terry Gilliam"}
cast["customer"] = "John Cleese"  # Add a new property in the dictionary, which is customer with key "customer" and value "John Cleese"
cast["shopkeeper"] = "Michael Palin" # Add a new property in the dictionary, which is customer with key "shopkeeper" and value "Michael Palin"
print(cast["shopkeeper"]) # Print the value, having "shopkeeper" as key--Output: Michael Palin
print(cast["Cardinal Ximenez"]) # Print the value, having "Cardinal Ximenez" as key--Output: Michael Palin
print(cast["Cardinal Fang"]) # Print the value, having "Cardinal Fang" as key--Output: Terry Gilliam