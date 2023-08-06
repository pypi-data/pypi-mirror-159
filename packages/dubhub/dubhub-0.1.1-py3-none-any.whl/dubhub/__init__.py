#!/usr/bin/env python3
import os
import sys
import json
import logging

from .commands import Commands

logger = logging.getLogger(__name__)

DEFAULT_HOST = "https://app.dubhub.io"
DEFAULT_HOST_ENV = "DUBHUB_HOST"

__version__ = "0.1.1"


def main():
    host = os.environ.get(DEFAULT_HOST_ENV, DEFAULT_HOST)
    dubhub = Commands(server=host)
    if "--dubUuid" in sys.argv and "--orgToken" not in sys.argv:
        logger.error("Please provide --orgToken")
    if "--dubUuid" in sys.argv and "--orgToken" in sys.argv:
        dub_uuid = sys.argv[4]
        org_token = sys.argv[2]
        dubhub.start_clone(dub_uuid, org_token)
    if "--orgToken" in sys.argv and "--cloneUuid" in sys.argv:
        try:
            # file = open("start_clone_output.json", "r")
            # clone_conn_json = json.loads(file.read())
            # cloneUuid = json.loads(clone_conn_json)["cloneUuid"]
            org_token = sys.argv[2]
            cloneUuid = sys.argv[4]
            dubhub.stop_clone(cloneUuid, org_token)
        except FileNotFoundError as e:
            logger.error("Error reading JSON file:" + str(e))
    if "--analyse" == sys.argv[1]:
        try:
            file = open("start_clone_output.json", "r")
            clone_conn_json = json.loads(file.read())
            cloneUuid = json.loads(clone_conn_json)["cloneUuid"]
            org_token = sys.argv[3]
            token = sys.argv[5]
            dubhub.analyse_clone(cloneUuid, org_token, token)
        except FileNotFoundError as e:
            logger.error("Error reading JSON file:" + str(e))
