def generate_auth_header(api_key):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
    }
    return headers

def arg_tup_to_dict(argument_tuples):
    """Given a set of argument tuples, set their value in a data dictionary if not blank"""
    data = dict()
    for arg_name, arg_val in argument_tuples:
        if arg_val != None:
            data[arg_name] = arg_val

    return data
