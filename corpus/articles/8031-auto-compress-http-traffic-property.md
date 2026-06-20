---
title: "Auto compress http traffic property"
source_id: 8031
source_url: https://wiki.genexus.com/commwiki/wiki?8031
genexus_version: "18"
---

# Auto compress http traffic property

To allow Web objects to send the HTML page compressed, for the browser to decompress it in real time. Compression is made only when the browser indicates that it is able to do so.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | They do not send the page compressed. Some browsers may not report their capacity to decompress the pages correctly, and they may not be able to display them correctly. |
| **Use Environment property value** | The object will be generated, depending on the value specified in the corresponding property at the Generator level. This value applies only at the object level. |
| **Yes** | They send the page compressed. It means to add the gzip Content-Encoding value on the Response Headers. |

### [Description](#Description)

#### [Note](#Note)

For the .NET generator, the *Microsoft .Net Framework 2.0* and IIS 6.0 or higher are needed.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)
