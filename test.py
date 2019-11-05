# -*- coding: utf-8 -*-

import os
import configparser
from collections import OrderedDict
from pprint import pprint

try:
    import typing
except:
    pass

DEFAULT_CREDENTIAL_FILE = os.path.join(os.path.expanduser("~"), ".aws", "credentials")
DEFAULT_CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".aws", "config")


class Profile(object):
    def __init__(self,
                 aws_access_key_id=None,
                 aws_secret_access_key=None,
                 aws_session_token=None,
                 region=None,
                 output=None,
                 role_arn=None,
                 role_session_name=None,
                 source_profile=None):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        self.region = region
        self.output = output
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self.source_profile = source_profile


class ProfileManager(object):
    def __init__(self,
                 credential_file=DEFAULT_CREDENTIAL_FILE,
                 config_file=DEFAULT_CONFIG_FILE):
        self.credential_file = credential_file
        self.config_file = config_file
        self.profiles = dict()  # type: typing.Dict[str, Profile]

    def parse(self):
        credentials = configparser.ConfigParser()
        credentials.read(self.credential_file)

        data = OrderedDict()
        for profile_name in credentials.sections():
            data.setdefault(profile_name, dict(credentials[profile_name]))

        config = configparser.ConfigParser()
        config.read(self.config_file)
        for profile_name in config.sections():
            new_profile_name = profile_name.split(" ")[-1]
            data.setdefault(new_profile_name, dict(config[profile_name]))
            data[new_profile_name].update(dict(config[profile_name]))

        self.profiles = OrderedDict([(k, Profile(**v)) for k, v in data.items()])


    def list_profile(self):
        return list(self.profiles)


from pprint import pprint

# pprint(list(config["eqtest"].keys()))

if __name__ == "__main__":
    pm = ProfileManager()
    pm.parse()
    pprint(pm.list_profile())
    pprint(pm.profiles["eq_sanhe"])