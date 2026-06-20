---
title: "GeneXus SDK for SAP Leonardo: Importing a ML service"
source_id: 41823
source_url: https://wiki.genexus.com/commwiki/wiki?41823
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Importing a ML service

To import a SAP Leonardo Machine Learning Foundation service(API), you have to go to the [SAP API Business Hub](https://api.sap.com/package/SAPLeonardoMLFunctionalServices?section=Artifacts)

`[imagen omitida: wiki id 41824]`

There select the API you want to incorporate to your Knowledge Base. In this example, the Inference Service for Language Detection will be used.

Once Selected go to the Details Tab and select Download Specification.

`[imagen omitida: wiki id 41825]`

When selected Download Specification two file options will be displayed JSON or YAML, both options are valid, in this example, YAML file will be used.

`[imagen omitida: wiki id 41863]`

After the file finished downloading go to the Knowledge Base you want to integrate the API.

On GeneXus go to Tools->Application Integration-> OpenAPI Import.

`[imagen omitida: wiki id 41826]`

This will open the following window where you need to input the File path of the YAML downloaded. You can use the three dots button (…) to open the windows explorer and allow you to search for the file.

Also, you can select where to import it by changing the Module/Folder option.

`[imagen omitida: wiki id 41827]`

Press OK.

GeneXus after reading the file will automatically generate all the necessary objects to allow you to work with the API.

These objects will be created inside three folders:

* Api: containing procedures that are the methods exposed by the API.
* Models: contains structured data types used by the procedures.
* Client: contains a procedure that returns the URL of the service.

For more information see [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864).


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: End User Documentation](https://wiki.genexus.com/commwiki/wiki?41183) | [GeneXus SDK for SAP Leonardo: FAQ](https://wiki.genexus.com/commwiki/wiki?41185) | [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
