---
title: "Environment Variables for Storage Provider Configuration"
source_id: 60682
source_url: https://wiki.genexus.com/commwiki/wiki?60682
genexus_version: "18"
---

# Environment Variables for Storage Provider Configuration

You can use environment variables to override the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB). This enables dynamic selection of storage providers without modifying the KB, allowing for environment-specific configurations.

To achieve this, you can use the following environment variables:

* **STORAGE\_DEFAULT\_NAME**: Specifies the name of the Storage Provider.
* **STORAGE\_DEFAULT\_CLASSNAME**: Defines the class name associated with the Storage Provider.

Configure these variables using the values in the following table:

| **STORAGE\_DEFAULT\_NAME** | **STORAGE\_DEFAULT\_CLASSNAME** |
| --- | --- |
| AMAZONS3 | com.genexus.db.driver.ExternalProviderS3V2 |
| AMAZONS3V1 | com.genexus.db.driver.ExternalProviderS3V1 |
| AZURESTORAGE | com.genexus.db.driver.ExternalProviderAzureStorage |
| BOX | com.genexus.db.driver.ExternalProviderBox |
| GOOGLE | com.genexus.db.driver.ExternalProviderGoogle |
| IBMCOS | com.genexus.db.driver.ExternalProviderIBM |
| OPENSTACKSTORAGE | com.genexus.db.driver.ExternalProviderOpenStack |

### [Sample](#Sample)

To configure Amazon S3 as your storage provider, set the following environment variables:

* STORAGE\_DEFAULT\_NAME=AMAZONS3
* STORAGE\_DEFAULT\_CLASSNAME=com.genexus.db.driver.ExternalProviderS3V2

By setting these environment variables, you can switch storage providers dynamically without changing the KB. This approach is useful for managing multiple environments or configurations.

### [Availability](#Availability)

This feature is available from [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,).
