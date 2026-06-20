---
title: "XML DSig Signer"
source_id: 43579
source_url: https://wiki.genexus.com/commwiki/wiki?43579
genexus_version: "18"
---

# XML DSig Signer

**Note**: This object is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) and performs XML signing and XML signature verification for the XML Digital Signature standard..

**Valid Private Key****Formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files are not admitted.
  + Encrypted PKCS8 private keys are admitted since GeneXus 17 Upgrade 2
  + Files with .key extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* DER certificate (.crt or .cer extension). It contains only public keys.
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

**Available signature algorithms:**

* RSA with
  + SHA1
  + SHA256
  + SHA512
* Just for Java; ECDSA with
  + SHA1
  + SHA256
* The algorithm is given by the configured certificate in DoSign parameters.
* .Net Framework [System.Security.Cryptography.Xml](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.xml?view=netframework-4.8)[.SignedXml](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.xml.signedxml?view=netframework-4.8) does not provide support for signatures based on Elliptic Curves.
  + If an ECDSA certificate is loaded on the XmlDSigSigner, the functions will return an Error with Code DS004 and Description "XML signature with ECDSA keys is not implemented on Net Framework."

## [DoSignFile](#DoSignFile)

```
DoSignFile(xmlFilePath, privateKey, certificate, outputPath, options)
```

Signs an indicated XML file obtained by xmlFilePath parameter and saves the signed version of the file on the given outputPath parameter. It signs all elements of the file.

If the signature was not successfully performed, it returns false and the output file will be empty.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input privateKey: PrivateKey object
* Input certificate: Certificate object
* Input outputPath: VarChar(9999)
* Input options: DSigOptions object
* Return: Boolean, true if the signature was successfully performed.

Example:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&outputPath = "C:\Temp\signedXml.xml"
&result = &XmlDSigSigner.DoSignFile(&xmlFilePath, &privateKey, &Certificate, &outputPath, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* xmlFilePath parameter only allows .xml extension files.
* The PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).

## [DoSign](#DoSign)

```
DoSign(xmlInput, privateKey, certificate, options)
```

Signs an indicated XML String obtained by xmlInput parameter and returns the signed version of the String. It signs all elements of the XML String.

If the signature was not successfully performed, it returns an empty String.

Read Module Error Management for troubleshooting and more error details.

* Input xmlInput: VarChar(9999)
* Input privateKey: PrivateKeyObject
* Input certificate: Certificate object
* Input options: DSigOptions object
* Returns: VarChar(9999)

Example:

```
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&result = &XmlDSigSigner.DoSign(&xmlInput, &privateKey,  &Certificate, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).

## [DoSignFileElement](#DoSignFileElement)

```
DoSignFileElement(xmlFilePath, xPath, privateKey, certificate, outputPath, options)
```

Signs an indicated element of an XML file obtained by xmlFilePath parameter and saves the signed version of the file on the given outputPath parameter. It signs one element of the file. If an xPath predicate is provided, it will sign the first element that matches the xPath.

If the signature was not successfully performed, it returns false and the output file will be empty.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input xPath: Character(100)
* Input privateKey: PrivateKey object
* Input certificate: Certificate object
* Input outputPath: VarChar(9999)
* Input options: DSigOptions object
* Return: Boolean, true if the signature was successfully performed.

Example with xPath predicate:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&xPath = "/bookstore/book[1]"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&outputPath = "C:\Temp\signedXml.xml"
&result = &XmlDSigSigner.DoSignFileElement(&xmlFilePath, &xPath, &privateKey, &Certificate, &outputPath, &DSigOptions)
```

The same method can be used to sign an element indicating its identifier value. In XML, a special Identification parameter with [type ID](https://www.w3.org/TR/SVGMobile12/types.html#DataTypeID) can be defined which is unique to the document; on this implementation, the identifier attribute name must be given on the DSigOptions property IdentifierAttribute. More information on [Optional data](https://wiki.genexus.com/commwiki/wiki?43578).

When an ID attribute is used, the prefix "#" is required for the identifier value.

Example with ID value:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&xPath = "#tag1"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&outputPath = "C:\Temp\signedXml.xml"
&DSigOptions.IdentifierAttribute = "id"
&result = &XmlDSigSigner.DoSignFileElement(&xmlFilePath, &xPath, &privateKey, &Certificate, &outputPath, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* The PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* When an XPath predicate is used, it will add an xPath Transform on the Signature's Transforms element. Example

```
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
                    <ds:XPath>/bookstore/book[1]</ds:XPath>
                </ds:Transform>
            </ds:Transforms>
```

* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)
* When an ID is used, it will indicate the identification value on the Reference URI attribute in the SignedInfo Signature element. Example:

```
    <SignedInfo>
        ....
        <Reference URI="#tag1">
        <Transforms>
            <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
             <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            .......
        </Reference>
    </SignedInfo>
```

## [DoSignElement](#DoSignElement)

```
DoSignElement(xmlInput, xPath, privateKey, certificate, options)
```

Signs an indicated element of an XML String obtained by xmlInput parameter and returns the signed version of the XML. It signs one element of the XML string. If an xPath predicate is provided, it will sign the first element that matches the xPath.

If the signature was not successfully performed, it returns an empty String.

Read Module Error Management for troubleshooting and more error details.

* Input xmlInput: VarChar(9999)
* Input xPath: Character(100)
* Input privateKey: PrivateKey object
* Input certificate: Certificate object
* Input options: DSigOptions object
* Returns: VarChar(9999)

Example with xPath predicate:

```
&xPath = "/bookstore/book[1]"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&result = &XmlDSigSigner.DoSignElement(&xmlInput, &xPath, &privateKey, &Certificate, &DSigOptions)
```

The same method can be used to sign an element indicating its identifier value. In XML a special Identification parameter with [type ID](https://www.w3.org/TR/SVGMobile12/types.html#DataTypeID) can be defined which is unique to the document; on this implementation, the identifier attribute name must be given on the DSigOptions property IdentifierAttribute. More information on [Optional data](https://wiki.genexus.com/commwiki/wiki?43578).

When an ID attribute is used, the prefix "#" is required for the identifier value.

Example with ID value:

```
&xPath = "#tag1"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&DSigOptions.IdentifierAttribute = "id"
&result = &XmlDSigSigner.DoSignFile(&xmlInput, &xPath, &privateKey, &Certificate, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* The PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* When an XPath predicate is used, it will add an xPath Transform on the Signature's Transforms element. Example

```
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
                    <ds:XPath>/bookstore/book[1]</ds:XPath>
                </ds:Transform>
            </ds:Transforms>
```

* .Net specific xPath Transform known Issues: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc). Signature verification does not work on .Net Core in conjunction with xPath transformations.
* When an ID is used it will indicate the identification value on the Reference URI attribute in the SignedInfo Signature's element. Example:

```
    <SignedInfo>
        ....
        <Reference URI="#tag1">
        <Transforms>
            <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
             <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            .......
        </Reference>
    </SignedInfo>
```

## [DoVerifyFile](#DoVerifyFile)

```
DoVerifyFile( xmlFilePath,  options)
```

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one. Only files with .xml extension are allowed.

It is meant to be used when it is expected to verify a signed XML that contains the KeyInfo element containing the public key information (as KeyValue or X509Data).

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input options: DSigOptions object
* Returns: Boolean true if the signature verifies without any errors.

Example:

```
&xmlFilePath="C:\Temp\signedXml.xml"
&result = XmlDSigSigner.DoVerifyFile( &xmlFilePath,  &DSigOptions)
```

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc).

## [DoVerify](#DoVerify)

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one.

It is meant to be used when it is expected to verify a signed XML that contains the KeyInfo element containing the public key information (as KeyValue or X509Data).

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

```
DoVerify(xmlSigned, options)
```

* Input xmlSigned: VarChar(9999)
* Input options: DSigOptions object
* Returns: Boolean true if the signature verifies without any errors.

Example:

```
&result = XmlDSigSigner.DoVerify( &xmlSigned, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* For other signature optional parameters read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)

## [DoVerifyFileWithCert](#DoVerifyFileWithCert)

```
DoVerifyFileWithCert(xmlFilePath, certificate, options)
```

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one. Only files with .xml extension are allowed.

It is meant to be used when it is expected to verify a signed XML that does not contain the KeyInfo element with the public key information to validate. In this case, an external certificate is needed for validation.

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input certificate: Certificate object
* Input options: DSigOptions object
* Returns: boolean true if the signature verifies without any error

Example:

```
&CertificateX509.Load("C:\Temp\keys\publicKey.pem")
&result = &XmlDsigSigner.DoVerifyFileWithCert(&xmlFilePath, &CertificateX509, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)

## [DoVerifyWithCert](#DoVerifyWithCert)

```
DoVerifyWithCert(xmlSigned, certificate, options)
```

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one.

It is meant to be used when it is expected to verify a signed XML that does not contain the KeyInfo element with the public key information to validate. In this case, an external certificate is needed for validation.

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

* Input xmlSigned: VarChar(9999)
* Input certificate: Certificate object
* Input options: DSigOptions object
* Returns: Boolean true if the signature verifies without any errors.

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)

## [DoSignFileWithPublicKey](#DoSignFileWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
DoSignFile(xmlFilePath, privateKey, publicKey, outputPath, options, hash)
```

Signs an indicated XML file obtained by xmlFilePath parameter and saves the signed version of the file on the given outputPath parameter. It signs all elements of the file.

If the signature was not successfully performed, it returns false and the output file will be empty.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input privateKey: PrivateKey object
* Input publicKey: PublicKey object
* Input outputPath: VarChar(9999)
* Input options: DSigOptions object
* Input hash: DSigHashAlgorithm domain value
* Return: Boolean, true if the signature was successfully performed.

Example:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&PublicKey.Load("C:\Temp\keys\publicKey.pem")
&outputPath = "C:\Temp\signedXml.xml"
&hash = DSigHashAlgorithm.SHA256
&result = &XmlDSigSigner.DoSignFileWithPublicKey(&xmlFilePath, &privateKey, &PublicKey, &outputPath, &DSigOptions, &hash)
```

### [Implementation details](#Implementation+details)

* xmlFilePath parameter only allows .xml extension files.
* The PrivateKey must be preloaded before method invocation.
* The PublicKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).

## [DoSignWithPublicKey](#DoSignWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
DoSignWithPublicKey(xmlInput, privateKey, publicKey, options, hash)
```

Signs an indicated XML String obtained by xmlInput parameter and returns the signed version of the String. It signs all elements of the XML String.

If the signature was not successfully performed, it returns an empty String.

Read Module Error Management for troubleshooting and more error details.

* Input xmlInput: VarChar(9999)
* Input privateKey: PrivateKeyObject
* Input publicKey: PublicKey object
* Input options: DSigOptions object
* Input hash: DSigHashAlgorithm domain value
* Returns: VarChar(9999)

Example:

```
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&hash = DSigHashAlgorithm.SHA256
&result = &XmlDSigSigner.DoSignWithPublicKey(&xmlInput, &privateKey,  &publicKey, &DSigOptions, &hash)
```

### [Implementation details](#Implementation+details)

* PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The PublicKey must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).

## [DoSignFileElementWithPublicKey](#DoSignFileElementWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
DoSignFileElementWithPublicKey(xmlFilePath, xPath, privateKey, publicKey, outputPath, options, hash)
```

Signs an indicated element of an XML file obtained by xmlFilePath parameter and saves the signed version of the file on the given outputPath parameter. It signs one element of the file. If an xPath predicate is provided, it will sign the first element that matches the xPath.

If the signature was not successfully performed, it returns false and the output file will be empty.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input xPath: Character(100)
* Input privateKey: PrivateKey object
* Input publicKey: PublicKey object
* Input outputPath: VarChar(9999)
* Input options: DSigOptions object
* Input hash: DSigHashAlgorithm domain value
* Return: Boolean, true if the signature was successfully performed.

Example with xPath predicate:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&xPath = "/bookstore/book[1]"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&hash = DSigHashAlgorithm.SHA256
&outputPath = "C:\Temp\signedXml.xml"
&result = &XmlDSigSigner.DoSignFileElementWithPublicKey(&xmlFilePath, &xPath, &privateKey, &publicKey, &outputPath, &DSigOptions, &hash)
```

The same method can be used to sign an element indicating its identifier value. In XML, a special Identification parameter with [type ID](https://www.w3.org/TR/SVGMobile12/types.html#DataTypeID) can be defined which is unique to the document; on this implementation, the identifier attribute name must be given on the DSigOptions property IdentifierAttribute. More information on [Optional data](https://wiki.genexus.com/commwiki/wiki?43578).

When an ID attribute is used, the prefix "#" is required for the identifier value.

Example with ID value:

```
&xmlFilePath = "C:\Temp\xmlToSign.xml"
&xPath = "#tag1"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&Certificate.Load("C:\Temp\keys\publicKey.pem")
&outputPath = "C:\Temp\signedXml.xml"
&hash = DSigHashAlgorithm.SHA256
&DSigOptions.IdentifierAttribute = "id"
&result = &XmlDSigSigner.DoSignFileElementWithPublicKey(&xmlFilePath, &xPath, &privateKey, &publicKey, &outputPath, &DSigOptions, &hash)
```

### [Implementation details](#Implementation+details)

* The PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* When an XPath predicate is used, it will add an xPath Transform on the Signature's Transforms element. Example

```
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
                    <ds:XPath>/bookstore/book[1]</ds:XPath>
                </ds:Transform>
            </ds:Transforms>
```

* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)
* When an ID is used, it will indicate the identification value on the Reference URI attribute in the SignedInfo Signature element. Example:

```
    <SignedInfo>
        ....
        <Reference URI="#tag1">
        <Transforms>
            <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
             <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            .......
        </Reference>
    </SignedInfo>
```

## [DoSignElementWithPublicKey](#DoSignElementWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
DoSignElementWithPublicKey(xmlInput, xPath, privateKey, publicKey, options, hash)
```

Signs an indicated element of an XML String obtained by xmlInput parameter and returns the signed version of the XML. It signs one element of the XML string. If an xPath predicate is provided, it will sign the first element that matches the xPath.

If the signature was not successfully performed, it returns an empty String.

Read Module Error Management for troubleshooting and more error details.

* Input xmlInput: VarChar(9999)
* Input xPath: Character(100)
* Input privateKey: PrivateKey object
* Input certificate: Certificate object
* Input options: DSigOptions object
* Input hash: DSigHashAlgorithm domain value
* Returns: VarChar(9999)

Example with xPath predicate:

```
&xPath = "/bookstore/book[1]"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&hash = DSigHashAlgorithm.SHA256
&result = &XmlDSigSigner.DoSignElementWithPublicKey(&xmlInput, &xPath, &privateKey, &publicKey, &DSigOptions, &hash)
```

The same method can be used to sign an element indicating its identifier value. In XML a special Identification parameter with [type ID](https://www.w3.org/TR/SVGMobile12/types.html#DataTypeID) can be defined which is unique to the document; on this implementation, the identifier attribute name must be given on the DSigOptions property IdentifierAttribute. More information on [Optional data](https://wiki.genexus.com/commwiki/wiki?43578).

When an ID attribute is used, the prefix "#" is required for the identifier value.

Example with ID value:

```
&xPath = "#tag1"
&privateKey.Load("C:\Temp\keys\privateKey.pem")
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&hash = DSigHashAlgorithm.SHA256
&DSigOptions.IdentifierAttribute = "id"
&result = &XmlDSigSigner.DoSignElementWithPublicKey(&xmlInput, &xPath, &privateKey, &publicKey, &DSigOptions, &hash)
```

### [Implementation details](#Implementation+details)

* The PrivateKey must be preloaded before method invocation.
* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition.
* The PublicKey must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* When an XPath predicate is used, it will add an xPath Transform on the Signature's Transforms element. Example

```
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
                    <ds:XPath>/bookstore/book[1]</ds:XPath>
                </ds:Transform>
            </ds:Transforms>
```

* .Net specific xPath Transform known Issues: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc). Signature verification does not work on .Net Core in conjunction with xPath transformations.
* When an ID is used it will indicate the identification value on the Reference URI attribute in the SignedInfo Signature's element. Example:

```
    <SignedInfo>
        ....
        <Reference URI="#tag1">
        <Transforms>
            <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
             <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            .......
        </Reference>
    </SignedInfo>
```

## [DoVerifyWithPublicKey](#DoVerifyWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one.

It is meant to be used when it is expected to verify a signed XML that contains the KeyInfo element containing the public key information (as KeyValue).

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

```
DoVerifyWithPublicKey(xmlSigned, publicKey, options)
```

* Input xmlSigned: VarChar(9999)
* Input publicKey: PublicKey object
* Input options: DSigOptions object
* Returns: Boolean true if the signature verifies without any errors.

Example:

```
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&result = XmlDSigSigner.DoVerifyWithPublicKey( &xmlSigned, &publicKey, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* For other signature optional parameters read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element this issue could be affecting your software. It only applies to xPath usage, and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)

## [DoVerifyFileWithPublicKey](#DoVerifyFileWithPublicKey)

```
DoVerifyFileWithPublicKey(xmlFilePath, publicKey, options)
```

Verifies an XML document signature. If the document contains more than one signature, it will verify only the first one. Only files with .xml extension are allowed.

It is meant to be used when it is expected to verify a signed XML that does not contain the KeyInfo element with the public key information to validate. In this case, an external certificate is needed for validation.

If the signature does not verify correctly or an execution error occurs, it will return false.

Read Module Error Management for troubleshooting and more error details.

* Input xmlFilePath: VarChar(9999)
* Input publicKey: PublicKey object
* Input options: DSigOptions object
* Returns: boolean true if the signature verifies without any error

Example:

```
&publicKey.Load("C:\Temp\keys\publicKey.pem")
&result = &XmlDsigSigner.DoVerifyFileWithPublicKey(&xmlFilePath, &publicKey, &DSigOptions)
```

### [Implementation details](#Implementation+details)

* If the property XmlSchemaPath of the DSigOptions is not empty, the signer will try to verify the XML to sign against the schema indicated by this property when it is loading. If it fails, the signature verification will not be performed. Only files with .xml, .dtd, and .xsd extension are allowed for schema definition. The signature schema definition should be provided on the schema, not just the signed XML.
* The Certificate must be preloaded before method invocation.
* For other optional signature parameters, read [DSig Optional data](https://wiki.genexus.com/commwiki/wiki?43578) and [DSig Domains](https://wiki.genexus.com/commwiki/wiki?43565).
* If an element signature based on an identifier is expected, DSigOptions's IdentifierAttribute property must be configured; otherwise, the verification will fail.
* Net specific xPath Transform known Issue: .Net Framework has disabled XPath Transform by default; if you are using an xPath predicate and it does not find the element, this issue could be affecting your software. It only applies to xPath usage and it is not needed in any other case. It will not affect Java applications even when running on Windows environments. More information: [Breaking changes for XML; summary](https://coding.abel.nu/2016/03/breaking-changes-to-signedxml-in-ms16-035/), [Security update and official patches](https://support.microsoft.com/en-us/help/3148821/after-you-apply-security-update-3141780-net-framework-applications-enc)

## [Security tips](#Security+tips)

* When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.

### [Key pair generation](#Key+pair+generation)

The key pair can be generated locally with some tools, of which the most popular is [OpenSSL](https://www.openssl.org/).

Anyone can create, sign, and distribute a certificate, but most people will not trust it and, by default, software will not trust it either. This type of certificate is known as self-signed and is commonly used for testing.

When the key pair is generated, the encryption and signing algorithms are established along with the hash algorithm that will be used to generate and verify signatures. The signature will always be verified using the algorithms preestablished on the certificate.

### [Useful tools:](#Useful+tools%3A)

* [OpenSSL](https://www.openssl.org/)
* [CertUtil](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil)
* [KeyStore Explorer](https://keystore-explorer.org/)
* [Java KeyTool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
