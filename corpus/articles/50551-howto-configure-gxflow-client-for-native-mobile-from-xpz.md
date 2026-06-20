---
title: "HowTo: Configure GXflow Client for Native Mobile from xpz"
source_id: 50551
source_url: https://wiki.genexus.com/commwiki/wiki?50551
genexus_version: "18"
---

# HowTo: Configure GXflow Client for Native Mobile from xpz

This article explains the steps needed to configure the [GXflow Native Mobile Custom Client based on Unanimo design system](https://wiki.genexus.com/commwiki/wiki?50518,,).

### [Step 1 - Enabling GAM Authentication](#Step+1+-+Enabling+GAM+Authentication)

To enable [GAM Authentication](https://wiki.genexus.com/commwiki/wiki?18456,,) the property [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) must be set to True, for details see [My first Native Mobile application with GAM](https://wiki.genexus.com/commwiki/wiki?15275).

### [Step 2- Importing the GXflow Client for Native Mobile](#Step+2-+Importing+the+GXflow+Client+for+Native+Mobile)

1. Create [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) from server <http://samples.genexusserver.com/v18/>.
2. Check out GXflowMXCustomClient KB.
3. From GXflowMXCustomClientKBGXflowMXCustomClient KB, generate a GXflowMXCustomClient.xpz file with all the objects inside the WorkflowClientMobile folder and all languages and images inside customization node and all files from root node.
4. Import that xpz file into your original KB (option Knowledge Manager > Import).
5. Select WorkflowMobileMenu as [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393).

By doing these steps, you will be able to associate any of your Business Process Diagrams with custom mobile objects. Don't forget to edit the *WorkflowMobileCalled*object and write the correspondent calls to the referenced objects.

### [Step 3- Creating a Business Process Diagram Object and running the process](#Step+3-+Creating+a+Business+Process+Diagram+Object+and+running+the+process)

Create a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) and run it.

A good example of a native Business Process Diagram using Mobile objects assigned to user tasks can be found in the My first BPM Application for Mobile Devices article, as well as an example using Web objects assigned to user tasks can be found in the [My first BPM Application](https://wiki.genexus.com/commwiki/wiki?11218) article.

### [Step 4 - Setting the Design System](#Step+4+-+Setting+the+Design+System)

Set the Style for Any Phone as UnanimoWorkflowMobile.

### [Step 5 - Setting the Startup Object and the Login Object for Native Mobile](#Step+5+-+Setting+the+Startup+Object+and+the+Login+Object+for+Native+Mobile)

Set the Startup Object property to "WorkflowMobileMenu", and the [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) to "WorkflowMobileLogin".

### [Step 6 - Done!](#Step+6+-+Done%21)

Press F5 and test your Workflow.

### [See Also](#See+Also)

[GXflow](https://wiki.genexus.com/commwiki/wiki?4179,,)  
[Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451)  
My first BPM Application for Mobile Devices  
[GAM Use Example: Public Application With Some Private Components](https://wiki.genexus.com/commwiki/wiki?15772)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Configure GXflow for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25444) |

---
