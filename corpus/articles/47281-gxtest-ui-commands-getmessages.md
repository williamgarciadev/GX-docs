---
title: "GXtest UI Commands - GetMessages"
source_id: 47281
source_url: https://wiki.genexus.com/commwiki/wiki?47281
genexus_version: "18"
---

# GXtest UI Commands - GetMessages

This command is useful to retrieve all messages, notifications, balloons, etc. shown on a webpage.

`[imagen omitida: wiki id 47282]`

**Returns:**

A collection of texts containing all messages present on the page.

**Examples:**

```
&charsCollection = &driver.GetMessages()
```

If you want to validate that a certain message is shown you can do it like this:

```
&driver.Verify(&driver.GetMessages().ToJson().Contains("Message to validate is being shown"))
```

### [Availability](#Availability)

This command  is available since GeneXus 17 upgrade 1.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
