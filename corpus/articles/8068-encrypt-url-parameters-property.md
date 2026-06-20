---
title: "Encrypt URL parameters property"
source_id: 8068
source_url: https://wiki.genexus.com/commwiki/wiki?8068
genexus_version: "18"
---

# Encrypt URL parameters property

Allows or denies the encryption of the parameters sent to a URL, and establishes security levels when parameter encryption is used in Web Objects.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Indicates that the parameters in the Web objects URL will not be encrypted. This is the default value. |
| **Session key** | Indicates that the parameters in the URL will be encrypted using a different key for each session. The encryption is made using local cookies. This value offers a higher level of security, but it does not allow shared URLs. This means that user X cannot send a URL with parameters to user Y because, in this case, the URL will not work given that the corresponding cookie is required for decryption. |
| **Site key** | Parameters in the Web objects URL are encrypted, but the encryption key will be the same for the whole site. In this case, cookies are not used. This implies a lower level of security, but simplifies link transfers. |
| **Use Environment property value** | The property value is obtained from the Environment property with the same name. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It is recommended to read [Protecting sensitive data used on the client side](https://wiki.genexus.com/commwiki/wiki?31506).

#### [Notes:](#Notes%3A)

* The encryption key for encrypting the URL parameters can be specified using the application.key file (see [SAC #29369](https://www.genexus.com/en/developers/websac?data=29369;;)). In the case of NET see [SAC #29874](https://www.genexus.com/en/developers/websac?data=29874;;) — more information in [Application Encryption Key property](https://wiki.genexus.com/commwiki/wiki?36909).
* When using [GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4179,,), all applications associated with a Task must have the **Encrypt URL Parameters property** set to 'Use Environment property value'.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[GetEncryptionKey function](https://wiki.genexus.com/commwiki/wiki?8385)


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |
| [Parameter encryption on Dynamic calls](https://wiki.genexus.com/commwiki/wiki?29842) | [Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404) | [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) |
| [Category:URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523) |

---
