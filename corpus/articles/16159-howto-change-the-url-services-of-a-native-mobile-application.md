---
title: "HowTo: Change the URL Services of a Native Mobile application"
source_id: 16159
source_url: https://wiki.genexus.com/commwiki/wiki?16159
genexus_version: "18"
---

# HowTo: Change the URL Services of a Native Mobile application

The purpose of this article is to explain the necessary steps to change the URL Services of a Native Mobile application.

When you develop and then publish a Native Mobile application, the URL service is taken from the [Web Root property](https://wiki.genexus.com/commwiki/wiki?9287). However, in some situations, you may need to change that URL for consuming the services from another server. In order to achieve that aim, GeneXus provides a way to indicate that the URL services can then be changed for the installed application without having to publish the application again in the relevant stores.

### [Scope](#Scope)

**Generators:**

[Android](https://wiki.genexus.com/commwiki/wiki?14453), 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Step 1 - Allow dynamic services](#Step+1+-+Allow+dynamic+services)

Go to the
[Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) properties and change the [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366) value to True and enter a default value for [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146).  
  
`[imagen omitida: wiki id 38268]`

**Note**: Refer to [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) for more information about URL format.

### Step 2 - Build the application

Generate, compile and publish your application as usual.

### Step 3 - Change the URL Service from the app

Once your application has been installed on a device you will be able to change the URL Services.

#### **3.1) Android settings**

Go to [Android](https://wiki.genexus.com/commwiki/wiki?14453), execute your application, go to the contextual menu and select Preferences. Then, a dialog will be displayed. Tap on the down arrow and enter the services URL.  
  
`[imagen omitida: wiki id 38269]`

#### [**3.2) Apple settings**](#3.2%29+Apple+settings)

Go to Settings and select your application. Now just enter the new services URL in the Address field.  
  
`[imagen omitida: wiki id 38270]`

### [Considerations](#Considerations)

If the URL Service is empty, the application will ask you for one when entering the application.  
Consider setting a default value for your products. For example, in the Apple approval process the application will not be approved without a sample server.


|  |
| --- |
| **Backlinks** |
| [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) |

---
