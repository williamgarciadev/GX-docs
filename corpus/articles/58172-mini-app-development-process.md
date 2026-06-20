---
title: "Mini App Development Process"
source_id: 58172
source_url: https://wiki.genexus.com/commwiki/wiki?58172
genexus_version: "18"
---

# Mini App Development Process

This document is a guide for developing [Native Mini App](https://wiki.genexus.com/commwiki/wiki?58298)s, including their creation in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290), as well as their development, prototyping, testing, and publication.

Whether starting from scratch or integrating new features, this guide aims to streamline the development process and highlight best practices for successful Mini App development.

### [Mini App Center](#Mini+App+Center)

The first step when creating a Mini App is to set it up in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).   
For detailed instructions, refer to the guide in [HowTo: Create a Mini App on the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53317).

### [Development](#Development)

Developing a Mini App in GeneXus is similar to developing a Native Mobile Application. If you have already created this type of application with GeneXus, developing a Mini App will be very easy.

1) Start by creating a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), which must be one of the mobile objects ([Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974)).

2) Continue with the implementation of the business logic and user interface.

As the Mini App is loaded dynamically from the Super App, the following restrictions will apply compared to other GeneXus apps (i.e., standard or compiled apps).

* It has to be an online app.
* [Functionalities for mobile with special behavior when executed as Native Mobile Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55120,,).
* The use of User Controls and Extensions will be limited to those declared in the Super App.

### [Integration with the Super App API](#Integration+with+the+Super+App+API)

To communicate with the [Super App API](https://wiki.genexus.com/commwiki/wiki?58207):

* **GeneXus Integration:** Import the corresponding module for the Super App API if it is developed with GeneXus.
* **Non-GeneXus Super App:** Implement the corresponding External Object.

For detailed instructions, refer to [HowTo: Call a Super App API from a Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58185).

### [Integration with Super App Render](#Integration+with+Super+App+Render)

You will also need to install the [GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076). This module provides additional resources for interacting with the Super App (for example, the Exit method for returning to the Super App).

### [Prototyping and Testing](#Prototyping+and+Testing)

During the incremental development of a [Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58298), there are at least three testing instances to consider:

1. Independent Testing of the Mini App

While the Mini App does not use anything from the Super App API (which will be the case at the beginning), it can be executed stand-alone (compiling and running it from an emulator) or using [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) (GPN).

2. Testing the Mini App with Super App API Integration

In a slightly more advanced development process, when integrating with the Super App API, there are two alternatives for testing that integration:

* [Mocking the Super App API](https://wiki.genexus.com/commwiki/wiki?58219)

Create a Mock of the Super App API directly in the Mini App development KB. This will allow you to test the integration with the Super App API using GPN.

* Using a test Super App

Set up a test Super App with the API functionality implemented and load the Mini App from there (this also requires the Mini App to be uploaded to the Mini App Center).

3. Real Integration Testing with the Super App

Real integration testing using the [Load Mini Apps in Sandbox Mode](https://wiki.genexus.com/commwiki/wiki?59273) from a pre-production Super App.

4. Post-Release testing with production Super App

Once you have passed the previous testing stages and the Mini App has been released to the Super App in production, make sure it works correctly by loading it in production.

### [Deploy and Review](#Deploy+and+Review)

Once you have completed the development of the Mini App, the next step is to submit it for the final test and review.

This means that you must:

1. Deploy the Mini App backend services in your production environment.  
   This step can be performed through the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092). To include the metadata, the "Enable KBN" property must be enabled.
2. Publish a new Mini App version and submit it for review through the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).  
   In this step, you must get the following from the previous step: the application metadata file (.gxsd file generated in the gxmetadata directory for each platform) and the service URL.

You can see the details in: [HowTo: Upload a Mini App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53318).


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [HowTo: Load Mini Apps in Sandbox Mode](https://wiki.genexus.com/commwiki/wiki?59273) | [Key elements to create a Mini App](https://wiki.genexus.com/commwiki/wiki?51289) |

---
