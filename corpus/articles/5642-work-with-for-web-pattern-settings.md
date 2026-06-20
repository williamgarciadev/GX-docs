---
title: "Work With for Web Pattern Settings"
source_id: 5642
source_url: https://wiki.genexus.com/commwiki/wiki?5642
genexus_version: "18"
---

# Work With for Web Pattern Settings

You can configure some general aspects for the **Work With for Web** pattern so that when you apply the pattern, those configurations are set by default.

`[imagen omitida: wiki id 51975]`

Here you can configure properties such as the following:

#### [Style](#Style)

This option indicates the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) / [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) / classes to be used.   
Read also [Style property in Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?52134).

#### [Grid](#Grid)

Page = Page.Rows - Indicates how many rows will be viewed in the grids.  
SaveGridState - Indicates whether or not Orders, Current Page and Filters will be saved for Work With Web Panels.

#### [Standard Actions](#Standard+Actions)

DefaultMode - Indicates whether to include an action by default in the grid. It applies to insert, update, delete, display and export\* actions.

\* You can export to xls or xlsx format using the File extension property (available from GeneXus X Evolution 2 Upgrade 3).

#### [Context](#Context)

This property can be used for "Context management". For example, to maintain information about the application's current user (especially for authentication/authorization purposes), the current company for multi-company systems, etc. By changing the Context variable properties, you can change the variables and the procedures called. For example, you can use a context variable to define a filter: CompanyId = &Context.CurrentCompanyId.

By default the "Context node" is empty. You can set the variables and procedures needed, in order to implement "context management". Once these values are defined and the patterns instance updated, the variables will be defined in the needed objects (e.g. transaction, workwith, etc)

#### [Security](#Security)

This property implements object level security. By default, the implementation includes a procedure called IsAuthorized, which is invoked in the Start event of each Web Panel, to control the authorization for accessing the resource. If this procedure returns a false, it means that the user is not authorized to execute the application, and therefore the Web Panel NotAuthorized is called. In the sample implementation this procedure always returns a True, so you should customize it as needed. You can change the called objects by changing the Security properties.


|  |
| --- |
| **Backlinks** |
| [Description property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52696) | [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) | [Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546) |
| [Rows per page property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52700) | [Style property in Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?52134) | [Style property in Work With for Web Pattern Settings (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53343) | [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |
| [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) |

---
