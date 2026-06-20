---
title: "GXflow Backend"
source_id: 25704
source_url: https://wiki.genexus.com/commwiki/wiki?25704
genexus_version: "18"
---

# GXflow Backend

The Backend consists of a group of applications whose purpose is to allow the user to create new Menus, Components and Actions in the [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836), as well as, making changes to the default ones.

By default only users with the GXflow Backend Administrator and GXflow Administrator roles will have access to this menu.

`[imagen omitida: wiki id 54135]`

The Backend has the following components:

* [Menus](https://wiki.genexus.com/commwiki/wiki?25709)
* [Components](https://wiki.genexus.com/commwiki/wiki?25710)
* [Actions](https://wiki.genexus.com/commwiki/wiki?25711)

### [Access to Menus, Components and Actions.](#Access+to+Menus%2C+Components+and+Actions.)

The access level to any Menu can be managed.  
When a new item is created, the [GXflow - Access Level property](https://wiki.genexus.com/commwiki/wiki?25723) can be set in order to give access to the: GXflow Administrator, GXflow Manager, or to all roles. The access level can be managed for Menus only—for components and actions, it is inherited from the menu to which belongs to.

Note that for default menus, this is not possible when not using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

However, when integrated security ([GAM](https://wiki.genexus.com/commwiki/wiki?14960)) is enabled in a Knowledge Base, it is possible to manage the access level for all Menus, Actions and Components.

When using GAM; users, roles and permissions are managed from [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935). See article [GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454) for further details.  
Therefore, we must use the GAM Web Backoffice in order to manage the access to each Menu, Component and Action.  
For Menus, Components and Actions permissions will be created as follows:

| Item | Permission Syntax | Description | Example |
| --- | --- | --- | --- |
| [Menus](https://wiki.genexus.com/commwiki/wiki?25709) | {MENU\_ID} | A permission with the ID1 of the menu—in case letters. This permission is created when the menu is added to a component, and manages the access level to that specific menu. | For the menu named 'Desktop'—ID = DESKTOP— the following permission will be created:  DESKTOP |
| [Components](https://wiki.genexus.com/commwiki/wiki?25710) | {COMPONENT\_ID} | A permission with the ID1of the component—in case letters. This permission is created when the component is added to a component, and manages the access level to that specific component. | For the component named 'Inbox'—ID = INBOX— the following permission will be created:  INBOX |
| [Actions](https://wiki.genexus.com/commwiki/wiki?25711) | {COMPONENT\_ID}\_{ACTION\_ID} | A permission with the ID1of the component followed by an underscore and the name of the action—in case letters. This permission is created when the action is added to a component and manages the access level to an action belonging to a specific component. | For the action named 'Send'—ID = COMPLETE— of the Inbox component, the following permission will be created:  INBOX\_COMPLETE |

**Note1**: the ID is used to create the permission and not the Name.

For an overview of the GXflow Standard client, please refer to the following section: [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836).

### [See Also](#See+Also)

[HowTo: Create a menu in GXflow Client](https://wiki.genexus.com/commwiki/wiki?25755)  
[HowTo: Create a Component in the GXflow Client](https://wiki.genexus.com/commwiki/wiki?25750,,)  
[HowTo: Create an Action in the GXflow Client](https://wiki.genexus.com/commwiki/wiki?25737,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow - Access Level property](https://wiki.genexus.com/commwiki/wiki?25723) |
| [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?17836) | [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809) |
| [HowTo: Create a menu in GXflow Client](https://wiki.genexus.com/commwiki/wiki?25755) |

---
