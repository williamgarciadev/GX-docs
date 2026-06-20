---
title: "HowTo: Get a Google Maps API Key for Apple"
source_id: 39319
source_url: https://wiki.genexus.com/commwiki/wiki?39319
genexus_version: "18"
---

# HowTo: Get a Google Maps API Key for Apple

To use Google Maps in any compiled 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) application, you need to have an API Key from Google. Otherwise, maps will not show when using the [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309), [PickLocation Method](https://wiki.genexus.com/commwiki/wiki?36729) (from [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274)) or [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644).

The purpose of this article is to explain the necessary steps to get a Google Maps API Key for Apple

### [Step 1 - Create a project](#Step+1+-+Create+a+project)

Go to [Google API](https://console.developers.google.com/apis/) console and if you do not have an existing project (e.g. for  an
[Android](https://wiki.genexus.com/commwiki/wiki?14453) application), create a new one by clicking on the *New project* option.  
`[imagen omitida: wiki id 39323]`

### [Step 2 - Enable Maps API for iOS](#Step+2+-+Enable+Maps+API+for+iOS)

Click on the *Enable APIs and Services* option.  
`[imagen omitida: wiki id 39324]`

Then, look for the *Google Maps SDK for iOS* service.  
`[imagen omitida: wiki id 39325]`

Finally, enable it.  
`[imagen omitida: wiki id 39326]`

### [Step 3 - Retrieve the API Key](#Step+3+-+Retrieve+the+API+Key)

Go to the *Credentials* option on the *APIs & Services* section and look for the iOS key. Then click on copy button (`[imagen omitida: wiki id 39327]`).  
`[imagen omitida: wiki id 39328]`

### [Step 4 - Optional - Add your restrictions](#Step+4+-+Optional+-+Add+your+restrictions)

By clicking on the API Key name, you are able to restrict access to your application (by default it is unrestricted, displaying a "warning" icon).  
`[imagen omitida: wiki id 39329]`  
Once your requirements are satisfied, click on the *Save* button.

### [Step 5 - Set Apple Maps API Key property](#Step+5+-+Set+Apple+Maps+API+Key+property)

Go back to your GeneXus [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and set [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268) by pasting the value that you had copied in Step 3.  
`[imagen omitida: wiki id 39330]`

### [Availability](#Availability)

This mechanism applies since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [See Also](#See+Also)

[Apple Maps API property](https://wiki.genexus.com/commwiki/wiki?39267)  
[Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268)  
[Google developers - Get an API Key for iOS SDK](https://developers.google.com/maps/documentation/ios-sdk/get-api-key)


|  |
| --- |
| **Backlinks** |
| [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268) |

---
