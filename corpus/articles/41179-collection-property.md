---
title: "Collection property"
source_id: 41179
source_url: https://wiki.genexus.com/commwiki/wiki?41179
genexus_version: "18"
---

# Collection property

Indicates whether the output returned by the Data Provider has multiple instances.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

Suppose you define a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) and drag that SDT to a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) source. The [Output property](https://wiki.genexus.com/commwiki/wiki?41037) of the Data Provider is then automatically set to the name of the SDT. This means the Data Provider will return a loaded structure whose data type is based on that SDT, and you must receive the output (where you invoke the Data Provider) in a variable of the same type.

If the SDT is not a collection, but your goal in the Data Provider is to load and return a collection of that data type, you can set the Data Provider's **Collection property** to True. Then, in the Data Provider source, you proceed to load multiple instances. Finally, the last step is to receive the result returned by the Data Provider (at the point where it is invoked) in a variable based on the SDT, which must be defined as a collection.

In conclusion, this property allows you to configure the Data Provider to load and return multiple instances of the SDT definition without modifying the original SDT.

The same applies to a [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) that is a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846). You can drag this type of object to a Data Provider source, and the [Output property](https://wiki.genexus.com/commwiki/wiki?41037) of the Data Provider is automatically set to the name of the Business Component. However, if your objective is to load and return a collection of that data type, you must set the Data Provider **Collection property** to True.

Unlike the case of the SDT, where there is another alternative solution (defining the SDT as collection and dragging it to the Data Provider source, so that the [Output](https://wiki.genexus.com/commwiki/wiki?41037) already is a collection), the only way to load and return multiple instances of a Business Component type using a Data Provider is by setting its Collection property to True.

In the context of the previous example, where the Data Provider source returns multiple instances of a Business Component type, ensure that the result is assigned to a variable based on the Business Component and defined as a collection at the point where the Data Provider is invoked. Finally, it's important to note that [the object calling the Data Provider](https://wiki.genexus.com/commwiki/wiki?5310) must handle the result returned by the Data Provider and execute the [Insert method](https://wiki.genexus.com/commwiki/wiki?31695) or the [InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) to perform the insertion(s) into the database.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

**1) Samples of a Data Provider object that loads and returns an SDT collection**

Consider the following Transaction:

```
Customer
{
   CustomerId*
   CustomerName
}
```

Below are two ways to load a collection of customers using a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270).

**1.1)** Suppose you define the following [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021), which is not a collection:

`[imagen omitida: wiki id 41210]`

Then, you create a DataProvider (DPCustomersList) and drag the SDT to its source:

`[imagen omitida: wiki id 41213]`

If your objective is to load all registered customers, you can modify the Data Provider source and properties as shown:

`[imagen omitida: wiki id 41214]`

Note that a [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) (Customer) was mentioned to specify the navigation intent. Also, in this particular case, since the SDT property names match the attribute names, it is not necessary to write the assignments explicitly.

To configure the Data Provider to return multiple instances, set its **Collection property** to True, as shown. As a result, the [Collection Name property](https://wiki.genexus.com/commwiki/wiki?41229) is automatically added and completed by default with a name for the returned collection (which you can modify).

**1.2)** Now, suppose you define the following [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021), which is a collection:

`[imagen omitida: wiki id 41225]`

Then, you create a DataProvider (DPCustomersList2) and drag the SDT to its source:

`[imagen omitida: wiki id 41226]`

Note that the [Output property](https://wiki.genexus.com/commwiki/wiki?41037) of the Data Provider is automatically set to the name of the SDT. This means the Data Provider will return a loaded structure whose data type is based on that SDT. Since you will be loading and returning a collection, you do not need to change the **Collection property**.

You only need to complete the source, and no more steps are required.

`[imagen omitida: wiki id 41228]`

**2) Sample of a Data Provider object that loads and returns a Business Component collection**

See sample #4 described in the [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695) article.


|  |
| --- |
| **Backlinks** |
| [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Collection Name property](https://wiki.genexus.com/commwiki/wiki?41229) | [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) |
| [Output property](https://wiki.genexus.com/commwiki/wiki?41037) |

---
