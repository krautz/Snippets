def pprint(json_input, indent=4, sort_keys=True):
    import json
    print(json.dumps(json_input, indent=indent, sort_keys=sort_keys))
