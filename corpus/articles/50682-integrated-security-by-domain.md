---
title: "Integrated Security by Domain"
source_id: 50682
source_url: https://wiki.genexus.com/commwiki/wiki?50682
genexus_version: "18"
---

# Integrated Security by Domain

In this article, you will learn how to configure the Integrated Security by Domain feature.

Integrated Security by Domain is provided for cases where you have several applications under the same domain and subdomain, and it is essential for them to function.

Its use is recommended when some of the domain applications do not require user authentication and the content of a [Panel](https://wiki.genexus.com/commwiki/wiki?24829) simply varies when there is an authenticated user. These applications have Panels with the property [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = None, so they can be accessed by everyone regardless if they are authenticated or not.

Integrated Security by Domain is implemented using a cookie called GAMIntSecByDomain. At login, when this property is enabled and configured in Server Mode, the cookie will be generated at Domain level.

To use this functionality, the following GeneXus Modules must be included in all knowledge bases:

* [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980)
* [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917)
* [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252)

### [Configuration](#Configuration)

The following configuration is required for each application in which we want to use this functionality (Server and Clients).  
To do so, go to the GAM backend > Settings > Repository Configuration > Sessions and select the Enable Integrated Security by Domain property.

`[imagen omitida: wiki id 50683]`

Next, the following properties will be displayed:

`[imagen omitida: wiki id 50690]`

* **Integrated Security by Domain mode**: it must be configured in Server mode for the Identity provider (application that requires authentication), and as Client in all the applications that will use this session.
* **Integrated Security by Domain JWT secret**: this is the symmetric hexadecimal key used to sign the token sent (256 bits is the default value).
* **Integrated Security by Domain AES encryption key**: it is the hexadecimal key of the AES encryption algorithm; different lengths–128, 192 or 256 bits–can be used (recommended: 256 bits).

This functionality must also be activated in the clients, which have a method that validates the cookie and returns True if there is an authenticated user in the domain:

```
GAMRepository.ValidIntegratedSecurityByDomain(out:&UserGUID, out:&GAMErrorCollection): Boolean
```

The GUID of the authenticated user in the domain is returned in &UserGUID. With this, for example, the user's data can be obtained:

```
If not &UserGUID.isEmpty()
      &GAMUser.Load(&UserGUID)
      &UserEmail = &GAMUSer.Email
Endif
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).
