#!/usr/bin/env python3
# coding=utf-8
from os import environ, chmod, lstat
import stat
from os.path import isfile
import yaml

default = """#settings for pubstore-client 
ip: 127.0.0.1
port: 5555
user: romeo
pass: ilovejuliet
"""

user_conf_path = "%s/.pubstore-client.yml" % environ['HOME']
sys_conf_path = "%s/pubstore-client.yml" % "/etc/pubstore"


def check_perms(path):
    if oct(stat.S_IMODE(lstat(path).st_mode)) in ["0o600"]:
        pass
    else:
        print(path, "has wrong permissions. adjusting")
        chmod(path, 0o600)


def load_cfg(path):
    check_perms(path)
    return yaml.safe_load(
        open(path)
    )


def start_up():
    if isfile(user_conf_path):
        cfg = load_cfg(user_conf_path)

    elif isfile(sys_conf_path):
        cfg = load_cfg(sys_conf_path)

    else:
        print("no valid config found. creating..")
        with open(user_conf_path, "w") as cf:
            cf.write(default)

        cfg = load_cfg(user_conf_path)

    return cfg


config = start_up()
