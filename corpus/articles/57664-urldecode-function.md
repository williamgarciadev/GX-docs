---
title: "UrlDecode function"
source_id: 57664
source_url: https://wiki.genexus.com/commwiki/wiki?57664
genexus_version: "18"
---

# UrlDecode function

Converts special characters that are encoded in a URL back to their original form.

### [Syntax](#Syntax)

**UrlDecode(***CharacterExpression***)**

**Where:**

*CharacterExpression*Attribute, variable, constant, or character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that contains/provides the encoded URL to be decoded. It must be based on the Character, Varchar, or LongVarchar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

A URL may contain special characters such as spaces, punctuation marks, and other non-alphanumeric characters. These special characters are encoded, the UrlDecode function takes a string corresponding to an encoded URL and decodes it, converting it back to its original form. For example, the "%20" becomes a space and the "%2C" becomes a comma.

### [Samples](#Samples)

```
&EncodedUrl="https://www.example.com/search?query=my%20search%20term"
&DecodedUrl = UrlDecode(&EncodedUrl) //The returned value is "https://www.example.com/search?query=my search term"
```

### [See Also](#See+Also)

[UrlEncode function](https://wiki.genexus.com/commwiki/wiki?57781)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |
| [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [UrlDecode function (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59696) | [urlDecode function (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58079) | [UrlEncode function](https://wiki.genexus.com/commwiki/wiki?57781) |
| [UrlEncode function (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59695) | [urlEncode function (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58080) |

---
