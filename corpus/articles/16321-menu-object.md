---
title: "Menu object"
source_id: 16321
source_url: https://wiki.genexus.com/commwiki/wiki?16321
genexus_version: "18"
---

# Menu object

Displays a set of items the user may choose to take actions.

### [Description](#Description)

A Menu is usually the entry point of a Native Mobile application. It displays a set of items the user may choose from, for example, it may display items such as [Work With objects](https://wiki.genexus.com/commwiki/wiki?15974), [Panel objects](https://wiki.genexus.com/commwiki/wiki?24829), Menus, links to web pages or actions like making a phone call or sending an email.

You can create a Menu object through the [New Object dialog](https://wiki.genexus.com/commwiki/wiki?9931).

## [Object properties](#Object+properties)

Remarkable properties of Menu object are listed below.

* **[Name property](https://wiki.genexus.com/commwiki/wiki?6985)**  
  Name of the object.
* **[Description property](https://wiki.genexus.com/commwiki/wiki?7446)**  
  Description of the object.
* **[Module/Folder property](https://wiki.genexus.com/commwiki/wiki?25540)**  
  [Folder](https://wiki.genexus.com/commwiki/wiki?9757) or [Module](https://wiki.genexus.com/commwiki/wiki?22411) to which the object belongs.
* **[Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473)**  
  Whether other Module objects can access it.
* **[Main program property](https://wiki.genexus.com/commwiki/wiki?7407)**  
  Enabled by default. See [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817).
* **[Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)**  
  Defines if the object will be online or offline.
* **[Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302)**  
  Specifies whether the object will use data caching or not.
* **[Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322)**  
  Indicates whether it uses cached data or asks the server if the data has been changed.

Once a Menu has been created it will have a tree-like interface where you can add the items you wish to be displayed on it, and adjust their properties to your needs.

`[imagen omitida: wiki id 54117]`

## [Menu node properties](#Menu+node+properties)

Selecting the 'Menu' item on the tree, there are the following properties available.

* **Title property**  
  Title for this Menu.
* **Background property**  
  Menu background image. It must be an Image object.
* **[Header property](https://wiki.genexus.com/commwiki/wiki?38239)**  
  Menu header image. It must be an Image object.
* **Class property**  
  Menu theme-class.
* **[Control property](https://wiki.genexus.com/commwiki/wiki?16098)**  
  Can be List, Tab, or Table.
* **Tabs Distribution property**  
  Only visible when Control property value is Tabs. Indicates how the Tab options will be distributed in the Tab control for the Menu. Possible values are *Platform Default, Fixed Size,*and *Scroll.* The  
  *Fixed* *Size* value applies when the control has few options (at most five), in that case, each of them has the same width in the Tab control. On the other hand, the *Scroll* value puts each option with the needed width depending on the image and caption. This option allows scrolling the tab control when the number of options exceeds the width of the screen.  
  Applies only for Android, Tab control in Menu always behave as *Fixed Size* value for iOS applications.
* **Appearance group**
  + **[Show Applications Bars](https://wiki.genexus.com/commwiki/wiki?17879)**  
    Enable or disable the Application Bars.
  + **[Application Bars Class](https://wiki.genexus.com/commwiki/wiki?17879)**  
    Application theme-class.

## [Items node properties](#Items+node+properties)

The Items are the elements that will compose the Menu (generally Work With associated with the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) or Panels). To add new Items drag the object from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) and drop it in the Items node of the Menu. Also, you can right-click on Items node following by Add Action.

`[imagen omitida: wiki id 54118]`

Each Item has the following properties.

* **Name property**  
  Name of the option. This name will be referred to as its action on the Event tab.
* **Description property**  
  Description of the option. If its value is empty, the property name will be is used. If you want an empty description on the Menu, it is needed to add a blank space in the property.
* **Image property**  
  An icon used for the option. It must be an Image object. If the Control property for the Menu node is set to Tabs, iOS and Android require the image file format to be [PNG](http://en.wikipedia.org/wiki/Portable_Network_Graphic) and only its [transparency](http://en.wikipedia.org/wiki/Portable_Network_Graphics#Transparency_of_image) will be taken into account.
* **Class property**  
  MenuItem theme-class used for the option.

### [Sample](#Sample)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Property
{
   PropertyId*
   PropertyName
   PropertyAddress
   PropertyPhoto
}
```

Assume that the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) was applied to it.

Then, the following Menu object is created and the WorkWithProperty object is dragged from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) and dropped to the Items node of the Menu

`[imagen omitida: wiki id 54119]`

The event associated with the new item is automatically defined when dragging and dropping the object:

```
Event 'WorkWithProperty'
    WorkWithProperty.Property.List()
EndEvent
```

Look at the Menu at runtime (and the objects called):

`[imagen omitida: wiki id 52224]`

### [Notes](#Notes)

* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,), when using Tab control for Menu options, the ActivePageChanged event, and the Menu.ActivePage property is available to be used in the object events.
* In iOS, showing a Menu as Tabs only works for the main object. If the Menu is not the application's main object and it has the Control property set to Tabs, it will be shown as a List. This is to conform to [Apple's Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/bars/tab-bars/) that state that:  
  *In general, **use a tab bar to organize information at the app level**. A tab bar is a good way to flatten your information hierarchy and provide access to several peer information categories or modes at once. <...> A tab bar enables global navigation for your app, so **it should remain visible everywhere**.*

### [See also](#See+also)

* [Several ways to show a Menu](https://wiki.genexus.com/commwiki/wiki?16098)
* [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392)
* [Theme object](https://wiki.genexus.com/commwiki/wiki?16595)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Conceptual model of mobile applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/conceptual-model-of-mobile-applications-6103178?p=3628)


|  |
| --- |
| **Pages** |
| [Deep Link Name property](https://wiki.genexus.com/commwiki/wiki?36162) |

---
