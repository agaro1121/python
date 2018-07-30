# -*- coding: utf-8 -*-

"""Github extension."""

import html
import json
import re
import subprocess
import os
from shutil import which

from albertv0 import *

from Github.CacheRepo import CacheRepo

__iid__ = "PythonInterface/v0.2"
__prettyname__ = "Github"
__version__ = "0.1"
__trigger__ = "ghh "
__author__ = "Anthony Garo"
__dependencies__ = []

cr = CacheRepo(cacheLocation()+"/com.github.agaro1121.ghh", 'example.db')
cr.create_token_table()
cr.create_repo_info_table()

def createCacheDirIfNotExist():
    try:
        os.mkdir(cacheLocation() + "/com.github.agaro1121.ghh")
    except OSError:
        info("Creation of the cache directory failed")


def isLoggedIn():
    path = cacheLocation() + "/com.github.agaro1121.ghh/ghh"
    try:
        with open(path) as f:
            token = f.read()
        if token:
            return True
        else:
            return False
    except OSError:
        info("Creation of the cache directory failed")


def handleQuery(query):
    createCacheDirIfNotExist()
    results = []
    if query.isTriggered:
        if query.string.startswith("> "):
            results.append(Item(text="> help", subtext=cacheLocation(), #subtext="View the readme",
                                completion=query.trigger + "> help"))
            # if not isLoggedIn():
            results.append(Item(text="> login", subtext="Log in this workflow",
                                completion=query.trigger + "> login"))
            results.append(Item(text="> logout", subtext="Log out this workflow",
                                completion=query.trigger + "> logout"))
            results.append(Item(text="> delete cache", subtext="Delete Github Cache",
                                completion=query.trigger + "> delete cache"))

        if query.string.startswith("login "):
            token = query.string.split(" ")[2]
            # cr.insert_token(token)
            results.append(
                Item(text="Git", subtext="%s" % query.string, completion="%s" % query.trigger,
                     actions=[UrlAction("Open Website", query.string)])
            )

    return results
