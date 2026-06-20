---
title: "External Storage for Multimedia"
source_id: 31120
source_url: https://wiki.genexus.com/commwiki/wiki?31120
genexus_version: "18"
---

# External Storage for Multimedia

Companies are putting more and more apps in the cloud because the cloud model keeps business agility during the app's lifetime; relevant benefits include high-performance access to data, data safety, and scalability.

Regarding multimedia storage (for videos, audios, or images), there are several compelling reasons to use external storage rather than storing data in the database, which are detailed below:

### [Scalability](#Scalability)

To ensure the scalability of a clustered application, the server file system cannot be used to store the multimedia, because it cannot be guaranteed that the same server will serve the client in the next HTTP request.  
   
The traditional way of saving images is in the database. When requested, they are downloaded to the file system of the same server where the application runs (related to the [Blob Local Storage](https://wiki.genexus.com/commwiki/wiki?6979) and [Temp media directory property](https://wiki.genexus.com/commwiki/wiki?7628) properties). This is a drawback for applications that run on a cluster with no server affinity, where different nodes can serve the images regardless if the web session remains the same.

### [Security](#Security)

Data should be guarded against access by non-authorized users.

The disadvantage of saving multimedia files in the database is that when they are retrieved to display an image, for example, it is temporarily stored in the server's file system in a location accessible from the web app (the Temp Media Directory). In addition, the file that is automatically downloaded to the file system when an image is retrieved to be displayed can harm the application or the server's stability.

With external storage, you can prevent data from being dangerously exposed to unauthorized users and protect the server from malicious attacks.

### [Performance](#Performance)

Temporarily storing data in the server's file system implies an I/O penalty. This can be avoided by using the external storage mechanism.

## [External Storage for Multimedia in GeneXus applications](#External+Storage+for+Multimedia+in+GeneXus+applications)

When an external storage system is used, multimedia files aren't stored in the database and the storage file location URL is saved in the "\_GXI" column of the table.

In other words, every insert or update from any source (they can be procedures, [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), or Transactions) automatically manages the data in the external storage. In addition, the external storage is automatically retrieved. The user doesn't need to program anything or change its logic.

For versions previous to  [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,), it is available for [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529), and [Video data type](https://wiki.genexus.com/commwiki/wiki?16608). Blobs are not included, and they are stored in the database as usual.

As since  [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,), the [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) supports the implementation also.

### [External storage providers supported](#External+storage+providers+supported)

There are several external storage providers to choose from:

[Amazon S3](https://aws.amazon.com/s3/)  
[IBM Cloud Object Storage](https://www.ibm.com/cloud/object-storage)   
[Windows Azure Storage](https://azure.microsoft.com/en-us/services/storage/)  
[Google Cloud Storage](https://cloud.google.com/storage/)

### [How to use External storage for multimedia files](#How+to+use+External+storage+for+multimedia+files+)

After having decided which is the most convenient provider for you, and setting all the necessary configurations in the cloud, you just need to configure the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) or use the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) in GeneXus.

This is valid for Web and mobile apps as well.

## [Implementation](#Implementation)

![enlightened](http://wiki.genexus.com/commwiki/static/CKEditor/ckeditor/plugins/smiley/images/lightbulb.png "enlightened") The CloudServices.config file includes the information for connecting to the external storage, so this file has to be taken to production. It's located in the WEB-INF folder for Java applications, and under the virtual directory for NET applications.

### [Considerations](#Considerations)

* When using external storage, data will always be automatically stored in an external manner as it is updated from the application. For this reason, you can start with data stored in the DB and end up with the data externally stored if it is updated using the application. The other way round, if you use external storage and change to database storage, you won't get any errors because the external storage remains accessible while the data isn't updated again. When the data is updated, it is stored in the database.
* When you delete a record, multimedia files aren't deleted from the external storage.
* If you change the bucket name or folder along the way when you retrieve the data the application won't throw any errors unless you remove the old bucket or folder. From then on, the application will store the files in the new bucket or folder.
* When using Amazon S3, the Bucket name must have "Public Access". This means that to access the file no authentication is performed; so, having the URL to it, it is accessible. If this solution is not suitable for you, we recommend using the [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087).

### [See Also](#See+Also)

[Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087)  
[Required configuration for Amazon S3 bucket](https://wiki.genexus.com/commwiki/wiki?54610)


|  |
| --- |
| **Backlinks** |
| [Access Key property](https://wiki.genexus.com/commwiki/wiki?45731) | [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) |
| [Bucket Name property](https://wiki.genexus.com/commwiki/wiki?45733) | [Download content in Offline applications property](https://wiki.genexus.com/commwiki/wiki?40907) | [Folder Name property](https://wiki.genexus.com/commwiki/wiki?45734) |
| [GeneXus for SAP Systems - Application Integration](https://wiki.genexus.com/commwiki/wiki?34317) | [Secret Key property](https://wiki.genexus.com/commwiki/wiki?45732) | [Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?45736) | [Storage Location property](https://wiki.genexus.com/commwiki/wiki?45735) |
| [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) |

---
