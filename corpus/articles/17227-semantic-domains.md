---
title: "Semantic Domains"
source_id: 17227
source_url: https://wiki.genexus.com/commwiki/wiki?17227
genexus_version: "18"
---

# Semantic Domains

A **Semantic Domain** is a predefined [Domain](https://wiki.genexus.com/commwiki/wiki?7221) with specific semantics.

For example, when defining an attribute or variable that contains in its name the word "Address", "Phone", "Email", "URL", etc., GeneXus automatically assigns to its data type a **Semantic Domain** called "Address", "Phone", "Email", "URL", etc., respectively.

`[imagen omitida: wiki id 53032]`

This provides the advantage of automatically including useful behaviors depending on the semantics of the attribute/variable you are defining. For example, at runtime, the *CustomerAddress* attribute will offer the installed applications related to maps. For the *CustomerPhone* attribute—if the application is running on a mobile phone—it will be possible to make a phone call. For the *CustomerEmail* attribute, an email may be sent (with the address data as the recipient). That is, the resources of the device on which the application is running are automatically used.

In the same way, when defining an attribute or variable that contains the word "Date" in its name, the "Date" **Semantic Domain** will be assigned to it, and a calendar or date picker will be displayed at runtime to choose a date.

In addition to automatic assignations when naming attributes or variables that contain the words mentioned, you can also assign, explicitly, a **Semantic Domain** to a certain attribute or variable that does not contain the name of a Semantic Domain in the attribute/variable name.

## [Some Semantic Domains](#Some+Semantic+Domains)

### [**Email**](#Email)

When an attribute or variable based on the **Email** Semantic Domain is displayed on the screen, a default action is set to open the default email client and create a new blank email to the address involved:

`[imagen omitida: wiki id 17848]`

### [**URL**](#URL)

When an attribute or variable based on the **URL** Semantic Domain is displayed on the screen, the URL appears as a link to the corresponding site.

`[imagen omitida: wiki id 17846]`

### [**Address**](#Address)

An attribute or variable based on the **Address** Semantic Domain appears on web screens as an address link. If you click on it, a map will open showing the address:

`[imagen omitida: wiki id 53109]`

### [**Geolocation**](#Geolocation)

The Geolocation Semantic Domain is based on the character data type and expects a "latitude, longitude" format (two numbers that specify the coordinates).

When an attribute or variable is based on the **Geolocation** Semantic Domain, it is character data that corresponds to a <latitude, longitude> point. So it is displayed on a Google map.

`[imagen omitida: wiki id 17847]`

Read more in [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644).

### [**Phone**](#Phone)

When the application is accessed from a Phone, for Attributes/Variables based on the **Phone** Semantic Domain,it will be able to call the desired number.

### **Date / DateTime**

When an attribute or variable based on the **Date** or **DateTime** Semantic Domain is present on the screen, a date picker/calendar will be invoked when inserting this field.

`[imagen omitida: wiki id 53110]`

### [**Image**](#Image+)

When an attribute or variable based on the **Image** Semantic Domain is present on the screen, if the application is running on a mobile phone the camera may be used to take a picture. Also, an image can be uploaded to the field.

`[imagen omitida: wiki id 53111]`

### [**Video**](#Video)

Like the Image Semantic Domain, this multimedia domain can handle and store video sequences.

### [**Audio**](#Audio)

The **Audio** Semantic Domain allows storing audio content.

### [**Component**](#Component)

This Semantic Domain can handle and store web page URLs.

It will load the page and show it on the Native Mobile device inside the application. It will show a Webview, that is, the web page of the URL specified on the field based on this domain.

The web page will occupy the space given for the variable.

### [**HTML**](#HTML)

An attribute/variable based on this domain can store HTML code.

The HTML code stored in this field will be rendered by the device.


|  |
| --- |
| **Backlinks** |
| [Allow Webview execute javascript property](https://wiki.genexus.com/commwiki/wiki?37299) | [Allow Webview execute local files property](https://wiki.genexus.com/commwiki/wiki?37300) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [GeneXus for SAP Systems - First Objects](https://wiki.genexus.com/commwiki/wiki?34052) | [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) |

---
