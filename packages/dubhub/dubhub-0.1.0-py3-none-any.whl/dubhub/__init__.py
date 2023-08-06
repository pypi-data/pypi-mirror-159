#!/usr/bin/env python3
import os
import sys
import json
import logging

import requests

logger = logging.getLogger(__name__)

DEFAULT_HOST = "https://app.dubhub.io"
DEFAULT_HOST_ENV = "https://app.dubhub.io"

__version__ = "0.1.0"


class DubHubCommands:
    def __init__(self, server):
        self.SERVER = server

    def start_clone(self, dub_uuid, org_token):
        try:
            CI_PIPELINE_ID = os.environ.get("CI_PIPELINE_ID", "GITHUB_RUN_ID")
            CI_COMMIT_REF_NAME = os.environ.get("CI_COMMIT_REF_NAME", "GITHUB_HEAD_REF")
            CI_COMMIT_SHA = os.environ.get("CI_COMMIT_SHA", "GITHUB_SHA")
            CI_MERGE_REQUEST_IID = os.environ.get("CI_MERGE_REQUEST_IID", "github")
            CI_DEFAULT_BRANCH = os.environ.get("CI_DEFAULT_BRANCH", "GITHUB_BASE_REF")
            if type(CI_MERGE_REQUEST_IID) != "str":
                CI_MERGE_REQUEST_IID = CI_MERGE_REQUEST_IID
            response = requests.post(
                f"{self.SERVER}/api/clone/start",
                json={
                    "dubUuid": dub_uuid,
                    "orgToken": org_token,
                    "CI_PIPELINE_ID": CI_PIPELINE_ID,
                    "CI_COMMIT_REF_NAME": CI_COMMIT_REF_NAME,
                    "CI_COMMIT_SHA": CI_COMMIT_SHA,
                    "CI_MERGE_REQUEST_IID": CI_MERGE_REQUEST_IID,
                    "CI_DEFAULT_BRANCH": CI_DEFAULT_BRANCH,
                },
            )
        except Exception as e:
            logger.error("Error with sending post request:" + str(e))
            # load and dump json so its formatted properly; also helps validate
            # that the json returned is proper
        try:
            print(json.dumps(json.loads(response.content)))
            pass
        except Exception as e:
            logger.error("Error converting response object to JSON file:" + str(e))

    def stop_clone(self, clone_conn_json, org_token):
        try:
            clone_conn_object = json.loads(clone_conn_json)
        except Exception as e:
            logger.error("Error converting JSON file to JSON object:" + str(e))
        try:
            requests.post(
                f"{self.SERVER}/api/clone/stop",
                json={
                    "cloneUuid": clone_conn_object["cloneUuid"],
                    "orgToken": org_token,
                },
            )
        except Exception as e:
            logger.error("Error with sending post request:" + str(e))

    def analyse_clone(self, clone_conn_json, org_token, token):
        try:
            CI_API_V4_URL = os.environ.get("CI_API_V4_URL", None)
            CI_PROJECT_ID = os.environ.get("CI_PROJECT_ID", None)
            CI_MERGE_REQUEST_IID = os.environ.get("CI_MERGE_REQUEST_IID", "github")
            if type(CI_MERGE_REQUEST_IID) != "string":
                CI_MERGE_REQUEST_IID = CI_MERGE_REQUEST_IID
            CI_DEFAULT_BRANCH = os.environ.get("CI_DEFAULT_BRANCH", "GITHUB_BASE_REF")
            GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", None)
            GITHUB_SHA = os.environ.get("GITHUB_SHA", None)
            GITHUB_REF = os.environ.get("GITHUB_REF", None)
            if GITHUB_REPOSITORY is None:
                GITHUB_OR_GITLAB = "gitlab"
            else:
                GITHUB_OR_GITLAB = "github"
            clone_conn_object = json.loads(clone_conn_json)
        except Exception as e:
            logger.error("Error converting JSON file to JSON object:" + str(e))
        try:
            requests.post(
                f"{self.SERVER}/api/clone/analyse",
                json={
                    "cloneUuid": clone_conn_object["cloneUuid"],
                    "orgToken": org_token,
                    "token": token,
                    "CI_API_V4_URL": CI_API_V4_URL,
                    "CI_PROJECT_ID": CI_PROJECT_ID,
                    "CI_MERGE_REQUEST_IID": CI_MERGE_REQUEST_IID,
                    "CI_DEFAULT_BRANCH": CI_DEFAULT_BRANCH,
                    "GITHUB_OR_GITLAB": GITHUB_OR_GITLAB,
                    "GITHUB_REPOSITORY": GITHUB_REPOSITORY,
                    "GITHUB_SHA": GITHUB_SHA,
                    "GITHUB_REF": GITHUB_REF,
                },
            )
            # print(f"See your results here: {response}")
        except Exception as e:
            logger.error("Error with sending post request:" + str(e))


def main():
    host = os.environ.get(DEFAULT_HOST_ENV, DEFAULT_HOST)
    dubhub = DubHubCommands(server=host)
    print(sys.argv[1])
    if "--dubUuid" in sys.argv and "--orgToken" not in sys.argv:
        logger.error("Please provide --orgToken")
    if "--dubUuid" in sys.argv and "--orgToken" in sys.argv:
        dub_uuid = sys.argv[2]
        org_token = sys.argv[4]
        dubhub.start_clone(dub_uuid, org_token)
    if "--orgToken" == sys.argv[1] and len(sys.argv) == 3:
        try:
            file = open("clone_connection.json", "r")
            clone_conn_json = file.read()
            org_token = sys.argv[2]
            dubhub.stop_clone(clone_conn_json, org_token)
        except FileNotFoundError as e:
            logger.error("Error reading JSON file:" + str(e))
    if "--analyse" == sys.argv[1]:
        try:
            file = open("clone_connection.json", "r")
            clone_conn_json = file.read()
            org_token = sys.argv[3]
            token = sys.argv[5]
            dubhub.analyse_clone(clone_conn_json, org_token, token)
        except FileNotFoundError as e:
            logger.error("Error reading JSON file:" + str(e))
