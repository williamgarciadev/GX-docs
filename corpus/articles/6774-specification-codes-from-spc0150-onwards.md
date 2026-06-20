---
title: "Specification Codes from spc0150 onwards"
source_id: 6774
source_url: https://wiki.genexus.com/commwiki/wiki?6774
genexus_version: "18"
---

# Specification Codes from spc0150 onwards

The list that follows shows the messages for codes spc0150 onwards, which can be displayed during **Program Specification**. The complete list can be found [here](https://wiki.genexus.com/commwiki/wiki?5933).

|  |  |
| --- | --- |
| **Code** | **Message** |
|  |  |
| [spc0150](#spc0150) | **Cannot update database %1. Changes to database are only allowed in procedures.** |
|  | This message indicates that you are trying to assign a value to an attribute outside the context of the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293). |
|  |  |
| [spc0151](#spc0151) | **"Default" attribute for element %1 cannot be applied %2. There must be a conditional element at the same level.** |
|  | This message indicates that there is an error in the Data Provider declaration using the "Default" clause.  The “Default” attribute works as the Otherwise clause in a Do Case conditional construction. This message warns you that the group must be preceded by at least one conditional group with the same name (i.e. there is an Otherwise clause with no previous Case clauses).  Usually, it means that group names have been written incorrectly.  Examples:  The following is correctly defined:   ``` DP_root  {     Group_1         {      ...         }         Group_1 [Default]         {      ...         }  } ```   The following is incorrectly defined:   ``` DP_root  {    Group_1        {     ...        }        Group_2 [Default]        {     ...        }  } ```  For more information about the Data Provider Default clause, see [Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309). |
|  |  |
| [spc0152](#spc0152) | **Cannot find subgroup definition for %1 at row %2** |
|  | It occurs when the Data Provider has a reference to a "Subgroup" by means of the "Insert" clause, but the Subgroup is not defined. For more information about the Data Provider Subgroup definition, see  [Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |
|  |  |
| [spc0153](#spc0153) | **Unsupported expression %1 %2** |
|  | There appears to be a problem with the Data Provider definition but the specifier cannot detect it. If you cannot recognize the problem, please send a distribution of the KB, thus enabling the error to be reproduced for your local support. |
|  |  |
| [spc0154](#spc0154) | **Group with OutputIfDetail attribute should have at least one child group with output %1.** |
|  | When a Group in a Data Provider has the "OutputIfDetail" clause, there has to be a nested group with output.  Examples:  The following is correctly defined:   ``` DP_root  {    Group_1 [OutputIfDetail]    {        Group_1_1       {          ...       }          }  } ```   The following is incorrectly defined:   ``` DP_root   {     Group_1 [OutputIfDetail]    {        ...              }     } ```  For more information about the OutputIfDetail clause, see [Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |
|  |  |
| [spc0155](#spc0155) | **Group with Input clause uses non-instantiated attributes %1.** |
|  | This message applies to Data Providers. It is triggered when a Group in the Data Provider declaration uses the "Input" clause and refers to attributes %1 that cannot be instantiated in that level. For more information about the Input clause, see [Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309). |
|  |  |
| [spc0156](#spc0156) | **Event %1 for control %2 is not defined.** |
|  | This message indicates that the control %2 needs to be associated with a trigger event, but the code was not defined in the source. |
|  |  |
| spc0157 | **Formula %1 is calculated on stored values only.** |
|  | Indicates that the (aggregation) formula will be calculated on the values stored in the tables referenced by the formula, so its value may be incorrect while the Transaction is being edited in update/insert mode. |
|  |  |
| [spc0158](#spc0158) | **Rules %1 not included** |
|  | Rule %1 cannot be included in the rule evaluation tree and therefore it will not be triggered. This mainly happens when the rule has an "input" variable that has not been initialized. A variable is considered initialized when:   * A value is assigned to them by another rule that is executed before. * A value is assigned in the Start Event. * It belongs to the Parm Rule as an input variable. * It is on the Form but it is not read-only. * It appears as an output variable in a Call rule or as returning value in Udp (Beware, other 'out' variables in UDPs are not considered as output).   **Example 1**   ``` Object.Call(&varInput);     //The parameter in the called object is an "In(put)" parameter. &varOutput = &varInput; ```   Both rules will not be included when &VarInput is not initialized.    **Example 2 - Business Components**    Suppose that a Person Transaction defined as Business Component has the following rules:   ``` Parm(in:&Mode, in:&PeronId); PersonId = &PersonId if not &PersonId.IsEmpty(); ```   In this case, the warning is not going to appear in the navigation of Person. Instead, it will appear in the Person\_BC navigation because Business Components ignore the parm rule and therefore &PersonId is not initialized.    **Example 3 - SDT Variables**  SDT variables are considered initialized not only when the variable itself is assigned but also when some of their elements are initialized in the same location/Event. For example:   ``` &Sdt1.Cod = Transaction1Cod on afterinsert; &Sdt1.Nom = Transaction1Nom on afterinsert; Procedure1.Call(&Sdt1) on afterinsert; ```   Note: In previous versions, rules that could not be triggered were shown when performing a detailed navigation. |
|  |  |
| [spc0159](#spc0159) | Property 'Initial Value' for %1 cannot reference attributes (%2). |
|  | The error can appear for attributes, variables and SDT elements that reference an attribute (%2) in their Initial Value property. The property value can be a constant, expression or UDP function which returns a value of %1's domain. Also, global variables such as &Today can be included. |
|  |  |
| [spc0160](#spc0160) | **Type mismatch in %1's Initial Value property. Expected type is %2, returned is %3.** |
|  | This message indicates that the data type of the expression or value referenced in the Initial Value property (%3) does not match the attribute's data type (%2). For example, if the attribute's data type is based on an enumerated domain, the Initial Value only accepts values from that domain (<Enumerated Domain Name>.<Enum Value>). |
|  |  |
| [spc0161](#spc0161) | **Line %2. Attribute %1 should not be assigned. It has the Autogenerate property set to on.** |
|  | Notifies that a self-generated attribute is being assigned (its data type is GUID and its Autogenerate property set to true). |
|  |  |
| [spc0162](#spc0162) | **Object exceeds maximum name length allowed by language (%1 characters).** |
|  | There are languages that have some restrictions about the length of their program name. For instance, RPG and Cobol do not support object names over 10 characters. In this scenario, GeneXus will warn you at specification time if there is an object that needs to be generated with those generators and its name length exceeds the limit. |
|  |  |
| [spc0163](#spc0163) | **Overlaying fields at line %1 column %2 between %3 and %4.** |
|  | For text generators (Cobol / RPG), it indicates that there are fields overlayed on the screen. |
|  |  |
| [spc0164](#spc0164) | **Multiple lines cannot start before column %1.** |
|  | For text generators (Cobol / RPG), it indicates that there is more than one line defined before the specified column. |
|  |  |
| [spc0165](#spc0165) | **Literal or attribute cannot start at Line 1 Column 1.** |
|  | For text generators (Cobol / RPG), it indicates that a literal can not start at the position (1,1) of the screen. |
|  |  |
| [spc0166](#spc0166) | **Window must be within coordinates %1 and %2.** |
|  | For text generators (Cobol / RPG), it indicates that the window defined in the form is greater than the maximum supported by the platform. |
|  |  |
| [spc0167](#spc0167) | **Invalid property values combination. %1 is incompatible with %2.** |
|  | This message is triggered upon specifying a report whose Call Protocol property has HTTP value, and an output (Output\_file rule) other than PDF (for example, RTF, TXT) has been specified. Thus, the object is not generated with that invalid combination that will cause compilation errors. It only applies to reports, that is, the object should have at least one printblock. |
| [spc0168](#spc0168) | **Control/object %1 not found/defined. Are you referencing a form control in a Business Component?** |
|  | This message indicates that control %1 seems to belong to the Form and therefore does not apply when the Transaction is specified as a Business Component. Solution: Wrap the rule within a [Win]/[Web] section using the Environment Attribute (Win, Web, BC, Text). |
|  |  |
| spc0169 | **%1 argument to function ''%2'' only supports %3 with this generator.** |
|  | Indicates that the generator has restrictions on the parameters in the function call. For example, in Cobol/RPG generators the round and trunc functions only support constants as the second argument. |
|  |  |
| spc0170 | **Attribute %1 will be empty when the value of description attribute %2 does not exist in table %3.** |
|  | Occurs in controls with hide codes when the associated attribute is not FK, so if the value for the assigned description is not found, the attribute will be empty. |
|  |  |
| spc0171 | **Prompt rule ''%1'' conflicts with previous prompt rule. Ignored.** |
|  | Indicates that there are two user rules prompt on the same attributes that identify the user. |
|  |  |
| [spc0172](#spc0172) | **Attribute %1 which is redundant in table %2 will not be updated** |
|  | It could appear when specifying a Transaction that includes an attribute that is part of the formula's expression (%2) in another Transaction (%1), which is defined as redundant in %2. The message warns you that this stored formula is not going to be automatically updated when the attribute changes its value.  For instance, suppose the canonical Invoice example is simplified as follows:  **Transaction Item**   ``` ItemId* ItemPrice ```   **Transaction Invoice**   ``` InvoiceId* ...   {    InvoiceLineId*    ItemId    ItemPrice    ItemLineQty    ItemLineTotal = ItemPrice * ItemLineQty } InvoiceTotal = sum(ItemLineTotal)  ===> This formula is redundant. ```   The warning appears when specifying the Item Transaction, because if ItemPrice is modified, the redundant formula on Invoice that refers to ItemPrice is not. |
|  |  |
| [spc0173](#spc0173) | **Failed to specify DataProvider %1. %2** |
|  | This message indicates that the data provider could not be specified because the Output property is empty or, in general, when the data provider is malformed. |
|  |  |
| [spc0174](#spc0174) | **Could not find a proper SDT for root element %1** |
|  | Indicates that the SDT selected in the Output property is not compatible with the data provider structure. |
|  |  |
| [spc0175](#spc0175) | **Element %1%2 is collection in %3, but not in %4.** |
|  | The message is triggered when a data provider element is inferred as a collection but in the SDT indicated as output it is not a collection or vice versa. |
|  |  |
| [spc0176](#spc0176) | **Cannot insert SubGroup ''%1'' at row %2.** |
|  | The error appears when you are trying to insert a Subgroup in the data provider, but for some reason it is impossible. |
|  |  |
| [spc0177](#spc0177) | **Cannot insert SubGroup ''%1'' in SubGroup ''%2'' starting at row %3. Insertion may loop indefinitely.** |
|  | The message is triggered when the specifier detects a loop between subgroup calls (for example SubGroup1 calls SubGroup2 and Subgroup2 calls SubGroup1) |
|  |  |
| [spc0178](#spc0178) | **Missing member %1 in SDT %2.** |
|  | The message appears when a member is referenced in the data provider, but that member doesn’t exist in the output SDT. |
|  |  |
| [spc0179](#spc0179) | **Attributes not allowed as parms in SubGroup ''%1'' starting at line %2.** |
|  | The error appears when an attribute is used as parameter in a subgroup definition because it’s forbidden. The use of an attribute as argument in a subgroup invocation is allowed but not as parameter in the subgroup definition. |
|  |  |
| [spc0180](#spc0180) | **'Count' attribute ignored in element starting at row %1** |
|  | This message appears when you are using paging in a Data Provider ([count] [skip]), in a group which isn’t a repetitive one. %1 indicates the row in the Data Provider where the invalid count appears. |
|  |  |
| [spc0181](#spc0181) | **There is already a %1 with the same name (%2).** |
|  | This message appears when you create an object whose name matches the name of an object automatically generated by GeneXus. This could happen in the following situations:   * A Procedure named Proc1 is defined as Main (AProc1 will be generated) and another object called AProc1 already exists in the KB. * A Transaction named Trn1 is defined as Business Component (Trn1\_BC will be generated), and an object called Trn1\_BC already exists in the KB. * The WorkWith for Smart Device Pattern generates programs that do not appear in the Knowledge Base; all prefixes are "WorkWithDevices<TransactionName>\*", so the warning may be displayed if you define an object that matches some of these names. |
| [spc0182](#spc0182) | **Cannot use associated Business Component ('<Transaction Name>')** |
|  | When the Work With for Smart Device pattern is applied to a Transaction, some Sections could be defined based on the table relationship. Each of these sections is associated with its corresponding Business Component. This warning appears when the user alters Layouts (edit mode) or Events of a Section, adding attributes that now imply navigating another table other than the previously associated BC. As a consequence, some implicit actions are not automatically generated. |
|  |  |
| [spc0183](#spc0183) | **Cannot use attribute and variable with the same name (''%1'').** |
|  | In Smart Devices, this message means that there are two fields (a variable and an attribute) with the same name and this is not supported. |
|  |  |
| spc0184 | **Cannot use command %1%2** |
|  | In Data Providers it indicates that a Load statement was placed in a non-repetitive group. |
|  |  |
| [spc0185](#spc0185) | **'%1****''s** **contents will not be preserved between calls to %2.'** |
|  | The variable is not being preserved between calls.  Solution: Consider initializing it properly. |
|  |  |
| [spc0186](#spc0186) | **Cannot use variable %1 in form's events** |
|  | This message appears when you reference a variable located in a Grid, on a Form Action (that means, an event outside the grid).  As the variable could have different values for each line of the grid, the actions at the Form Level does know its value. |
|  |  |
| [spc0187](#spc0187) | **Method %1 has no effect** |
|  | This message appears when the result of applying the method (%1) is not specified.  For instance, it has:   ``` B.Trim() ```   and the returned value is not assigned to anything.  It must be:   ``` &res = B.Trim() ``` |
|  |  |
| [spc0188](#spc0188) | **Rule %1 for inferred/formula attributes (%2) has no effect.** |
|  | This message appears when it is detected that applying the rule (%1) has no effect. For instance, it has:   ``` Noaccept(A); ```   But attribute A" is a formula or an inferred attribute. |
|  |  |
| [spc0189](#spc0189) | **Rule %1 has no effect** |
|  | The warning indicates that the rule does not have any effect on the program.  For instance, it will be triggered in this kind of rules:   ``` A = "a" on AfterInsert; ```   Because the assignment is declared after the Insert, so it has no sense.  Or in the following rule when "A" is an inferred attribute:   ``` Default(A,1); ```   **Note:** In versions prior to GeneXus X Evolution 2 Upgrade 3, the message description was: "Assignment rule %1 has no effect". |
|  |  |
| [spc0190](#spc0190) | **Rule %1 has no effect** |
|  | This warning appears when it is detected that applying the rule (%1) has no effect.  For instance, it has:   ``` Default(A,1); ```   But "A" is an inferred attribute.  **Note:** As from GeneXus X Evolution 2 Upgrade 3 this warning is shown as spc0189. |
| [spc0191](#spc0191) | **Synchronize event for attributes %1 matches a previously defined synchronize event (%2).** |
|  | Indicates that the referenced OfflineDatabase object has a synchronize user event on a list of attributes that determine a table for which another synchronize event already exists in this same object. |
|  |  |
| [spc0192](#spc0192) | **Synchronize event for %1 is not referenced by the application.** |
|  | Indicates that the referenced OfflineDatabase object has a synchronize user event on a list of attributes that determine a table that is not among the tables stored offline. |
|  |  |
| [spc0193](#spc0193) | **Attributes %1 need to be assigned in synchronize event for %2.** |
|  | Indicates that the referenced OfflineDatabase object has a synchronize user event that attempts to allocate some attributes by code but not all those required by that event. |
|  |  |
| [spc0194](#spc0194) | **Cannot assign attributes %1 in synchronize event for %2.** |
|  | Indicates that the referenced OfflineDatabase object has a synchronize user event that attempts to assign an attribute that is not in the table that synchronizes that event. |
|  |  |
| [spc0195](#spc0195) | **Unsupported expression %1. Ignored** |
|  | The message indicates that GeneXus will not generate code for expression %1.  For instance, this could happen when :   * an array variable is assigned to another one. * an array variable is initialized in this way: &var = <exp>  instead of:  &var() = <exp> .   See [How to define Variables and Arrays](https://wiki.genexus.com/commwiki/wiki?7385) for more details.  This message appears as from GeneXus X Evolution 2 Upgrade 3. In previous GeneXus versions, the problem also exists but no warning is displayed. |
|  |  |
| [spc0196](#spc0196) | **Synchronize event for attributes %1 may generate duplicate records.** |
|  | Indicates that the referenced OfflineDatabase object has a synchronize event that can attempt to insert duplicate records (the event navigation can not, in this case, ensure uniqueness in the records). |
|  |  |
| [spc0197](#spc0197) | **%1 should be exposed as a REST protocol Web Service.** |
|  | The message indicates that %1 needs to be defined as [REST Web Service](https://wiki.genexus.com/commwiki/wiki?14573) in order to be invoked.  This could happen in the followings scenarios:   * Online Native Mobile Object that refers a BC code inside a User Event. * Online Native Mobile Object that calls a Procedure or Data Provider inside a User Event.   Whenever you call a Procedure, Data Provider or BC from a User Event in Online Native Mobile apps, this invocation will be generated as a REST Web Service call. So the called objects have to be defined as [Rest services](https://wiki.genexus.com/commwiki/wiki?28213).  For instance, suppose we have this user event on Smart Device app Layout:   ``` Event "Insert"    Composite        &Customer.CustomerName = "Peter"        &Customer.Save()    EndComposite Endevent ```   Where &Customer is a variable defined as Customer Data Type (and Customer Transaction is Defined as Business Component).  If the Customer Transaction is not exposed as REST web service, the warning will appear; otherwise, the program could know how to handle this invocation. |
|  |  |
| [spc0198](#spc0198) | **DataSelector %1 (directly or indirectly) references itself.** |
|  | This warning appears when it is detected that a DataSelector references itself directly or indirectly.  This could happen in the following scenarios   * If the property "DataSelector" of the DataSelector **%1** references itself. * If the chain of references ends with DataSelector **%1** iteself. |
|  |  |
| [spc0199](#spc0199) | **Procedure cannot be exposed as Client Side Script (%1)** |
|  | Occurs when the object has set the Expose as Client Side Script property but it can not be generated in this way because it uses some function that requires access to the DBMS or uses some function not implemented for the generator associated with the object. |
|  |  |
| [spc0200](#spc0200) | **External Object %1 does not implement method '%2(' for %3 environment. (%4 '%5')** |
|  | Example : error: spc0200: External Object Notifications does not implement method 'opensession(' for Java Web environment. (Procedure 'WorkflowSDSendNotification')  This error applies when a method — %2 — from an [External object](https://wiki.genexus.com/commwiki/wiki?5669) — %1 — is used by a [GeneXus Object](https://wiki.genexus.com/commwiki/wiki?1866) — %5 — and the method is not implmented for the environment — %3 — you are generating.  There is a particular case when developing Native Mobile applications, where some methods can only be called from [client events](https://wiki.genexus.com/commwiki/wiki?24332). E.g.: [Network](https://wiki.genexus.com/commwiki/wiki?31310).IsServerAvailable() |
|  |  |
| [spc0201](#spc0201) | **The value of ''%1'' does not take into account changes to the value of %2** |
|  | This applies in the following scenario:  An inline formula inside a For each references a variable that is modified in the same For each.  At execution time, the value of the variable remains constant in the calculation of the formula.  This problem occurs because the formula and the variable are calculated in the same select sentence of the For each, to improve performance.  This message appears as from GeneXus X Evolution 2 Upgrade 4. In previous GeneXus versions, the problem also exists, but no warning is displayed. |
|  |  |
| [spc0202](#spc0202) | **%1 ''%2'' cannot be called, it is %3 to module ''%4''.** |
|  | Example 1: error: spc0202: Web Panel 'List\_Clients' cannot be called, it is private to module 'B'.  Example 2: error: spc0202: Table 'Company' cannot be accessed, it is private to module 'A'.  The error is triggered, at specification time, when an object in a given Module, references another object in a different Module, and it is not allowed to. Usually, to remove the error you should check if you are calling the right object. If it is the right one, change the value of its [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473). If not, change the reference.  Message added in [GeneXus Tilo Beta 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22217,,) |
|  |  |
| [spc0203](#spc0203) | **'New, update or delete to local database will not be sent to the server%1. Consider using Business Components instead.'** |
|  | This warning appears when the procedure performs updates to the [offline database](https://wiki.genexus.com/commwiki/wiki?22237) using new, delete or assignments in for each commands.  It indicates that these changes made to the offline database in this procedure will not be sent to the server and suggests using business components instead. |
|  |  |
| [spc0204](#spc0204) | **''Enabled'' property assignment over attribute %1%2 conflicts with ''%3'' rule.'** |
|  | This message is displayed when a transaction has a NoAccept rule and the Enabled property of the attribute that is not accepted is assigned. This conflict may cause a forbidden 403 error in a web application at runtime if the control is enabled through code and the NoAccept rule is also applied. |
|  |  |
| [spc0205](#spc0205) | **Option DISTINCT not supported with Unique clause%1.** |
|  | It occurs when in a group (eg: For each) the Unique clause is indicated and also the Option Distinct clause is present. |
|  |  |
| [spc0206](#spc0206) | **Cannot reference attribute(s) %1 unless they are referenced in Unique clause%2.** |
|  | It occurs when in a group (eg: For each) the Unique clause is indicated and within the For each body are named attributes that are not found in the extended tables of the attributes indicated as unique. The solution is either to remove the mentioned attributes from the For each body or to add them to the list of unique. |
|  |  |
| [spc0207](#spc0207) | **Formula %1 referenced in Unique clause cannot be evaluated in server%2.** |
|  | It occurs when in a group (eg: For each) the Unique clause is indicated by referencing a formula attribute that can not be evaluated in the server. |
|  |  |
| [spc0208](#spc0208) | **'warning: spc0208: No triggered actions '%1''** |
|  | This warning is displayed when an object has a list of actions (rules or formulas) which cannot be generated because one of its dependencies never becomes instantiated (known in the context of the object). |
| [spc0209](#spc0209) | **'error: spc0209: Table '%1' cannot be accessed.'** |
|  | This error is displayed when an object is accessing any of the attributes of a transaction' table, and only if the following conditions are met:   * The transaction' [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) is set to *Private* —  or **all** parallel transactions` [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) is set to *Private*. * The object accesing the attributes belongs to another [Module object](https://wiki.genexus.com/commwiki/wiki?22414) — in case of defining parallel transactions the error will be displayed when the object accesing the attributes does not belong to the same [Module object](https://wiki.genexus.com/commwiki/wiki?22414) of any of the parallel transactions. |
| [spc0210](#spc0210) | **'warning: spc0210: '%1' not supported, using '%2' function instead.** |
|  | This warning is displayed when the functions ServerNow(), ServerDate() or ServerTime() are used in a Smart Devices object with the Connectivity Support property offline.   * 'ServerNow()' not supported, using 'Now()' function instead. * 'ServerDate()' not supported, using 'Date()' function instead. * 'ServerTime()' not supported, using 'Time()' function instead. |
|  |  |
| [spc0211](#spc0211) | **Unique clause in break group not supported%1.** |
|  | It occurs when the Unique clause is used in a break. |
|  |  |
| [spc0212](#spc0212) | **Cannot update readonly %1 %2%3.** |
|  | This error is displayed when the developer tries to update a table whose associated transaction is set as Read Only ([Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) = Read Only).  %1 = Table (if the developer is trying to update in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) using a [For Each](https://wiki.genexus.com/commwiki/wiki?24744) or [New](https://wiki.genexus.com/commwiki/wiki?6714) command) or Business Component. |
|  |  |
| [spc0213](#spc0213) | **Attribute %1 is a non redundant formula. It cannot be updated.** |
|  | Occurs when trying to update a non-redundant formula inside a For each. |
|  |  |
| [spc0214](#spc0214) | **Attribute(s) %1 should be %2 to navigate table %3%4.** |
|  | Indicates that you have a [Dynamic Transactions that receives parameters](https://wiki.genexus.com/commwiki/wiki?36732) and there are missing parameters to be able to navigate that table. |
|  |  |
| [spc0215](#spc0215) | **'Subtype groups %1 identify the same base table (attributes %2). Consider merging them.****'** |
|  | This warning is displayed If two or more subtypes groups have the same primary key (i.e. base table). In this case, the groups should be defined as one group. More information: [SAC 38242](https://www.genexus.com/en/developers/websac?data=38242;;) |
| [spc0216](#spc0216) | **Break not allowed in group starting at line %1 (web panel %2)** |
|  | As since GeneXus 15, this error is displayed when in the web panel %2 there is a grid and also an event with a for each that navigates the same base table of the grid.  Example:  A web panel has a grid with attribute "Att", and the following event:   ``` Event 'Test'    For each         where Att =&Att              msg('test')    endfor Endevent ```   In order to avoid this error, and in case you need this [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) for some reason, move the for each code to a subroutine. But if you want to just read these attributes mentioned in the for each, the for each is not necessary. Just use the attributes. |
| [spc0217](#spc0217) | **Object is unreachable** |
|  | This warning is displayed when no main object is in the callers tree of that object. It applies to [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) and [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087). For objects with this warning, neither code nor metadata is generated. See Also [Modules Distribution in GeneXus - General Restrictions](https://wiki.genexus.com/commwiki/wiki?31376). |
|  |  |
| [spc0218](#spc0218) | **Control %1 has an empty value that conflicts with its Empty Item property** |
|  | This warning is displayed when a ComboBox/ListBox Control type variable is based on a domain including the empty value, and the control enables the Empty Item property. |
|  |  |
| [spc0219](#spc0219) | **%1 property value %2 not allowed.** |
|  | It occurs when specifying a web object in a KB that does not have a defined web style. In this case, it is indicated 'Style property value (none) not allowed.' To solve it, choose a web style in the properties of the version. |
|  |  |
| [spc0220](#spc0220) | **Cannot call %1.%2) from %3s.** |
|  | This happens if you try to call a global event from a non-web event (% 1 is the object type,% 2 is the method, and% 3 indicates the type of the calling object). |
|  |  |
| [spc0221](#spc0221) | **Event ''%1'' must be defined for updatable %2.** |
|  | It occurs when specifying a [Dynamic Transaction that allows update data](https://wiki.genexus.com/commwiki/wiki?28656), but to which the insert / update / delete events were not defined. To solve it, you have to define the events. |
|  |  |
| [spc0222](#spc0222) | **%1%2 currently not supported.** |
|  | It is a generic error indicating that something (described in% 1% 2) is not currently supported. |
|  |  |
| [spc0223](#spc0223) | **Updatable %1%2 will be read-only for %3 environment.** |
|  | This warning indicates that the mentioned [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062) will be considered as read-only in the mentioned environment. It occurs in offline smart devices environments when a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) / [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) has set its [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data and also has defined the Insert / Update / Delete events. |
|  |  |
| [spc0224](#spc0224) | **Module %1 not available for %2 environment.** |
|  | This error message is displayed when the GeneXus Module version installed on the KB being used doesn't match the GeneXus Module version provided by the GeneXus version being run.    When GeneXus is run after installing a new version, and the opened KB was created with a previous version, the Build operation updates the GeneXus Module (and the following warning is displayed in the output: Updating 'GeneXus' module version from X.X.X.XXXXX to required Y.Y.Y.YYYY.).     So, just building an object is usually enough to fix the problem. If not, selecting **Knowledge Manager / Manage Module References** opens a dialog box showing the GeneXus Module version that the KB has installed and the GeneXus Module new version to manually update it.     Advanced notes:  * The binary files are located in the directory %appdata%\GeneXus\GeneXus\<GXVersion>\Modules\_v1.0\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\<ModuleVersion>\Platforms\<PlatformName>.   + A module has N implementations. It is possible to have only the implementation for a CSharp environment. In the GeneXus module, we have it for each one of the environments supported: Java, CSharp, Android and iOS. * If you only have the directory %appdata%\GeneXus\GeneXus\<GXVersion>\Modules\_v1.0\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\<ModuleVersion> and inside it only the .opc file, you need to check the version of the module referenced in the KB.   + Workaround: open the dialog box "Manage Module References" and update the version in the KB. * If you don't have some of the directories highlighted in the path  %appdata%\GeneXus\GeneXus\<GXVersion>\**Modules\_v1.0\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\<ModuleVersion>**.   + Workaround: run "genexus /install"; doing so creates that path and copies the .opc in the GeneXus installation directory. |
| [spc0225](#spc0225) | **Cannot navigate table %1 unless attribute(s) %2 are referenced in Unique clause%3.** |
|  | This error occurs when:   * The navigation with the Unique clause performs a join that must be resolved in the client (that is, the statement is split into at least 2 statements) and some of the "source" attributes of the join is not present in the list of attributes of the Unique clause. * An update is performed but the attributes that compound the primary key are not mentioned in the unique clause. This is necessary in order to perform the Update part of that navigation. |
|  |  |
| [spc0226](#spc0226) | **Cannot navigate to multiple Data Stores in control %1.** |
|  | Indicates that the navigation of a control ([Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) or edit with the [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) = 'Descriptions') goes over more than one Data Store. For the case of a Dynamic Combo Box, it can be solved by creating a Data Provider that returns the required data and by setting the combo [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) = 'Data Provider'. |
|  |  |
| [spc0227](#spc0227) | **Property ''%1'' for table %2 should be set to perform synchronization by timestamp %3.** |
|  | It occurs when specifying an Offline Database which their [Logically Deleted Attribute](https://wiki.genexus.com/commwiki/wiki?37091) / [Last Modified Date Time Attribute](https://wiki.genexus.com/commwiki/wiki?37092) properties are not set, so that timestamp synchronization can be applied to the indicated table. |
|  |  |
| [spc0228](#spc0228) | **Ambiguous command Load in ''%1'', use grid.load() method instead.** |
|  | This error is displayed when a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) includes more than one grid and the Load command is used inside a user event. Instead of using the Load command you have to use the GridName.Load() method to point out the grid you want to load. |
|  |  |
| [spc0229](#spc0229) | **%1 must belong to table %2 in order to be used in %3 property.** |
|  | This error indicates that when specifying the timestamp synchronization of a table in an OfflineDatabase it was detected that the  [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) / [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) points to an attribute that is not in the associated table (for example, found in the extended). The IDE filter this but after a normalization may be an invalid value. |
|  |  |
| [spc0230](#spc0230) | **External data store %1 (%2): %3.** |
|  | This warning/error message is triggered by the queries evaluator of the external Data Store. %1 is the name of the Data Store, %2 is the type of Data Store (ex: OData), and %3 is the message provided by the evaluator's implementer. |
|  |  |
| [spc0231](#spc0231) | **Rule '%1' references non instantiated attributes (%2).** |
|  | This warning message indicates that rule %1, when triggered, will not have the %2 attributes available. This occurs, for example, when using a [Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865) that references secondary attributes of the table that is being checked. This warning message indicates that rule% 1, when triggered, will not have the% 2 attributes available. |
|  |  |
| [spc0232](#spc0232) | **Cannot have events '%1' and '%2' at the same time, use one or the other.** |
|  | This error message indicates that an object cannot have both events '%1' and '%2' defined at the same time. This is the case, for example, when you have a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with a single grid and the Load and Grid.Load events. |
|  |  |
| [spc0233](#spc0233) | **Parameter %1 (%2 %3) submitting ''%4'' will not be assigned.** |
|  | This warning message indicates that a certain output (or input/output) parameter will not be assigned when submitting an object. In other words, if you call an object using the Submit method and you define in the Parm rule of the submitted object an output parameter, it will not be assigned. |
|  |  |
| [spc0234](#spc0234) | **Variable %1 whose value is assigned in event %2 will have a default value in event %3 due to its datatype.** |
|  | This warning message indicates that an automatic parameter associated with a Data Provider of a Panel will not be taken into account and will instead take its default value in the server-side event.  For example, if a variable based on SDT (or any other non-basic data type) is assigned in the ClientStart event and it is an input parameter or a conditional assignment in the Start / Refresh / Load event, it will be reinitialized from these events. |
|  |  |
| [spc0235](#spc0235) | **'Grid ''%1'' has no base table and no load %2 found in event ''%3''.'** |
|  | This warning message advises that a grid does not have a base table and a Load command is missing within a Load/Grid.Load event. |
|  |  |
| [spc0236](#spc0236) | **'Invalid rule ''%1''.'** |
|  | This error message indicates that rule %1 has an invalid definition. |
|  |  |
| [spc0237](#spc0237) | **'Duplicate Rest Path for Method %1 ''%2''.'** |
|  | It indicates that the same [API object](https://wiki.genexus.com/commwiki/wiki?46151) has the RestPath repeated for different methods. |
|  |  |
| [spc0238](#spc0238) | **'Cannot use multiple Read Replica datastores (%1, %2)%3.'** |
|  | This message informs that more than one Read Replica is indicated in the same navigation. This can occur if a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) references a [Data Selector](https://wiki.genexus.com/commwiki/wiki?5312) and that Data Selector references another Data Selector, having both Data Selectors different Read Replicas. |
|  |  |
| [spc0239](#spc0239) | **'Variable %1''s datatype (%2) is deprecated and %3 removed in %4.'** |
|  | This warning message advises that a variable based on a certain data type will no longer be supported in the indicated version. That is, the data type will be deprecated.  Sample: "Variable xxx's datatype (CryptoSign) is deprecated and will be removed in v18 U5." indicates that [Cryptography data type](https://wiki.genexus.com/commwiki/wiki?22980) will be discontinued in GeneXus 18 Upgrade 5. |
|  |  |
| [spc1001](#spc1001) | **'Empty' is not a valid value for property 'Control Name' in <control>.** |
|  | It's an error message. Since GeneXus 15, the control names cannot be empty. |


|  |
| --- |
| **Backlinks** |
| [Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215) | [ClearProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25190) | [Table of contents:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) |
| [GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [No triggered actions](https://wiki.genexus.com/commwiki/wiki?17062) | [Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865) |
| [SetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25166) | [Specification Codes from spc0100 to spc0149](https://wiki.genexus.com/commwiki/wiki?6433) | [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |

---
