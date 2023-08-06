#!/usr/bin/env python3
import os
import sys
import logging

from .commands import Commands

logger = logging.getLogger(__name__)

DEFAULT_HOST = "https://app.dubhub.io"
DEFAULT_HOST_ENV = "DUBHUB_HOST"

__version__ = "0.1.3"


def main():
    host = os.environ.get(DEFAULT_HOST_ENV, DEFAULT_HOST)
    dubhub = Commands(server=host)
    # if "--dubUuid" in sys.argv and "--orgToken" not in sys.argv:
    #     logger.error("Please provide --orgToken")
    if len(sys.argv) >= 2 and sys.argv[1] == "clone":
        if (
            len(sys.argv) == 6
            and sys.argv[4] == "--dubUuid"
            and sys.argv[2] == "--orgToken"
        ):
            dub_uuid = sys.argv[5]
            org_token = sys.argv[3]
            dubhub.start_clone(dub_uuid, org_token)
        else:
            print("Usage: dubhub clone --orgToken <token> --dubUuid <dubuuid>")
    elif len(sys.argv) >= 2 and sys.argv[1] == "stop":
        if (
            len(sys.argv) == 6
            and sys.argv[4] == "--cloneUuid"
            and sys.argv[2] == "--orgToken"
        ):
            try:
                # file = open("start_clone_output.json", "r")
                # clone_conn_json = json.loads(file.read())
                # cloneUuid = json.loads(clone_conn_json)["cloneUuid"]
                org_token = sys.argv[3]
                cloneUuid = sys.argv[5]
                dubhub.stop_clone(cloneUuid, org_token)
            except FileNotFoundError as e:
                logger.error("Error reading JSON file:" + str(e))
        else:
            print("Usage: dubhub stop --orgToken <token> --cloneUuid <cloneuuid>")
    else:
        print("Usage: dubhub clone|stop [arguments]")
    # if "--analyse" == sys.argv[1]:
    #     try:
    #         file = open("start_clone_output.json", "r")
    #         clone_conn_json = json.loads(file.read())
    #         cloneUuid = json.loads(clone_conn_json)["cloneUuid"]
    #         org_token = sys.argv[3]
    #         token = sys.argv[5]
    #         dubhub.analyse_clone(cloneUuid, org_token, token)
    #     except FileNotFoundError as e:
    #         logger.error("Error reading JSON file:" + str(e))
