---
title: "How to convert my application to make it responsive"
source_id: 25214
source_url: https://wiki.genexus.com/commwiki/wiki?25214
genexus_version: "18"
---

# How to convert my application to make it responsive

This guide is meant for converting earlier versions into GeneXus X Evolution 3, according to a [Responsive Web Design (RWD)](https://wiki.genexus.com/commwiki/wiki?25161) approach.

Converting from an HTML layout to an [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) can be done automatically as since [GeneXus X Evolution 3 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?29164,,), using the [Convert to Abstract Layout menu option](https://wiki.genexus.com/commwiki/wiki?29297).

In all cases where this is possible, we have ways to do the conversion smoothly, and here is an explanation of what you should take into account in order to do the conversion. There are objects in the KB whose forms were created by GeneXus. When they have not been customized by the user, then the conversion is automatic: this is discussed in the Default Forms section in this document.

There are also objects whose default forms have been customized, which, like any object form -such as web panel forms-, must be fully designed in order to fit a Responsive layout. Nevertheless, the layout can be initialized using the [Convert to Abstract Layout menu option](https://wiki.genexus.com/commwiki/wiki?29297).

In the case of forms capable of applying the Default Web Form - [Apply Default menu option (for Win and Web Forms)](https://wiki.genexus.com/commwiki/wiki?9751), the full design is not necessary. The process may start at the default form.

## [Default Forms](#Default+Forms)

* Set [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) to Responsive Web Design value.

In case of default web form of transactions, work with [Pattern](https://wiki.genexus.com/commwiki/wiki?2814) objects, or prompts that have not been customized, an automatic conversion to the abstract layout is performed, if the value of [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive Web Design.

The Flat Theme is used by default ([Default Theme property](https://wiki.genexus.com/commwiki/wiki?8145) = Flat), with the RWDMasterpage set as the [Default Master Page property](https://wiki.genexus.com/commwiki/wiki?11597). These settings are automatic when [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive.

The Flat Theme has the classes adequate for this approach, and it may be adjusted to the application's style. The same happens with the RWDMasterpage, which is a [What is a Master Page](https://wiki.genexus.com/commwiki/wiki?17088) using the abstract layout. The user should change this Master Page according to the application's design lines.

### [Example](#Example)

See [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,).

## [User-updated Forms](#User-updated+Forms)

If a non-default web transaction form or a non-default work with Pattern object form has been customized, then the form is not re-defined and it uses the [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673). The same happens with all web panels or web components.

In this case, we must bear in mind that the form will use the Flat Theme, which, in general, is not adequate for non-abstract layouts.

So, here we will need to do either one of the options below:

1. Adapt the objects so that the object's controls do not use classes designed specifically for responsive design, in which case we must create other classes for these controls in the Theme, different from the classes designed to fit the Responsive look & feel.

2. Convert the web form to an [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209).

An immediate way to do the conversion is through the [Convert to Abstract Layout menu option](https://wiki.genexus.com/commwiki/wiki?29297), available as since GeneXus X Evolution 3 upgrade 5.

Another way to convert an HTML layout to an abstract layout is through the [Add Layout as Root Form](https://wiki.genexus.com/commwiki/wiki?24967) contextual menu option in the [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673). The result of this will be the [Root form](https://wiki.genexus.com/commwiki/wiki?24972), including an [HTML container](https://wiki.genexus.com/commwiki/wiki?24960). We must gradually convert the parts of this HTML container, to be designed using the abstract layout.

### [Example](#Example)

In the following example, the Airport Transaction has been customized and consequently, it does not have the default web form. So, the transaction's web form is not converted automatically into an abstract layout. It uses the Theme "Flat", so it will look like this:

`[imagen omitida: wiki id 25240]`

An alternative, in this case, is to apply the form default to the transaction ([Apply Default menu option (for Win and Web Forms)](https://wiki.genexus.com/commwiki/wiki?9751)), and then make any changes necessary on the form.

`[imagen omitida: wiki id 25241]`

After applying the default web form, the web transaction abstract form will look like this:

`[imagen omitida: wiki id 25242]`

## [New objects in the Knowledge Base](#New+objects+in+the+Knowledge+Base)

* Set [Default Web Form Editor property](https://wiki.genexus.com/commwiki/wiki?25154) to Abstract Layout.

To use the [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) for the [Root form](https://wiki.genexus.com/commwiki/wiki?24972) of the newly-created objects in the KB, set [Default Web Form Editor property](https://wiki.genexus.com/commwiki/wiki?25154) property to Abstract Layout.

## [See Also](#See+Also)

[Nesting abstract and HTML form layouts](https://wiki.genexus.com/commwiki/wiki?24786,,)  
[RWA - Tips and FAQ](https://wiki.genexus.com/commwiki/wiki?25971)


|  |
| --- |
| **Backlinks** |
| [Control Properties - Font](https://wiki.genexus.com/commwiki/wiki?8889) | [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673) |
| [Toc:Responsive Web Design in GeneXus](https://wiki.genexus.com/commwiki/wiki?29134) | [Root form](https://wiki.genexus.com/commwiki/wiki?24972) |

---
