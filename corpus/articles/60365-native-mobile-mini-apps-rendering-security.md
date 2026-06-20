---
title: "Native Mobile Mini Apps rendering security"
source_id: 60365
source_url: https://wiki.genexus.com/commwiki/wiki?60365
genexus_version: "18"
---

# Native Mobile Mini Apps rendering security

This article describes the security mechanisms implemented by GeneXus for running Native Mobile Mini Apps within Super Apps, with a focus on code execution, data isolation, authentication, and secure APIs.

The approach used by GeneXus for rendering Native Mobile Mini Apps in Super Apps offers strong security in several important aspects.

### [Native code rendering security](#Native+code+rendering+security)

The Render is responsible for rendering Native Mobile Mini Apps using native code, which is analyzed statically for security concerns. This approach differs from other solutions that rely on WebViews to dynamically render code from external sources, potentially introducing security risks.

The logic layer, implemented with thoroughly analyzed native code, ensures that a Mini App cannot execute malicious code. Native capabilities are accessed through specific APIs from the Super App, with the Render Engine acting as a bridge for API calls.

The following figure illustrates the flow of an API call:

`[imagen omitida: wiki id 60366]`

### [Cross-domain attack prevention](#Cross-domain+attack+prevention)

Cross-domain attacks are prevented because the Super App code is wired to communicate directly with a specific Mini App Store to load Mini Apps.

Packages retrieved from the Mini App Store are digitally signed on the server side, and the Super App checks the consistency of the package by verifying the signature on the client side. This mechanism is built into the Render package.

`[imagen omitida: wiki id 60368]`

`[imagen omitida: wiki id 60369]`

### [Data isolation between Mini Apps](#Data+isolation+between+Mini+Apps)

Sensitive data is not exposed between Mini Apps. Each Mini App can use its storage, but can’t access the storage of other Mini Apps. They can access the storage through a well-known API, which Mini Apps use to sandbox the data.

More specifically, on Apple platforms, this means:

* Mini Apps do not have direct access to [Keychain services](https://developer.apple.com/documentation/security/keychain_services). Instead, indirect access (i.e. for [ClientStorage API secure storage](https://wiki.genexus.com/commwiki/wiki?31272)) is provided via a centralized API by the [SuperApp Render](https://wiki.genexus.com/commwiki/wiki?58435). This API consistently adds a prefixed [kSecAttrService](https://developer.apple.com/documentation/security/ksecattrservice) attribute unique to each Mini App identifier.
* Direct file system access is not allowed for Mini Apps, as it is restricted by the Super App Render. Instead, indirect access (i.e. for [ClientStorage API](https://wiki.genexus.com/commwiki/wiki?31272) or [cached data](https://wiki.genexus.com/commwiki/wiki?18602)) is also provided via a centralized API by the Super App Render, and it’s sandboxed for each Mini App under the “GXMiniApps/{MiniApp-ID}” folder (for each of the supported [FileManager.SearchPathDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory): [cachesDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/cachesdirectory), [applicationSupportDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/applicationsupportdirectory) or [documentDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/documentdirectory)).
* In general, access to any shared native resource is only possible through the Super App Render, which can control access to Mini Apps, restricting it when necessary (similar to how the In-App purchases API operates).

Analogously, this also applies to the Android platform:

* Access to the file system is restricted by the Render, so Mini Apps cannot access it.
* A Mini App's data is saved within its directory, identified by the Mini App's Id.
* The ClientStorage (a SharedPreferences instance) is unique for each Mini App, so it is not shared with the Super App either.

### [Secure Authentication Management](#Secure+Authentication+Management)

To prevent broken authentication, Mini Apps can only gain access to a valid authentication session through the [Super App API](https://wiki.genexus.com/commwiki/wiki?58207). Therefore, the Super App owner is responsible for creating a valid authentication method.

For more information, see [Authentication between Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59284,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [What are Native Mobile Mini Apps?](https://wiki.genexus.com/commwiki/wiki?58298) |

---
