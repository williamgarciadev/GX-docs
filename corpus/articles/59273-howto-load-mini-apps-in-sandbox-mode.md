---
title: "HowTo: Load Mini Apps in Sandbox Mode"
source_id: 59273
source_url: https://wiki.genexus.com/commwiki/wiki?59273
genexus_version: "18"
---

# HowTo: Load Mini Apps in Sandbox Mode

This article explains how to load and test Mini Apps in Sandbox mode in Super Apps developed with GeneXus and in non-GeneXus Super Apps.

### [Description](#Description)

Sandbox mode allows testing and validating a Mini App within the Super App before its official release.

During the [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172), it is crucial to ensure that it integrates correctly with the Super App, especially when calling services or using specific Super App screens.

To achieve this without requiring the Mini App to go through the full approval process, the Super App can run in sandbox mode, enabling developers and reviewers to load the Mini App directly. This provides a controlled testing environment where functional validations can be performed without impacting end users.

Sandbox mode is useful in these main scenarios:

* **Development Testing:** Developers can test the Mini App within the Super App to validate its integration before approval.
* **Pre-Release Review:** Super App reviewers can evaluate the Mini App and verify compliance with requirements before making it available to end users.

### [Steps to load Mini Apps in Sandbox mode](#Steps+to+load+Mini+Apps+in+Sandbox+mode)

You can load Mini Apps in [Pending or Review state](https://wiki.genexus.com/commwiki/wiki?53315) without prior approval from the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) by following these steps:

**1. Obtain the QR Code**

* When a Mini App version is uploaded to the Mini App Center, a QR code is generated.
* Both the Mini App developer and the Super App reviewer have access to this QR code.

**2. Trigger Sandbox Mode in the Super App**

* Open the Super App.
* Activate the Load Sandbox Mode.

**3. Scan the QR Code**

* The phone camera will open automatically.
* Scan the Mini App’s QR code to load it into the Super App.

**4. Run the Mini App**

* Once scanned, the Mini App will execute within the Super App in Sandbox mode.

The implementation of Sandbox mode varies depending on whether the Super App was developed with GeneXus or not.

Below are the steps for each case:

#### [**GeneXus Super Apps**](#GeneXus+Super+Apps)

Add a button to a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) of your Super App with the following event configured:

```
Event 'Sandbox'
   Composite
     GeneXusSuperApps.MiniApps.LoadSandbox()
    EndComposite
Endevent
```

This line of code in the event adds the [GeneXusSuperAppSandbox](https://wiki.genexus.com/commwiki/wiki?58517) library to the application, which enables the loading of Mini Apps by scanning their QR code.

Additionally, to control the behavior of the code in the API exposed to Mini Apps based on the execution mode, you can use the property: [GeneXusSuperApps.MiniApps.IsSandboxEnvironment](https://wiki.genexus.com/commwiki/wiki?58517) (Boolean).

It enables you to implement conditional logic in the API when the Super App is running in Sandbox mode.

#### [**Non-GeneXus Super Apps**](#Non-GeneXus+Super+Apps)

For setting up Sandbox mode in non-GeneXus Super Apps, refer to the article [Super App Sandbox Mode for Mini Apps Test and Review](https://github.com/genexus-books/gx-super-app/blob/main/docs/CreateSuperAppSandboxMode.md).

### [Important considerations](#Important+considerations)

* **Do not use the Sandbox module in production:** It is strongly recommended **not**to upload applications with the GeneXusSuperAppSandbox module to production, as it should not be publicly available. This module should only be used internally by the organization managing the Super App to test the developed Mini Apps.
* In GeneXus, there is no property yet to compile the app with or without the Sandbox module. It is included whenever the LoadSandbox method is referenced.
* The Super App version published in stores should **not** include the Sandbox module to prevent unapproved Mini Apps from being used. When the module is not in the project, the [LoadSandbox method](https://wiki.genexus.com/commwiki/wiki?58517) does not work, and the IsSandboxEnvironment property takes the value False, disabling access to the conditioned code.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Mini App Development Process](https://wiki.genexus.com/commwiki/wiki?58172) | [Mini App review and approval](https://wiki.genexus.com/commwiki/wiki?53315) |
| [MiniApps external object in GeneXusSuperApps module](https://wiki.genexus.com/commwiki/wiki?58517) |

---
