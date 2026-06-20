---
title: "Transaction object"
source_id: 1908
source_url: https://wiki.genexus.com/commwiki/wiki?1908
genexus_version: "18"
---

# Transaction object

Describes an object or actor of reality, defining the structure of the database, business rules, and the UI for data manipulation.

### [Description](#Description)

Transactions are the first [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) you create in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), as they allow you to describe objects or actors of reality. By paying attention to the nouns used by the users when describing their reality and needs, you can identify which Transactions you must create (I.e., Customer, Country, etc.).

Each Transaction contains several selectors.

* [GeneXus](#tabs1-1)
* [GeneXus Next](#tabs1-2)

`[imagen omitida: wiki id 48670]`

|  |  |
| --- | --- |
| **[Structure](https://wiki.genexus.com/commwiki/wiki?7240)** | The Transaction structure allows you to define the attributes or fields that describe the object of reality.  The structure may have one Level or several Levels (nested or parallel). The attributes that belong to the same level will be entered, updated, and deleted together. It is necessary to define, among the attributes making up each level, an attribute or set of attributes, acting as a unique identifier (primary key). |
| **[Web Layout](https://wiki.genexus.com/commwiki/wiki?8057)** | GeneXus automatically creates a Web Layout according to the defined structure. This layout will allow users to add, change, and delete data at runtime. |
| **[Rules](https://wiki.genexus.com/commwiki/wiki?8213)** | This section is used to define specific behavior rules for the Transaction. For example, validations for the entered data, etc. |
| **[Events](https://wiki.genexus.com/commwiki/wiki?8042)** | This section allows you to define events with idle code, which are activated in response to certain actions by the user or the system. |
| **[Variables](https://wiki.genexus.com/commwiki/wiki?7375)** | This section allows you to define variables that will be local to the Transaction (temporary, in memory). |
| **[Help](https://wiki.genexus.com/commwiki/wiki?9924)** | Here you can write help texts, which users will be able to refer to during Transaction runtime. |
| **[Documentation](https://wiki.genexus.com/commwiki/wiki?6685)** | Here you can write technical text, in wiki format, to be used as documentation of the system. |
| **[Patterns](https://wiki.genexus.com/commwiki/wiki?2814)** | Here you can apply Patterns to the Transaction. Patterns allow you to empower your applications by easily adding new features! When you apply a pattern, GeneXus creates all the necessary objects to provide the desired behavior without the need to program them.     **Work With for Web.** You can apply the [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) to the Transaction. The Work With Pattern is one of the best-known and most useful patterns in business applications.     **Work With**. You can apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) to the Transaction. In user interfaces, you frequently find a view that shows a list of items and when one of them is selected, that item's detail is displayed. Sometimes this pattern is called Master-DetailTransaction. |

`[imagen omitida: wiki id 58227]`

|  |  |
| --- | --- |
| **Source** | If you like / prefer writing code instead of using an editor that allows you to make selections (typing less as well as using shortcuts), the Source selector allows you to type some of the Transaction definitions. In particular, the Transaction [Structure](https://wiki.genexus.com/commwiki/wiki?7240) and [Variables](https://wiki.genexus.com/commwiki/wiki?7375)can be defined either using the Source selector or using the Structure and Variables selectors, respectively. The definitions you make through the Source selector will be reflected in the Structure and Variables selectors and vice versa.   The Transaction [Rules](https://wiki.genexus.com/commwiki/wiki?8213) and [Events](https://wiki.genexus.com/commwiki/wiki?8042) can only be defined in the Source selector. |
| **[Structure](https://wiki.genexus.com/commwiki/wiki?7240)** | The Transaction structure allows you to define the attributes or fields that describe the object of reality.  The structure may have one Level or several Levels (nested or parallel). The attributes that belong to the same level will be entered, updated, and deleted together. It is necessary to define, from the attributes that make up each level, an attribute or set of attributes acting as a unique identifier (primary key). |
| **[Web Layout](https://wiki.genexus.com/commwiki/wiki?8057)** | GeneXus automatically creates a Web Layout according to the defined structure. This layout will allow users to add, change, and delete data at runtime. |
| **[Variables](https://wiki.genexus.com/commwiki/wiki?7375)** | This section allows you to define variables that will be local to the Transaction (temporary, in memory). |
| **Documentation** | Here you can write technical text, in Markdown, to be used as documentation of the system. |
| **[Patterns](https://wiki.genexus.com/commwiki/wiki?2814)** | Here you can apply Patterns to the Transaction. Patterns allow you to empower your applications by easily adding new features! When you apply a pattern, GeneXus creates all the necessary objects to provide the desired behavior without the need to program them. |

GeneXus analyzes the Transaction structures and generates the necessary programs to create the database (if it doesn't exist), which will be automatically normalized to third normal form, according to the main theories of relational databases. In other words, GeneXus extracts the knowledge from the Transaction structures to define the physical tables to be created or updated in the database. After that, GeneXus also generates programs (forms with several functionalities) to interact with the database previously created.

### [See Also](#See+Also)

[GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866)  
[Transaction Object Limits](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28747,,)  
[GeneXus Knowledge Base Limits](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10669,,)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [First Transaction design](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/first-transaction-design-v16?p=5331)  
`[imagen omitida: wiki id 20668]` [Defining more Transactions](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/defining-more-transactions-v16?p=5340)  
`[imagen omitida: wiki id 20668]` [Working with attributes and domains](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/working-with-attributes-and-domains-v16?p=5337)


|  |
| --- |
| **Pages** |
| [ActiveLinkColor property](https://wiki.genexus.com/commwiki/wiki?8652) | [Allow Collapsing property](https://wiki.genexus.com/commwiki/wiki?8674) | [Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237) |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) | [AlternateText property](https://wiki.genexus.com/commwiki/wiki?8685) | [Application Icon property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7955,Application+Icon+property,) |
| [Auto Resize property](https://wiki.genexus.com/commwiki/wiki?8687) | [Autocenter Objects in (0,0) Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7434,Autocenter+Objects+in+%280%2C0%29+Property,) | [Automatic enter property](https://wiki.genexus.com/commwiki/wiki?13367) |
| [BackColor property](https://wiki.genexus.com/commwiki/wiki?8688) | [BackColorEven property](https://wiki.genexus.com/commwiki/wiki?8694) | [BackColorOdd property](https://wiki.genexus.com/commwiki/wiki?8702) |
| [BackColorStyle property](https://wiki.genexus.com/commwiki/wiki?8692) | [Background property](https://wiki.genexus.com/commwiki/wiki?8723) | [BackStyle property](https://wiki.genexus.com/commwiki/wiki?8710) |
| [Beep on messages property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7406,Beep+on+messages+property,) | [Border Style Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13368,Border+Style+Property,) | [BorderColor property](https://wiki.genexus.com/commwiki/wiki?8725) |
| [BorderWidth property](https://wiki.genexus.com/commwiki/wiki?8727) | [BottomMargin property](https://wiki.genexus.com/commwiki/wiki?8728) | [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) |
| [Buyer property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7961,Buyer+property,) | [Cancel Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13327,Cancel+Key+Property,) | [Cell Padding property](https://wiki.genexus.com/commwiki/wiki?8732) |
| [Cell Spacing property](https://wiki.genexus.com/commwiki/wiki?8733) | [Collapsed property](https://wiki.genexus.com/commwiki/wiki?8675) | [Columns Grids property](https://wiki.genexus.com/commwiki/wiki?8753) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Commit on Exit property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7942,Commit+on+Exit+property,) | [Commitment property](https://wiki.genexus.com/commwiki/wiki?7951) |
| [Confirm Transactions property](https://wiki.genexus.com/commwiki/wiki?7999) | [ContextualTitle property](https://wiki.genexus.com/commwiki/wiki?4842) | [Control Box Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13364,Control+Box+Property,) |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) | [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) |
| [Copyright property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7960,Copyright+property,) | [Create Transaction from Attributes command](https://wiki.genexus.com/commwiki/wiki?26553) | [Default Master Page property](https://wiki.genexus.com/commwiki/wiki?11597) |
| [Display Attribute Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13372,Display+Attribute+Property,) | [DisplayMode property](https://wiki.genexus.com/commwiki/wiki?8764) | [DW transaction property](https://wiki.genexus.com/commwiki/wiki?8052) |
| [DW transaction type property](https://wiki.genexus.com/commwiki/wiki?8053) | [Enable Datepicker property](https://wiki.genexus.com/commwiki/wiki?13339) | [Enable Distributed Transactions property](https://wiki.genexus.com/commwiki/wiki?9243) |
| [Enable Show Password property](https://wiki.genexus.com/commwiki/wiki?35577) | [Enabled property](https://wiki.genexus.com/commwiki/wiki?8765) | [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Exit Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13328,Exit+Key+Property,) | [Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569) |
| [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) | [Fast first rows property](https://wiki.genexus.com/commwiki/wiki?8071) | [Fill property](https://wiki.genexus.com/commwiki/wiki?8722) |
| [Font property](https://wiki.genexus.com/commwiki/wiki?8774) | [FontBold property](https://wiki.genexus.com/commwiki/wiki?8775) | [FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776) |
| [FontName property](https://wiki.genexus.com/commwiki/wiki?8777) | [FontSize property](https://wiki.genexus.com/commwiki/wiki?8778) | [FontStrikethru property](https://wiki.genexus.com/commwiki/wiki?8779) |
| [FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780) | [ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693) | [Form icon property](https://wiki.genexus.com/commwiki/wiki?13374) |
| [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Generate As a Popup Window property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13375,Generate+As+a+Popup+Window+property,) |
| [Generate FOR UPDATE clause property](https://wiki.genexus.com/commwiki/wiki?7952) | [Generate Object property](https://wiki.genexus.com/commwiki/wiki?7633) | [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) |
| [Height property](https://wiki.genexus.com/commwiki/wiki?8792) | [HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681) | [HSpace property](https://wiki.genexus.com/commwiki/wiki?8790) |
| [Image property](https://wiki.genexus.com/commwiki/wiki?9846) | [Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946) | [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) |
| [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) | [IsValid event](https://wiki.genexus.com/commwiki/wiki?8049) | [Location property](https://wiki.genexus.com/commwiki/wiki?7956) |
| [Maximize Button Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13369,Maximize+Button+Property,) | [Minimize Button Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13370,Minimize+Button+Property,) | [Modal Dialog Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13393,Modal+Dialog+Property,) |
| [Nulls in Form behavior property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7870,Nulls+in+Form+behavior+property,) | [On session timeout property](https://wiki.genexus.com/commwiki/wiki?17458) | [Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209) |
| [Private object property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7409,Private+object+property,) | [Prompt Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13330,Prompt+Key+Property,) | [Purpose property](https://wiki.genexus.com/commwiki/wiki?9580) |
| [Rendering Mode property in Free Style Grids](https://wiki.genexus.com/commwiki/wiki?26598) | [Retrieve Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14481,Retrieve+Key+Property,) | [Return On Click property](https://wiki.genexus.com/commwiki/wiki?8745) |
| [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) | [Rules in Transactions](https://wiki.genexus.com/commwiki/wiki?8213) | [Scrollable Form Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13434,Scrollable+Form+Property,) |
| [Search viewer property](https://wiki.genexus.com/commwiki/wiki?36676) | [Select Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13332,Select+Key+Property,) | [SelectionColor property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8682,SelectionColor+property,) |
| [Show form property](https://wiki.genexus.com/commwiki/wiki?13435) | [Show in taskBar (SDI) property](https://wiki.genexus.com/commwiki/wiki?13379) | [Sortable property](https://wiki.genexus.com/commwiki/wiki?14173) |
| [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013) | [Structure Editor](https://wiki.genexus.com/commwiki/wiki?3913) | [TitleForeColor property](https://wiki.genexus.com/commwiki/wiki?8784) |
| [Tooltiptext property](https://wiki.genexus.com/commwiki/wiki?4840) | [TrackContext event](https://wiki.genexus.com/commwiki/wiki?8051) | [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) |
| [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) | [Transaction Structure/Form](https://wiki.genexus.com/commwiki/wiki?8059) | [Transaction Web Layout](https://wiki.genexus.com/commwiki/wiki?8057) |
| [Triggering context for Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735) | [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) | [Value range property](https://wiki.genexus.com/commwiki/wiki?6797) |
| [Values property (for Check Boxes, List Boxes and Radio Buttons)](https://wiki.genexus.com/commwiki/wiki?8819) | [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) | [Width property](https://wiki.genexus.com/commwiki/wiki?38374) |

---
