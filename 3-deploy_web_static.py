#!/usr/bin/python3
# a Fabric script that generates a .tgz archive
# from the contents of the web_static directory


import os.path
from fabric.api import *
from fabric.contrib import files
from datetime import datetime


env.user = "ubuntu"
env.hosts = ['34.74.9.233', '18.215.156.149']


def do_pack():
    """do pack script for compressing
    """

    local('mkdir -p versions')
    str_date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(str_date)
    check = local('tar -cvzf {} web_static'.format(path))

    if check.failed:
        return None
    else:
        return path


def do_deploy(archive_path):
    """ Transfers `archive_path` to web servers
    """
    if not os.path.isfile(archive_path):
        return False
    basename = path = os.path.basename(archive_path)
    root, ext = os.path.splitext(basename)
    target = '/data/web_static/releases/{}'.format(root)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target))
        run("sudo tar -xzf /tmp/{} -C {}/".format(path, target))
        run("sudo rm /tmp/{}".format(path))
        run("sudo mv {}/web_static/* {}/".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
        print('New version deployed!')
    except:
        return False
    else:
        return True

def deploy():
    """Creates and distributes an archive to web servers
    """
    my_archive = do_pack()
    if my_archive is None:
        return False
    return do_deploy(my_archive)
