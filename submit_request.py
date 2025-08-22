import requests

url = "http://127.0.0.1:8000/classify"

# Test case 1: Likely edible
edible_mushroom = {
    "cap_shape": "x",  # convex
    "cap_surface": "s",  # smooth
    "cap_color": "n",  # brown
    "bruises": "f",  # no
    "odor": "n",  # none
    "gill_attachment": "f",  # free
    "gill_spacing": "c",  # close
    "gill_size": "b",  # broad
    "gill_color": "n",  # brown
    "stalk_shape": "e",  # enlarging
    "stalk_root": "b",  # bulbous
    "stalk_surface_above_ring": "s",  # smooth
    "stalk_surface_below_ring": "s",  # smooth
    "stalk_color_above_ring": "n",  # brown
    "stalk_color_below_ring": "n",  # brown
    "veil_type": "p",  # partial
    "veil_color": "w",  # white
    "ring_number": "o",  # one
    "ring_type": "p",  # pendant
    "spore_print_color": "n",  # brown
    "population": "a",  # abundant
    "habitat": "d",  # woods
}

# Test case 2: Likely poisonous
poisonous_mushroom = {
    "cap_shape": "f",  # flat
    "cap_surface": "y",  # scaly
    "cap_color": "r",  # green
    "bruises": "t",  # bruises
    "odor": "f",  # foul
    "gill_attachment": "a",  # attached
    "gill_spacing": "w",  # crowded
    "gill_size": "n",  # narrow
    "gill_color": "k",  # black
    "stalk_shape": "t",  # tapering
    "stalk_root": "e",  # equal
    "stalk_surface_above_ring": "f",  # fibrous
    "stalk_surface_below_ring": "f",  # fibrous
    "stalk_color_above_ring": "o",  # orange
    "stalk_color_below_ring": "o",  # orange
    "veil_type": "p",  # partial
    "veil_color": "w",  # white
    "ring_number": "o",  # one
    "ring_type": "p",  # pendant
    "spore_print_color": "n",  # brown
    "population": "c",  # clustered
    "habitat": "g",  # grasses
}


# Test case 3 - Edible mushroom
edible_mushroom = {
    "cap_shape": "x",  # convex
    "cap_surface": "s",  # smooth
    "cap_color": "y",  # yellow
    "bruises": "t",  # bruises
    "odor": "a",  # almond
    "gill_attachment": "f",  # free
    "gill_spacing": "c",  # close
    "gill_size": "b",  # broad
    "gill_color": "k",  # black
    "stalk_shape": "e",  # enlarging
    "stalk_root": "c",  # club
    "stalk_surface_above_ring": "s",  # smooth
    "stalk_surface_below_ring": "s",  # smooth
    "stalk_color_above_ring": "w",  # white
    "stalk_color_below_ring": "w",  # white
    "veil_type": "p",  # partial
    "veil_color": "w",  # white
    "ring_number": "o",  # one
    "ring_type": "p",  # pendant
    "spore_print_color": "n",  # brown
    "population": "n",  # numerous
    "habitat": "g",  # grasses
}

for mushroom in [edible_mushroom, poisonous_mushroom, edible_mushroom]:
    resp = requests.post(url, json=mushroom)
    print(resp.json())
