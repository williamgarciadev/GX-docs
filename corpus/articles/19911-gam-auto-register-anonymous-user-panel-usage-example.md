---
title: "GAM - Auto-register anonymous user - Panel usage example"
source_id: 19911
source_url: https://wiki.genexus.com/commwiki/wiki?19911
genexus_version: "18"
---

# GAM - Auto-register anonymous user - Panel usage example

This example describes the use of [Auto - register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) for developing an application for the users of a library.

Its main functionalities include: showing books, novels, etc. by different criteria (date published, author, etc.), keeping a record of lists of favorites, read or to be read, receiving different notifications and buying books. The idea is also to obtain information on the user profiles for informing statistics referred, among other things, to reading habits, preferences, etc.

Since applications that require a registry as the first step necessary are usually rejected, it was decided that the design would allow for all its functionalities to be totally anonymous (without registries) to the extent possible. Users must register only when it is absolutely necessary (such as in the case of purchases made).

The design guideline "anonymous user to the largest extent possible" implies a number of technical challenges. How could non-registered users subscribe to "monthly news", for example? Or What or who is to be considered the subscriber?

The following example is based on the fact that the application will have, whenever necessary, access to a [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) user identifier. The use of Auto-register anonymous user will guarantee this possibility.

### [Developing the solution](#Developing+the+solution)

Consider a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (in this case called "Subscriptions") like the one shown below, that allows the possibility of relating a user to a book for which there is an interest in receiving news, reviews, etc.

`[imagen omitida: wiki id 55407]`

Note that the user is identified in the Transaction object with the GAMUserGUID attribute of the GAM[GUID data type](https://wiki.genexus.com/commwiki/wiki?31772).

Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) with its [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set to True, where different Action Items are defined to call each object in the application.  
Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) where the user can select preferences, called "SubscribeNovel" containing a Grid, which is loaded through the call to a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270). What should be pointed out in the example is that a 'subscribe' event is invoked for each line selected from the grid, which calls a [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) to perform the subscription (the entry in the table associated with the previously mentioned Transaction).

`[imagen omitida: wiki id 55408]`

The "SubscribeNovel" Panel object is invoked from the application’s main menu (Menu1 object) shown below:

`[imagen omitida: wiki id 55409]`

Note that the value of [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) in the Menu object is True, to accept the access of "anonymous" users to the various options in the Menu and the objects in the call tree of such options.  
Likewise, the Menu includes a login option in case the user decides to perform actions that will require a non-anonymous user.

When the auto-registered user accesses the "SubscribeNovel" option, a record is created for that user in the GAM’s user table, with an assigned [GUID](https://wiki.genexus.com/commwiki/wiki?21842).  
The book preferences selection made by the "anonymous" user in the "SubscribeNovel" Panel will be recorded in the "Subscriptions" table under the GUID assigned to the anonymous user.  
Upon registering in the GAM ([GAM Registration](https://wiki.genexus.com/commwiki/wiki?19913,,)), the user applies the same GUID of the anonymous user for the registered user, so the information entered by the previous one will be the same for this one.

To put it in other words, in the case of a Panel with query regarding the subscriptions of the logged-in user, the preferences declared by the anonymous user prior to registration will be the ones shown for the user registered.

See below how to view the user subscriptions.

Suppose that you have a Panel object called "MySubscriptions" like the one below, which loads on a Grid the subscriptions of the user logged in.

`[imagen omitida: wiki id 55410]`

Note that the Grid has a Data Selector object called "Authorized" in the Data Selector property. That Data Selector contains a condition for filtering only the logged-in users (see image below):

`[imagen omitida: wiki id 55411]`

```
GAMUserGUID = GetUser()
```

where GAMUserGUID is one of the Grid’s columns (the objective is to filter by that attribute).  
GetUser is a Procedure that returns the [GUID](https://wiki.genexus.com/commwiki/wiki?21842) of the user logged in:

```
&GamuserGUID = GAMUser.GetId()
```

`[imagen omitida: wiki id 55412]`

### [Note](#Note)

There are different ways for identifying the user that is logged in (see [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534)). Considering that users may access anonymously, the most appropriate way is to obtain their GUID.


|  |
| --- |
| **Backlinks** |
| [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) | [GAM - Auto-register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) |
| [GAM - Auto-register anonymous users - How to identify them](https://wiki.genexus.com/commwiki/wiki?19910) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
