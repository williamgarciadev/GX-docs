---
title: "Specification Codes from spc0100 to spc0149"
source_id: 6433
source_url: https://wiki.genexus.com/commwiki/wiki?6433
genexus_version: "18"
---

# Specification Codes from spc0100 to spc0149

The list that follows shows the message codes from spc0100 to spc0149, that can appear during **Program Specification**. The complete list can be found [here](https://wiki.genexus.com/commwiki/wiki?5933).

|  |  |
| --- | --- |
| **Code** | **Message** |
|  |  |
| [spc0100](#spc0100) | **Item description in dynamic combo box %1 has an unsupported data type %2.** |
|  | The attribute used as ItemDescription in control %1 has a data type that is not supported. Please change the ItemDescription attribute or its data type.  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0101](#spc0101) | **Item value %1 does not match control %2 data type.** |
|  | The data type of the attribute used as ItemValue in control %2 must be compatible with the control's data type. Please change the ItemValue attribute or its data type.  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0102](#spc0102) | **Property "%1" does not support nulls.** |
|  | You are trying to assign a null value to a property that does not support it. You may change %1 nullability or avoid assigning nulls to it. |
|  |  |
| [spc0103](#spc0103) | **The first level of a transaction must not be a grid.** |
|  | The selected generator does not support this transaction design. Please change the design. |
|  |  |
| [spc0104](#spc0104) | **Grids are mandatory for all levels but the first one.** |
|  | The selected generator does not support this transaction design. Please change the design. |
|  |  |
| [spc0105](#spc0105) | **The Enter event must be associated to a control on the screen (a button, for example).** |
|  | The selected generator requires the Enter event to be assigned to any control. Please assign the Enter event to a valid control. |
|  |  |
| [spc0106](#spc0106) | **Data type %1 is not supported by this generator.** |
|  | The selected generator does not support data type %1. Please change the data type. |
|  |  |
| [spc0107](#spc0107) | **Candidate key %1 for %2 may have duplicate values.** |
|  | The attribute used as candidate key for %1 can have duplicate values in the Database. You should define %1 as Candidate Key by creating a unique index on it, to avoid wrong referential integrity controls. |
|  |  |
| [spc0108](#spc0108) | **%1 is a formula. It cannot be used as a candidate key.** |
|  | %1 is not stored. Only stored attributes may be used as candidate keys. |
|  |  |
| [spc0109](#spc0109) | **% it must be referenced in the transaction’s structure.** |
|  | The Description Atribute of Suggest Controls must be referenced in the transaction's structure. Please add %1 to the transaction's structure.  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953).    Note: Deprecated since GeneXus X Evolution 1 Upgrade 4. See [SAC #29075](https://www.genexus.com/en/developers/websac?data=29075;;). |
|  |  |
| [spc0110](#spc0110) | **Transaction is not valid. Two or more levels refer to the same table %1.** |
|  | Each transaction level should have a different underlying table. Please check the transaction’s structure to ensure this. |
|  |  |
| [spc0111](#spc0111) | **Cannot reference %1 by %2 in this transaction.** |
|  | InputType Description cannot be used for those attributes in a transaction that are part of the primary key, unless they are also a foreign key. |
|  |  |
| [spc0112](#spc0112) | **Item value %1 for control %2 must be Character or VarChar.** |
|  | Suggest supports Character or Varchar data types only.  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  |  |
| [spc0113](#spc0113) | **Maximum number of lines (%1) has been exceeded.** |
|  | Screen design exceeds the number of rows supported. |
|  |  |
| [spc0114](#spc0114) | **Maximum number of columns (%1) has been exceeded.** |
|  | Screen design exceeds the number of columns supported. |
|  |  |
| [spc0115](#spc0115) | **Literal %1 truncated to %2 at line %3 column %4.** |
|  | Literal %1 exceeds screen width or overlaps another control. To avoid compiling time errors, it has been truncated. |
|  |  |
| [spc0116](#spc0116) | **Group cannot be ordered by %1 %2.** |
|  | The specified order cannot be served.    Examples that can trigger this error:   * Order by a Blob attribute. * Order by a Long VarChar attribute when the DBMS is Informix, Oracle, DB2 and iSeries. * Order by an attribute that belongs to an extended table and the join between the tables is performed in the client side (the navigation list said: Join Location: Client) * Conditional Order when the DBMS is Informix, DB2 and iSeries. |
|  |  |
| [spc0117](#spc0117) | **Internal error, source line is:%1.** |
|  | This is an internal error. Please send the error text and any information you find useful (Knowledge Base, object with error, etc.) to Support. |
|  |  |
| [spc0118](#spc0118) | **Subtype groups %1 and %2 overlap. You should consider merging them. The following attribute(s) may be reported as "not instantiated" when referenced: %3..** |
|  | This error message is issued in the Subtype Groups Analysis. It shows that the mentioned groups overlap. These groups should be combined in one group; if you do not change that, the navigation may not be solved. |
|  |  |
| spc0119 | **External file %1 is not defined.** |
|  | An external file is not defined when is not in a Data View object. |
|  |  |
| spc0120 | **Invalid file or index name found%1** |
|  | This occurs when you are in an foreach and could not resolve the Data View. |
|  |  |
| [spc0121](#spc0121) | **Control %1 attributes are not supported by this generator.** |
|  | This error message is issued when control attributes are not supported by the target generator. %1 is the control name.    Possible causes:    § Dynamic Combo Box or Dynamic List Box using conditions, instantiated attributes, empty item, attribute formula as Description attribute or requiring a multi-table navigation. |
|  |  |
| [spc0122](#spc0122) | **Suggest specification in control %1 is not supported by this generator.** |
|  | This warning message is issued when the Suggest property has been set and it is not supported by the target generator. %1 is the control name.    Suggest specifications are ignored by generators that do not support them. |
|  |  |
| [spc0123](#spc0123) | **Attribute %1 used in %2's FileTypeAttribute property has an unsupported data type (%3).** |
|  | The attribute (%1) in which the blob file extension will be stored (%2) must be defined as character or varchar data type instead of %3. |
|  |  |
| [spc0124](#spc0124) | **Attribute %1 used in %2's FileNameAttribute property has an unsupported data type (%3).** |
|  | The attribute (%1) in which the blob file name will be stored (%2) must be defined as character or varchar data type instead of %3. |
|  |  |
| [spc0125](#spc0125) | **%1 is a formula. It cannot be used in %2's FileTypeAttribute property.** |
|  | Attribute formula (%1) cannot be used as FileTypeAttribute property for attributes of Blob data type (%2). As it will be storing the file extension of a blob attribute, it must be a non-formula char or varchar data type. |
|  |  |
| [spc0126](#spc0126) | **%1 is a formula. It cannot be used in %2's FileNameAttribute property.** |
|  | Attribute formula (%1) cannot be used as FileNameAttribute property for attributes of Blob data type (%2). As it will be storing the file name of a blob attribute, it must be a non-formula char or varchar data type. |
|  |  |
| [spc0127](#spc0127) | **%1 must belong to table %2 in order to be used in %3's FileTypeAttribute property.** |
|  | The attribute (%1) where the blob file extension will be stored must belong to the same table (%2) of the blob attribute (%3). |
|  |  |
| [spc0128](#spc0128) | **%1 must belong to table %2 in order to be used in %3's FileNameAttribute property.** |
|  | The attribute (%1) where the blob file name will be stored must belong to the same table (%2) of the blob attribute (%3). |
|  |  |
| [spc0129](#spc0129) | **Poor performance may be noticed if the first level is a repetitive group.** |
|  | This warning message is issued when the first level of a transaction is a repetitive group. |
|  |  |
| [spc0130](#spc0130) | **Use accept rule with level for variable %1.** |
|  | Variables in a transaction have no level (they are not in the structure). Following this, the place in the form where the variables are inserted is not suitable to determine the level where they are accepted. Accept rule must have the level clause in order to be valid.  The message indicates that the variable is placed in a grid but the accept rule is being applied in the first level. |
|  |  |
| [spc0131](#spc0131) | **Attribute %1 is a parameter. It should not be updated.** |
|  | This warning message is issued when the attribute %1 is a parameter and is updated in the rules. The attribute should not be updated. |
|  |  |
| [spc0132](#spc0132) | **Subtypes should be defined for %1 in Subtype Group %2 for formula %3 to avoid ambiguity.** |
|  | This message is issued when it has a subtype of formula attribute (%3), whose expression references an attribute (%1) that must also be defined as a subtype in the same group %2. Let's see an example:      **Transactions**  |  |  | | --- | --- | | PERSON | CLIENT | | PersonId\* | ClientId\* | | PersonFirstName | ClientFullName | | PersonLastName |  | | PersonFullName = PersonFirstName + PersonLastName |  |              **Subtype group**  |  | | --- | | ClientId st PersonId | | ClientFullName st PersonFullName |        In this case, the following warning is triggered at specification time:  spc0132: Subtypes should be defined for PersonFirstName, PersonLastName in Subtype Group Client\_Person for formula ClientFullName to avoid ambiguity.    So, to avoid the ambiguity, define ClientFirstName and ClientLastName in the Client Transaction and add them to the above subtype group. |
|  |  |
| [spc0133](#spc0133) | **spc0133: Formula %1 cannot be evaluated in control %2.** |
|  | The error is issued when the formula %1 cannot be evaluated in the server, within context %2.    For example, a formula using the UDP function referenced in a Dynamic Combo Box Description Attribute or a formula using a text that can be translated when you have Run-time translation in the kb environment. |
|  |  |
| [spc0134](#spc0134) | **spc0134: Poor performance may be noticed in group starting at line %4 as %1 index %2 is not defined in Data view %3.** |
|  | The error is issued when the Data View %3 does not define an index %2 (Type %1). |
|  |  |
| [spc0135](#spc0135) | **Order %1 of DataSelector %2 not used in group starting at line %3.** |
|  | For Each Groups and Grids using a Data Selector inherit the Data Selector's Order clause. When both, the For Each (or Grid) and the Data Selector object have unconditional Order(s), the former is discarded and this message appears. |
|  |  |
| [spc0136](#spc0136) | **Order %1 is a formula %2.** |
|  | It is just a warning indicating that the order clause uses an attribute defined as a formula (%1). The formula might have to be evaluated for each record in order to sort the results and this could be costly to the server.  %2 indicates the context where the attribute formula is referenced, for instance, the For Each' Order Clause or the Item Description attribute of Suggest/Dynamic ComboBox control.  Note: Only "server side" formulas can be used in the order clause. If GeneXus determines that the formula cannot be evaluated on the server, the spc0139 also appears. |
|  |  |
| [spc0137](#spc0137) | **Attribute %1 is not part of the extended table defined by DataSelector ''%2.** |
|  | When invoking a Data Selector through the "IN" operator in the "For Each Where" clause, the Data Selector has a base table by itself. This means that a SELECT sentence will be generated for the Data Selector definition, which will be a different and independent SELECT from the SELECT sentence that will be generated in relation to the For Each.    The attribute that precedes the "IN" operator **must belong to the extended table of the Data Selector base table**. The Data Selector query will return a collection of values corresponding to the same definition as the attribute which precedes the IN operator.    See an example in the second part of [this document](https://wiki.genexus.com/commwiki/wiki?5312). |
|  |  |
| [spc0138](#spc0138) | **spc0138: Order %1 has repeated attributes (%2)%3.** |
|  | The error is issued when an attribute is repeated in the order clause. |
|  |  |
| [spc0139](#spc0139) | **Formula %1 cannot be evaluated in the server.** |
|  | %1 is a formula that cannot be evaluated in the server by the DBMS. Therefore, it cannot be used in that part of the code.  For example, the error is triggered when a formula attribute belongs to the For Each's Order Clause and it uses some function or expression that cannot be resolved by the DBMS (refer to [Server Side Functions/Methods](https://wiki.genexus.com/commwiki/wiki?11572)).  In some cases, the formula could be resolved by the DMBS but run-time translation option disables that optimization. This is the case when the formula refers some string constant that has not been marked as non-translatable. See [ApplicationLocalization](https://wiki.genexus.com/commwiki/wiki?1988,,)  Another scenario where an optimized formula is not longer resolved by the DBMS is when [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is enabled. Look at [this considerations](https://wiki.genexus.com/commwiki/wiki?20834,,). |
|  |  |
| [spc0140](#spc0140) | **This object cannot be specified as it has the GenerateObject property set to false.** |
|  | Check the Generate Object property for mode details. |
|  |  |
| [spc0141](#spc0141) | **Rule %1 is deprecated.** |
|  | The rule %1 is no longer supported in the current version. See compatibility section in the release notes for more information. |
|  |  |
| [spc0142](#spc0142) | **The value of %1 will be the same for all rows. No relationship found between attribute %1 and attributes in its expression %2.** |
|  | The message indicates that the value returned by the formula will be the same for all rows, as no relationship has been found between the base table defined by the formula and the base table where it is being referenced. |
|  |  |
| [spc0143](#spc0143) | **Property "%1" is write-only. It cannot be read.** |
|  | This error appears when your code is trying to read a property that can only be modified. |
|  |  |
| [spc0144](#spc0144) | **Condition ''%1''%2 cannot be evaluated in the server.** |
|  | This message appears when the condition needs to be evaluated in the server but it uses a function or expression not supported by the DBMS. |
|  |  |
| [spc0145](#spc0145) | **Calling stored procedure %1 in datastore %2 via the call keyword is deprecated.** |
|  | Store Procedures can be defined as an [External Object](https://wiki.genexus.com/commwiki/wiki?5669). This has many advantages, for instance, the code becomes clearer because you can use as if it were another Genexus objects, and also for maintenance and deployment.  While it is possible to use the old syntax and declare the list of Stored Procedures used in the property List of external stored procedures at the Data Store level, it is recommendable to use the [new object type](https://wiki.genexus.com/commwiki/wiki?6138). |
|  |  |
| [spc0146](#spc0146) | **Formula %1 (directly or indirectly) references itself.** |
|  | The warning indicates that the formula has a reference to itself and therefore it cannot be resolved.  Example:  Formula1 = Formula2  Formula2 = Formula1 |
|  |  |
| [spc0147](#spc0147) | **Formula %1 references an invalid formula (%2).** |
|  | The message is triggered when %1 references an invalid formula, for instance, a self-referenced formula (see spc0146). |
|  |  |
| [spc0148](#spc0148) | **Event %1 has a duplicate argument set (other definition in line %2).** |
|  | The TrackContext event can be defined several times in the same object, but with different set of arguments as the event’s uniqueness is determined by their input parameters. This message warns you that the event has been defined at least twice with the same arguments. |
|  |  |
| [spc0149](#spc0149) | **Condition %1 found in %2 does not evaluate to boolean.** |
|  | The expression of the search condition does not evaluate to boolean in the formula definition. |
| **[Next](https://wiki.genexus.com/commwiki/wiki?6774)** |  |


|  |
| --- |
| **Backlinks** |
| [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) |
| [DynamoDB - Navigation restrictions](https://wiki.genexus.com/commwiki/wiki?50640) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Offline non-implemented DataTypes](https://wiki.genexus.com/commwiki/wiki?25398) | [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) |
| [Specification Codes from spc0050 to spc0099](https://wiki.genexus.com/commwiki/wiki?6432) | [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933) |

---
