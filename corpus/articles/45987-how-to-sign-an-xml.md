---
title: "How to sign an XML"
source_id: 45987
source_url: https://wiki.genexus.com/commwiki/wiki?45987
genexus_version: "18"
---

# How to sign an XML

```
&pathToKeys = !"C:\Temp\keys\" //->put your path here

//--Loading Private Key--
&PrivateKey.Load(&pathToKeys+!"public_key.pem") //->put your public key name file here
if &PrivateKey.HasError()
    msg("Error loading private key. Code: " + &PrivateKey.GetErrorCode() + " Description: " + &PrivateKey.GetErrorDescription(), status)
else
    msg("Private key correctly loaded", status)
endif

//--Loading Public Key--
&Certificate.Load(&pathToKeys+!"certificate.crt") //->put your certificate name file here

if &Certificate.HasError()
    msg("Error loading public key. Code: " + &Certificate.GetErrorCode() + " Description: " + &Certificate.GetErrorDescription(), status)
else
    msg("Public key correctly loaded", status)
endif

//Load methods are for base64 keys and DER certificates
//If you are using a PKCS12 type of file (.pfx .jks .pkcs12) use LoadPKCS12 method
//More information: https://wiki.genexus.com/commwiki/servlet/wiki?43918,Asymmetric+Key+Management

//This example will use the default and most used configuration for XML DSig Signature
//therefore will use the default values of DSigOptions without using a XMLSchemma for validation 
//and without selecting any particular element to sign. It will sign the hole document at once
//More information about options and its defaults values: https://wiki.genexus.com/commwiki/servlet/wiki?43578,Optional+data
//More information about the signer object: https://wiki.genexus.com/commwiki/servlet/wiki?43579,XML+DSig+Signer

//--Signing---
if not &PrivateKey.HasError() and not &Certificate.HasError()
    &pathXmlFileToSign = !"C:\Temp\toSign.xml" //->put your path here
    &pathXmlFileSigned = !"C:\Temp\signedXML.xml" //->put your path here
    
    &XmlDSigSigner.DoSignFile(&pathXmlFileToSign, &PrivateKey, &Certificate, &pathXmlFileSigned, &DSigOptions)
    
    if &XmlDSigSigner.HasError()
        msg("Error signing document. Code: " + &XmlDSigSigner.GetErrorCode() + " Description: " + &XmlDSigSigner.GetErrorDescription(), status)
    else
        msg("Correctly signed", status)
    endif
endif

//--Verifying--
if not &XmlDSigSigner.HasError()
    &verification = &XmlDSigSigner.DoVerifyFile(&pathXmlFileSigned, &DSigOptions)
    
    if &verification = true
        msg("It verifies OK" , status)
    else
        if &XmlDSigSigner.HasError()
            msg("Error verifying document. Code: " + &XmlDSigSigner.GetErrorCode() + " Description: " + &XmlDSigSigner.GetErrorDescription(), status)
        endif
    endif
endif
```

Download SampleXmlSignature


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
