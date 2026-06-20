---
title: "State persistence of Grids"
source_id: 46491
source_url: https://wiki.genexus.com/commwiki/wiki?46491
genexus_version: "18"
---

# State persistence of Grids

This article explains different mechanisms to persist information related to the state of a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) or [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) (included in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864), or [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348)).

State information such as pagination position, filtering, and sorting can be read, changed, and handled automatically.

Several properties and methods allow this at runtime or design time.

### [Design time configuration](#Design+time+configuration)

The [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) allows, at design time, enabling or disabling automatic state saving and loading.

### [Runtime programming state persistence](#Runtime+programming+state+persistence)

The following methods and properties can be used in Events and/or Subroutines of a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864), and [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348):

#### [**LoadSessionState method**](#LoadSessionState+method)

This method allows loading the Grid's state from the session, programmatically.

**Note**: Variables that are the input for the Grid's orders are only loaded if they are not empty.

#### [**SaveSessionState method**](#SaveSessionState+method)

This method allows saving the Grid's state to the session, programmatically.

What is saved:

* Editable Variables that are the input for the Grid's conditions and are also in the layout (eg.: &ClientId).
* Variables that are the input for the Grid's orders (eg.: &OrderedBy).

#### [**State property**](#State+property)

You can set the Grid's State property at runtime and get its values.

Its data type is based on the GeneXus.Common.GridState [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).

You may use the Grid's **State** property to persist the state somewhere else; for example, to store it in the database, associated with your application user's preferences.

The automatic assignment of the User Interface's state to the State property (and vice versa) depends on the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017).

## [Samples](#Samples)

### [Sample 1: Automation vs Flexibility](#Sample+1%3A+Automation+vs+Flexibility)

The following three cases are equivalent:

A) Set the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) to True.

B) Set the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) to False and write the following in the Events section of the object:

```
Event Start
    //some other lines of code
    Grid.LoadSessionState()
EndEvent

Event Refresh
    Grid.SaveSessionState()
    // some other lines of code
EndEvent
```

**Note**: This is actually what the [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) writes by default.

C) Set the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) to False and write the following in the Events section of the object:

```
Event Start
    // some other lines of code 
    Do 'LoadGridState'
EndEvent

Event Refresh
    Do 'SaveGridState'
    // some lines of code 
EndEvent

/*** Subroutines used to load and save the Grid state. ***/

Sub 'LoadGridState'
    If (&HTTPRequest.Method = HttpMethod.Get)
        // Load grid state from session.
        &GridState.FromXml(&Session.Get(&PgmName + !"GridState"))  //&GridState is a variable based on the GridState predefined SDT

        If &GridState.InputValues.Count >= 1
            &ClientName.FromString(&GridState.InputValues.Item(1).Value)
        Endif

        If &GridState.CurrentPage > 0
            &GridPageCount = Grid.PageCount
            If (&GridPageCount > 0 and &GridPageCount < &GridState.CurrentPage)
                Grid.CurrentPage = &GridPageCount
            Else 
                Grid.CurrentPage = &GridState.CurrentPage
            Endif            
        Endif
    Endif    
EndSub

Sub 'SaveGridState'
    &GridState.FromXml(&Session.Get(&PgmName + !"GridState"))  //&GridState is a variable based on the GridState predefined SDT

    // Save grid state in session.
    &GridState.CurrentPage = Grid.CurrentPage
    &GridState.InputValues.Clear()   //InputValues collection is cleaned.
    &InputValuesItem = new()         //&InputValuesItem is a variable based on the GridState.InputValues.InputValuesItem data type
    &InputValuesItem.Value = &ClientName.ToString()
    &GridState.InputValues.Add(&InputValuesItem)

    &Session.Set(&PgmName + !"GridState", &GridState.ToXml())
EndSub
```

**Note**: This is actually what the [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) wrote by default in [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,) or prior.

### [Sample 2: Persisting the Grid's state in the Database](#Sample+2%3A+Persisting+the+Grid%27s+state+in+the+Database)

You can persist the state of the Grid to places like the database or the cache, and load it from there afterward, using the Grid's State property.

The following two samples are equivalent:

A) Set the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) to False and write the following in the Events section of the object:

```
Event Start
    //some other lines of code
    Grid1.State = GridStateFromBD(&pgmname, !"Grid1") //Updates session and internal state
    Grid1.LoadSessionState() //Updates user interface
EndEvent
```

```
Event Refresh
    Grid1.SaveSessionState() //Reads user interface and updates session and internal state
    GridStateToDB(&pgmname, !"Grid1", Grid1.State) //Saves internal state to database
    //some other lines of code
EndEvent
```

B) Set the [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) to True and write the following in the Events section of the object:

```
Event Start
    //some other lines of code
    Grid1.State = GridStateFromBD(&pgmname, !"Grid1") //Updates session and internal state
EndEvent
```

```
Event Refresh
   GridStateToDB(&pgmname, !"Grid1", Grid1.State) //Saves internal state to database
   //some other lines of code
EndEvent
```


|  |
| --- |
| **Backlinks** |
|
| [Save State property](https://wiki.genexus.com/commwiki/wiki?46017) |

---
