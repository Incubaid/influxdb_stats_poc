Docker Monitoring
=================
cool monitoring, shows all about local docker instances

```
docker run \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```

this will install cadvisor
it will be running on port 8080

go to [http://localhost:8080/containers/docker](http://localhost:8080/containers/docker)
to see the docker monitoring
