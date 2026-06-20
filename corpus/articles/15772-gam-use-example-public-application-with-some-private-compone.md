---
title: "GAM Use Example: Public Application With Some Private Components"
source_id: 15772
source_url: https://wiki.genexus.com/commwiki/wiki?15772
genexus_version: "18"
---

# GAM Use Example: Public Application With Some Private Components

How to use GAM in my application: Public application with some private components.

In this case,  the application is mostly public, and has only some components which require authentication.

The sample is based on [Lab Application](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,8,8,O,E,0,,3310e). In this sample “BuildTeam” object will be considered as private.

So, the home page of the application will consist of a webpage of public access. This webpage will be included in a master page which includes a “login object” with the purpose of enabling the final user to enter his credentials and access to the private components of the application.

The “look &  feel ” of this sample webpage is as follows:

`[imagen omitida: wiki id 15778]`  
Figure 1.

So what we actually want is that when the user tries to access “BuildTeam” from the menu, show to him a “PermisssionError” object which displays a message telling the user that he needs to be logged to perform the action desired, as shown in the figure.

`[imagen omitida: wiki id 15779]`  
Figure 2.

**Notes:**

* That in this particular sample case, our [Login Object for Web](https://wiki.genexus.com/commwiki/wiki?15590) will be “PermissionError” object, as this is the object which will be loaded in case of an Authentication Error.
* In this case, as all the objects of the application except some of them will be private, the [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) property has to be set as None. So, all the objects of the KB will inherit this value for the same property.

Only “BuildTeam” will have [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) = "Authentication".  
  
`[imagen omitida: wiki id 15773]`  
Figure 3.

Steps to follow:

1. Set [Enable Integrated Security](https://wiki.genexus.com/commwiki/wiki?14706) property to Yes, in order to incorporate GAM API to the Knowledge Base.
2. Create a "PermissionError" Object which only displays that message on the form. Note that GAMExampleLoginObject is set by default as [Login Object for Web](https://wiki.genexus.com/commwiki/wiki?15590) property. In this case we´ll configure [Login Object for Web](https://wiki.genexus.com/commwiki/wiki?15590)  = "PermissionError" object (as shown in Figure 3).
3. “Save” GAMExampleLoginObject “as” another object in order to preserve the changes. This new saved object is called “LoginGAM” in my case.

Edit “LoginGAM” and make the changes needed. In this case, we need a “login” web component, and some changes in the layout of the form. In particular, we added the logout button and code to this component. This is a re-design of GAMExampleLoginObject using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

So the resulting object form is as follows:  
  
`[imagen omitida: wiki id 15774]`  
Figure 4.

4. Edit the masterpage in order to include the “login” object in it.

`[imagen omitida: wiki id 15775]`  
Figure 5.  
  
5. Change “BuildTeam” object to check security.

`[imagen omitida: wiki id 15777]`  
Figure 6.

As a result of following this steps, when the user logs in (by using the login component), an implicit refresh is done so the authentication session (managed by GAM) is saved. When trying to access “BuildTeam” object the permission error won´t be shown any more.

Download sample: [FootBall](https://wiki.genexus.com/commwiki/wiki?20684,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM use Example: Private web application](https://wiki.genexus.com/commwiki/wiki?15923) | [HowTo: Configure GXflow Client for Native Mobile from xpz](https://wiki.genexus.com/commwiki/wiki?50551) |
| [HowTo: Configure GXflow for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25444) |

---
