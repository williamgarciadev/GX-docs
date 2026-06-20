---
title: "Load balancing considerations"
source_id: 45291
source_url: https://wiki.genexus.com/commwiki/wiki?45291
genexus_version: "18"
---

# Load balancing considerations

This article states several considerations to take into account to run a web application or service in a load-balancing environment.

Those considerations must be taken into account by architects, developers, and the operations team.

## [Scenario](#Scenario)

The scenario that is covered here is the one of (a) Browsers or other applications (clients) connecting (or making requests) to (b) a Load balancer that 'balances the load' of (c) a Web application or service running in several instances of a farm or cluster and that connect to (d) one or several databases and other external resources or services.

## [Considerations and Recommendations](#Considerations+and+Recommendations)

The following considerations and recommendations may affect

* architecture decisions (eg.: using a distributed caching engine or not)
* how you develop your application (eg.: decide if you use Blobs or not)
* the configuration of your application (eg.: how you handle Logging),
* the configuration of the Load Balancer (eg.: using sticky sessions or not)
* the configuration of each instance of the farm (eg.: configuring containers to allow storing temporary files or not)

### [Session state](#Session+state)

Handling this is required in applications that need to maintain session information between requests.

The following GeneXus features or feature options require session state handling:

* [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321)
* [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) with a value different than 'Site key'
* [On session timeout property](https://wiki.genexus.com/commwiki/wiki?17458) with value 'WARN'
* [PopUp command](https://wiki.genexus.com/commwiki/wiki?6226)
* [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) with value 'True'

If you use one or more of those options, then use some way of session replication, persistence or Server Affinity (Sticky Sessions).  
More information at [Session state handling](https://wiki.genexus.com/commwiki/wiki?45308).

### [URLs](#URLs)

All links to local resources or objects that GeneXus returns are relative to the web app, so you do not need to do anything unless you want to explicitly create and return an absolute URL to the browser or client. If you need an absolute URL you must get the base path from the database or from a configuration file and then create the string with the absolute URL using the base path + the relative path using the [Link Function](https://wiki.genexus.com/commwiki/wiki?8444).

### [[File data type](https://wiki.genexus.com/commwiki/wiki?6915)](#wiki%3F6915%2CFile%2Bdata%2Btype+File+data+type)

Avoid using the local file system for persisting files. Use an external storage provider, specifically the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) for that.

If you can not avoid it, then use [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,).

Note that storing files may not be allowed by the [PaaS](https://wiki.genexus.com/commwiki/wiki?32096,,) or given infrastructure configuration.

### [[Blob data type](https://wiki.genexus.com/commwiki/wiki?6704)](#wiki%3F6704%2CBlob%2Bdata%2Btype+Blob+data+type)

Avoid using this data type, use [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) instead.

If you can not avoid it, then use [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,).  
Note that when this data type is used, temporary files are stored and this may not be allowed by the PaaS or given infrastructure configuration.

### [[BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420), [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529), [Video data type](https://wiki.genexus.com/commwiki/wiki?16608)](#wiki%3F40420%2CBlobFile%2Bdata%2Btype+BlobFile+data+type%2C+wiki%3F15204%2CImage%2Bdata%2Btype+Image+data+type%2C+wiki%3F16529%2CAudio%2Bdata%2Btype+Audio+data+type%2C+wiki%3F16608%2CVideo%2Bdata%2Btype+Video+data+type)

Use Object storage to persist those, by setting the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) to an external storage provider or using [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087). Using an external storage provider, you avoid overloading the database with these binaries and also reduce the workload of the database and application servers since the traffic that results from requests that the browsers do to those resources will not affect them.

If you can not use Object storage to persist those, then use [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,).

### [Sockets](#Sockets)

When using web notification features ([Client.Socket External Object](https://wiki.genexus.com/commwiki/wiki?41299), [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442)), use an independent socket server, if not, broadcasts will not reach the browsers as expected.

More information: [HowTo: Receiving and processing a notification message from an external app](https://wiki.genexus.com/commwiki/wiki?33633)

### [Caching](#Caching)

As stated in [Caching in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28166,,), the applications use caching mechanisms in several cases. Set up and use [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136).

If you can not use a distributed caching provider, then use [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,).

### [Logging](#Logging)

Log information is created by generated programs and by [Log external object](https://wiki.genexus.com/commwiki/wiki?37872).

Use agents to capture and send it to an external or centralized repository.

eg.:

* [FileBeat for Elastic Stack (ELK Stack)](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-getting-started.html )
* [Cloudwatch on AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html)

### [Smart Devices applications](#Smart+Devices+applications)

All the above-mentioned considerations apply to the rest services that are on the server-side of Smart Devices Applications.

If [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370) is set 'On' (which is the default setting), refer to the above-mentioned recommendations for Caching.

Additionally, avoid reading in a Load Event or User Event variables assigned in the Start. If you can not avoid it, refer to the above-mentioned recommendations for [Session state handling](https://wiki.genexus.com/commwiki/wiki?45308).

### [Applications with [Integrated Security](https://wiki.genexus.com/commwiki/wiki?24746) or [GXflow](https://wiki.genexus.com/commwiki/wiki?17835)](#Applications+with+wiki%3F24746%2CToc%253AGeneXus%2BAccess%2BManager%2B%2528GAM%2529+Integrated+Security+or+wiki%3F17835%2CCategory%253AGXflow%2BClient+GXflow)

GAM and GXflow internally use

* [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321)
* [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)
* [Caching in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28166,,)
* [Log external object](https://wiki.genexus.com/commwiki/wiki?37872)

So take into account the considerations stated in the corresponding sections of this document.

###


|  |
| --- |
| **Backlinks** |
| [Considerations for building and deploying applications to containers](https://wiki.genexus.com/commwiki/wiki?45309) | [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416) | [Toc:Scalability and Performance of GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45280) |
| [Stateless vs Statefull](https://wiki.genexus.com/commwiki/wiki?45284) |

---
