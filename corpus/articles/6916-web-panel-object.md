---
title: "Web Panel object"
source_id: 6916
source_url: https://wiki.genexus.com/commwiki/wiki?6916
genexus_version: "18"
---

# Web Panel object

Defines a web application UI screen.

The main purpose of this GeneXus object is to define interactive queries to the database; however, it is a very flexible object that lends itself to multiple uses.

It allows end users to interactively query the database at runtime through a screen. The term "interactively" refers to end users being able to repeatedly enter different filter values through a Web Panel screen, and then query the data that match them. End users can also perform different actions on the queried data.  
  
Web Panels don't allow updating the database; they only allow for queries (unless they're used in combination with [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s).  
  
Every Web Panel has an associated screen (Web Layout) where the attributes included will be queried/retrieved from the database and displayed (read-only). The variables included will be entry variables.  
  
The following classification describes the possible uses of Web Panels:

* **Entry Web Panel:** A Web Panel whose only function is to accept values entered by the end user (this means its screen only contains variables).
* **Display Web Panel:** A Web Panel whose only function is to display information (this means the screen only contains attributes and can contain variables whose default behavior as entry variables has been changed, defining them as display variables and adding values explicitly).
* **Mixed Web Panel:** A Web Panel in which it is possible to enter values and display information (in this case, the screen contains both variables and attributes, or only variables—some with their default entry behavior and others explicitly defined as display variables with added values).

This classification is independent of GeneXus; that is, GeneXus does not classify Web Panels internally.

A Web Panel object has several sections that can be defined:

|  |  |
| --- | --- |
| **Web Layout** | Defines the screen of the Web Panel, which the analyst designs by adding variables, attributes, and other controls, in order to allow end users to interact with it. |
| **Rules** | Define specific behaviors of said object to be defined. For example, specifying what parameters it receives, defining what variables you don't want to be accepted on the screen but rather used for displaying information, etc. |
| **Events** | Web Panels use event-driven programming. This kind of programming allows you to define idle code, which is activated in response to certain actions by the end user or the system. |
| **Conditions** | In this section, you can define conditions to be matched by the data to be retrieved (filters). There is another option to define filters locally in each Grid control included in the Web Layout. |

Like most objects, it also has a section for defining [variables](https://wiki.genexus.com/commwiki/wiki?3173) (as usual, local to the object), the object's Help and [Documentation](https://wiki.genexus.com/commwiki/wiki?6685) as well as a [Properties Editor](https://wiki.genexus.com/commwiki/wiki?3160) that allows you to set up general aspects of the object.

### [Samples](#Samples)

#### **1) Entry Web Panel**

The following Web Panel includes variables and buttons in its Web Layout. The variables are enabled for the end user to assign values to them. This means they are input controls; in other words, they are not read-only.

`[imagen omitida: wiki id 47011]`

Specifically, the &CountryId variable has been set of the Dynamic Combo Box [Control Type](https://wiki.genexus.com/commwiki/wiki?9550); it has been set to show all the CountryName values stored in the COUNTRY table and the end user can select one. The CountryId corresponding to the CountryName selected by the end user will be kept in the &CountryId variable. After pressing the button “List Attractions by country,” the associated event will be executed invoking the PDF file containing the list of attractions in that country.

The variables &AttractionNameFrom and &AttractionNameTo allow entering a range of attraction names. After pressing the button “List Attractions by name,” the PDF list will show the attractions within the range received by parameter.

#### [**2) Display Web Panel**](#2%29+Display+Web+Panel)

Considering the following Customer [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) structure:

```
Customer
{
  CustomerId*
  CustomerName
  CustomerPhoto
  CustomerAddress
  CustomerEmail
  CustomerPhone
}
```

The ViewCustomers Web Panel was defined including only [Attributes](https://wiki.genexus.com/commwiki/wiki?7240) in its Web Layout to display information. The attributes present in a Web Layout are always Read Only.

`[imagen omitida: wiki id 49639]`

In this example, the attributes are included in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817). So, the Grid Control has a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). In other words, GeneXus takes into account those attributes to determine a database table to be navigated and to load its records in the Grid.

If you look at the Navigation View of this Web Panel you will see the following:

`[imagen omitida: wiki id 49640]`

This Navigation View shows that the table being navigated is Customer. It is scanned ordered by CustomerId because it is the Customer table Primary key. You can indicate another order by setting the Grid [Order property](https://wiki.genexus.com/commwiki/wiki?9842).

It is also possible to define a Display Web Panel without a Grid. You can insert attributes directly in the Web Layout and GeneXus will analyze them and will determine the base table to be navigated. In general, this kind of Web Panel receives the primary key as a parameter (using the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)) to filter a specific record and show its data.

#### **3) Mixed Web Panel**

Consider the same Web Panel shown in the second example. Besides containing the Grid with attributes, it also contains variables in the Web Layout fixed part.

`[imagen omitida: wiki id 49641]`

Variables allow end users to enter values for them. So, this Web Panel contains variables (that are editable) and attributes (that are read-only).

The variables are located in the fixed part of the Web Layout and the attributes are included inside the Grid.

The Grid navigates all the Customer table records and loads their data as rows in the Grid. To show in the grid only those records whose customer names are included in the range entered by the end user in the variables, you only have to define the Grid Conditions:

```
CustomerName >= &CustomerNameFrom;
CustomerName <= &CustomerNameTo;
```

Look at the following image that shows the Grid Conditions defined:

`[imagen omitida: wiki id 49642]`

This is an interactive query.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Web panel object. First steps](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/web-panel-object-first-steps-6104784)


|  |
| --- |
| **Pages** |
| [ActiveLinkColor property](https://wiki.genexus.com/commwiki/wiki?8652) | [Allow Collapsing property](https://wiki.genexus.com/commwiki/wiki?8674) | [Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237) |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) | [AlternateText property](https://wiki.genexus.com/commwiki/wiki?8685) | [Auto Resize property](https://wiki.genexus.com/commwiki/wiki?8687) |
| [Automatic refresh property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55923) | [BackColor property](https://wiki.genexus.com/commwiki/wiki?8688) | [BackColorEven property](https://wiki.genexus.com/commwiki/wiki?8694) |
| [BackColorOdd property](https://wiki.genexus.com/commwiki/wiki?8702) | [BackColorStyle property](https://wiki.genexus.com/commwiki/wiki?8692) | [Background property](https://wiki.genexus.com/commwiki/wiki?8723) |
| [BackStyle property](https://wiki.genexus.com/commwiki/wiki?8710) | [BorderColor property](https://wiki.genexus.com/commwiki/wiki?8725) | [BorderWidth property](https://wiki.genexus.com/commwiki/wiki?8727) |
| [BottomMargin property](https://wiki.genexus.com/commwiki/wiki?8728) | [Button property](https://wiki.genexus.com/commwiki/wiki?12791) | [Buyer property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7961,Buyer+property,) |
| [Cache expiration lapse property](https://wiki.genexus.com/commwiki/wiki?8067) | [Cell Padding property](https://wiki.genexus.com/commwiki/wiki?8732) | [Cell Spacing property](https://wiki.genexus.com/commwiki/wiki?8733) |
| [Checked Value property](https://wiki.genexus.com/commwiki/wiki?8734) | [Collapsed property](https://wiki.genexus.com/commwiki/wiki?8675) | [Columns Grids property](https://wiki.genexus.com/commwiki/wiki?8753) |
| [Control Title property](https://wiki.genexus.com/commwiki/wiki?8736) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) |
| [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) | [Copyright property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7960,Copyright+property,) | [CurrentPage property](https://wiki.genexus.com/commwiki/wiki?10328) |
| [Default Master Page property](https://wiki.genexus.com/commwiki/wiki?11597) | [DisplayMode property](https://wiki.genexus.com/commwiki/wiki?8764) | [Enable Datepicker property](https://wiki.genexus.com/commwiki/wiki?13339) |
| [Enable Show Password property](https://wiki.genexus.com/commwiki/wiki?35577) | [Enabled property](https://wiki.genexus.com/commwiki/wiki?8765) | [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) |
| [Events in Web Panels](https://wiki.genexus.com/commwiki/wiki?8178) | [Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569) | [Fast first rows property](https://wiki.genexus.com/commwiki/wiki?8071) |
| [Fill property](https://wiki.genexus.com/commwiki/wiki?8722) | [Font property](https://wiki.genexus.com/commwiki/wiki?8774) | [FontBold property](https://wiki.genexus.com/commwiki/wiki?8775) |
| [FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776) | [FontName property](https://wiki.genexus.com/commwiki/wiki?8777) | [FontSize property](https://wiki.genexus.com/commwiki/wiki?8778) |
| [FontStrikethru property](https://wiki.genexus.com/commwiki/wiki?8779) | [FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780) | [ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693) |
| [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Generate Object property](https://wiki.genexus.com/commwiki/wiki?7633) |
| [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) | [Height property](https://wiki.genexus.com/commwiki/wiki?8792) | [HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681) |
| [HSpace property](https://wiki.genexus.com/commwiki/wiki?8790) | [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673) | [Image property](https://wiki.genexus.com/commwiki/wiki?9846) |
| [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) | [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) | [IsValid event](https://wiki.genexus.com/commwiki/wiki?8049) |
| [Join management property](https://wiki.genexus.com/commwiki/wiki?7966) | [Join Type property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8984,Join+Type+property,) | [Lapse property](https://wiki.genexus.com/commwiki/wiki?17303) |
| [Location property](https://wiki.genexus.com/commwiki/wiki?7956) | [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062) | [Notify Context Change property](https://wiki.genexus.com/commwiki/wiki?8856) |
| [On Click Event property](https://wiki.genexus.com/commwiki/wiki?8746) | [On session timeout property](https://wiki.genexus.com/commwiki/wiki?17458) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) |
| [Private object property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7409,Private+object+property,) | [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) | [Purpose property](https://wiki.genexus.com/commwiki/wiki?9580) |
| [Radio Direction property](https://wiki.genexus.com/commwiki/wiki?8818) | [RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757) | [Refresh event](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,Refresh+event,) |
| [Rendering Mode property in Free Style Grids](https://wiki.genexus.com/commwiki/wiki?26598) | [Return On Click property](https://wiki.genexus.com/commwiki/wiki?8745) | [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) |
| [Rules in Web Panels](https://wiki.genexus.com/commwiki/wiki?8288) | [SelectionColor property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8682,SelectionColor+property,) | [SetObjectTheme Property](https://wiki.genexus.com/commwiki/wiki?12790) |
| [Sortable property](https://wiki.genexus.com/commwiki/wiki?14173) | [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013) | [Subtitle Property](https://wiki.genexus.com/commwiki/wiki?12792) |
| [TableGridContainer Property](https://wiki.genexus.com/commwiki/wiki?12788) | [TitleForeColor property](https://wiki.genexus.com/commwiki/wiki?8784) | [Tooltiptext property](https://wiki.genexus.com/commwiki/wiki?4840) |
| [Triggers property](https://wiki.genexus.com/commwiki/wiki?7420) | [Unchecked Value property](https://wiki.genexus.com/commwiki/wiki?8737) | [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) |
| [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) | [Values property (for Check Boxes, List Boxes and Radio Buttons)](https://wiki.genexus.com/commwiki/wiki?8819) | [Web Editor Toolbars Formatting](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8119,Web+Editor+Toolbars++Formatting,) |
| [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) | [Width property](https://wiki.genexus.com/commwiki/wiki?38374) |

---
