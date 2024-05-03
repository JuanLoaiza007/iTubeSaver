import json

debug = True


def print_debug(message):
    new_message = "[JSONUtils.py]: " + message
    if debug:
        print(new_message)


class JSONUtils:
    @staticmethod
    def read_downloads_register():
        return JSONUtils.read_json("./data/register.json")

    @staticmethod
    def write_downloads_register(data):
        return JSONUtils.write_json("./data/register.json", data)

    @staticmethod
    def read_json(file_path):
        print_debug(f"Reading JSON from file: {file_path}")
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print_debug(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print_debug(f"JSON decode error: {e}")
            return None

    @staticmethod
    def write_json(file_path, data):
        print_debug(f"Writing JSON to file: {file_path}")
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            print_debug("JSON write successful.")
            return True
        except Exception as e:
            print_debug(f"Error writing JSON to file: {e}")
            return False
