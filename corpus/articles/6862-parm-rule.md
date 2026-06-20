---
title: "Parm rule"
source_id: 6862
source_url: https://wiki.genexus.com/commwiki/wiki?6862
genexus_version: "18"
---

# Parm rule

Declares the list of parameters that a GeneXus object receives from the object(s) which invoke(s) it.

### [Syntax](#Syntax)

**Parm(**[*in*:|*out*:|*inout*:]*parm1,* …, [*in*:|*out*:|*inout*:] *parmN***);**

**Where:**

*in: | out: | inout:*  
    Are operators which allow defining for each parameter, how it is going to be used in the called object ([in, out, inout](https://wiki.genexus.com/commwiki/wiki?8220)).

*parm1, ..., parmN:*  
   Are variables or attributes that are defined in the called object. For each parameter received, you can decide whether you declare it as an attribute or a variable, regardless of how it was sent.

### [Description](#Description)

When an object is called from another object with parameters, the set of parameters received must be declared inside the Parm rule in the called object, respecting the order and the data type as they were sent, each one separated by a comma. In addition to this, for each parameter it is optional to point out how it is going to be used ([in, out, inout](https://wiki.genexus.com/commwiki/wiki?8220)).

If the object was invoked with [Call](https://wiki.genexus.com/commwiki/wiki?16224), and N parameters were transferred, the N parameters must be declared in the parm rule. However, if the object was invoked with the [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) and unless it was invoked in a [Data Provider)](https://wiki.genexus.com/commwiki/wiki?5270), bear in mind the following:

* N + 1 parameters must be declared in the parm rule of the called object.
* The last parameter declared in the parm rule corresponds to the value which is returned (in other words, corresponds to the value received in the caller object).
* A value must be assigned to the returned (the last) parameter somewhere in the called object.

**Considerations:**

* As they receive parameters and they must be called with the parameters' values, none of the objects that have a Parm rule defined are included in the [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484).
* Parameters do not receive a null value. If a null value is sent in a parameter, the called program receives an empty value.
* Variables that are in a Parm rule are set as read-only by default when they are put in a form of a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

The difference between using a variable on an at or an attribute in the Parm rule of the invoked object lies in the fact that If you receive the value in a variable, it may be used freely in programming, as a filter condition for equality (higher than, greater than or equal to, lesser than, lesser than or equal to), for some arithmetical operations, or whatever you may need to do with it. On the other hand, if you receive the value in an attribute, it will automatically act as a filter for equality in the object.

If your objective is not to use a value received to filter for equality, then the only solution possible is to receive the values in variables to use them freely.

### Samples

The following codes, show two ways of filtering for equality the same information. The result and performance of both solutions are equal.

`[imagen omitida: wiki id 24354]`

**Example 1**

Suppose you define a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) for the user to enter a start and end range of names of attractions to be listed.

`[imagen omitida: wiki id 24358]`

As the image shows, two variables and a button are present in the Web Panel form (the default Caption -Confirm- and the default event -Enter- are kept for the button). In the Enter event associated with the button, you have to call the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that prints the attractions that their names are included in the range indicated by the user.

The Procedure will receive the start and end range of names of attractions, and you have to use the range received to filter the requested attractions.

This is the invocation defined in the Web Panel:

`[imagen omitida: wiki id 24359]`

And this is the Parm rule declared in the Procedure:

`[imagen omitida: wiki id 24361]`

Note that the variables are named differently regarding the names defined in the Web Panel. What it is important is that the data types sent and received match.  
  
The variables you receive in the Procedure will be used to filter the requested attractions. The following image shows the Procedure Source section, with the code that solves the requirement and using the received variables to filter:

`[imagen omitida: wiki id 24360]`

**Note**: This Procedure has the necessary properties and rules to print the output in a PDF format.

**Example 2**

See the proposed examples in the following articles:

[Call method](https://wiki.genexus.com/commwiki/wiki?16224)

[Udp method](https://wiki.genexus.com/commwiki/wiki?3964)

### Related specification messages

* [spc0068](https://wiki.genexus.com/commwiki/wiki?6432) when a parameter has a data type that cannot be used for parameters in certain circunstances.
* [spc0023](https://wiki.genexus.com/commwiki/wiki?6431) for each parameter in the call command having a data type that is not compatible with the correspondig in the parm rule
* [spc0024](https://wiki.genexus.com/commwiki/wiki?6431) if there are too few parameters in the call command
* [spc0025](https://wiki.genexus.com/commwiki/wiki?6431) if there are too many parameters in the call command


|  |
| --- |
| **Backlinks** |
| [API object - Delete service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49781) | [API object - GetByKey service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50052) | [API object - Insert service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49778) |
| [API object - Update service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49780) | [Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217) | [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) | [Base Trn property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55948) |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) | [Call method](https://wiki.genexus.com/commwiki/wiki?16224) | [Calling a GeneXus generated program from other Environments](https://wiki.genexus.com/commwiki/wiki?21387) | [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) |
| [Compensation application property](https://wiki.genexus.com/commwiki/wiki?11896) | [Day method](https://wiki.genexus.com/commwiki/wiki?12646) | [Definition of type of parameters received (in, out, inout)](https://wiki.genexus.com/commwiki/wiki?8220) | [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) |
| [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149) |
| [Group Navigations that receive attributes as parameters](https://wiki.genexus.com/commwiki/wiki?18243) | [GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583) | [HowTo: Create a Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52874) |
| [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) | [Is it possible to modify Selection Lists?](https://wiki.genexus.com/commwiki/wiki?23900) |
| [Line variable](https://wiki.genexus.com/commwiki/wiki?8099) | [Loop type property](https://wiki.genexus.com/commwiki/wiki?11898) | [Mapping relevant data](https://wiki.genexus.com/commwiki/wiki?25149) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) |
| [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) | [Object Mock Testing](https://wiki.genexus.com/commwiki/wiki?55859) | [On deadline property](https://wiki.genexus.com/commwiki/wiki?11477) | [On new instance property](https://wiki.genexus.com/commwiki/wiki?11479) |
| [On priority change property](https://wiki.genexus.com/commwiki/wiki?11480) | [On resource non available property](https://wiki.genexus.com/commwiki/wiki?11481) | [On state change property](https://wiki.genexus.com/commwiki/wiki?11483) | [On warning property](https://wiki.genexus.com/commwiki/wiki?11478) |
| [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) | [Output property](https://wiki.genexus.com/commwiki/wiki?41037) | [Package Module with database access for Solutions extensibility scenarios](https://wiki.genexus.com/commwiki/wiki?42900) |
| [Procedure rules](https://wiki.genexus.com/commwiki/wiki?8262) | [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578) | [Refresh method for Grid controls (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57357) | [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) |
| [Start event](https://wiki.genexus.com/commwiki/wiki?8043) | [Submit command](https://wiki.genexus.com/commwiki/wiki?15386) | [Submit method](https://wiki.genexus.com/commwiki/wiki?24382) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |
| [Transaction rules when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?2280) | [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) | [Update Transaction property](https://wiki.genexus.com/commwiki/wiki?51941) | [Web Object property](https://wiki.genexus.com/commwiki/wiki?11884) |
| [Category:Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) | [Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288) | [What is a Master Page](https://wiki.genexus.com/commwiki/wiki?17088) |
| [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) |

---
