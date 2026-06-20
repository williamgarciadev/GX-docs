---
title: "GeneXusCryptography Module Asymmetric"
source_id: 42685
source_url: https://wiki.genexus.com/commwiki/wiki?42685
genexus_version: "18"
---

# GeneXusCryptography Module Asymmetric

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [Asymmetric Cryptography](#Asymmetric+Cryptography)

It is also known as Public Key Cryptography.

The main characteristic of asymmetric cryptography is that it uses a pair of mathematically bound keys; one of them is known as a private key and the other as a public key. Public keys are derived from private keys but private keys cannot be derived from public keys.

It can be used for the same things as symmetric cryptography plus digital signing, as encryption mechanisms are slower and more limited than symmetric encryption schemas.

The most commonly used types of key pairs are RSA and ECDSA and differ on the mathematical basis for the key pair generation which gives them some proper properties.

**The private key must be kept secret**; this key is not shared under any circumstances, as nobody needs it for anything and nobody should ask for it (unless it is just for testing and is not official).

The public key is meant to be shared with everyone with whom a communication channel will be established. It is usually distributed on digital certificates for which the standard is X509 using PKI (Public Key Infrastructure).

Encryption can be done with a private key and then decrypted with a public key or vice versa, depending on the purpose of the encryption or the place of each in the communication. If the message is encrypted with a private key, everyone who has the public key can decrypt it. If the message is encrypted with the public key, only the owner of that key will be able to decrypt the messages because he is the only one who has or knows the private key. Some communication schemes are defined where someone encrypts with a public key and then decrypts with his private key or vice versa, or they are mixed with previous or later signatures.

A message is always signed with the private key and verified with the public key.

### [Public Key Infrastructure](#Public+Key+Infrastructure)

A system is implemented on the Internet where trustworthy third parties called Certificate Authorities (CAs) are widely known and trusted. The goal of the CA is to validate the identity of a certificate's owner.

The process goes as follows:

* A person or company creates a key pair and sends the public key (on a certificate) to a CA along with other validating identity information for the CA to verify that the person or company actually is who the certificate says he is.
* The CA creates a certificate with the public key and the other required data and signs it with its own private key.

CA public keys are publicly known and some of them come preinstalled on commonly used software. This way, CA signatures can be verified by anyone and a chain of trust is established. Trusting the CA means trusting the certificates that are signed by that CA. Certificates can then contain a chain of certificates representing a hierarchical chain of trust.

### [Key pair generation](#Key+pair+generation)

The key pair can be generated locally with some tools, the most popular of which is [OpenSSL](https://www.openssl.org/).

Anyone can create, sign, and distribute a certificate, but most people will not trust it and software will not trust it by default, either. This type of certificate is known as self-signed and is commonly used for testing.

When the key pair is generated, the encryption and signing algorithms are established along with the hash algorithm that will be used to generate and verify signatures. The signature will always be verified using the algorithms preestablished on the certificate.

### [Digital signature](#Digital+signature)

NIST definition:

*"Digital signatures are used to provide assurance of origin authentication and data integrity. These assurances are sometimes extended to provide assurance that a party in a dispute (the signatory) cannot repudiate (i.e., refute) the validity of a signed document; this is commonly known as non-repudiation"*[Source](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)

The messages to sign are usually too big for these types of algorithms so, what is done is actually calculate the hash digest of the message (with a secure hashing function) and sign the digest, not the actual message. That is why a hash function must be established and respected on the certificates.

#### [NIST Recommendations (March 21, 2019)](#NIST+Recommendations+%28March+21%2C+2019%29)

| Digital Signature Process | Domain Parameters | Status |
| --- | --- | --- |
| Digital Signature  Generation | ECDSA: len(n) < 224  RSA: len(n) < 2048 | Disallowed |
| ECDSA: len(n) ≥ 224  RSA: len(n) ≥ 2048 | Acceptable |
| Digital Signature  Verification | ECDSA: 160 ≤ len(n) < 224  RSA: 1024 ≤ len(n) < 2048 | Legacy use |
| ECDSA: len(n) ≥ 224  RSA: len(n) ≥ 2048 | Acceptable |

Definition of status approval terms

* Acceptable: is used to mean that the algorithm and key length in a FIPS or SP is safe to use; no security risk is currently known when used in accordance with any associated guidance.
* Deprecated: means that the algorithm and key length may be used, but the user must accept some security risk.
* Disallowed: means that the algorithm or key length is no longer allowed for cryptographic protection.

### [Useful tools:](#Useful+tools%3A)

* [OpenSSL](https://www.openssl.org/)
* [CertUtil](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil)
* [KeyStore Explorer](https://keystore-explorer.org/)
* [Java KeyTool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)

### [Useful readings](#Useful+readings)

* [Testing for weak encryption (OWASP)](https://www.owasp.org/index.php/Testing_for_Weak_Encryption_(OTG-CRYPST-004))
* [NIST Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)


|  |
| --- |
| **Backlinks** |
| [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918) | [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
