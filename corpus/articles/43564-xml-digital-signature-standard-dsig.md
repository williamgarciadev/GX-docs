---
title: "Xml Digital Signature Standard (DSig)"
source_id: 43564
source_url: https://wiki.genexus.com/commwiki/wiki?43564
genexus_version: "18"
---

# Xml Digital Signature Standard (DSig)

Also known as XmlDSig or DSig, it defines the XML syntax to sign an XML document.

It defines a Signature tag that will contain all signature related information; for example, for canonicalization methods, references needed to identify elements of signed documents, etc.

The standard also defines 3 types of signatures depending on how it relates to the signed document. It can be Enveloped, Enveloping or Detached.

* Enveloped signatures are contained within the signed document. They add a reference to the signed element in cases in which just some document elements are signed.
* Enveloping signatures include the signed elements within their tags.
* Detached signatures are stored in another XML document separate from the original and linked with some reference to the original document.

Signature structure example

```
<Signature Id="MyFirstSignature" xmlns="http://www.w3.org/2000/09/xmldsig#"> 
  <SignedInfo>  
   <CanonicalizationMethod Algorithm="http://www.w3.org/2006/12/xml-c14n11"/> 
   <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/> 
   <Reference URI="http://www.w3.org/TR/2000/REC-xhtml1-20000126/"> 
     <Transforms> 
       <Transform Algorithm="http://www.w3.org/2006/12/xml-c14n11"/> 
     </Transforms> 
     <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/> 
     <DigestValue>dGhpcyBpcyBub3QgYSBzaWduYXR1cmUK...</DigestValue> 
   </Reference> 
 </SignedInfo> 
   <SignatureValue>...</SignatureValue> 
   <KeyInfo> 
    <KeyValue>
      <DSAKeyValue> 
        <P>...</P><Q>...</Q><G>...</G><Y>...</Y> 
      </DSAKeyValue> 
    </KeyValue> 
   </KeyInfo> 
 </Signature>
```

[Source](https://www.w3.org/TR/xmldsig-core1/)

### [DSig structure in a nutshell](#DSig+structure+in+a+nutshell)

* CanonicalizationMethod defines an algorithm to process special characters; it is used to preprocess the input before the hash digest calculation. It is a way to preprocess the text in the same way on both ends of the conversation or the signature would fail.
* SignatureMethod defines the hash algorithm and the signature asymmetric algorithm that will be used for signing.
* DigestMethod defines the hash algorithm to be used to calculate the digest value.
* DigestValue element contains the Base64 encoded hash of the signed text.
* Reference element defines references by URI, ID within the document or to another signed document in case of detached signatures.
* Transforms element contains definitions to transform the document before it is digested (hashed). It could also include XPath transformation to define an XPath predicate to find elements signed.
* SignatureValue element contains the Base64 encoded signature value calculated using all the definitions expressed in the SignedInfo element.
* KeyInfo is an optional element; it may or may not be attached to the signature in the standard. If it is present it could contain a KeyValue element type or an X509Data element type. When the KeyInfo element is not included in the Signature, the public key to verify the signature has to be obtained elsewhere.
  + KeyValue element type would have information about the type and parameters of the public key to be used to verify the signature. The parameters must be expressed using Basse64 encoding.
  + X509Data element type would contain data related to the public key certificate and other certificate information to use in the signature verification process.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
