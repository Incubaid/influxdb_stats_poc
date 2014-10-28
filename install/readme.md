to get started:
===============


```
pip install fabric
#go to this directory (the install dir of this repo)
```

to use docker
-------------
on a system where docker is installed in jumpscale env

```python
jpackage install -n base
jpackage install -n docker

#login
##docker login #not sure this is required
#make sure latest docker is downloaded
docker pull despiegk/mc

#create new docker
jsdocker new -n mydocker --ports "7766:9766"

#to login
ssh localhost -p 9022

#to use fab, passwd does not have to be specified
fab test.hostname -H localhost:9022
```

install system (in docker)
--------------------------

```
fab deploy.base -H localhost:9022

#make sure that next time we use this docker we don't have to redo the base
docker commit mydocker despiegk/mytest  

#stop the docker & create new one
#influxdb std port = 8066
#hekad std port=
jsdocker new -n mydocker -b despiegk/mytest -p "8086:9086"

fab deploy.js -H localhost:9022
fab deploy.influxdb -H localhost:9022
fab deploy.hekad -H localhost:9022
```

remarks
-------
to restart hekad do
```
jpackage restart -n hekad
```

example fab usage
-----------------
```
fab deploy.installjs -p rooter -H localhost
fab -l #lists the different available commands

-p = passwd
-H = ipaddr
```
