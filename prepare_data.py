import json


def prepare_data(raw_data: str):
    """
    Makes a JSON from provided string
    :param raw_data: str
    :return: JSON
    """
    res_dict = {}
    print(raw_data)
    temp_lst = raw_data.strip("\r\n").split("\r\n")
    method, protocol = temp_lst[0].split(" / ")
    lst_to_work = temp_lst[1:]
    for i in lst_to_work:
        key_value = i.split(": ")
        res_dict.update({key_value[0]: key_value[1]})

    res_dict.update({"Method": method, "Protocol": protocol})
    result_json = json.dumps(res_dict)
    return result_json
