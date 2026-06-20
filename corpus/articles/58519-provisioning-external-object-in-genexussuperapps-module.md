---
title: "Provisioning external object in GeneXusSuperApps module"
source_id: 58519
source_url: https://wiki.genexus.com/commwiki/wiki?58519
genexus_version: "18"
---

# Provisioning external object in GeneXusSuperApps module

The Provisioning external object  (located in the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959)) enables a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) to query and manage the [Mini App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) catalog in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290), providing access to detailed information and metadata about available Mini Apps.

`[imagen omitida: wiki id 58520]`

### [Properties](#Properties)

#### [**ServerURL (Url)**](#ServerURL+%28Url%29)

A read-only property that returns the provisioning server's URL of the Mini App Center.

### [Methods](#Methods)

These methods allow the Super App to query the Mini App catalog in the Mini App Center, filtering with various criteria. You need to configure the Super App properties to access the corresponding catalog.

Notes on returned MiniAppInformation fields:

* **Metadata & ServiceURL** are required (should not be empty).
* **Icon, Banner & Card** are optional (can be empty) and could be relative URLs. If URLs are relative, Provisioning implementations transform URLs to absolute; URLs are relative to ProvisioningURL.

#### [**GetByText method**](#GetByText+method)

Returns the list of Mini Apps that match the given text criteria. The search is performed with a full-text search on the Mini Programs (name, title, description).

#### [**Parameters**](#Parameters)

* &Text: (String) - The string with the search criteria.
* &Start: (Integer) - 0-based index from which elements will be returned.
* &Count: (Integer) - Maximum number of returned elements (0 means all).

Returns: A collection of MiniAppInformation.

#### **GetByLocation method**

Returns the list of Mini Apps that are available inside the circular region with the center in the given &geopoint and a maximum radius given by &radius.

#### [**Parameters**](#Parameters)

* &Center: (Geopoint) - The center point of the specified region.
* &Radius: (Numeric) - The radius in meters of the circular region.
* &Start: (Integer) - 0-based index from which elements will be returned.
* &Count: (Integer) -  Maximum number of returned elements (0 means all).

Returns: A collection of MiniAppInformation.

#### [**GetByTag method**](#GetByTag+method)

When registering a Mini App in the Mini App Center, several tags can be declared. This method will look for exact matches for the given tag.

#### [**Parameters**](#Parameters)

* &Tag: (String) - The tag to search for.
* &Start: (Integer) - 0-based index from which elements will be returned.
* &Count: (Integer) -  Maximum number of returned elements (0 means all).

Returns: A collection of MiniAppInformation.

#### [**GetById method**](#GetById+method)

Returns the Mini Apps corresponding to the given Id.

#### [**Parameters**](#Parameters)

&Id: (String) - Mini App Id

Returns: MiniAppInformation SDT.

#### [**GetFeatured method**](#GetFeatured+method)

Returns the list of [Mini Apps declared as highlighted](https://wiki.genexus.com/commwiki/wiki?56095) in a time window (validFrom <= &today =< validTo).

#### [**Parameters**](#Parameters)

* &Start: (Integer) - 0-based index from which elements will be returned.
* &Count: (Integer) - Maximum number of returned elements (0 means all).

Returns: A collection of MiniAppInformation.

#### [**GetByFilters method**](#GetByFilters+method)

The Provisioning.GetByFilters method allows searching for Mini Apps in the Mini App Center based on certain filter criteria.

Parameters

●    &Filters: (Collection of MiniAppFilter SDT) - The filters to search for.  
●    &Start: (Integer) - 0-based index from which elements will be returned.  
●    &Count: (Integer) - maximum number of returned elements (0 means all).

Read more at [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960).

### [Availability](#Availability)

This module is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).


|  |
| --- |
| **Backlinks** |
| [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959) |

---
