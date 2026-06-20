---
title: "HTML Document Type property"
source_id: 13517
source_url: https://wiki.genexus.com/commwiki/wiki?13517
genexus_version: "18"
---

# HTML Document Type property

Allows you to define if the Html code follows an specific DOCTYPE standard.

### [Values](#Values)

|  |  |
| --- | --- |
| **HTML 4.01 Transitional** | This declares the document to be HTML 4.01 Transitional. HTML 4 Transitional includes all elements and attributes of HTML 4 Strict but adds presentational attributes, deprecated elements, and link targets. |
| **HTML 4.01 Strict** | This declares the document to be HTML 4.01 Strict. HTML 4.01 Strict is a trimmed down version of HTML 4.01 that emphasizes structure over presentation. |
| **HTML 5** | This declares the document to be HTML 5 (Available since GeneXus X Evolution 2). |
| **Do not specify** | No DOCTYPE standard is specified. This is the default value. |
| **XHTML 1.0 Transitional** | This declares the document to be XHTML 1.0 Transitional. XHTML 1.0 Transitional is an XML version of HTML 4 Transitional. |

### [Description](#Description)

The default value is compatible with all the Genexus previous versions.

When the *Html 4.01 transitional* is selected, you could view, at the top of the source the following header:

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
```

When using *HTML 4.01 Strict*:

```
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

When using *XHTML 1.0 Transitional*:

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

When using HTML5:

```
<!DOCTYPE html>
```

For more information please refer to [W3c- Html 401](http://www.w3.org/TR/html401/) or [W3c - xhtml](http://www.w3.org/TR/xhtml1/).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Considerations to develop a Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?29133) | [Considerations when changing the HTML Document type property](https://wiki.genexus.com/commwiki/wiki?17945) |
| [Default Web Form Editor property](https://wiki.genexus.com/commwiki/wiki?25154) | [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) |
| [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [My first Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?25206) |

---
