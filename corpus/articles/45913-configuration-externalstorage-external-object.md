---
title: "Configuration.ExternalStorage External Object"
source_id: 45913
source_url: https://wiki.genexus.com/commwiki/wiki?45913
genexus_version: "18"
---

# Configuration.ExternalStorage External Object

With this functionality, you can change at runtime the Storage Provider set in the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121), change its settings, or connect to other Storage Providers configured in cloudservices.config.

An external object called GeneXus.Common.Configuration.ExternalStorage that is part of the [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) exposes all the methods needed for this functionality.

|  |  |
| --- | --- |
|  |  |

### [Methods](#Methods)

#### [**Create method**](#Create+method)

Returns an instance of the Storage Provider that is being used in the programs as configured in the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) configured in the environment.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | ProviderType:StorageProviderType,  Properties:[Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606),  OutStorageProvider:StorageProvider,  OutMessages:Messages |

**Warning**: Temporary Restriction: The &Properties input must include authentication credentials for your provider.

#### **Connect method**

Given a ProfileName defined in cloudservices.config, returns an instance of the corresponding Storage Provider.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | ProfileName:Character,  Properties:[Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606),  OutStorageProvider:StorageProvider,  OutMessages:Messages |

**Note**: Temporary Restriction: The only supported value for ProfileName is 'Default'.

### [Domains](#Domains)

#### [**StorageProvider domain**](#StorageProvider+domain)

Enumerated domain with the Storage Provider Types available in [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121):

|  |  |
| --- | --- |
| **Amazon\_S3** |  |
| **Box** | Not supported |
| **Google\_CloudStorage** |  |
| **IBM\_Bluemix** | Not supported |
| **IBM\_ObjectStorage** |  |
| **Microsoft\_Azure** |  |
| **OpenStack** | Not supported |

**Note**: Supported values depend on the existence of the corresponding implementation in [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) for the generator or installation that is being used.

### [Examples](#Examples)

In these samples:

* &Properties is of [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606)
* &StorageProvider, &fromStorageProvider, &toStorageProvider are of [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) data type
* &ExternalStorage, &fromExternalStorage, &toExternalStorage are of GeneXus.Common.Configuration.ExternalStorage data type
* &Messages is of GeneXus.Common.Messages data type.

**Use case 1**: Just change a property (i.e.: the Bucket name)

```
&Properties = new()
&Properties.set(!"BUCKET_NAME", !"my-bucket")
if &ExternalStorage.Connect(!"Default", &Properties, &StorageProvider, &Messages)
     //{{ use &StorageProvider }}
endIf
```

**Note**: "Default" makes reference to the one defined in the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) at design time.

**Use case 2**: Completely configure a provider at runtime

```
&Properties = new()
&Properties.set(!"STORAGE_PROVIDER_ACCESSKEYID", !"{access-key-id_by-S3}")
&Properties.set(!"STORAGE_PROVIDER_SECRETACCESSKEY", !"{secret-access-key_by-S3}")
&Properties.set(!"STORAGE_PROVIDER_REGION", !"{region}")
&Properties.set(!"STORAGE_ENDPOINT", !"{endpoint_by-S3}")
if &ExternalStorage.Create(StorageProviderType.Amazon_S3, &Properties, &StorageProvider, &Messages)
     //{{ use &StorageProvider }}
endIf
```

**Note**: This case is useful for multitenant scenarios, where for each tenant you need to use another storage environment.

**Use case 3**: Copy objects (files) from one Bucket or storage environment to another

```
&AWSProperties.clear()
&AzureProperties.clear()
if &ExternalStorage.Create(StorageProviderType.Amazon_S3, &AWSProperties, &OutStorageProvider, &OutMessages)
    //{{ &OutStorageProvider points to Amazon, now you can download the files from there }}
    if &ExternalStorage.Create(StorageProviderType.Microsoft_Azure, &AzureProperties, &OutStorageProvider, &OutMessages)    
        //{{ &OutStorageProvider now points to Azure, and you can upload the previously downloaded files to Azure }}
    endIf 
endIf
```

**Warning**: Only one instance of StorageProvider Data type can be used in a program. That is why the same variable &OutStorageProvider has been used in case 3.

**Use case 4**: Get the names of the properties

Here is how to get the names of the properties that can be configured for the storage provider in the Storage section of the cloudservices.config file.

1. In the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) you must assign values to the properties (for example, those used to configure the connection to Google Cloud Storage): Service Account Key, Project ID and Application Name.
2. To obtain the names of these properties, you can perform the following steps:
   * Perform a [Build](https://wiki.genexus.com/commwiki/wiki?5692) of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) so that GeneXus generates the configuration files.
   * Find the cloudservices.config file of your model. This file is generated during the Build and contains the cloud services configuration.
   * Open the cloudservices.config file in a text editor.
   * Inside the file, find the Storage section.
   * Inside the Storage section, you will see the properties with their respective names and values. Copy the names of the properties that correspond to the properties you configured.

### [Scope](#Scope)

Cases 1 and 2 are supported in .NET, .NET Core, and Java generators.  
Case 3 is, as of GeneXus 16 Upgrade 10, only supported in .NET and .NET Core generators.

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

### [See Also](#See+Also)

[Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087)


|  |
| --- |
| **Backlinks** |
| [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) |

---
