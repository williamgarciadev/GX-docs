---
title: "Cryptography data types"
source_id: 22980
source_url: https://wiki.genexus.com/commwiki/wiki?22980
genexus_version: "18"
---

# Cryptography data types

**Warning**: These data types will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace these data types. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

It is common for corporate applications to imply security requirements for storing, transporting, and exchanging information. To meet such requirements, a data type for encrypting texts and signing documents becomes necessary.

Cryptography data types enable us to:

* Digitally sign text.
* Validate a digital signature.
* Encrypt /de-encrypt a given text.
* Calculate the hash for a given text.

When applied together, these methods ensure authentication, integrity, confidentiality, and non-repudiation of messages.

Scenarios for use

* In general, passwords should not be stored in plain text. Instead, the result of a hash applied on a password is what we store.
* Hash and digital signature functions are used in the case of electronic invoices.

### [Implementation of Cryptography data types](#Implementation+of+Cryptography+data+types)

The following data types: CryptoHash, CryptoSign, CryptoSymmetricEncrypt, CryptoAsymmetricEncrypt, CryptoCertificate, and CryptoSignXML, are the ones available to solve the cryptography needs of GeneXus applications.

Enumerated domains, such as CryptoHashAlgorithm, CryptoSignAlgorithm, and CryptoEncryptAlgorithm, contain the cryptography algorithms supported.

Here you can find details about the methods of each data type, including examples for use.


* [CryptoHash data type](https://wiki.genexus.com/commwiki/wiki?33457)
* [CryptoSign data type](https://wiki.genexus.com/commwiki/wiki?33458)
* [CryptoSignXML data type](https://wiki.genexus.com/commwiki/wiki?33459)
* [CryptoSymmetricEncrypt data type](https://wiki.genexus.com/commwiki/wiki?33461)
* [CryptoAsymmetricEncrypt data type](https://wiki.genexus.com/commwiki/wiki?33462)
* [CryptoCertifcate data type](https://wiki.genexus.com/commwiki/wiki?33463)

---
