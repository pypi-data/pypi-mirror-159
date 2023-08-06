import builtins


def dummy_arn(string_value: builtins.str):
    if "dummy-value" in string_value:
        return "arn:aws:service:eu-central-1:123456789012:entity/dummy-value"
    return string_value
