---
title: "How to create a dynamic menu for WEB applications"
source_id: 33589
source_url: https://wiki.genexus.com/commwiki/wiki?33589
genexus_version: "18"
---

# How to create a dynamic menu for WEB applications

The way to create a dynamic menu in your web application is through the use of the Dynamic Items of the Action Group. An [Action Group](https://wiki.genexus.com/commwiki/wiki?25631) can be dynamic, which means that some or all of its items are loaded using a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) structure.

See [Action Group](https://wiki.genexus.com/commwiki/wiki?25631) to know the ways to insert an action group into the form.

After creating the action group, dynamic items are added by dragging the "Dynamic Items" option of the GeneXus toolbox (grouped under Extended Controls) to the toolbar.

`[imagen omitida: wiki id 33590]`  
Note: Click on the gray area —where the action group is defined— to be able to see the Dynamic Items extended control.

The *Action group dynamic items* control has the Items property, where you can specify the Structured Data Type variable which will load the items of the menu (&ActionGroupItemCollection in the example).

`[imagen omitida: wiki id 33591]`

The &ActionGroupItemCollection variable is a collection of ActionGroupItem SDT, which is automatically defined in the KB when you use an *Action group dynamic items* control.

`[imagen omitida: wiki id 33593]`

## [Sample](#Sample)

In the following example, we have a [What is a Master Page](https://wiki.genexus.com/commwiki/wiki?17088) where we've defined an action group called "MainMenu". It includes an *Action group dynamic items* control, and its Control Type property is set to Menu (so it will behave like a [Web Navigation Bar](https://wiki.genexus.com/commwiki/wiki?31918)).

`[imagen omitida: wiki id 33592]`

In the Events of the Master Page, we call a subroutine where we load the &ActionGroupItemCollection variable calling a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417).  
And we also add the events to bind the DataProvider "EventName" properties:

```
           
Event Start
    Do 'Add Action Group Items'
Endevent

Sub 'Add Action Group Items'
  &ActionGroupItemCollection = LoadActions()
EndSub

Event 'VisitWebsite'
    link("https://www.youtube.com/")
EndEvent

Event 'AuthorActions'
    Do Case
    Case &ActionGroupItemPressed.Id = "AuthorInfo"
        wwAuthor.Link()
    Case &ActionGroupItemPressed.Id = "LiteraryWork"
        wwLiteraryWork.Link()
    EndCase
EndEvent
        
```

The Data Provider is as follows:

```
ActionGroupItem
{
    Caption = "Visit Website"
    EventName = "VisitWebsite"
    Class = ThemeClass:MenuLiterature1
    TooltipText = "Visit Website"
}

ActionGroupItem
{
    Id = "AuthorInfo"
    Caption = "Author"
    EventName = "AuthorActions"
    Class = ThemeClass:MenuLiterature1
    TooltipText = "Author"
}

ActionGroupItem
{
    Id = "LiteraryWork"
    Caption = "Literary Work"
    EventName = "AuthorActions"
    Class = ThemeClass:MenuLiterature1
    TooltipText = "Literary Work"
}

ActionGroupItem
{
    Caption = "Editorial Topic"
    Link = wweditorialTopic.Link()
    Class = ThemeClass:MenuLiterature1
    TooltipText = "Editorial Topic"
}
```

Note that the "EventName" properties must be the exact same as defined on the Events of the Master Page or Web Panel.

At runtime:

`[imagen omitida: wiki id 33598]`

`[imagen omitida: wiki id 33599]`

Download sample from [here](https://wiki.genexus.com/commwiki/wiki?33597,,).

Note that:

1. Using the Toolbar control type, you can nest as many items as you want, using the children node of the SDT. In the case of the Menu control type, only two levels of nesting are supported.
2. The Link property must be empty when the toolbar item has children items.
3. You can assign a Theme Class to each link item. Remember that the class associated with the action group control has precedence over the class assigned to the link item.

### [Limitations](#Limitations)

The only items supported are text items. Buttons, images, and edit boxes are not supported.


|  |
| --- |
| **Backlinks** |
| [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631) | [Menu for Web Applications](https://wiki.genexus.com/commwiki/wiki?38477) |

---
