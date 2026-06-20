---
title: "UrlEncode function (GeneXus 18 Upgrade 10)"
source_id: 59695
source_url: https://wiki.genexus.com/commwiki/wiki?59695
genexus_version: "18"
---

# UrlEncode function (GeneXus 18 Upgrade 10)

Encodes special characters included in a URL.

### [Syntax](#Syntax)

**UrlEncode(***CharacterExpression***)**

**Where:**

*CharacterExpression*  
             Attribute, variable, constant, or character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that contains/provides the URL to be encoded. It must be based on the Character, Varchar, or LongVarchar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

URLs often contain special characters, such as spaces and punctuation marks, which have to be encoded for correct transmission over the Internet. This function takes a string representing a URL and encodes it according to the URL encoding standard. For example, spaces are converted to "%20", commas to "%2C", etc.

### [Sample](#Sample)

```
&OriginalUrl = "https://www.example.com/search?query=my search term"
&EncodedUrl = UrlEncode(&OriginalUrl) //The returned value is "https%3A%2F%2Fwww.example.com%2Fsearch%3Fquery%3Dmy%20search%20term"
```

### [See Also](#See+Also)

[UrlDecode function](https://wiki.genexus.com/commwiki/wiki?57664)
