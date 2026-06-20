---
title: "HowTo: Define Panels"
source_id: 15289
source_url: https://wiki.genexus.com/commwiki/wiki?15289
genexus_version: "18"
---

# HowTo: Define Panels

In order to make a Data Entry, display information obtained from various sources, and expose actions and data to the end user, you need to use a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) (or Entry Panel) object, which captures:

* **Data** – It indicates if data is displayed or edited on screen. In the model, this is done by using attributes and variables.
* **Conditions** – Conditions are specified on data items, as well as the order of some of them. Conditions part in Panels and Work With.
* **Data Layout** – They indicate how data is to be arranged on the screen, in which container, in what position, with what alignment. Given that the layout may change depending on the target device, especially when talking about a Tablet vs. a Phone, there are multiple layouts for one Panel. Hence, at design time there's the first connection between the platform-independent model (GeneXus) and the specific model (what you want to obtain:
  [Android](https://wiki.genexus.com/commwiki/wiki?14453),
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917), etc).
* **Data display (associated Controls)** – Positioning alone is not enough, because there are several ways to show the same data. For this reason, the connection with how data should be displayed is made by associating the data item and a control info. Note that this differs from the traditional methodology, which is oriented to controls. It is a data oriented design, that is to say, the data item is placed and the control to be used is selected. It could be said that binding is automatic.
* **Display Rules** - In a Panel, viewing data or actions is not always something static and many times it is conditioned. For example, an *Add to Cart* button is displayed only if the item hasn’t been added yet.
* **Actions / Events**
  + Actions are one of the basic elements used to add behavior to a Panel. When you think of a Panel, it generally has a user interface case associated with it, in which one or more actions have to be performed. For this reason, the Action concept is essential.
  + An action makes it possible to Submit a purchase order, make transitions between Panels, and so on. Again, note that the traditional methodology uses specific controls and doesn't handle the concept itself. Handling the Action concept allows you to associate the same action to several controls, which can be different. For example, you can have the purchase action in a button on the screen, but also in the menu and in the Application Bar.
  + Executing an action triggers an Event, which is where the GeneXus user programs the expected behavior.

The Login Panel is a typical Entry Panel. Take a look at the [GAMSDLogin object](https://wiki.genexus.com/commwiki/wiki?15370) and [GAMSDRegister object](https://wiki.genexus.com/commwiki/wiki?15371) objects in the [MyCowBook](https://wiki.genexus.com/commwiki/wiki?15265,,).

**Note**: [Transactions](https://wiki.genexus.com/commwiki/wiki?1908) are somehow Entry Panels, too. If you want the user to enter data that will be saved in a table (at least temporarily), use the Transactions. If the WorkWithDevices Edit form is associated to a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), then you will be using a Transaction as Entry Panel.

To make use of this feature, you have Panel objects. After creating the object, its use mechanism is the same as in the standard [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), except that it doesn't have an associated BC. In other words, you can add and erase nodes, actions and variables in the layouts.

### [See Also](#See+Also)

[Entry Panels as Filters for a List in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16337,,)
