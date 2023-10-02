def pprint(json_input, indent=4, sort_keys=True):
    import json
    print(json.dumps(json_input, indent=indent, sort_keys=sort_keys))

def get_aws_secret(
    secret_name: str,
    region_name: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
):
    import boto3
    import json
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    pprint(json.loads(get_secret_value_response["SecretString"]))
    return get_secret_value_response

