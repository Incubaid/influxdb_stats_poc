influxdb_grafana_poc
====================

goal demonstrate & document a end2end monitoring flow using influxdb
--------------------------------------------------------------------

what
----

* stat collection
  * use collectd on linux to sent stats to hekad
  * use http://ssc-serv.com/ which is collectd for windows

* stat aggregation
  * use hekad to aggregate stats & forward to influxdb
  * group agents in groups and aggregate certain stats e.g. IOPS over the groups & over all disks
    * create multiple levels of aggregation e.g. all disks in 1 machine for iops, all disks over all machines in 1 rack
    * so influxdb stores the aggregated values doesn't do the aggregation at query time

* stat visualization
  * create multiple dashboards in grafana to visualize stats

* docker 
  * create docker images for the server side (start from despiegk/mc docker) 
  * in the docker checkout this repo which has the required dashboards, hekascripts, ...
  * in the docker
    * influxdb
    * hekad (collectd sends to these)
    * collectd dumping to local hekad

* create howto docs
  * how to install collectd on each platform and configure to send to central hekad
  * how to get started with the docker image
  * explain with clear screenshots how to work with grafana & create new dashboards
  * explain how the hekad was configured and why
  
* what to visualize
  * iops per disk
  * disk space per disk (total,used)
  * network stats
  * ...

* snmp integration
  * install snmp agent (just to prove the point)
  * pull some info from the snmp agent and also dump to heka to get visualized later


