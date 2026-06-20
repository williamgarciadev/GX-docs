---
title: "Enable Sign in with Apple property"
source_id: 44467
source_url: https://wiki.genexus.com/commwiki/wiki?44467
genexus_version: "18"
---

# Enable Sign in with Apple property

Allows the app to use the device's Apple ID as an identity provider.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

For an iOS app to sign in with Apple, the ["Sign In with Apple" entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_applesignin) must be enabled in the Xcode project.

The Enable Sign in with Apple property in a Smart devices main object enables this entitlement.

Apple requires to have Sign In with Apple if the app has another external sign in provider (like Facebook or Twitter), according to [this App Store Review Guideline](https://developer.apple.com/app-store/review/guidelines/#sign-in-with-apple). It is available for iOS 13, tvOS 13, watchOS 6 and macOS Catalina.

You can check the effect of enabling this property by editing the XCode project:

`[imagen omitida: wiki id 44489]`  
  
The property Enable Sign in with Apple applies only to main Smart Devices objects.

See the Apple documentation about this topic [here](https://developer.apple.com/sign-in-with-apple/get-started/).

To Sign in with Apple, see [GAM - Apple Authentication type](https://wiki.genexus.com/commwiki/wiki?44478).

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

### [Scope](#Scope)

**Objects:** [Menu for Smart Devices](https://wiki.genexus.com/commwiki/wiki?16321), [Panel for Smart Devices](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974)  
**Platforms:** Smart Devices(IOS)

### [See Also](#See+Also)

* [GAM - Apple Authentication type](https://wiki.genexus.com/commwiki/wiki?44478)


|  |
| --- |
| **Backlinks** |
| [GAM - Apple Authentication type](https://wiki.genexus.com/commwiki/wiki?44478) |

---
