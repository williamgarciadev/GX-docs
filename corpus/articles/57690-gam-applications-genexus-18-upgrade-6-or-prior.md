---
title: "GAM - Applications (GeneXus 18 Upgrade 6 or prior)"
source_id: 57690
source_url: https://wiki.genexus.com/commwiki/wiki?57690
genexus_version: "18"
---

# GAM - Applications (GeneXus 18 Upgrade 6 or prior)

As a security component, [GAM](https://wiki.genexus.com/commwiki/wiki?24746) can be used by different applications (which can be Native Mobile applications, Web applications, or even Web Services).

Conceptually, GAM applications group [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) which are related to GeneXus objects.

### GAM Applications that are automatically generated

* **WEB GAM application**  
    
  If the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has at least one web [environment](https://wiki.genexus.com/commwiki/wiki?7115), a WEB GAM application is automatically generated including the permissions of all the web objects of the KB. This WEB GAM application is identified with a GUID assigned in the [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667). The name of the WEB GAM application is the name of the KB.    
    
  The information of the WEB GAM application GUID is stored in the application.gam file, which is saved in the model directory and must be included in the deployment.  
    
  Note that only one WEB GAM application is automatically generated for the KB even if it has N environments.
* **GAM applications associated with each Native Mobile / Angular [Main Object](https://wiki.genexus.com/commwiki/wiki?5770)**  
     
  For each main object (like [Menus](https://wiki.genexus.com/commwiki/wiki?16321) or [Panels](https://wiki.genexus.com/commwiki/wiki?24829)) a GAM application is automatically generated.

GAM applications are defined within a [repository](https://wiki.genexus.com/commwiki/wiki?17568). Each repository can contain more than one GAM application.

Additionally, one Repository can store more than one GAM WEB application because from different KBs you can use a different [Application Id](https://wiki.genexus.com/commwiki/wiki?18667) to create a different GAM WEB application in the same repository.

### [What is the purpose of GAM applications?](#What+is+the+purpose+of+GAM+applications%3F)

First, the GAM application is checked at runtime at the moment of user authentication.

Another purpose of defining GAM applications within the GAM repository is to associate Permissions to these applications and to form groups of permissions.

At runtime, permissions are checked considering the application which is being executed. So, when the user logs in to a repository, and a permission is needed to execute an action, the permission must be defined in the GAM application he is executing (and he needs to have a [role](https://wiki.genexus.com/commwiki/wiki?17569) where this permission is allowed).

So the permissions which can be associated to a GAM application are all related in some sense.

By default, when F5 processes permissions, the following GAM applications are created in the repository:

* A GAM application for the WEB application of the KB. The WEB GAM application groups the permissions of all the web objects of the KB and its descendants.
* A GAM application for each main object for Native Mobile applications. The application groups the permissions of this main object and its descendants. So if you have Dashboard1, and Dashboard2 which are main, there will be a GAM application for each of them.

### [How can I work with GAM applications?](#How+can+I+work+with+GAM+applications%3F)

Each GAM application is identified by a GAM application GUID, and has *"Client Application data"*: [Client Id and Client Secret information](https://wiki.genexus.com/commwiki/wiki?21454,,).

You can see the running [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935) as an administrator, all the available GAM applications for the repository you've connected to, and you can also define new applications. See figure 1.

`[imagen omitida: wiki id 51903]`

###### [Figure 1.](#Figure+1.)

**Note:** To add a new application, you have to click on "Applications" and then click on the "Add" button.

### [What happens at runtime?](#What+happens+at+runtime%3F)

When the user executes a web object, the GAM application Identifier is taken from application.gam file located in the virtual directory. See [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) in order to understand how this ID is automatically generated.

If the user executes a GeneXus object for Native Mobile and Angular application, the GAM application is identified by its *"Client Application data"* ([Client Id and Client Secret information](https://wiki.genexus.com/commwiki/wiki?21454,,)). See [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) to understand how this information is used at a low level, using OAuth protocol.

#### [Notes:](#Notes%3A)

* The *"Client Application data"* of GAM applications which have web object permissions is not used in GeneXus Evolution 3.
* At present only one [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667) is referenced in application.gam file so all the permissions related to web objects have to be grouped in the same WEB GAM application in the web application deployment. Although you can have more than one WEB GAM application in a repository, you need to deploy a different web application for each of them.

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)  
[GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150)  
[GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568)  
[Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512)
