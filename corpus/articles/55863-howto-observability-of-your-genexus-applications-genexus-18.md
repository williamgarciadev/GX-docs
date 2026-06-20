---
title: "HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)"
source_id: 55863
source_url: https://wiki.genexus.com/commwiki/wiki?55863
genexus_version: "18"
---

# HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)

The purpose of this article is to explain the necessary steps to allow OpenTelemetry for your applications’ observability.

### [Steps](#Steps)

**1.** Activate Observability in GeneXus.

In [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408), select the service with which you desire the observability of your applications.

**2.** Build any object.

**3.** Deploy.  

**Note**: For**Java** **applications**, the Observability support is available only for applications deployed through Docker (Containers).

**4.** Configure the app with the Observability data, according to the provider selected:

* [Observability with OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775)
  + [Observability with Lightstep](https://wiki.genexus.com/commwiki/wiki?53776)
* [Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774)
* [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383)

### [Availability](#Availability)

This functionality is available as Beta since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).
