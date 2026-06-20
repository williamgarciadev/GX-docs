---
title: "HowTo: Create Mini App Bundle"
source_id: 57803
source_url: https://wiki.genexus.com/commwiki/wiki?57803
genexus_version: "18"
---

# HowTo: Create Mini App Bundle

This guide shows the step-by-step process of creating a Mini App Bundle.

1. Start by creating a file named **MANIFEST.MF**; make sure the file encoding is set to UTF8.

This file should include the following configuration entries:

|  |  |
| --- | --- |
| Version | Numeric with the bundle version format (Required) |
| Info | String with the name of the file containing the Mini App info. If not included, the default filename is miniapp.json |

For example (**MANIFEST.MF**):

```
Version: 1
info:mini.json
```

2. Next, create a file that contains the information of the [Mini App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,).

This file should be in JSON format and include the following fields:

```
{
    "id": "string",
    "name": "string",
    "organization_id": "GUID",
    "type": "string",    /*Native, WEB*/
    "superapp_id": "string",
    "description": "string",
    "keywords": "string",
    "icon": "string",    /*The filename for a file that is included in the bundle or URL for external image*/
    "card": "string",    /*The filename for a file that is included in the bundle or URL for external image*/
    "banner": "string",    /*The filename for a file that is included in the bundle or URL for external image*/
    "additional_attributes":[
        {
            "field": "string",
            "value": "string"
        },
        ...
    ],
    "locations":[
        {
            "name": "string",
            "geo_point": "GeoPoint"
        },
        ...
    ]
}
```

GeoPoint: Geography object represented by the WKT text (<https://en.wikipedia.org/wiki/Well-known_text>).  
Sample: "POINT(-56.163740158081055 -34.92478600243492)".

For example (**miniapp.json**):

```
{
    "id":"com.genexus.verdant.coffeemuffins",
    "name":"Coffee & Muffins",
    "organization_id":"19fae2dd-64a9-4659-847a-2b7cdfd593ca",
    "type":"Native",
    "superapp_id":"com.genexus.verdantbank",
    "description":"Coffee & Muffins Mini App",
    "keywords":"coffee cafe muffins breakfast",
    "icon":"image.svg",
    "banner":"https://www.genexus.com/media/images/coffee.svg",
    "locations":[
        {
            "name":"Central",
            "geo_point":"POINT(-56.163740158081055 -34.92478600243492)"
        }
    ]
}
```

3. Lastly, create a ZIP containing the **MANIFEST.MF** file and all the other files you used for the Mini App info.

For example (**MiniApp.mac**):

`[imagen omitida: wiki id 57806]`

By following the steps in this guide, you've learned how to construct the Manifest file, define Mini App information, and package everything into a ZIP file.

With your Mini App Bundle ready, you can deploy and distribute your Mini Apps specifically within the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).

### [See Also](#See+Also)

[HowTo: Create Mini App Version Bundle](https://wiki.genexus.com/commwiki/wiki?57804)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create Mini App Version Bundle](https://wiki.genexus.com/commwiki/wiki?57804) | [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Mini App Center - API Reference - Mini App](https://wiki.genexus.com/commwiki/wiki?57798) |

---
