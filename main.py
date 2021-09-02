#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location):
	pass

def get_input():
	return ""

def update(current_location, location_label, response):
	return location_label


# ----------------------------------------------------------------

location_label = "West of House"
current_location = {}
response = ""

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location)
	response = get_input()


print("Thanks for playing!")