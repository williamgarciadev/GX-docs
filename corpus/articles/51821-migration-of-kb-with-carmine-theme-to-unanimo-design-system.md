---
title: "Migration of KB with Carmine Theme to Unanimo Design System"
source_id: 51821
source_url: https://wiki.genexus.com/commwiki/wiki?51821
genexus_version: "18"
---

# Migration of KB with Carmine Theme to Unanimo Design System

This article offers a step-by-step guide to migrate your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) developed in versions prior to [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) and based on the Carmine Theme to the design proposed by [Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?48382).

If you have a Knowledge Base in [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,) and open it with [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066), everything will work correctly based on the Carmine Theme. However, you may want to use the design proposed by [Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?48382), and here are instructions to do so.

It is recommended to save a copy of your KB before following the migration steps. To do so, [create a local Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681) or freeze a version in the GeneXus Server you are connected.

### [Steps to migrate/use Unanimo Design System](#Steps+to+migrate%2Fuse+Unanimo+Design+System)

1. After opening your KB with GeneXus 18, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). Check that the applications still work correctly based on the Carmine Theme.

**Note**:  If the KB has [GAM](https://wiki.genexus.com/commwiki/wiki?24746) activated and you do not want to affect the design of the front-end objects that GAM imports (login, registration, password change, etc.), go to Tools > GeneXus Access Manager > Installation Settings. In the combo box "Select how to manage the future upgrades," select the "Never Update" value. In this way, the login and other panels that are imported with this option will continue using the Carmine design. If you want them to use the Unanimo-based design, you should update these objects.

2. Install the GeneXusUnanimo module in your KB. To do so, go to Knowledge Manager > Manage Module References > Global Matrix and install it.

3. Import the GeneralWeb.xpz file located in the GeneXus installation directory under \Startup\Web.

4. Create a new [Design System](https://wiki.genexus.com/commwiki/wiki?47375) with the following structure in its [Style](https://wiki.genexus.com/commwiki/wiki?47379) section:

```
styles KBName {
    @import GeneXusUnanimo.UnanimoWeb;
}
```

5. Go to Preferences and at [version level](https://wiki.genexus.com/commwiki/wiki?7860), set:

[Default Style property](https://wiki.genexus.com/commwiki/wiki?8145) with the Design System you created in the previous step.

[Default Form Layout property](https://wiki.genexus.com/commwiki/wiki?51685) to Unanimo Template

[Default Master Page property](https://wiki.genexus.com/commwiki/wiki?11597) to MasterUnanimoSidebar object.

Note: Consider that you probably have to migrate logic from your previous Master Page to the MasterUnanimoSidebar Master Page created by default.

6. The MasterUnanimoSidebar Master Page menu options are loaded from the SidebarItemsDP Data Provider. For this Data Provider to load the links loaded by the Home object when the Work With for Web pattern was applied, the code should be as follows:

```
SidebarItems
{
    /* Code managed by Work With Pattern [Start] - Load WW instances */
    &wwProgramNames = ListPrograms()
    
    SidebarItem
    input &wwProgramName in &wwProgramNames
    {
        id = &wwProgramName.Name
        title = &wwProgramName.Description
        target = &wwProgramName.Link
        hasSubItems = false
    }
    /* Code managed by Work With Pattern [End] - Load WW instances */
}
```

#### [Consideration](#Consideration)

The variables are defined as follows:

`[imagen omitida: wiki id 51824]`

So, you have to move the ProgramNames [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) inside the General.UI module:

`[imagen omitida: wiki id 51920]`

This link offers an [.xpz file with the SidebarItems Data Provider and the ProgramNames SDT to import.](https://wiki.genexus.com/commwiki/wiki?52282,,)

7. Delete the automatically generated prompts. Make sure that the [Prompts Master Page property](https://wiki.genexus.com/commwiki/wiki?51714) has the MasterPrompt value, which is the Unanimo Master Page to apply to the prompts.

8. Go to [Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?5642). In Standard Actions, set the Button Class for the Insert action empty.  For the Update and Delete Standard Actions leave the associated images set to none, and use the classes shown in the following image:

`[imagen omitida: wiki id 51845]`

9. Go to the [Work With Objects tool window](https://wiki.genexus.com/commwiki/wiki?46737). Select all instances of the Work With for Web pattern, right-click, and select **Apply Pattern**:

`[imagen omitida: wiki id 51851]`

10. Use again the Work With Objects tool window and search by "Carmine". Select the Carmine Theme, right-click on it and select: References. Look at the left window titled "Is referenced by". If there are objects that use/reference the Carmine Theme, check if it is correct for you. If not, change that through the object's [Style property in Map User Control](https://wiki.genexus.com/commwiki/wiki?42433).

11. Execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [Migrate to Unanimo](https://wiki.genexus.com/commwiki/wiki?52177) | [Steps to build with GeneXus 18 a KB of GeneXus 17 or prior](https://wiki.genexus.com/commwiki/wiki?52345) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |
| [Toc:Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) |

---
