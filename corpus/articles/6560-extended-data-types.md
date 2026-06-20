---
title: "Extended data types"
source_id: 6560
source_url: https://wiki.genexus.com/commwiki/wiki?6560
genexus_version: "18"
---

# Extended data types

The way to work with external files, directories, web sessions, [cookies](https://wiki.genexus.com/commwiki/wiki?6322),  mail sessions, etc., is through variables of special Data Types.

By defining a variable of the [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321), you can create a session on the Web Server to maintain global variables. By defining a variable of the [Directory Data Type](https://wiki.genexus.com/commwiki/wiki?6567), you can create, move or delete a directory from your file system. By defining a variable of the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?5967,,), you can read an XML file. And so it goes on.

How can you achieve this? Through **Properties** and **Methods** related to these Data Types (each one will have a set of particular properties and methods, according to the subject it represents).

#### Example

Consider a site where the user must authenticate through a username and a password that are previously recorded in the database (a WebUser table exists to that end). We want to recover the user in every page visited, showing his or her name, and, for example, only their preferences.  Because of that, a [websession](https://wiki.genexus.com/commwiki/wiki?6321) variable is needed to get the user in every page. Suppose that a 'Home' web panel is created for login purposes, with the input variables &User and &Password put on the form (to get those values from the user). We will define a webSession variable (&session) on the 'Home'  web panel to set the user's name, that later could be get from every other page visited.

Therefore, in the event associated to the login (for example: Enter) we can do the following:

```
For each
    Where WebUserName = &User
    Where WebUserPsw = &Password
          &Session.Set(“Name”, WebUserName)
          Call (HWelcome)
    When none
          ... //Not valid user
Endfor
```

See how the **&Session** variable let's you define a "Name" global variable on the Server, and set it with the WebUserName -through the **Set method** of the variable.

Then, in the Start event of any other object, we can get that value for the user, through the **Get method**:

```
&UserName = &Session.Get( "Name" )
```

 As you can see, we have created a variable of the WebSession extended data type and handle it through methods. This is just a particular case of the more general one: all extended data types have the same behavior.


|  |
| --- |
| **Pages** |
| [ContentInfo Data Type](https://wiki.genexus.com/commwiki/wiki?7712) | [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) |
| [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) | [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631) | [File data type](https://wiki.genexus.com/commwiki/wiki?6915) |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) |
| [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) | [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |
| [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) | [MailRecipient Data Type](https://wiki.genexus.com/commwiki/wiki?6926) | [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) |
| [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) | [Property Data Type](https://wiki.genexus.com/commwiki/wiki?6888) | [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913) |
| [QueueMessage Data Type](https://wiki.genexus.com/commwiki/wiki?6914) | [Regular Expressions (RegEx)](https://wiki.genexus.com/commwiki/wiki?4606) | [SearchResult Data Type](https://wiki.genexus.com/commwiki/wiki?7726) |
| [SearchResultItem Data Type](https://wiki.genexus.com/commwiki/wiki?7729) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) | [StringCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6954,StringCollection+Data+Type,) |
| [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) | [WebWrapper data type](https://wiki.genexus.com/commwiki/wiki?6624) | [Window Data Type](https://wiki.genexus.com/commwiki/wiki?7112) |
| [WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,WordDocument+Data+Type,) | [WSAddressing Data Type](https://wiki.genexus.com/commwiki/wiki?44549) | [WSSecurity Data Type](https://wiki.genexus.com/commwiki/wiki?44552) |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
