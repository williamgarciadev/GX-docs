---
title: "XmlDSig Domains"
source_id: 43565
source_url: https://wiki.genexus.com/commwiki/wiki?43565
genexus_version: "18"
---

# XmlDSig Domains

**Note**: These domains are part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [DSigSignatureType](#DSigSignatureType)

It defines the type of DSig signature to be used.

Available values:

```
ENVELOPED
```

\*\*\*Enveloping and Detached signatures are not available in this module edition.

Example of an Enveloped signature:

```
<?xml version="1.0" encoding="UTF-8"?>
<Envelope xmlns="http://example.org/envelope">
  <Body>
    Hello world
  </Body>
    <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
        <SignedInfo>
            <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#WithComments" />
            <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
            <Reference URI="">
                <Transforms>
                    <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                    <Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#WithComments" />
                </Transforms>
                <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
                <DigestValue>RnMv...Ztmp8YOI=</DigestValue>
            </Reference>
        </SignedInfo>
        <SignatureValue>/jW1L...24vppECVoR6ckfZNI=</SignatureValue>
    </Signature>
</Envelope>
```

## [Canonicalization](#Canonicalization)

It defines the canonicalization method to be used to preprocess the data to be signed.

Available values:

```
C14n_WITH_COMMENTS, C14n_OMIT_COMMENTS, exc_C14n_OMIT_COMMENTS, exc_C14N_WITH_COMMENTS
```

Implementation details:

* C14n\_WITH\_COMMENTS will include the transform "http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"
* C14n\_OMIT\_COMMENTS will include the transform "http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
* exc\_C14N\_WITH\_COMMENTS will include the transform "http://www.w3.org/2001/10/xml-exc-c14n#WithComments"
* exc\_C14n\_OMIT\_COMMENTS will include the transform "http://www.w3.org/2001/10/xml-exc-c14n#"

\*\*\*C14N11 transformations are not available in this module edition. 

## [KeyInfoType](#KeyInfoType)

It defines the type of KeyInfo element to be used on the signature.

Available values:

```
NONE, KeyValue, X509Certificate
```

* NONE won't include a KeyInfo Element on the Signature structure.
* X509Certificate will include a KeyInfo Element with an X509Data Element inside the Signature structure. It will contain some information on the certificate and the Base64 encoded certificate.
* KeyValue will include a KeyInfo Element with a KeyValue Element inside the Signature structure. It will contain the Base64 encoded parameters of the public key.

Example of X509Certificate KeyInfoType:

```
<KeyInfo>
    <X509Data>
        <X509IssuerSerial>
            <X509IssuerName>E=test@genexus.com, CN=test, OU=security, O=GX, L=Montevideo, S=Montevideo, C=UY</X509IssuerName>
            <X509SerialNumber>135465464315</X509SerialNumber>
        </X509IssuerSerial>
        <X509SubjectName>E=test@genexus.com, CN=test, OU=security, O=GX, L=Montevideo, S=Montevideo, C=UY</X509SubjectName>
        <X509Certificate>MI.....3qvV1YXMaTdbWy7Ks=</X509Certificate>
    </X509Data>
</KeyInfo>
```

Example of KeyValue KeyInfoType:

```
<KeyInfo>
    <KeyValue>
        <RSAKeyValue>   
            <Modulus>40l......LRs=</Modulus>
            <Exponent>JJJJ</Exponent>
        </RSAKeyValue>
    </KeyValue>
</KeyInfo>
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [XML DSig Signer](https://wiki.genexus.com/commwiki/wiki?43579) |

---
