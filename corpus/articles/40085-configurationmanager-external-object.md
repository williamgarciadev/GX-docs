---
title: "ConfigurationManager external object"
source_id: 40085
source_url: https://wiki.genexus.com/commwiki/wiki?40085
genexus_version: "18"
---

# ConfigurationManager external object

The ConfigurationManager external object allows you to read the application configuration at runtime.  
This means that you have a way to access the configuration that is being used at runtime and has been set in environment variables (only the variables explained in [this](https://wiki.genexus.com/commwiki/wiki?39459) document) or configuration files (a.k.a. web.config, client.cfg., CloudServices.config).

|  |  |
| --- | --- |
|  |  |

## [Methods](#Methods)

### [HasValue](#HasValue+)

Returns true if the property has a value set.  
The parameter *filename* is optional. If it is not set, a valid property is one that is set in the standard configuration files (web.config / client.cfg or CloudServices.config) or an environment variable.

|  |  |
| --- | --- |
| **Return value** | [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | propName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778) [  fileName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778) ] |

### [GetValue](#GetValue)

Returns the value set in the property.  
The parameter *filename* is optional. If it is not set, the property must be one that is set in the standard configuration files (web.config / client.cfg or CloudServices.config) or an environment variable.

|  |  |
| --- | --- |
| **Return value** | [VarChar](https://wiki.genexus.com/commwiki/wiki?6778) |
| **Parameters** | propName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778) [  fileName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778) ] |

## [Notes](#Notes)

In both methods, the name of the property is instantiated as it is in the web.config or client.cfg. If you require a property of another file, either from the CloudServices.config file or from your own, the name of the property must be prefixed with the service type separated by a colon (:). eg: Notifications: APP\_ID.

If a file is specified, the format of this file must be similar to the CloudServices.config and the way to choose the value of a property is the same as in the case of the CloudServices.config (<ServiceType>:<propName>)

As of GeneXus 16 Upgrade 7, services from the same type can appear more than once. That's the case of the Chatbot type where every property is saved under a Chatbot instance identified by the Conversational Flows name. So in that case you should get the property with the following format <ServiceType>:<ServiceName>:<propName>,

### [Sample Configuration file:](#Sample+Configuration+file%3A)

```
<?xml version="1.0" encoding="utf-8"?>
<Services>
  <Service>
    <Name>MyServiceName</Name>
    <Type>MyServiceType</Type>
    <ClassName>MyServiceClass</ClassName>
    <Properties>
      <Property>
        <Name>Property1</Name>
        <Value>Value of Property 1</Value>
      </Property>
      <Property>
        <Name>Property2</Name>
        <Value>Value of Property 2</Value>
      </Property>
    </Properties>
  </Service>
</Services>
```

To get the value of Property1, write the following:

```
&FileName = !"MyConfigFile.config"
&propName = !"MyServiceType:Property1"
if ConfigurationManager.HasValue(&propName, &FileName)
   msg(ConfigurationManager.GetValue(&propName, &FileName))
else
   msg("Property has not been set")
endif
```

### [Availability](#Availability)

Configuration Manager is available as of [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See also](#See+also)

* [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)


|  |
| --- |
| **Backlinks** |
| [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339) | [Docker Environment variables property](https://wiki.genexus.com/commwiki/wiki?40607) |
|

---
