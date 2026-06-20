---
title: "Grids with Multiple Selection for Native Mobile Applications"
source_id: 16149
source_url: https://wiki.genexus.com/commwiki/wiki?16149
genexus_version: "18"
---

# Grids with Multiple Selection for Native Mobile Applications

GeneXus lets you define that a [Grid](https://wiki.genexus.com/commwiki/wiki?24817) has multiple selecction, and then lets you scan all the selected items in the Grid with the **for each selected line** command. The code to execute an action on all selected items will look as follows.

```
for each selected line [in <GridName>]
     <action or set of actions to execute for each item>
endfor
```

## [Adding multiple selections](#Adding+multiple+selections)

To further explain the use of multiple selection actions, suppose that you have a set of customers and you want to apply a tax of 25% for some of them depending on their total amount.

### [Step 1 - Setting the UI behavior](#Step+1+-+Setting+the+UI+behavior)

Previously, create a Customer [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) as follows and apply the WorkWithDevices pattern.

`[imagen omitida: wiki id 36211]`

In the Grid control from the List section of WorkWithDevicesCustomer, set the following properties:

* [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) = <default>  
  In this case, the end-user is able to see the Detail section of the WorkWithDevicesCustomer when tapping in a register.
* [Enable Multiple Selection property](https://wiki.genexus.com/commwiki/wiki?36197) = True  
  For allowing multiple selections over the Customer grid in the List Node.
* [Show Selector property](https://wiki.genexus.com/commwiki/wiki?36199) = Always  
  It sets the user interface behavior for multiple item selections as always show its selector.

`[imagen omitida: wiki id 36212]`

### [Step 2 - Creating the action](#Step+2+-+Creating+the+action)

Create a new action called "Add tax" (right-click on the Application Bar > Insert Button).

`[imagen omitida: wiki id 36213]`

This action will perform an *ApplyTax procedure* for updating the CustomerAmount by adding interest of 25% on the selected items. In this procedure, you have to write the following code:

```
for each
     CustomerAmount = CustomerAmount * 1.25
endfor
```

The procedure must have a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) as it is shown below for automatically filtering the items in the for each command.

```
Parm(in:CustomerId);
```

### [3. Writing the action execution code](#3.+Writing+the+action+execution+code)

Finally, you have to write the section code associated with the action 'Add tax' on the *Event section* as follows.

```
Event 'Add tax'
     Composite
          For each selected line in Grid1
               ApplyTax(CustomerId)
          Endfor
          Refresh
     EndComposite
EndEvent
```

**Note**:

* For SDT or BC collection based Grids, the way to access to each item is by the CurrentItem runtime property.  
  For example:

```
For each selected line in Grid1
    ApplyTax(&Customer.CurrentItem.CustomerId)
Endfor
```

where &Customer is a variable based on an SDT or BC item.

## [Application runtime behavior](#Application+runtime+behavior)

1. You have to select the items that you would like to update. Every item can be selected by tapping on the left check-box.  
`[imagen omitida: wiki id 36214]`

2. Once you finish the selection, tap on "Add tax" action for executing the action to apply the 25% tax interest.  
`[imagen omitida: wiki id 36215]`

3. After the refresh of the device, you can see the total amount has changed correctly.  
`[imagen omitida: wiki id 36216]`

## [Notes](#Notes)

* If you have an action with several **for each selected line** over different Grids, the behavior of the User Interface is the platform default.
* An attribute used in a **for each selected line** command must be present in the grid on the form to work correctly.
* In the **for each selected line in <grid>** command, the grid's name is optional when you have only one grid in the SD Panel or WorkWithDevices object.
* If the grid row theme class has highlighted background color, this color will be used to mark the selected items.
* For Android devices, the selection user interface may depend on the operating system version.


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Enable Multiple Selection property](https://wiki.genexus.com/commwiki/wiki?36197) |
| [Enable Multiple Selection property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54466) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Select method](https://wiki.genexus.com/commwiki/wiki?36234) |
| [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232) | [Selection Flag Field Specifier property](https://wiki.genexus.com/commwiki/wiki?36203) | [Selection Type property](https://wiki.genexus.com/commwiki/wiki?24120) |
| [Selection Type property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54490) | [Show Selector property](https://wiki.genexus.com/commwiki/wiki?36199) |

---
