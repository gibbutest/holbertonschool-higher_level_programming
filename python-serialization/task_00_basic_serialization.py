""" The module """

import json

def serialize_and_save_to_file(data, filename):
    """ Convert dict to json and save to file """

    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """ Load json from file and convert to dict """

    with open(filename) as file:
        data = json.load(file)
    return data
