---
title: "Load command"
source_id: 8196
source_url: https://wiki.genexus.com/commwiki/wiki?8196
genexus_version: "18"
---

# Load command

Forces the loading of a new line into a Grid control.

### [Syntax](#Syntax)

**Load**

### [Scope](#Scope)

**Objects:**[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This command can be used within the [Load event](https://wiki.genexus.com/commwiki/wiki?8188) or within a [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s that contain only one grid. Also, in [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)s.

The Load command can be used in the following scenarios:

* [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s without a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) and with [Base Table](https://wiki.genexus.com/commwiki/wiki?6347)
* [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s without a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) and with [Base Table](https://wiki.genexus.com/commwiki/wiki?6347)
* [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)s

### [Samples](#Samples)

**Example 1:** Web Panel without a base table

Consider the following two [Transactions](https://wiki.genexus.com/commwiki/wiki?1908):

```
Invoice
{
     InvoiceId*
     InvoiceDate
}
```

```
Receipt
{
     ReceiptId*
     ReceiptDate
}
```

Suppose you want to define a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with one grid that shows all the invoices data and all the receipts data, like the following image, shows:

`[imagen omitida: wiki id 39678]`

To solve this need, one option can be to define a Web Panel without a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). The Web Panel must contain a grid that only includes variables. Make sure there are no attributes mentioned in the Web Form, Events (except those included inside [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s), Conditions or Orders. Needless to say, the [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) can't be set in the grid.

Suppose the variables you include in the grid are: &Id, &Date, and &Type. Thus, the Web Panel does not have a Base Table because no attributes are present in any part where GeneXus verifies to determine a Base Table. This means that the Web Panel doesn't have neither automatic navigation nor an automatic grid loading, you have to define the grid loading explicitly.

For every Web Panel (or Panel) without a base table, the Load Event will be triggered only once. Inside this event, you have to define the desired navigation and grid loading explicitly. The following code solves the described need:

```
Event Load
    For each Invoice
           &Id = InvoiceId
           &Date = InvoiceDate
           &Type = "INVOICE"
           Load // Load command
    EndFor
    For each Receipt
           &Id = ReceiptId
           &Date = ReceiptDate
           &Type = "RECEIPT"
           Load // Load command
    EndFor
EndEvent //Load
```

Note that two consecutive For each commands were defined inside the Load Event. The first For each command scans and loads the invoices data in the grid and the second For each command scans and loads the receipts data in the grid, too. As the code shows, inside each [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), the variables are being assigned explicitly with the instantiated attribute values (or fixed values, calculations, etc.). Once the desired values are assigned to the variables when you want to proceed to load a line in the grid with those values, you have to include a Load command. The Load command loads a line in the grid effectively so, if you forget to include it in the correct place in the code, the lines will not be loaded, despite having assigned values to the grid variables, .

**Example 2:** Web Panel with a base table

Now consider only the Invoice [Transaction](https://wiki.genexus.com/commwiki/wiki?1908):

```
Invoice
{
     InvoiceId*
     InvoiceDate
     InvoiceAmount     
}
```

If you define a Web Panel that contains one grid that includes the InvoiceId, InvoiceDate, and InvoiceAmount attributes, GeneXus determines that the Web Panel has Invoice as a Base Table. This means that the Web Panel has an automatic navigation (there is an implicit For each command that scans all the stored invoices) and the grid is automatically loaded with the navigated Invoice data.

By just defining a Web Panel with the following form (and nothing else in any other part of the object):

`[imagen omitida: wiki id 39704]`

you will see the following result in runtime:

`[imagen omitida: wiki id 39706]`

For every Web Panel (or Panel) with a base table with base table, the Load Event will be triggered as many times as records are scanned (three times in the previous example), just before loading each record data in a new grid line.

Probably you do not need to define any code inside the Load event (as in the previous example), but if you need to execute, validate or perform something before loading each line, the appropriate section to define that code is inside the Load event.

Suppose that you want to show for each line a text with the following criteria:

* If the invoice amount < 800, the text to be shown is "Receives a gif voucher"
* If the invoice amount >= 800, the text to be shown is "Receives a discount voucher for the next invoice"

In order to solve the described requirement, first, include a variable named &Text (based on a character data type) inside the grid. Then, as the Load Event is executed immediately prior to the addition of each line to the grid, the necessary code to evaluate the InvoiceAmount value and assign the text to the &Text variable is:

```
Event Load
  If InvoiceAmount < 800
     &Text = "Receives a gif voucher"
  else
     &Text = "Receives a discount voucher for the next invoice"
  endif
Endevent
```

**Important:** Note that there isn't a Load command inside the Load Event code. As the Web Panel has a Base Table (Invoice), the query to the Invoice physical table as well as the loading of the lines in the grid is automatic (and just before the loading of each line, the Load Event is executed; thus, the &Text variable will have the corresponding text just before each line is automatically loaded and the desired text will be displayed).

This command is necessary only when you need to evaluate whether you want to load a line or not, before actually doing it.

Suppose you have to validate several things with a procedure for each navigated invoice. Depending on the procedure's returned value, you need to evaluate whether to load the line into the grid or not. You can do so by applying the following code:

```
Event Load
  &Ok = SeveralValidations(InvoiceId)  //&Ok: Boolean variable
  If &Ok
     Load  
  endif       
Endevent
```

In conclusion, before loading each line you are evaluating a condition. If it is true, you are loading the line. Otherwise, the load will not be performed.

**Note**: This command is the only one allowed for this purpose for mobile applications. The [Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814) is not available in that case.

### [See Also](#See+Also)

[Load event](https://wiki.genexus.com/commwiki/wiki?8188)  
[Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814)


|  |
| --- |
| **Backlinks** |
| [Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814) | [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) |

---
