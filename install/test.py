

from fabric.api import *

@task
def hostname():
    run("cat /etc/hostname")
