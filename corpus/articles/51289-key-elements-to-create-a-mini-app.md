---
title: "Key elements to create a Mini App"
source_id: 51289
source_url: https://wiki.genexus.com/commwiki/wiki?51289
genexus_version: "18"
---

# Key elements to create a Mini App

Mini Apps can be developed as either Native Mini Apps or Web Mini Apps, depending on your needs, the UI requirements, and the kind of services you want to integrate as mini applications.

* A [Native Mini App](https://wiki.genexus.com/commwiki/wiki?58298) is an application executed within the Super App domain through the Super App Render. GeneXus is used for its development, and the same process is followed as for any other mobile application created with GeneXus, requiring no additional skills beyond those of a typical GeneXus mobile developer. Native Mini Apps are composed of metadata (a .gxsd file that will be rendered as a native app) and backend services.
* A [Web Mini App](https://wiki.genexus.com/commwiki/wiki?57422), on the other hand, can be developed with GeneXus or any web technologies and executed within a WebView inside the Super App.

## [Enroll as a Mini App Developer](#Enroll+as+a+Mini+App+Developer)

A Mini App makes sense in the context of a Super App. Therefore, the first step is to register as a developer of a certain Super App (especially when developing a Mini App for a Super App that is external to your organization). This enables you to get all the resources needed to carry out the integration, namely, the Super App API and any design and interaction resources that it provides.

## [Development and Prototyping](#Development+and+Prototyping)

During the development stage, you will have to import the Super App API in order to program the invocations to the services that it exposes.

For Native Mini Apps, you will also need to install the [GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076). This module provides additional resources for interacting with the Super App (for example, the Exit method for returning to the Super App).

The Mini App is loaded dynamically from the Super App, so some restrictions apply. See details in [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172)

Finally, to be able to test your Mini App integrated into the services of the Super App, you need a sandbox version of the Super App.

## [Deploy and Review](#Deploy+and+Review)

Once you have completed the development and testing of the Mini App, the next step is to deploy the application (or the backend services for the Native Mini App) and submit it for review.

You can see the details in [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172) and [HowTo: Upload a Mini App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53318).


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Key elements when building a Super App ecosystem](https://wiki.genexus.com/commwiki/wiki?50902) |

---
