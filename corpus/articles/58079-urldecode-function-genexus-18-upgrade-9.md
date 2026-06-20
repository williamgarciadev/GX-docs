---
title: "urlDecode function (GeneXus 18 Upgrade 9)"
source_id: 58079
source_url: https://wiki.genexus.com/commwiki/wiki?58079
genexus_version: "18"
---

# urlDecode function (GeneXus 18 Upgrade 9)

Converts special characters that are encoded in a URL back to their original form.

### [Syntax](#Syntax)

**urlDecode(***CharacterExpression***)**

**Where:**

*CharacterExpression*Attribute, variable, constant, or character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that contains/provides the encoded URL to be decoded. It must be based on the Character, Varchar, or LongVarchar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

A URL may contain special characters such as spaces, punctuation marks, and other non-alphanumeric characters. These special characters are encoded, the urlDecode function takes a string corresponding to an encoded URL and decodes it, converting it back to its original form. For example, the "%20" becomes a space and the "%2C" becomes a comma.

### [Samples](#Samples)

```
&EncodedUrl="https://www.example.com/search?query=my%20search%20term"
&DecodedUrl = urlDecode(&EncodedUrl) //The returned value is "https://www.example.com/search?query=my search term"
```

### [Availability](#Availability)

This function is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).

### [See Also](#See+Also)

[UrlEncode function](https://wiki.genexus.com/commwiki/wiki?57781)
