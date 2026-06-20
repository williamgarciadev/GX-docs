---
title: "HowTo: Solve multi-tenant filter with Fiori Pattern"
source_id: 54817
source_url: https://wiki.genexus.com/commwiki/wiki?54817
genexus_version: "18"
---

# HowTo: Solve multi-tenant filter with Fiori Pattern

If you have a multi-tenant application where the tenant is represented with the Organization entity and you want to automatically generate the filter by OrganizationId in your CRUD options for your back office, you can do the following:

1. Go to Preferences > Patterns > Fiori for Web. (**Note:** In order to see the Fiori for Web pattern you have to previously [install the GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33839) in your KB).
2. Open the Pattern Settings, click on the “Transaction Floorplan (Main)”  tab, and select the “List Report” tab.
3. Right-click on “Events & Subs” and add a new EventBlock.
4. For the new EventBlock:

* Complete the **Block Name \*** property with a name (in this example, GetUserContext).
* Set the **Event/Sub Name** property to “Start”.
* Write in the **Code** property the code you want to include in the Start event. In this example, a call to the GetUserContext Procedure:

`[imagen omitida: wiki id 54822]`

        5. In the “Variables (Not included in Web)” node add the variables needed for the code. In this example, the &UserContextSDT:

`[imagen omitida: wiki id 55032]`

        6. Right click on “List floorplan - (<TRN\_DESCRIPTION>)” and select: Add > Conditions

`[imagen omitida: wiki id 55033]`

The “Automatic Conditions” node will be added.

7. To add a new condition, right-click on the “Automatic conditions” node and select:  Add > Condition. Give a name to it (in this case, it is called “FilterByOrganization”).  
  
`[imagen omitida: wiki id 55034]`

8. Complete the Condition and the **Regular Expression** property with the attribute name that indicates the tenant (in this example, OrganizationId). This will apply the condition only if OrganizationId is present in the Transaction structure.

`[imagen omitida: wiki id 55035]`

            These settings are needed in each template available in the Fiori Pattern to generate this kind of CRUD UIs.

`[imagen omitida: wiki id 55037]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
