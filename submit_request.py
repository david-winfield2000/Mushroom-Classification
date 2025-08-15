import requests

url = "http://127.0.0.1:8000/classify"

# Test case 1: Likely edible
edible_mushroom = {
    "cap_shape": "x",
    "cap_surface": "s",
    "cap_color": "n",
    "bruises": "f",
    "odor": "n",
    "gill_attachment": "f",
    "gill_spacing": "c",
    "gill_size": "b",
    "gill_color": "n",
    "stalk_shape": "e",
    "stalk_root": "b",
    "stalk_surface_above_ring": "s",
    "stalk_surface_below_ring": "s",
    "stalk_color_above_ring": "n",
    "stalk_color_below_ring": "n",
    "veil_type": "p",
    "veil_color": "w",
    "ring_number": "o",
    "ring_type": "p",
    "spore_print_color": "n",
    "population": "a",
    "habitat": "d",
}

# Test case 2: Likely poisonous
poisonous_mushroom = {
    "cap_shape": "f",
    "cap_surface": "y",
    "cap_color": "l",
    "bruises": "t",
    "odor": "f",
    "gill_attachment": "a",
    "gill_spacing": "w",
    "gill_size": "n",
    "gill_color": "k",
    "stalk_shape": "t",
    "stalk_root": "e",
    "stalk_surface_above_ring": "f",
    "stalk_surface_below_ring": "f",
    "stalk_color_above_ring": "o",
    "stalk_color_below_ring": "o",
    "veil_type": "p",
    "veil_color": "w",
    "ring_number": "o",
    "ring_type": "p",
    "spore_print_color": "n",
    "population": "c",
    "habitat": "g",
}

# Test case 3: Likely poisonous
edible_mushroom2 = {
    "cap_shape": "x",
    "cap_surface": "y",
    "cap_color": "g",
    "bruises": "f",
    "odor": "a",
    "gill_attachment": "f",
    "gill_spacing": "c",
    "gill_size": "b",
    "gill_color": "k",
    "stalk_shape": "e",
    "stalk_root": "b",
    "stalk_surface_above_ring": "s",
    "stalk_surface_below_ring": "s",
    "stalk_color_above_ring": "w",
    "stalk_color_below_ring": "w",
    "veil_type": "p",
    "veil_color": "w",
    "ring_number": "o",
    "ring_type": "p",
    "spore_print_color": "n",
    "population": "s",
    "habitat": "d",
}

for mushroom in [edible_mushroom, poisonous_mushroom, edible_mushroom2]:
    resp = requests.post(url, json=mushroom)
    print(resp.json())
