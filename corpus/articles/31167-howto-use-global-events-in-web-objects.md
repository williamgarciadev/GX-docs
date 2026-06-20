---
title: "HowTo: Use Global Events in Web Objects"
source_id: 31167
source_url: https://wiki.genexus.com/commwiki/wiki?31167
genexus_version: "18"
---

# HowTo: Use Global Events in Web Objects

Most times it's necessary to implement a solution where one action in a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) of the screen causes a reaction in another web component.

For example, if the user selects an item in a Menu (of another component of the screen), it triggers an action in some other web component.

Since communication between the web components of the screen is a bit limited - the only feasible communication is between parents to children-, [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) are very useful for enabling the GeneXus user to establish communication between [Web Components](https://wiki.genexus.com/commwiki/wiki?1864) that are disengaged (1).

### [Benefits of using Global Events on the web](#Benefits+of+using+Global+Events+on+the+web)

* Global Events give a solution for communication between the web components of a form.
* Also, you can execute a specific event of a component with no need to Refresh the component's form.

### [Samples](#Samples)

**Communicating with a sibling object**

An action in component A should trigger an action in component B.

`[imagen omitida: wiki id 32497]`

Consider a hypothetical case where there are two sibling components, one of them ("AuthorsComponent") loads a list of Authors, and the other ("BooksComponent") filters the literary works of the author selected in the first component.

`[imagen omitida: wiki id 31908]`

As both components have no communication with each other, the best way to trigger the refresh of the Component B's grid is to use *Global Events*.

**1.** Open the [GlobalEvents external object](https://wiki.genexus.com/commwiki/wiki?31169) and add an event called "SelectAuthor". Consider adding the necessary parameters there.

`[imagen omitida: wiki id 31977]`

**2.** In the "AuthorsComponent", the "SelectAuthor" Global Event is called when the user activates a line of the grid.

```
"AuthorsComponent" code:
Event grid1.OnLineActivate
    GlobalEvents.SelectAuthor(AuthorId)
Endevent
```

**3.** In "BooksComponent", define the "SelectAuthor" Global Event. It receives the &authorId as a parameter and calls the grid refresh. &authorId is a variable present on the screen in this case.

```
"BooksComponent" code
Event GlobalEvents.SelectAuthor(&authorId)
    grid1.Refresh()
Endevent
```

This is a specific example, but any combination of the localization of the components in the form is possible. The parent object of all the components can also define or invoke a Global Event.

**Note**: In this scheme, there are N web components that can publish an event, and M web components which are subscribers to the events.

Then, another web component could subscribe to the "SelectAuthor" *Global Event*. For example, a component that shows the author's biography.

`[imagen omitida: wiki id 55669]`

To try it yourself, download the sample [Web Global Events sample for books](https://wiki.genexus.com/commwiki/wiki?31980,,).

### [Restrictions](#Restrictions)

* If a web component which defines a *Global Event* ispresent more than once on the screen, the Global Event is called only once (only for one instance of the web components and not for all of them).
* Global Events can only be called from objects with UI (web panels and web transactions). In [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) rules, they have to be called inside the [Web] section. Eg:

  ```
  Web Trn rules:
  [ web ] 
  {
  GlobalEvents.TotalWorksEvent(-1) 
      if delete on aftercomplete;

  GlobalEvents.TotalWorksEvent(1) 
      if insert on aftercomplete;
  }
  ```

**Notes:** (1)The traditional problem of web components communication.

The traditional ways to communicate between web components (solution without Global Events), are:

1. Executing a [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579)  
   In general, web sessions are used to pass information to other web components, and the web session is read in a Refresh event.  
   However, the WebComponent.Refresh command can be executed for the child components of a given component, not for parents or siblings.  
   Besides, the [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069) executes a full refresh of the screen, and in the majority of the cases, this is not desired.
2. Calling the Web Component, passing it the necessary parameters (WebComponent.create command).  
   A Web Component can be created as a child, you cannot create parent or sibling components.

In sum, sibling components, cannot communicate with each other, and one web component cannot communicate with its parent or grandparents.


|  |
| --- |
| **Backlinks** |
| [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) |

---
