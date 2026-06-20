---
title: "HowTo: Setup Single Sign On between GeneXus and SAP Cloud Platform Fiori Application using SAML"
source_id: 43404
source_url: https://wiki.genexus.com/commwiki/wiki?43404
genexus_version: "18"
---

# HowTo: Setup Single Sign On between GeneXus and SAP Cloud Platform Fiori Application using SAML

This article describes how to setup Single Sign On (SSO) between a GeneXus application and an SAP Cloud Platform (SCP) Portal Fiori application using SAML 2.0.

## [Prerequisites:](#Prerequisites%3A)

* An SCP account that has access to [SAP Cloud Platform Identity Authentication](https://cloudplatform.sap.com/capabilities/product-info.SAP-Cloud-Platform-Identity-Authentication.06dbcc67-ab2a-4d2e-aff1-28dfaaf95063.html) service.
* An SCP Portal application running.
* A GeneXus application that uses SAML as an Authentication Type. If you do not know how to do it, read [HowTo: Configuring SAML 2.0 GAM Authentication type using SAP](https://wiki.genexus.com/commwiki/wiki?41235).

## [Setup link between SCP Portal app to GeneXus app](#Setup+link+between+SCP+Portal+app+to+GeneXus+app)

First of all, you have to create a link between your applications. To achieve this, you have to do the following:

**1. On the SCP Portal application:**

Go to your app’s [Fiori Launchpad Configuration Cockpit](http://help.sap.com/viewer/e37f3c54603c4647b0b5d73c870f6223/SAP%20Fiori%20Cloud/en-US/78b024c68abd4ce2af96bcbdcee0d9ae.html). Once there, you have to select **Content Manager > Applications**in the menu and create a new Application. You have to set the Application Type Property with the URL value. Then, you have to set the URL property with the link to your GeneXus application.

**2. On GeneXus:**

While there are many ways, the easiest solution is to create a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) and, inside its Start Event, add a link to the Fiori application.

## [Setup Fiori App to use the same Identity Provider(IdP) as GeneXus](#Setup+Fiori+App+to+use+the+same+Identity+Provider%28IdP%29+as+GeneXus)

First, you have to log in to the SCP where you have your Fiori app. Then, select “Trust” option in the menu. After that, on the “Local Service Provider” tab, select the Edit button and set the Configuration Type property with the Custom value. In consequence, three more options will appear:

* Local Provider Name
* Signing Key
* Signing Certificate

`[imagen omitida: wiki id 43405]`

If the “Signing Key” and the “Signing Certificate” fields are blank, click on “Generate Key Pair” button.

`[imagen omitida: wiki id 43406]`

Then, click on the Save button, and after that, click the “Get Metadata” option:

`[imagen omitida: wiki id 43407]`

An XML file that contains the information to set up the SAML authentication will be downloaded.

Next, go to the Identity Provider Tab and click on “Add Trusted Identity Provider”.

`[imagen omitida: wiki id 43408]`

A new window will appear containing a form to include all the data about the Identity Provider.

`[imagen omitida: wiki id 43409]`

You can complete it all by yourself but if you go to your Administration Console for SAP Cloud Platform Identity Authentication and you select on the menu: **Application and Resources > Tenant Settings > SAML 2.0 Configuration,** there is a “Download Metadata File” button to download the metadata file needed to complete the previous form.

`[imagen omitida: wiki id 43416]`

After setting all this, you have to create a new application on the Administration Console for SAP Cloud Platform Identity Authentication. Once there, you have to enter to the Applications section and press the button to add a new application.

`[imagen omitida: wiki id 43417]`

Give a name to the application (for example, Login GeneXus-SAP) and press the Save button.

The following screen will appear. Select the SAML 2.0 Configuration option.

`[imagen omitida: wiki id 43418]`

The following screen will appear.

`[imagen omitida: wiki id 43419]`

Upload the SAP Cloud Platform metadata previously downloaded.

Once uploaded the XML, the SAML configuration will be automatically completed, and the app will be ready to use.

**Consideration:** The GeneXus app and the Fiori app must have different SCP Identity Authentication apps.

## [Setup SSO on GeneXus](#Setup+SSO+on+GeneXus)

To set up the SSO on the GeneXus app, first, you have to change your Knowledge Base Login screen by setting the [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590), available at the KB Version level, with the Web Panel GAMSSOLogin.

`[imagen omitida: wiki id 43420]`

After that, you have to go to the Web Panel GAMSSOLogin and open the Events Tab. On the Start Event change this code line:

```
GAMRepository.LoginGAMRemote()
```

by the following two code lines:

```
&AdditionalParameter.AuthenticationTypeName =  "<YourSAMLAuthenticationTypeName>"

&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors )
```

This will connect to the Identity Provider to obtain a valid session for the user if it exists. On the other hand, it will show a login window for the user to enter his credentials.

`[imagen omitida: wiki id 43421]`

You are ready to try out the Single Sign On.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
