---
title: "SSL Pinning Pin Set property"
source_id: 44258
source_url: https://wiki.genexus.com/commwiki/wiki?44258
genexus_version: "18"
---

# SSL Pinning Pin Set property

Specifies SSL Pinning Pin Set values to validate HTTPS connection from devices to the server.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Front end

### [Description](#Description)

The SSL Pinning Pin Set defines the server's public key hash (pin sha-256). The Android generator allows defining a single key hash, while the Apple generator requires at least 2 key hashes, separated by a comma (,). In both cases, having more than one hash configured is recommended.

If this property has a value, a Certificate pinning is performed by the device when it is connected to the server set in the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146).

Certificate pinning is done by providing a set of certificates by hash of the public key (SubjectPublicKeyInfo of the X.509 certificate). A certificate chain is then valid only if the certificate chain contains at least one of the pinned public keys.

**More Info:**

[OWASP Certificate and Public Key Pinning](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

For example, in the case of the server apps5.genexus.com the key hash is as follows:

"LjCcH/Lyd5M5T2ulEMxYhqS7JkgJmCzUf1fxoYzy5D4="

One key hash is always a 44-character long string.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Compatibility](#Compatibility)

Available for Apple as of Genexus 17 upgrade 1.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

### [See Also](#See+Also)

[OWASP Certificate and Public Key Pinning](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning)  
[Android Developer Security Certificate Pinning](https://developer.android.com/training/articles/security-config#CertificatePinning)  
[Services URL property](https://wiki.genexus.com/commwiki/wiki?21146)
