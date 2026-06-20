---
title: "Page variable"
source_id: 8103
source_url: https://wiki.genexus.com/commwiki/wiki?8103
genexus_version: "18"
---

# Page variable

Stores the current page number. It is useful when the Procedure object prints information. The page count starts at 1 and GeneXus automatically manages this variable value by adding 1 to it every time the page advances. If another starting value is required, the value of &Page can be changed.

**Data Type:**  
Numeric (6)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Sample](#Sample)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Customer
{
  CustomerId*
  CustomerName
  CustomerDateOfBirth
  CustomerEmail
  CustomerPhone
}
```

Suppose you need to implement a PDF report that lists all the customers' names, dates of birth, emails, and phone numbers.

This listing may have several pages. Therefore, each page must show the current page number and the total number of pages, as follows:

`[imagen omitida: wiki id 59626]`

To do so, follow these steps:

1. [Create](https://wiki.genexus.com/commwiki/wiki?9931) a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293).

2. Configure the Procedure properties, as shown below:

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP
* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to file

3. Go to the Rules tab and write:

```
Output_File("CustomersPDF","PDF");
```

4. Go to the [Layout](https://wiki.genexus.com/commwiki/wiki?5468) tab. You will see one predefined [Printblock control](https://wiki.genexus.com/commwiki/wiki?1958) (named "printBlock1"). Edit the Printblock's **Name property** and set it to "CustomerInfo".

5. Insert the Customer attributes you want to list inside that Printblock:

`[imagen omitida: wiki id 59624]`

6. Create a new Printblock control. To do so, right-click on the "CustomerInfo" Printblock and select **Insert Printblock** in the contextual menu.

7. Edit the **Name property** of the newly insertedPrintblock and set it to "CurrentPage".

8. In the "CurrentPage" Printblock, insert the &Page variable. Also, insert a **Textblock control** and edit its **Text property** to {{Pages}}:

`[imagen omitida: wiki id 59625]`

9. Finally, in the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) define the following code:

```
For each Customer
   Print CustomerInfo   
endfor
Footer
   Print CurrentPage
End
```

That's all! You can now run the listing and view the &Page variable and {{Pages}} template.

### [See Also](#See+Also)

[Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386)


|  |
| --- |
| **Backlinks** |
| [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
