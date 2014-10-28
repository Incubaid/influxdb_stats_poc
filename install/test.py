#fabric install script (not using jumpscale)

#install jumpscale (from code)
#install influxdb (jpackage)
#install hekad (jpackage)

from fabric.api import *

@task
def hostname():
    run("cat /etc/hostname")
