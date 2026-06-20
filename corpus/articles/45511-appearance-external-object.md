---
title: "Appearance external object"
source_id: 45511
source_url: https://wiki.genexus.com/commwiki/wiki?45511
genexus_version: "18"
---

# Appearance external object

It lets you know what the current color scheme of the device is and if it changes at any time.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [PreferredColorScheme](#PreferredColorScheme)

It returns an enumerated value based on the ColorScheme enumerated domain with the device color scheme. Read-only.

## [Event](#Event)

### [PreferredColorSchemeChanged](#PreferredColorSchemeChanged)

It is triggered when the color scheme of the device changes.

## [Domains](#Domains)

**ColorScheme:**

|  |  |
| --- | --- |
| **Unspecified** | The color scheme is unknown or the user has no preference. |
| **Light** | Light color scheme. |
| **Dark** | Dark color scheme. |

### [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Availability](#Availability)

Since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).
