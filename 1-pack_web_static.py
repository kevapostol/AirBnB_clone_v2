#!/usr/bin/python3
# a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
import os.path
from os import path
from fabric.api import *
from datetime import datetime

def do_pack():
    """do pack script for compressing
    """

    is_dir = os.path.isdir('versions')
    if not is_dir:
        local('mkdir versions')
        if mkdir.failed:
                return None

    str_date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(str_date)
    check = local('tar -cvzf {} web_static'.format(path))

    if check.failed:
        return None
    else:
        return path
