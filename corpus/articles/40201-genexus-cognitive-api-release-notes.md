---
title: "GeneXus Cognitive API - Release notes"
source_id: 40201
source_url: https://wiki.genexus.com/commwiki/wiki?40201
genexus_version: "18"
---

# GeneXus Cognitive API - Release notes

The table below describes the main [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) features for each release. It's highly recommended to use the last available version.


### [**GeneXus 17 - Beta channel**](#GeneXus+17+-+Beta+channel)

**Date**: By night-build.  
**Version**: 3.5.X  
`[imagen omitida: wiki id 40856]` [Download](https://www.genexus.com/en/developers/downloadcenter?data=4978;;)

What's new.

* Uber Ludwig on-premise provider added (2.8.7)
* MLKit for iOS on-devide provider added (3.2.0)
* Kybalion (by [IDHATA](http://www.idatha.com/)) provider added (3.4.2)
* Improvements and bug fixes.

---

### [**GeneXus 17 Upgrade 7 - Preview Channel**](#GeneXus+17+Upgrade+7+-+Preview+Channel)

**Date**: Jan, 2022  
**Version**: 2.7.X

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 6**](#GeneXus+17+Upgrade+6)

**Date**: Nov 29, 2021  
**Version**: 2.6.1

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 5**](#GeneXus+17+Upgrade+5)

**Date**: Aug 20, 2021  
**Version**: 2.5.1

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 4**](#GeneXus+17+Upgrade+4)

**Date**: Jun 23, 2021  
**Version**: 2.4.1

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 3**](#GeneXus+17+Upgrade+3)

**Date**: May 3, 2021  
**Version**: 2.3.0

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 2**](#GeneXus+17+Upgrade+2)

**Date**: February 24, 2021  
**Version**: 2.2.1

What's new.

* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 1**](#GeneXus+17+Upgrade+1)

**Date**: December 16, 2020  
**Version**: 2.1.4

What's new.

* IBM support for JSON-Auth string instead of API-Key has been added (2.1.1).  
    
  Detailed explanation:  
  Instead of doing something like this for setting the provider:

  ```
  &prop = new()
  &prop.Key = PropertyKey.Key
  &prop.Value = !"{API-Key}"
  &provider.Properties.Add(&prop)
  ```

  you must do the following:

  ```
  &prop = new()
  &prop.Key = PropertyKey.Key
  &prop.Value = !'{"apikey":"xxx", "iam_apikey_description":"xxx", ... "url":"xxx"}' // JSON-string
  &provider.Properties.Add(&prop)
  ```

  or this alternative:

  ```
  &prop = new()
  &prop.Key = PropertyKey.Key
  &prop.Value = !'C:\path\to\IBM_Service_Auth.json' // JSON-filepath
  &provider.Properties.Add(&prop)
  ```

  Where the IBM\_Service\_Auth.json contains the JSON-string provided by IBM (go to [IBM Cloud Resources](https://cloud.ibm.com/resources) (logged-in) > Select your resource > Service Credentials).
* Improvements and bug fixes after beta release.

---

### [**GeneXus 17 Upgrade 0**](#GeneXus+17+Upgrade+0)

**Date**: October 20, 2020  
**Version**: 2.0.0

What's new.

* Improvements and bug fixes after beta release.

---

## [Availability](#Availability)

This document applies as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

---

|  |
| --- |
| **Backlinks** |
|
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
|

---
