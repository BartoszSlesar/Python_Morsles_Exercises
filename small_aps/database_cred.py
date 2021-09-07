import json as js
import os


def read_cred(path_raw):
    path = os.fspath(path_raw)
    with open(path, "r") as cred:
        data_cred = js.load(cred)["cred"]
    return data_cred
