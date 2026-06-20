---
title: "XmlDSig .Net specific information"
source_id: 43603
source_url: https://wiki.genexus.com/commwiki/wiki?43603
genexus_version: "18"
---

# XmlDSig .Net specific information

.Net Specific information to performs XML signing and XML signature verification using [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921)

* [System.Security.Cryptography.Xml](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.xml?view=netframework-4.8) does not qualify XML. This means Signatures created with .Net and Net Core generators will have the below format:

```
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
        <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
        <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
        <Reference URI="">
            <Transforms>
                <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
            <DigestValue>Oy8OX..Ug8ho=</DigestValue>
        </Reference>
    </SignedInfo>
   <SignatureValue>DTl51DmjF..v8z1bl5S+9wyWE3PuB7kk=</SignatureValue>
</Signature>
```

* Also, elements without contents (example; Transform element) will close the XML tag on the same tag (<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" **/>**). This is the equivalent on XML to <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" ></Transform>, which means it is compatible with Java xmlsec implementation.
* The use of an xPath is disallowed by default for .Net Framework applications. For more information, read [link1](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [link2](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc).
* The use of an xPath is disallowed by default for .Net Core System.Security.Cryptography.Xml library for checksignature.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
