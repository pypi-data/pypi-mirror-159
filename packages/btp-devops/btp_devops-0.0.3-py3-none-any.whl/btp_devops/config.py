import json


class RawConfig:
    def __init__(self, config_name, config_dir_path, default_config_name="config"):
        self.config_name = config_name
        self.config_dir_path = config_dir_path
        self.default_config_name = default_config_name

    def get_config(self):
        config_file_path = f"{self.config_dir_path}/{self.config_name}.json"

        default_config_name = f"{self.default_config_name}.json"
        default_config_file_path = f"{self.config_dir_path}/{default_config_name}"

        with open(default_config_file_path, "r+", encoding="utf-8") as base_json_file:
            base_json_dict = json.load(base_json_file)
            with open(config_file_path, "r+", encoding="utf-8") as json_file:
                json_dict = json.load(json_file)

                merged_dict = base_json_dict | json_dict
                return merged_dict
