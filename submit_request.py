import requests

url = "http://127.0.0.1:8000/classify"  # adjust if your FastAPI runs elsewhere

mushroom_data = {
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

response = requests.post(url, json=mushroom_data)
print(response.json())
