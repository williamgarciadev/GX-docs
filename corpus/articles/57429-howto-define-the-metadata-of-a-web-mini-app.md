---
title: "HowTo: Define the metadata of a Web Mini App"
source_id: 57429
source_url: https://wiki.genexus.com/commwiki/wiki?57429
genexus_version: "18"
---

# HowTo: Define the metadata of a Web Mini App

One of the differences between a [Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58298) and a [Web Mini App](https://wiki.genexus.com/commwiki/wiki?57422) is that in the former case, the metadata is created automatically. In the latter case, you must create it yourself.

To define the metadata of a Web Mini App you have to create a file named webminiapp.json, and compress it into a zip file with the .gxsd extension.

The properties to be included in the webminiapp.json must be written in the following format:

```
{
    "EntryPointURL": String,
    "SuperAppObjectName": String,
    "MiniAppObjectName": String
}
```

**EntryPointURL:** Defines the HTTPS URL that loads when you start the Web Mini App. Refers to the main entry URL for the Web Mini App. It is the starting point or main access to the application.  
**SuperAppObjectName (Optional):** Indicates the name of the property on the window object that the Web Mini App will use to interoperate with the Super App through a Js bridge. The default value is gxsuperapp.  
**MiniAppObjectName (Optional):** Indicates the name of the property on the window object that the Web Mini App will use to interoperate with the Mini App through a Js bridge. For example, to Exit the Mini App. The default value is gxminiapp.

If the SuperAppObjectName and/or MiniAppObjectName properties are not completed, their default values will be used.

### [Sample](#Sample)

```
{
    "EntryPointURL": "https://your_miniapp_services_url",
    "SuperAppObjectName": "GxSuperAppApi",
    "MiniAppObjectName": "MiniAppAPI"
}
```

These definitions indicate how the Web Mini App communicates with the Super App. The property EntryPointURL is the gateway to the Web Mini App. At the same time, SuperAppObjectName and MiniAppObjectName are used to interact with the Super App and handle the internal operations of the Web Mini App.

To illustrate the process, below is shown a .gxsd file displaying the webminiapp.json file and its content:

`[imagen omitida: wiki id 58433]`

After the Web Mini App is created in the Mini App Center, go to the Mini Apps section and click on the Web Mini App to upload the metadata (webminiapp.gxsd file) created.

`[imagen omitida: wiki id 57426]`

Click on the NEW VERSION button.

`[imagen omitida: wiki id 57427]`

Next, upload the webminiapp.json file with the metadata.

`[imagen omitida: wiki id 57428]`

Lastly, click on the CONFIRM button.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [HowTo: Call a Super App API from a Web Mini App](https://wiki.genexus.com/commwiki/wiki?57430) | [HowTo: Publish a Web Mini App in the Mini App Center](https://wiki.genexus.com/commwiki/wiki?57425) |

---
