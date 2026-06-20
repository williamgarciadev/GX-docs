---
title: "GetMessageText function"
source_id: 21782
source_url: https://wiki.genexus.com/commwiki/wiki?21782
genexus_version: "18"
---

# GetMessageText function

Looks for a given text in the [Language object](https://wiki.genexus.com/commwiki/wiki?7258) sent as a parameter (or in the current active Language object if that parameter is omitted) and returns the corresponding translated text.

### [Syntax](#Syntax)

**GetMessageText(***MessageCode*, [*LanguageObjectName*] **)**

**Where:**  
  
*MessageCode*  
    Is the text for which you want to find its translation.

*LanguageObjectName*  
    Is the name of the Language object in which you want to look for a translation.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Sample](#Sample)

Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) whose default language is English ([Kb Language property](https://wiki.genexus.com/commwiki/wiki?7671) = 'English').

Set your Environment [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) to 'Static'.

Select the Spanish [Language object](https://wiki.genexus.com/commwiki/wiki?7258) in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) below the Localization node:

`[imagen omitida: wiki id 58527]`

Set the Environment [Translate to language property](https://wiki.genexus.com/commwiki/wiki?13242) to 'Spanish'.

Create a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that contains a Text Block control in its Web Layout with its Caption = "Hello World".

Define the Web Panel Start event as follows:

```
Event Start
   Textblock1.Caption = GetMessageText('Hello World', 'Spanish')
Endevent
```

Build the Web Panel (select 'Build With This Only' from the Web Panel contextual menu).

After this action, open the Spanish [Language object](https://wiki.genexus.com/commwiki/wiki?7258).

Note that the "Hello World" text is added (as a Code). Enter the corresponding Localized text (in this case, "Hola Mundo"):

`[imagen omitida: wiki id 58529]`

Press F5 and when executing the Web Panel, the Text Block Caption is translated as shown below:

`[imagen omitida: wiki id 58530]`

**Note**: No errors are returned by this function. If the *MessageCode* is not found in the current Language, the *MessageCode* is returned. It is, therefore, a good design method to use full text message codes that can be used as message texts.

### [Run-time translation considerations](#Run-time+translation+considerations)

Make sure to place an exclamation mark (!) in the GetMessageText function for both parameters when the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) is set to Run-time.

```
Textblock1.Caption = GetMessageText(!'Test about the GetMessageText function', !'Spanish')
```

You will need to reference the desired texts in the code too so that the application metadata will include the desired translations. The correct code when using Run-time translation is:

```
&sample = 'Test about the GetMessageText function' // needed so the text is added to the application metadata
Textblock1.Caption = GetMessageText(!'Test about the GetMessageText function', !'Spanish')
```

Note that, at specification time, the GetMessageText function is used so that texts with no exclamation mark appear translated at runtime. This may lead to performance issues because the GetMessageText function cannot be evaluated by the DBMS, or to specification warnings or errors like the following:

```
spc0075 Operand getmessagetext( "M") does not match the data type of &var in the IN comparison. (Events, Line: 2)
```


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) |

---
