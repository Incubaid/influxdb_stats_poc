#fabric install script (not using jumpscale)

#install jumpscale (from code)
#install influxdb (jpackage)
#install hekad (jpackage)

from fabric.api import *

@task
def base():
    """
    update ubuntu & install required packages
    """
    env.warn_only=True
    run("apt-get update")
    env.warn_only=False
    run("apt-get upgrade -y")
    run("apt-get install mc python-git git ssh python2.7 python-requests python-apt openssl ca-certificates python-pip ipython -y")
    run("apt-get install byobu tmux libmhash2 -y")

@task
def js():
    """
    install jumpscale
    """
    run("pip install https://github.com/Jumpscale/jumpscale_core/archive/master.zip")
    run("jpackage mdupdate")
    run("jpackage install -n base -r")
    run("jpackage install -n core -r --debug")
    run("jpackage install -n libs -r --debug")

@task
def influxdb():  
    run("jpackage install -n influxdb -i main -r --data=\"influxdb.seedservers:\"")
    cmd="""
#install influxdb client
jpackage install -n influxdb_client -i main -r --data="\
influxdb.client.addr=localhost #\
influxdb.client.port=8086 #\
influxdb.client.login=root #\
influxdb.client.passwd=root"
"""
    run(cmd)

@task
def hekad(): 
    cmd="""
#install hekad
jpackage install -n hekad -r --data="\
hekad.upstart=1"
"""
    run(cmd)
    
@task(default=True)
def all():
    """
    will do all
    """
    base()
    js()
    influxdb()
    hekad()



