---
title: "Event Execution Scheme"
source_id: 22472
source_url: https://wiki.genexus.com/commwiki/wiki?22472
genexus_version: "18"
---

# Event Execution Scheme

This document describes event trigger behavior in web applications when the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to "Smooth".

The main aspects of event handling that should be taken into account by the GeneXus user are as follows:

* The Refresh event is not triggered automatically after a user event.
* The Start event is only triggered once when the object is executed.
* Web components are refreshed independently from its container. The application gives feedback for the refresh in each [web component](https://wiki.genexus.com/commwiki/wiki?1864).

## [User events do not automatically trigger the Refresh Event](#User+events+do+not+automatically+trigger+the+Refresh+Event)

User events do not automatically trigger the refresh event on exit.

When a [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) is executed and [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to "Smooth", the following happens:

* Variables on the screen are read
* User event is executed

Remember that form variables and web panel parameters are in the scope of the user event. That means that whenever the event is triggered, it has the form variables and parameters available.

As for the Refresh operation, the user can force its execution using the [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069) or the [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578) when needed.

### [Automatic Refresh of a grid row](#Automatic+Refresh+of+a+grid+row)

As a result of the behavior explained above, when a user event is triggered for a row of the grid, only the row is affected because the grid is not reloaded implicitly.

For example, consider a grid with &ProductId and &ProductPrice columns. The code below is associated with a control included in the grid columns and calls a procedure that returns the new &ProductPrice given the &ProductId.

```
Event "Update Price of Line"
      &ProductNewPrice = CalculatePrice(&ProductId)
      &ProductPrice = &ProductNewPrice
EndEvent
```

In this case, even if the "CalculatePrice" procedure is executed, the refresh is not implicitly executed. So, the &ProductPrice column of the grid is updated, and the other rows of the grid remain unchanged, without being reloaded.

As a general rule, the grid row is automatically refreshed when a grid variable is assigned in a user event of the row:

```
Event "X"

&Var=expression //or
&Var=Procedure.call(InParams) //&Var is the output of the procedure - out, or inout parameter.

EndEvent
```

## [Start Event behavior](#Start+Event+behavior)

It is triggered only when the object is executed for the first time using the GET HTTP method. It is not triggered when executed with the POST HTTP method.

Note that if web panel X calls web panel Y, and web panel Y returns to X (or calls X), the start event of X is triggered.

## [Web component events are local to the web component](#Web+component+events+are+local+to+the+web+component)

The refresh inside a web component only affects the web component where it is executed and the web components nested in it.

### [How to refresh other web components](#How+to+refresh+other+web+components)

Methods are available to explicitly refresh a web component. Consider the following scenarios:

1. If you need to refresh a web component that is descendant of the web component where the event is triggered:

For example, suppose you have a web page that loads web component A (besides, A loads web component B). Web Component A has the following code:

```
Event "GetBalance"
   &UserBalance = GetUserBalance(&UserId)
   &websession.set("UserBalance",&UserBalance)
EndEvent
```

Web Component B uses &UserBalance to display information in the form. It won't get the information from &UserBalance unless the previous code includes an explicit refresh that causes the web component B to reload.

```
Event "GetBalance"
   &UserBalance = GetUserBalance(&UserId)
   &websession.set("UserBalance",&UserBalance)
   WebComponentB.refresh()
EndEvent
```

This causes web component B to execute the Start, Refresh, and Load events so that &UserBalance can be read from the web session in the Refresh event.

Note: The scope of the [WebComponent.Refresh command](https://wiki.genexus.com/commwiki/wiki?22579) includes the web component and the components it contains.

2. If you need to refresh the parent web component or the parent web page:

To refresh the entire page, use [Form.Refresh command](https://wiki.genexus.com/commwiki/wiki?25287).

In order to refresh the parent web component take a look at [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) solution.

3. If you need to refresh all the descendants of a web component, use [Refresh command](https://wiki.genexus.com/commwiki/wiki?25286).

4. In order to refresh web components individually, use the [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) solution. The same for refreshing a parent web component or a sibling web component.

See [HowTo: Use Global Events in Web Objects](https://wiki.genexus.com/commwiki/wiki?31167).

### [Note](#Note)

For compatibility reasons, when [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to "Previous Versions Compatible" the user event execution triggers the following actions:

* Start Event
* Variables on the screen are read
* User event is executed
* Refresh
* Load

See [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296)

Objects with different values of the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) can't be on the same web page.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Web Panel Object. Event Execution Scheme](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/web-panel-object-event-execution-scheme-6104795)

###


|  |
| --- |
| **Backlinks** |
| [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) | [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) |
| [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579) | [Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356) | [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) |

---
