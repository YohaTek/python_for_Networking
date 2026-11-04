devices = ["ASA", "NEXUS", "CATALYST", "NEXUS", "asa"]

# dir() shows the available functions for the object devices
print(dir(devices))

# count is one of those functions; help() documents how to use it
help(devices.count)

print(devices.count("NEXUS"))

