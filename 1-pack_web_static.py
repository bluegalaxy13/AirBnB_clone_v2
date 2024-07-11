#!/usr/bin/python3
from datetime import datetime
from fabric import Connection, task

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    archive_path = 'versions/' + archive_name

    # Create versions directory if it doesn't exist
    run('mkdir -p versions')

    # Create the archive
    create = run('tar -cvzf {} web_static'.format(archive_path))

    # Check if the archive was created successfully
    if create.ok:
        return archive_path
    else:
        return None
