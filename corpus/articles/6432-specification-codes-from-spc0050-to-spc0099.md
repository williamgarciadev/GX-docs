---
title: "Specification Codes from spc0050 to spc0099"
source_id: 6432
source_url: https://wiki.genexus.com/commwiki/wiki?6432
genexus_version: "18"
---

# Specification Codes from spc0050 to spc0099

The list that follows shows the messages code from spc0050 to spc00099 that can appear during **Program Specification**. The complete list can be found [here](https://wiki.genexus.com/commwiki/wiki?5933).

|  |  |
| --- | --- |
| **Code** | **Message** |
|  |  |
| [spc0050](#spc0050) | **Inferred subtype %1, cannot be assigned.** |
|  | It indicates if an attempt to update subtype %1, which is inferred, is occurring and if there is any cause that makes this not possible. The cause may be that the subtypes-supertypes group is wrong or that it belongs to the \*None group.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0051](#spc0051) | **Supertype %1 cannot be instantiated. Use subtype %2 instead %3** |
|  | It indicates that supertype %1 (inferred) cannot be instantiated and suggests using subtype %2 instead. %3 is used as a reference to identify the problem and its message may be: "in group starting at row xxx" or "in grid "xxx"' depending on the circumstances.    The reason for this is that there is at least one access by subtype to the group to which %2 belongs and, in the code, there is a reference to %1 (supertype of %2) instead of to %2. The specifier can detect the situation, but it cannot correct it, as it could be expected, generating this message. |
|  |  |
| [spc0052](#spc0052) | **Attribute %1 must be present on the screen or assigned by a rule.** |
|  | It occurs when the attributes making up the primary key in a Transaction are neither present in the form nor assigned in the rules. |
|  |  |
| [spc0053](#spc0053) | **Unsupported conditional constraint %1 changed to standard constraint %2.** |
|  | %1 is the specified constraint and %2 is the group (For each) or grid where the change was made.  It occurs in the following situations:   * When the generator does not support conditional constraints. * When the condition cannot be evaluated by the DBMS. For instance, the conditional attribute is a formula, that calls an UDP or refers a function that can not be [evaluated by the DBMS](https://wiki.genexus.com/commwiki/wiki?11572).    In this case; if there is a formula attribute used in the grid conditions; the LastPage paging button does not work and CurrentPage returns -1. * Conditional constraints are not supported in Breaks. * Conditional constraints are not supported when the resulting select joins local and external tables (from differents Data Stores) * When referencing a Data Selectors in conditions. If a Data Selector uses conditional constraints, the warning also appears when the Data Selector is referenced in [For Each's conditions](https://wiki.genexus.com/commwiki/wiki?5312) (through the "IN" operator in the Where clause) or participates in the [Aggregate Formula Definition](https://wiki.genexus.com/commwiki/wiki?5432).   In all these cases, the condition will be transformed into a “standard” restriction by replacing WHEN with OR. |
|  |  |
| [spc0054](#spc0054) | **Unsupported conditional order %2. Using default order in %1.** |
|  | It occurs when the generator does not support conditional orders. The navigation order will be the one specified as unconditional order, or, if there were not one, the primary key of the base table of the For each group.  %1 is the list of ordering attributes. %2 is the For each group or grid where the change was made. |
|  |  |
| [spc0055](#spc0055) | **Conditional order in group starting at line %1 not allowed (Break group).** |
|  | %1 is the line number of the For each group or grid where the situation was detected. |
|  |  |
| [spc0056](#spc0056) | **Internal error. Variable %1 definition is incorrect or not available. Data: [%2],%3,%4,%5,%6,%7,%8,%9** |
|  | It occurs when we distribute an object having variables that are structures and it is consolidated to a model that does not contain the definition of these structures.    Data values means:  %2 - Data Type  %3 - Length  %4 - Decimals  %5 - Signed  %6 - Dimensions  %7 - Picture  %8 - Description  %9 - Internal Identifier |
|  |  |
| [spc0057](#spc0057) | **Internal error. Incorrect order clause syntax.** |
|  | This is an internal error. If it occurs, please send a distribution of the KB, thus enabling the reproduction of the error to your local support. |
|  |  |
| [spc0058](#spc0058) | **%1 must be an array or collection.** |
|  | It occurs when making a reference to a variable that is not Array or Collection type in the command For %2 in %1. |
|  |  |
| [spc0059](#spc0059) | **Table %1 with two different orders.** |
|  | It occurs when navigating to the same table (%1) by different orders and the generator does not support this. |
|  |  |
| [spc0060](#spc0060) | **The program may be called by another program and the Commit on Exit property is set to YES.** |
|  | It occurs when there is a Procedure that makes a database update with the “Commit on Exit” property in “Yes”, it is called by another object and it has a parm rule defined.  The warning is mainly due to two reasons:  a.     Because, in fact, the intention is that the called object be included in the caller’s UTL and, as the “Commit on Exit” property has its default value, the procedure will commit all the pending changes to be made to the Database since the last commit.    b.     Because when the procedure that does commit is called from a For Each making an update, an error will occur (in any DBMS) on account of cursors closing. Therefore, in this case, the Procedure can neither have this property in YES nor do a commit explicitly. For more information please refer to the corresponding documentation. |
|  |  |
| [spc0061](#spc0061) | **Group without attributes starting at line 1.** |
|  | It occurs when there is a For Each group without attributes. |
|  |  |
| [spc0062](#spc0062) | **Order none %1 not allowed (Break group).** |
|  | It occurs when any For Each participating in the Control Break has the Order None clause. |
|  |  |
| [spc0063](#spc0063) | **Cannot perform updates when using the Distinct option** |
|  | When using the Option Distinct in a For Each it is not possible to make an update within the For Each group (or in Breaks that are children of the one with the Distinct Option). The reason for this is that each row returned by the For Each does not necessarily have only one database row associated (usually it has several). |
|  |  |
| [spc0064](#spc0064) | **Option DISTINCT not supported in this environment.** |
|  | The Option DISTINCT is only supported for generators accessing the database with SQL. |
|  |  |
| [spc0065](#spc0065) | **Option DISTINCT cannot be specified in BREAK groups.** |
|  | The Option DISTINCT is only supported in the first For Each of a For Each group defining Breaks. To solve the problem, we only need to move the code (Option Distinct) to the first For Each of the group. |
|  |  |
| [spc0066](#spc0066) | **Option DISTINCT not supported for local table %1.** |
|  | The Option DISTINCT is only supported for tables accessed via SQL. |
|  |  |
| [spc0068](#spc0068) | **This object does not support ‘%2’ data type parameters (%1).** |
|  | A (%2) data type has been specified for a parameter that is not supported by this object type.    Possible causes:   * Web Panels and Main programs with Call Protocol ‘Command line’ do not support Collections or SDTs or Arrays as parameters. * Web Components with the URL Access property in ‘Yes’ do not support Collections or SDTs or Arrays as parameters. * VB generator does not support calling main objects with structured parameters, regardless of the Call Protocol property’s value. * Data Providers Exposed as REST Services do not support SDTs as input parameters. Note that they may be created automatically related to SD Object's Navigation. [More Information...](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,37128) |
|  |  |
| [spc0069](#spc0069) | **When duplicate code will never execute. There are no updates to any attribute of a unique index.** |
|  | The ‘When Duplicate’ command has been specified in the context of a 'For Each' (XFor Each or XFor First). Nevertheless, no attribute that is part of a unique index is being updated. In this context, the code will never execute. |
|  |  |
| [spc0070](#spc0070) | **No When duplicate code found to handle possible duplicate condition when updating %1.** |
|  | An attribute that is part of a unique index is being updated in the context of a For Each (XFor Each o XFor First). The new value may produce a duplicate key, and there is no code to handle it. |
|  |  |
| [spc0071](#spc0071) | **%1 cannot be displayed or printed due to its data type (%2).** |
|  | Variables with %2 data type cannot be present in the form or print block. For example, a Structured Data Type variable (SDT). |
|  |  |
| [spc0072](#spc0072) | **External %3 index not defined for attribute(s) %1 in Data View %2.** |
|  | No mapping was found for a required index of type %3 (Primary key/Unique/Duplicate) on attribute(s) %1 for Data view %2.    Required Data View indices are:   * All associated table indices when the access method is not SQL. * Primary key index when the access method is SQL and the program is performing any update on the associated table. * Unique indexes when the access method is SQL and the program is performing updates or deletes on the associated table.   Please check platform-specific information, composition and type of all indexes on Data view %2. |
|  |  |
| [spc0073](#spc0073) | **Formula %1 is invalid.** |
|  | %1 is the name of an attribute defined as a formula. A valid navigation to evaluate the formula cannot be found. If %1 is a conditional aggregate, the probable cause of the problem is that navigation involves more than one table.    For example, this error can be present if we have a sum aggregate over inferred subtype. |
|  |  |
| [spc0074](#spc0074) | **Join to table %1 may not perform well as there is no index on %1's primary key.** |
|  | Table %1 is associated to a Data view and no matching index was found for its primary key on its associated Data View. This may lead to slow join performance if table %1 has a large number of rows.    Please check platform-specific information, composition and type of the primary key table %1 associated Data view. |
|  |  |
| [spc0075](#spc0075) | **Operand %1 does not match the data type of %2 in the IN comparison.** |
|  | %1 cannot be compared to %2. Comparison is carried out using the IN logical operator.    Please change data types as appropriate.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0076](#spc0076) | **%1 must be a collection to be used as the right operand in an IN comparison.** |
|  | %1 is the right operand of an IN operator. It must be a collection or array.    Please define %1 as an array or collection.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0077](#spc0077) | **%1’s data type (%2) is not supported in an IN comparison.** |
|  | %1 is the left operand of an IN operator. Its data type (%2) must be either Numeric, Character, VarChar, Date or [Date Time](https://www.artech.com.uy/openwiki/ow.asp?DateTime).    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0078](#spc0078) | **Internal error. Line %1 not recognized as a command.** |
|  | This error should not occur. The source line %1 contains code that could not be recognized/parsed by the GeneXus Specifier.    Please contact support. |
|  |  |
| [spc0079](#spc0079) | **Attribute(s) %2 in subtype group %1 is (are) not associated to any transaction.** |
|  | Attribute(s) %2 is (are) primary attributes in group %1. As it (they) is (are) not associated to any transaction, GeneXus does not know how to infer them. The subtype group is not valid.  This warning message usually occurs when a Subtype group is no longer in use or has been defined and imported from other Knowledge bases.    To solve this problem you may remove the Subtype group or reference the attribute(s) specified in the message in the appropriate Transaction. |
|  |  |
| [spc0080](#spc0080) | **Attribute(s) %2 in subtype group %1 could not be solved.** |
|  | The Subtype group %1 contains inferred attributes (%2) that cannot be "associated" to their stored counterpart.    Possible causes:  a.     The ending stored counterpart (supertype) is not stored in any table.  You may solve this problem by removing the subtype definition for attributes %2 or checking why their corresponding supertypes are not stored.  b.     The subtype group does not have subtype definitions for foreign key attributes that determines %2 as in the following example that raises this warning (spc0080) for attribute ClientCategoryName:    Transactions  |  |  |  | | --- | --- | --- | | CategoryId\* | PersonId\* | ClientId\* | | CategoryName | PersonName | ClientName | |  | CategoryId | ClientCategoryName | |  | CategoryName |  |  Subtype group  |  | | --- | | ClientId            st PersonId | | ClientName          st PersonName | | ClientCategoryName st CategoryName |    Adding ClientCategoryId as subtype of CategoryId in the subtype group and adding ClientCategoryId to the Client transaction solves the problem. |
|  |  |
| [spc0081](#spc0081) | **Attributes %1 do not allow nulls in table %2 and are not referenced %3.** |
|  | The list of attributes referenced in %1 do no allow nulls and the program being specified is trying to insert data without specifying values for them.    To fix the error you may:  a.     If the program is a transaction, you may reference these attributes in the transaction structure or disable insertion in the appropriate level (use the “error() if insert” rule).  b.     If it is a procedure, the New group must reference them. Otherwise, you may change the nullability property of these attributes.  c.     Set the Initialize not referenced attributes property to Yes. |
|  |  |
| [spc0082](#spc0082) | **Attribute %1 in table %2 does not allow nulls %3.** |
|  | A null value could be assigned to attribute %1 and it does not support nulls in table %2. The error context is %3.  The nullvalue() function is assigned to attribute %1 and the "Generate null for nullvalue()" property is set to Yes.  You may remove the assignment, change the "Generate null for nullvalue()" property value or change the attribute nullability for this table. |
|  |  |
| [spc0083](#spc0083) | **%1 not implemented by this generator.** |
|  | The feature %1 is not available for the generator. You may choose another generator or try to achieve the same results without using this feature. |
|  |  |
| [spc0084](#spc0084) | **%1 not implemented by this generator. Ignored.** |
|  | This is an information message stating that the feature %1 is not available for the generator and can be ignored safely. |
|  |  |
| [spc0085](#spc0085) | **Allownulls rule conflicts with null definition for foreign key %1.** |
|  | The foreign key %1 does not allow nulls as none of its attributes support nulls.    Remove the Allownulls rule (it should not be necessary) and change nullability of foreign key attributes as needed. |
|  |  |
| [spc0086](#spc0086) | **Internal error. Wrong parameter information for program %1. Try saving it again. Problem data: %2, %3.** |
|  | This error should only happen if redundant object parameter information is not found or is incorrect.    You should send the full message text and the root directory of your Knowledge Base to GeneXus support to fix the problem. Additionally, try saving the program %1 again and specify again. |
|  |  |
| [spc0087](#spc0087) | **%1 language statements are used in this object.** |
|  | This is a warning message stating that language-specific statements are used in the program. It is useful when converting your application between languages. |
|  |  |
| [spc0088](#spc0088) | **Grid %1 is associated to a collection. It cannot have navigation.** |
|  | Grids associated to collections cannot have navigation (i.e. an implicit For Each). %1 is the control name of the Grid. It may be empty if it hasn't been set.    You should either remove any attributes from the Grid or from the Grid’s Load event. It could aslo happen when assigning an attribute to a variable without using a for each, since it gets associated to the navigation of the Grid. |
|  |  |
| [spc0089](#spc0089) | **Event %1 cannot be specified when there are multiple grids.** |
|  | When more than one grid is on the screen, events as Load or Refresh become ambiguous. They must be changed to GridControlName.Load(), for example. |
|  |  |
| [spc0090](#spc0090) | **Cannot use For Each Line when there are multiple grids.** |
|  | When more than one grid is on the screen, the For Each Line block becomes ambiguous. Add the "IN GridControlName" clause to eliminate the ambiguity. |
|  |  |
| [spc0091](#spc0091) | **Grid ''%1'' is associated to a collection. It cannot have a load method or command.** |
|  | Grids associated to collections are automatically loaded with all collection items. There is no need for a Load command or method. |
|  |  |
| [spc0092](#spc0092) | **Master Pages do not support the parm() rule.** |
|  | Master Pages cannot be executed stand-alone. Parameters are taken from the objects referencing the Master Page. |
|  |  |
| [spc0093](#spc0093) | **The Master Page property references an object that is not a Master Page.** |
|  | Probably, the Master Page object has been deleted. |
|  |  |
| [spc0094](#spc0094) | **Grid ''%1'' is associated to a collection. It cannot have a refresh method or command.** |
|  | Grids associated to collections are automatically refreshed when changes are detected. There is no need for a Load command or method. |
|  |  |
| [spc0095](#spc0095) | **Object ''%1'' in Lookup rule is not a Data Provider** |
|  | This error code is not currently in use. |
|  |  |
| [spc0096](#spc0096) | **Description value %1 in control %2 is not guaranteed to be unique.** |
|  | The attribute used as ItemDescription in control %2 can have duplicate values in the Database. You may ignore this message or add a unique index on this attribute. |
|  |  |
| [spc0097](#spc0097) | **Rule (%1) ; does not apply to Business Component. Ignored.** |
|  | Some rules do not apply or make sense to transactions used as Business Components. You may enclose them in WIN/WEB blocks to avoid this warning. |
|  |  |
| [spc0098](#spc0098) | **No relationship found among attributes in control %3. Attributes: %1 are incompatible with: %2.** |
|  | This error code is not currently in use. |
|  |  |
| [spc0099](#spc0099) | **%1 is a dynamic combo box. Combo boxes are not supported on this platform.** |
|  | Some generators do not support Combo boxes. Please use a supported control type. |
|  |  |
| **[Next](https://wiki.genexus.com/commwiki/wiki?6433)** |  |


|  |
| --- |
| **Backlinks** |
| [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) |
| [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) | [Specification Codes from spc0000 to spc0049](https://wiki.genexus.com/commwiki/wiki?6431) | [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933) |

---
