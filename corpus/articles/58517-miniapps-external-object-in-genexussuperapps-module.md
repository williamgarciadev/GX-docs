---
title: "MiniApps external object in GeneXusSuperApps module"
source_id: 58517
source_url: https://wiki.genexus.com/commwiki/wiki?58517
genexus_version: "18"
---

# MiniApps external object in GeneXusSuperApps module

The MiniApps external object (located in the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959)) provides functionalities for loading, managing, and interacting with [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) from a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,).

`[imagen omitida: wiki id 58518]`

### [Properties](#Properties)

#### [**IsSandboxEnvironment**](#IsSandboxEnvironment+)

Allows the implementation of conditional code in the API exposed to the Mini App, depending on the Super App's execution mode (whether using Load or LoadSandbox methods).

#### [**CurrentMiniAppId**](#CurrentMiniAppId+)

Returns the unique identifier of the Mini App that is currently running. This identifier is useful when a Mini App makes a request or redirects to the Super App using the Super App API.

Knowing the CurrentMiniAppId lets you determine which Mini App initiated the request or performed the redirection.

In the [Verdant Bank - GeneXus Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766), the CurrentMiniAppId property is used to determine which Mini App initiated a payment request to the Super App. This is crucial for processing Transactions and ensuring that the payment is associated with the correct Mini App.

**Important Note**:

**Empty Value:** If CurrentMiniAppId returns an empty value, the operation is not taking place in the context of a Mini App. This may occur if the Super App is handling a request that does not originate from a Mini App, or if the Mini App context needs to be properly established.

You can use the CurrentMiniAppId property in the KB Object that makes the API call. It can be used with all client-side calls made by this object, including events from Menus and Panels, or when calling offline objects directly. This means you can adapt how your Super App interacts based on which Mini App is involved.

### [Methods](#Methods)

#### [**Load method**](#Load+method)

Loads a Mini App and transitions to it.

#### [**Parameters**](#Parameters)

&MiniAppInformation: (SDT) Input parameter with the Mini App information, as previously defined.

Details about MiniAppInformation SDT:

**Id:** (String) The Mini App identifier as required by the Load method (see below).  
**Name:** (String) The Mini App's human-readable name.  
**Description:** (String) A short description of the Mini App.  
**Metadata:** (URL) A URL pointing to the Mini App metadata.  
**EntryPoint:** (String) Mini App main name.  
**ServiceURL:** (URL) A URL pointing to the Mini App backend service URL.  
**Signature:** (String) Mini App signature.  
**Version:** (Integer) Mini App version.  
**Icon:** (Image) An application icon for the Mini App.  
**Banner:** (Image) An alternative image for promoting or featuring the Mini App.  
**Card:** (Image) An alternative image to present the Mini App in the Super App.

The following validations should be performed on MiniAppInformation fields; otherwise, the load will fail:

* EntryPoint should have the format {GUID}-{Name}, where {GUID} is the GUID of the KB Object type (currently valid are Panel and Menu).
* Signature should not be empty and should be valid for the downloaded metadata from the URL in the Metadata field (If cached, no re-validation is required).

If the Mini App does not exist in the Mini App Center or is not compatible with the current version of the Super App, the method call fails (aborting the composite block when appropriate).

**Note:** The event where the Load method is used cannot contain invocations to other Super App objects (Procedures, Data Providers, Panels). This is due to the context shift from the Super App to the Mini App, which makes it impossible to guarantee that these requests can be fulfilled.

#### [**GetCached method**](#GetCached+method)

Returns a collection of cached Mini Apps.

Return Type:  
Collection of CachedMiniApp SDT: Represents Mini Apps that have been loaded and cached on the device.

#### [**RemoveCached method**](#RemoveCached+method)

Deletes a specific Mini App from the cache.

#### [Parameters](#Parameters)

&miniAppId: The identifier of the Mini App to be removed.  
&miniAppVersion: The version of the Mini App to be removed.

#### [**ClearCached method**](#ClearCached+method)

Deletes all the Mini Apps from the cache.

#### [**LoadSandbox method**](#LoadSandbox+method)

Loads a Mini App in sandbox mode. The Mini App version must be under Review at the Mini App Center to scan its QR code.

**Warning:** It is not recommended to distribute applications with this method to production, since it must be used internally by the Super App administrative organization to test the developed Mini Apps.

For more information, see [HowTo: Load Mini Apps in Sandbox Mode](https://wiki.genexus.com/commwiki/wiki?59273).

### [Considerations](#Considerations)

The MiniApps external object is available only when a Mini App is loaded inside a Super App. If called in another context, all methods will fail.

### [Scope](#Scope)

Generators: [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)


|  |
| --- |
| **Backlinks** |
| [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959) | [HowTo: Load Mini Apps in Sandbox Mode](https://wiki.genexus.com/commwiki/wiki?59273) |

---
