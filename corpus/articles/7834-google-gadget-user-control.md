---
title: "Google Gadget User Control"
source_id: 7834
source_url: https://wiki.genexus.com/commwiki/wiki?7834
genexus_version: "18"
---

# Google Gadget User Control

This control allows you to include any Google gadget inside your application.

[Download latest version](http://marketplace.genexus.com/viewproduct.aspx?27)

### [Properties](#Properties)

**GadgetURL**: This property indicates the location of the gadget. This is the parameter pass to the main Url Gadget.

The value could be set on runtime, with a code like this :

Control.GadgetURL = '*URL\_VALUE*'  
              Where *Url\_Value* is as follows, when you get the gadget code: < script src="http://gmodules.com/ig/ifr?url=URL\_VALUE"> </script >

Title, width and heigth: are not take into account yet. However could be set inside the Gadget Url (this depends on the specific implementation of the gadget).

Versions

   1.1  - The url property is a combo where you can choose among the different predefined values.  
   1.0 -  The Url property is a text value where you can write the gadget Url.


|  |
| --- |
| **Backlinks** |
| [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |

---
