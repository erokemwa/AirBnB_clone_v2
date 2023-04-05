#!/usr/bin/python3
"""
This script defines a function do_deploy that distributes a given archive to web servers.
"""

from fabric.api import env, put, run
import os.path

# List of servers to deploy the archive to
env.hosts = ['3.229.122.175', '35.171.146.79']
env.user = "ubuntu"  # User to use when logging in to the servers
env.key_filename = '~/.ssh/school'  # Path to private key file used for authentication

def do_deploy(archive_path):
    """
    Distributes the archive at archive_path to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extracting the archive filename and name
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        path = "/data/web_static/releases/{}/".format(name)

        # Transfer the archive to the web servers
        put(archive_path, "/tmp/")

        # Creating the folder where the contents of the archive will be extracted
        run('sudo mkdir -p {}{}'.format(path, name))

        # Extracting the contents of the archive
        run('sudo tar -xzf /tmp/{} -C {}{}'.format(filename, path, name))

        # Removing the archive from the web servers
        run('sudo rm /tmp/{}'.format(filename))

        # Moving the contents of the archive to the right place
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, name))

        # Removing the now empty folder
        run("sudo rm -rf {}{}/web_static".format(path, name))

        # Updating the symbolic link to the new version of the site
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, name))

        # Printing a message to show that the deployment was successful
        print("New version deployed!")
        return True
    except BaseException:
        # If anything goes wrong, return False
        return False

