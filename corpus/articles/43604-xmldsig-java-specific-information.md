---
title: "XmlDSig Java specific information"
source_id: 43604
source_url: https://wiki.genexus.com/commwiki/wiki?43604
genexus_version: "18"
---

# XmlDSig Java specific information

Java Specific information to performs XML signing and XML signature verification using [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921)

* [XML Security Library (xmlsec)](https://www.aleksey.com/xmlsec/) does qualify the Signature tags. This means Signatures created with the Java generator will have a ds: prefix on its elements as shown in the example below:

```
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#WithComments"></ds:CanonicalizationMethod>
    <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1"></ds:SignatureMethod>
        <ds:Reference URI="">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></ds:Transform>
                <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#WithComments"></ds:Transform>
            </ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></ds:DigestMethod>
            <ds:DigestValue>Oy8O...LjdjPUg8ho=</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>jFbB..Fh0J8MDL</ds:SignatureValue>
</ds:Signature>
```

* It adds the closing XML tags to elements without contents (example; Transform element). It will generate tags like this <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" ></Transform>. This is the equivalent on XML to <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" **/>**, which means it is compatible with the .Net implementation.
* The latest [XML Security Library (xmlsec)](https://www.aleksey.com/xmlsec/) implementations include newline characters on encoded outputs. This behavior is correct but it is an unwanted feature in most cases. This module includes the configuration to avoid those characters by default ([Details](http://santuario.apache.org/java212releasenotes.html)). If you need to use the default [XML Security Library (xmlsec)](https://www.aleksey.com/xmlsec/) configuration, a workaround could be to set -Dorg.apache.xml.security.ignoreLineBreaks flag ([Details](https://howtodoinjava.com/java/basics/java-system-properties/), [More information](https://issues.shibboleth.net/jira/browse/JOST-118)). To avoid you the trouble we've added an object to set the System property before library initialization:

### [JavaConfig](#JavaConfig+)

```
JavaConfig.UseLineBreaks(false)
```

This line before using the module will configure XmlDSigSigner to not use newline characters every 76 characters, and this is the default module configuration. This line is not really required if you never changed the default settings. Output example:

```
<?xml version="1.0" encoding="UTF-8"?>
<messages>
  <note id="tag1">
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
  <note id="tag2">
    <to>Jani</to>
    <from>Tove</from>
    <heading>Re: Reminder</heading>
    <body>I will not</body>
  </note>
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:SignedInfo>
    <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"></ds:CanonicalizationMethod>
    <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"></ds:SignatureMethod>
        <ds:Reference URI="#tag1">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></ds:Transform>
                <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"></ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"></ds:DigestMethod>
            <ds:DigestValue>C4lUehylIRHUX/Fy3M4dz+IqLNW+Y2uCzjxkK3u6yoA=</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
   <ds:SignatureValue>yHy63ovehDkvGp/X4HPiCTmvtw3Kw/7jC0vZqa/CDmxfx9eWz/9PzNpIr/NSspG5zA3IRl0lEahuDKwyYU0g3w2JX2raQc8LDzuPHVj2Yz3c8qnWrsVq9W5z8qGrCeA9</ds:SignatureValue>
</ds:Signature>
```

Default library configuration (not module's):

```
JavaConfig.UseLineBreaks(true)
```

This line before using the module will configure XmlDSigSigner and will insert newline characters every 76 characters. Output example:

```
<?xml version="1.0" encoding="UTF-8"?>
<messages>
  <note id="tag1">
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
  <note id="tag2">
    <to>Jani</to>
    <from>Tove</from>
    <heading>Re: Reminder</heading>
    <body>I will not</body>
  </note>
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"></ds:CanonicalizationMethod>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"></ds:SignatureMethod>
        <ds:Reference URI="#tag1">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></ds:Transform>
                <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"></ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"></ds:DigestMethod>
            <ds:DigestValue>C4lUehylIRHUX/Fy3M4dz+IqLNW+Y2uCzjxkK3u6yoA=</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>
    VJG049CyBg8y6Ur3bFnn2UQplbA39JiMdwM6JDY5LdEWIsH0JO/D7JHAQK2ARS0j0eqzmSz0hqzx&#xD;
    PBj+oCiLgGs9ir3aeQtNoEIRkJmn7n+t2AfUj3F3B0NAS9je4EZ7
    </ds:SignatureValue>
</ds:Signature>
```

* This configuration for xmlsec library has to be the same on both ends of the communication. Adding or erasing newline characters "by hand" will not do the trick, as signatures will not verify if this is done.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) |

---
