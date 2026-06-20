---
title: "HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication"
source_id: 41243
source_url: https://wiki.genexus.com/commwiki/wiki?41243
genexus_version: "18"
---

# HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication

[SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) requires some configuration steps regarding the creation of certificates and the setup of the servlet's server in some cases (using Java generator). This document explains in detail the steps that should be considered.

This is useful for completing the Credentials tab information of SAML 2.0 Authentication type configuration.

First, note that, for testing purposes, you will not need a valid CA certificate. A self-signed certificate will do.

Listed below are some examples of how certificates can be generated for some of the most used Identity Providers, in some examples the way they are generated is separated by Environment (Java or .Net Framework), however, the resulting certificate extensions .jks or .pkcs12, .p12 and .pfx for Java or .Net Framework respectively, is independent of the Identity Provider and directly related to the Environment.

**Note**: The detailed information below on generating self-signed certificates is purely and exclusively for illustrative purposes; it may not work in your environment. It is the developer's responsibility to research how to generate valid self-signed certificates for their environment..

## [Agesic](#Agesic)

#### [How to generate a key pair using OpenSSL](#How+to+generate+a+key+pair+using+OpenSSL)

```
openssl req -newkey rsa:2048 -keyout key.pem -x509 -days 365 -out certificate.pem
```

As a result, you'll have key.pem containing the private key, and certificate.pem containing the public key.

For [Agesic](https://centroderecursos.agesic.gub.uy/web/seguridad/wiki/-/wiki/Main/Integraci%C3%B3n+con+servicio+de+autenticaci%C3%B3n), you have to change the format of the file containing the public key, and turn it into a .crt file (the certificate to be sent to Agesic):

```
openssl x509 -outform der -in certificate.pem -out certificate.crt
```

The certificate used to sign the request (of the [Service Provider](https://en.wikipedia.org/wiki/Service_provider_(SAML)) to the [Identity Provider](https://en.wikipedia.org/wiki/Identity_provider_(SAML))) should have the following characteristics:

* RSA
* 2048 key length
* SHA256 algorithm
* No flags

#### [**Request Credentials**](#Request+Credentials)

You will need to change the format of the file containing the private key and turn it into a .pfx file in order to have it referenced in the **Key Store Path** property of the Request Credentials section of SAML 2.0 Authentication type configuration. Use the same password used to define the certificate in the step described above.

```
openssl pkcs12 -export -in certificate.pem -inkey key.pem -out certificate.pkcs12
```

Then rename the certificate.pkcs12 to certificate.pfx.

In Java you must have the .pfx certificate referenced within a Key Store, so to create one, follow the next steps:

```
$>cd C:\Program Files\Java\jdk-11\bin

$>keytool -genkeypair -alias gamrequest -keyalg RSA -keystore keystorerequest.jks -keysize 2048 -validity 365 -storepass changeit
```

After these commands the keystorerequest.jks file will be created in /bin where we will add our .pfx certificate.

To add this certificate.pfx to the keystore we just created use the following command:

```
$> keytool -importkeystore -srckeystore certificate.pfx -srcstoretype PKCS12 -destkeystore keystorerequest.jks -deststoretype JKS
```

Once this command is executed, we will have inside our keystorerequest.jks our certificate.pfx referenced with alias 1.

**Note**: The alias of the .pfx certificate is 1, this alias is the one to be used in the request configuration in the GAM Backoffice.

#### [**Response Credentials**](#Response+Credentials)

For configuring the Response Credentials section of SAML 2.0 Authentication type, bear in mind that you must create a Keystore using the Agesic-Coesys-Testing.cer file provided by Agesic.

```
cd c:\Program Files\Java\jdk1.8.0_20\jre\bin
keytool -importcert -trustcacerts -file Agesic-Coesys-Testing.cer -alias gamagesic -keystore agesicResponse.jks
```

As a result, you'll have a .cer file that must be referenced under the **Trust Store Path** property of the Response Credentials configuration.

After all these steps, the TAB Credentials of the SAML 20 authentication type for Agesic should look like this:

`[imagen omitida: wiki id 56623]`

## [SAP](#SAP)

You can use OpenSSL to generate a key pair as explained above.

To Request credentials, take a look at the credentials request section in this document, as it must be considered for both SAP and Agesic.

#### [**Response Credentials**](#Response+Credentials)

You must convert the certificate provided by SAP to read the response in X509 format. To this end, you may use [samlTool](https://www.samltool.com/format_x509cert.php).

Then save the result to a .pem file.

Afterwards, execute the following:

```
cd C:\Program Files\Java\jdk1.8.0_162\bin
keytool -import -file C:\cert\sapkey.pem -keystore C:\cert\sapkeystore.jks
```

You may generate a new alias by executing:

```
-alias newAlias
```

## [OKTA](#OKTA)

**Request Credentials**

First, you have to generate a Key Store.

In a command line, go to the folder where you have the keytool app.

```
cd C:\Program Files\Java\jdk-11\bin
```

**Note**: This is the standard location. Your location could be different depending on your installation.

When you are there, execute the following:

```
keytool -genkeypair -alias myalias -keyalg RSA -keystore keystorerequestokta.jks -keysize 2048 -validity 365 -storepass mypassword
```

The generated key will be stored in the keystore.jks file. Be sure to replace myalias, keystore.jks, mypassword and other values according to your needs.

You can use a [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) to generate a *keyresponse.jks* as explained above. Download Java JDK from [here.](https://www.oracle.com/my/java/technologies/downloads/)

#### [**Response Credentials**](#Response+Credentials)

First, download the certificate provided by OKTA and then convert it to a keyresponse.jks*.*

`[imagen omitida: wiki id 54249]`

In a command line, go to the folder where you have the keytool app.

```
cd C:\Program Files\Java\jdk-11\bin
```

**Note**: This is the standard location. Your location could be different depending on your installation.

When you are there, execute the following:

```
keytool -importcert -trustcacerts -file C:\...\okta.cert -alias alias -keystore keystoreresponse.jks
```

**Note**: The path of your okta.cert that you enter in **-file** depends on where your certificate is placed. The **-alias** and **-keystore** are up to the developer.

After that, a file.jks will be created in the current directory.

#### [Considerations](#Considerations)

In .NET you cannot use a Java KeyStore.

## [Azure](#Azure)

### [Java](#Java)

You can use a [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) to generate a *keyresponse.jks* as explained above. Download Java JDK from [here](https://www.oracle.com/my/java/technologies/downloads/).

#### [**Request Credentials**](#Request+Credentials)

First, you have to generate a Key Store.

In a command line, go to the folder where you have the keytool app.

```
cd C:\Program Files\Java\jdk-11\bin
```

**Note**: This is the standard location. Your location could be different depending on your installation.

When you are there, execute the following:

```
keytool -genkeypair -alias myalias -keyalg RSA -keystore keystore.jks -keysize 2048 -validity 365 -storepass mypassword -keypass mypassword //Command that generates a key
```

The generated key will be stored in the keystore.jks file. Be sure to replace myalias, keystore.jks, mypassword and other values according to your needs.

#### [**Response Credentials**](#Response+Credentials)

First, download the certificate provided by Azure and then convert it to a keyresponse.jks*.*

`[imagen omitida: wiki id 54764]`

```
keytool -importcert -trustcacerts -file C:\...\Azure.cert -alias alias -keystore keystoreresponse.jks
```

**Note**: The path of your Azure.cert that you enter in **-file** depends on where your certificate is placed. The **-alias** and **-keystore** are up to the developer.

After that, a file.jks will be created in the current directory.

`[imagen omitida: wiki id 54763]`

### [.NET & Net Framework](#.NET+%26+Net+Framework)

When working with .NET and Net Framework you cannot use a Java Trust Store.

#### [**Request Credentials**](#Request+Credentials)

In a command line, go to the folder where you have the keytool app.

```
cd C:\Program Files\Java\jdk-18.0.2.1\bin
```

**Note**: This is the standard location. Your location could be different depending on your installation.

When you are there, execute the following:

```
keytool -genkey -alias alias -keystore keystore.p12 -storetype PKCS12  -keyalg RSA  -storepass yourpass -validity 730  -keysize 4096
```

This command will generate a keystore.p12 file.

#### [**Response Credentials**](#Response+Credentials)

#### [Download the certificate provided by Azure*.*](#Download+the+certificate+provided+by+Azure.)

`[imagen omitida: wiki id 54764]`

After that, just put the path in the gam backoffice in Response Credentials.

`[imagen omitida: wiki id 54765]`

### [Additional Information](#Additional+Information)

[Certificates and encodings](https://info.ssl.com/article.aspx?Id=12149)


|  |
| --- |
| **Backlinks** |
| [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Configure SAML 2.0 GAM Authentication type using Azure](https://wiki.genexus.com/commwiki/wiki?54751) |
| [HowTo: Configure SAML 2.0 GAM Authentication type using Okta](https://wiki.genexus.com/commwiki/wiki?49660) | [HowTo: Configuring SAML 2.0 GAM Authentication type using Agesic](https://wiki.genexus.com/commwiki/wiki?41266) | [HowTo: Configuring SAML 2.0 GAM Authentication type using SAP](https://wiki.genexus.com/commwiki/wiki?41235) |

---
