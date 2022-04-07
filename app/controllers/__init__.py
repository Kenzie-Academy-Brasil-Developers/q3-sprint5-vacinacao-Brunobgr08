
TRUSTED_KEYS = ['cpf', 'name', 'vaccine_name', 'health_unit_name']


def verify_keys(data):
    trusted_keys = TRUSTED_KEYS

    err_missing_key = {
                    "required_keys": trusted_keys,
                    "sended_keys": list(data.keys())
                }

    for key in trusted_keys:
        if key not in data.keys():
            raise KeyError(err_missing_key)

    err_wrong_cpf_key = {
                    "err": "CPF must be 11 numeric characters",
                    "required_model": "12345678921",
                    "sended_key": data['cpf']
                }
    verify_data_type(data)

    if len(data['cpf']) != 11 or not int(data['cpf']):
        raise KeyError(err_wrong_cpf_key)

def verify_data_type(data:dict):
        for key in data.keys():
                if type(data[key]) != str:
                        raise TypeError({
                                "error": f"wrong type data for key '{key}'",
                                "expected": "string",
                                "received": f"{get_data_type(data[key])}"
                                })

def get_data_type(value):
    if type(value) == int:
        return 'integer'
    elif type(value) == str:
        return 'string'
    elif type(value) == float:
        return 'float'
    elif type(value) == list:
        return 'list'
    elif type(value) == dict:
        return 'dictionary'
