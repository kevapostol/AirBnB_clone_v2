import os.path
from os import path
from fabric.api import *
import datetime

def do_pack():
    """
    return the archive path  if the archive path has been correctly generated
    """
    # is_dir = os.path.dir()

    date = datetime.datetime.now()
    archive = 'versions/web_static_{}{}{}{}{}{}'.format(date.year,
                                                        date.month,
                                                        date.day,
                                                        date.hour,
                                                        date.minute,
                                                        date.second)

    local('mkdir -p versions')
    check = local('tar -cvzf {} web_static'.format(archive))

    if check.failed:
        return None
    else:
        return archive
