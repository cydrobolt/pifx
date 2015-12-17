def generate_auth_header(api_key):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
    }
    return headers
