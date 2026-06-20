---
title: "Specification Codes from spc0000 to spc0049"
source_id: 6431
source_url: https://wiki.genexus.com/commwiki/wiki?6431
genexus_version: "18"
---

# Specification Codes from spc0000 to spc0049

The list that follows shows the message codes from spc0000 to spc0049 that can appear during **Program Specification**. The complete list can be found [here](https://wiki.genexus.com/commwiki/wiki?5933).

|  |  |
| --- | --- |
| **Code** | **Message** |
|  |  |
| --- | --- |
|  | |
| [**spc0000**](#spc0000) | **%1** |
|  | It is a generic message code that usually should not appear. |
|  | |
| [**spc0001**](#spc0001) | **Control/object %1 not found/defined. Is it on the form?** |
|  | It refers to a property/method of a control or object that could not be identified. Usually, it occurs when controls are deleted from/renamed in the Form but the references to them are not corrected in the rules/methods/subroutines.    It could also happen when a Transaction is specifying as Business Components; which contains a Rule or Event associated with a control in the form. The BC specification ignores the Transaction's form so the control could not be identified. You may enclose them in [Win]/[Web]/[Text] environment attributes to avoid this error.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0002**](#spc0002) | **%1 object does not have the %2 property.** |
|  | It refers to a property (%2) that is not supported by object type (%1). |
|  | |
| [**spc0003**](#spc0003) | **Property ‘Component’ is deprecated.** |
|  | The Component property is being used but it is no longer supported. |
|  | |
| [**spc0005**](#spc0005) | **This object cannot be generated on this environment %1.** |
|  | The environment (%1) does not support the object type.    Possible causes are:  a.     When specifying Work Panels in a Web environment. (\*)  b.     When specifying Web Panels in a Win environment. (\*)  c.     When specifying Master Page Web Panels and the generator does not support Master Pages.  d.     When specifying Business Component Transactions and the generator does not support Business Components.  e.     When specifying a Work panel, Menu or Menu Bar belonging to a module different from the root.    (\*) This can occur, for example, when a Web Panel calls a Work Panel or vice-versa. |
|  | |
| [**spc0006**](#spc0006) | **%1 objects do not have the ‘%2’ method.** |
|  | It refers to the method (%2) that %1 type objects do not support.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0007**](#spc0007) | **Assignment between objects %1 is not allowed.** |
|  | The assignment between "object" type variables (such as HttpResponse) is not supported. |
|  | |
| [**spc0008**](#spc0008) | **Call to program %1 that cannot be generated****or accessed (URL Access = No)** |
|  | The call to program %1 could not be generated for one of these reasons:  a.     The %1 program cannot be generated in the defined environment. Quite probably, if the %1 program is specified, the *spc0005* message will appear.  b.     The %1 program has the property Generate Object in False.  c.     The %1 program is a Web Component (Transaction or Web Panel) with the “URL Access” property in “No”. In this case, it is not possible to have a Call, Link (the command) or Submit to this object. |
|  | |
| [**spc0009**](#spc0009) | **Type mismatch in %1: %2.** |
|  | A type error occurred in %1 whose value can be an expression, condition, assignment, etc. %2 presents additional information that allows identifying the error.     To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0010**](#spc0010) | **Type mismatch in assignment: %1 = %2 (%3=%4).** |
|  | A type error occurred in an assignment. %1, of the %3 data type, does not support to be assigned %2, which has the %4 data type.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0011**](#spc0011) | **Type mismatch in rule %1.** |
|  | The rule identified by %1 does not support the data type of the parameters specified to it.    To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0012**](#spc0012) | **Object %1 referenced in a Create function must be a component. Did you specify it?** |
|  | The first parameter of the Create() function must be an object with the Web Component property in Yes. The message can appear even when the object has the Web Component property in Yes, if it has not been specified yet. |
|  | |
| [**spc0013**](#spc0013) | **Use %1 instead of %2 %3.** |
|  | It suggests the use of the %2 super-type instead of the %1 subtype in a group or grid (%3) since using the super-type may cause ambiguity. |
|  | |
| [**spc0014**](#spc0014) | **Cannot update table %1 when using a temporary index.** |
|  | It applies to generators other than SQL (RPG, Cobol, etc.) avoiding updates when a temporary index is being used. |
|  | |
| [**spc0015**](#spc0015) | **Invalid rule syntax: %1** |
|  | It is an internal error that usually should not occur. It can occur if a specifier of previous versions is being executed in newer versions of GeneXus. |
|  | |
| [**spc0016**](#spc0016) | **Invalid condition syntax: %1** |
|  | It is an internal error that usually should not occur. It can occur if a specifier of previous versions is being executed in newer versions of GeneXus. |
|  | |
| [**spc0017**](#spc0017) | **Expression %1 does not return a value.** |
|  | The expression identified in %1 does not return a value. E.g.: This can occur when trying to assign the result of a method that does not return values to a variable/attribute.    As from GeneXus X Evolution 1 Upgrade 3, this control has been extended to Procedures, Data Providers and Web Components. For instance:  * &result = ProcWithoutParm() * WebComp.Object = WebPanelwithoutParm()  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0018**](#spc0018) | **Property %1 is read only. It cannot be assigned.** |
|  | This error appears when your code is trying to assign the value of:  * A property that cannot be modified * A Business Component member that is read-only.  Business Component members are read-only if any of the following is true:  * They are inferred attributes * They have an unconditional noaccept rule * They are assigned in the Start Event of the Business Component  To make this error message a warning see [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953). |
|  | |
| [**spc0019**](#spc0019) | **%1 is not a valid value for parameter %2 of %3.** |
|  | A non-supported value (%1) is being used for the %2 parameter of the %3 function. |
|  | |
| [**spc0020**](#spc0020) | **Line %1. Failed to expand dynamic call.** |
|  | An error occurred when trying to expand a dynamic call in static calls. Usually, this error occurs when the list of parameters specified in the dynamic call could not be analyzed because of its complexity. |
|  | |
| [**spc0021**](#spc0021) | **Line %1. No programs found matching dynamic %2 parameters.** |
|  | It can occur when expanding dynamic Calls or Creates. It occurs when, in the Knowledgebase, it has not been possible to find already specified programs matching the number and type of parameters indicated in the dynamic Call or Create. |
|  | |
| [**spc0022**](#spc0022) | **Input parameter %1 cannot be assigned.** |
|  | When trying to assign a variable/attribute defined as IN in the Parm() rule.    This warning can appear when you are assigned reserved variables. For instance, this is the case of &Count and &Start, within the context of Panel grid's load event (see [HowTo: Use external services](https://wiki.genexus.com/commwiki/wiki?21226,,)for more details). |
|  | |
| [**spc0023**](#spc0023) | **Parameter %1 %3 %2 has wrong type.** |
|  | It indicates that a parameter that does not correspond to the one expected by the program referred to is being transferred in a Call, Submit, Link, Udf or Udp. |
|  | |
| [**spc0024**](#spc0024) | **Not enough parameters %2 %1.** |
|  | The number of parameters specified in a Call, Submit, Link, Udf or Udp is lower than the one specified in the Parm() rule of the program referred to.    In the case of submit command/method, an additional parameter is required as explained [Submit method](https://wiki.genexus.com/commwiki/wiki?24382) |
|  | |
| [**spc0025**](#spc0025) | **Too many parameters %2 %1.** |
|  | The number of parameters specified in a Call, Submit, Link, Udf or Udp is higher than the one specified in the Parm() rule of the program referred to. |
|  | |
| [**spc0026**](#spc0026) | **Formula %1 cannot be evaluated in this program.** |
|  | The %1 formula cannot be worked out in the program. This situation occurs because the navigation required to evaluate the formula conflicts with the navigation of the program using it. |
|  | |
| [**spc0027**](#spc0027) | **No relationship found among attributes %3. Attributes: %1 are incompatible with: %2.** |
|  | It has not been possible to find a way to solve the navigation for the attributes mentioned in %1 and %2. The incompatibility information is not necessarily strict, it is actually a guide.    Tip: if the message includes "control" (i.e. “No relationship found among attributes in control %3…”) the problem could be caused by a "dynamic combo box with conditions," check the Attribute control type definition. |
|  | |
| [**spc0028**](#spc0028) | **Attribute %1 is part of the index. It cannot be updated.** |
|  | The attributes making up the index that is being used to navigate cannot be updated unless the access to data is made with SQL. |
|  | |
| [**spc0029**](#spc0029) | **Attribute %1 is part of the primary key. It cannot be updated.** |
|  | A table primary key cannot be modified. |
|  | |
| [**spc0030**](#spc0030) | **Line %2. Attribute %1 should not be assigned in an insert group. It has the Autonumber property set to on.** |
|  | Attributes with the Autonumber property in On do not need to be assigned to the New groups or transactions. The assignment is ignored but it can be used in environments where the Autonumber property is not natively supported. |
|  | |
| [**spc0031**](#spc0031) | **No relationship found among attributes %1.** |
|  | It applies to New groups and is similar to the case of the spc0027 message.    This could be due to the following causes:  * The same as spc0027 in New-EndNEw groups. * When the object includes a control attribute that is not supported by the target generator. For example, a Dynamic Combo Box using attribute formula as "Description attribute" or requiring a multi-table navigation in VB. %1 is the control name. |
|  | |
| [**spc0032**](#spc0032) | **&Mode cannot be assigned in this type of objects.** |
|  | The &Mode variable cannot be modified in transactions. |
|  | |
| [**spc0033**](#spc0033) | **%1 will be read only in update mode.** |
|  | It occurs when updating data in tables superordinated to the base table of a transaction. The %1 attribute is part of the key of those tables that are being updated. |
|  | |
| [**spc0034**](#spc0034) | **Syntax error in: %1. Ignored.** |
|  | It is an internal generic error that usually should not occur. It can occur if a specifier of previous versions is being executed in newer GeneXus versions. |
|  | |
| [**spc0035**](#spc0035) | **Line %4. The program %1 that implements property %2 of data type %3 does not exist in this model.** |
|  | It applies to the user data types (such as the Workflow data types) when the GeneXus object handling this property does not exist in the knowledge base. |
|  | |
| [**spc0036**](#spc0036) | **Line %4. The program %1 that implements method %2 of data type %3 does not exist in this model.** |
|  | It applies to the user data types (such as the Workflow data types) when the GeneXus object handling this method does not exist in the knowledge base. |
|  | |
| [**spc0037**](#spc0037) | **%1 cannot be inferred.** |
|  | It occurs when GeneXus cannot navigate the %1 attribute that is a subtype. The attribute value is undefined and could vary from one specification to the other. |
|  | |
| [**spc0038**](#spc0038) | **There is no index for order %1 in group starting at line XXX.** |
|  | It is a warning that indicates that as long as many records exist in the table (or the number of records selected from the table is important), performance can be bad, and this could be caused by the lack of an index according to the indicated criteria. |
|  | |
| [**spc0039**](#spc0039) | **Ambiguous reference to attribute %1. Subtype group %G1 instead of %G2 chosen this time.** |
|  | It occurs when making a reference to the %1 super-type and there are several ways to instance it (several subtypes). The specifier chooses one of the possible ways (subtype groups %G1 or directly by the supertype (“none” appears in this case instead of the group name). The chosen way can vary from one specification to the other.  We suggest defining a subtype for the %1 attribute and using it to guarantee consistency among specifications. |
|  | |
| [**spc0040**](#spc0040) | **Subtype group %1 contains secondary attributes (%2). Secondary attributes ignored.** |
|  | The definition of the %1 subtype group contains attributes (%2) that cannot be determined by the primary attributes of the same group (called secondary attributes). The definition of subtypes for these attributes is ignored, which means %2 attributes could not be inferred. |
|  | |
| [**spc0041**](#spc0041) | **Subtype group %1 does not have primary attributes. Subtype group definition ignored.** |
|  | The definition of the %1 subtype group lacks primary attributes thus making it impossible to use it. The definition of subtypes for these attributes is ignored. |
|  | |
| [**spc0042**](#spc0042) | **Subtype group %1 (%2) does not identify a base table. Subtype group definition ignored.** |
|  | Primary attributes of the %1 subtype group do not coincide with the primary key of any of the model tables. The definition of subtypes for these attributes is ignored. |
|  | |
| [**spc0043**](#spc0043) | **%1 is not instantiated %2.** |
|  | This warning message can occur in several situations. In all cases, the attribute value can't be obtained or inferred (it is undefined).  Samples:   * Attributes of the "flat" part (which don't belong to the extended table of any grid) in Work Panels or Web Panels with multiple grids. * Attributes of subordinated levels that can't be instantiated in the higher levels. * New/XNew groups that mention attributes that cannot be instantiated. |
|  | |
| [**spc0044**](#spc0044) | **%2 cannot be assigned in NEW group starting at line %1.** |
|  | The %2 attribute is being assigned in a New group, and it does not belong to the base table of this New. |
|  | |
| [**spc0045**](#spc0045) | **Object %1 referenced by control %2 must be a component.** |
|  | The object referred to in the Object property of a WebComponent type control must have the Web Component property in Yes.    The validation is made against the last specification of the program referred to; thus, the problem could be corrected by specifying the program referred to and then the caller again. |
|  | |
| [**spc0046**](#spc0046) | **Variable %1 not defined. Same as %2 assumed.** |
|  | The variable mentioned in %1 has not been defined. It is assumed equal to the %2 attribute because they have the same name. |
|  | |
| [**spc0047**](#spc0047) | **Variable %1 not defined; %2 assumed.** |
|  | The variable mentioned in %1 has not been defined. The %2 definition, which was inferred from the first assignment to %1, is assumed. |
|  | |
| [**spc0048**](#spc0048) | **Attribute(s) %1 is(are) defined in table %2 but not in Data view %3.** |
|  | It occurs when accessing the Data View %3 associated to the %2 table, and the mapping for the %1 attribute(s) has not been defined yet. |
|  | |
| [**spc0049**](#spc0049) | **Attribute %1 is present more than once on the screen.** |
|  | It occurs when the attribute %1 appears more than once on the form of the object. |
|  | |
| **[Next](https://wiki.genexus.com/commwiki/wiki?6432)** | |


|  |
| --- |
| **Backlinks** |
| [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) |
| [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) | [Error List tool window](https://wiki.genexus.com/commwiki/wiki?42243) | [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) | [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933) |
|

---
