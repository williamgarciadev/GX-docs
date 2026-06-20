---
title: "Business Component ToXml method"
source_id: 23483
source_url: https://wiki.genexus.com/commwiki/wiki?23483
genexus_version: "18"
---

# Business Component ToXml method

Converts the data stored in a variable into an XML structure with a Tag for each [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) attribute. For each Transaction attribute, a Tag\_Z will be created with its old value.

### [Syntax](#Syntax)

**&***VarStr* = **&***VarBasedOnBC*.**ToXml()**

****Where:****

*****&******varStr*  
     Is a variable defined in a GeneXus object based on the character data type.

*****&******varBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

### [**Samples**](#Samples)

Suppose you define the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Customer
{
  CustomerId*     (Autonumber property = True)
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerEmail
  CustomerAddedDate
}
```

Customer rule:

```
Default(CustomerAddedDate,&today);
```

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object.

Thus, in any [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) you can define a variable named &Customer based on the Customer type.

The objective of the Web Panel is to allow the user to enter a customer Id value. Then, by pressing a button, the Event associated with the button will load in memory (in the &Customer Business Component variable) the customer data stored in the database associated with the customer id entered by the user. Next, the ToXml method will be applied to the &Customer variable, to convert the customer data to an XML format and it will be shown in the [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132).

To achieve this, you will also have to define these variables in the Web Panel:

```
&CustomerId: Based on the CustomerId attribute
&xml: Character(200)
```

and design the Web Panel screen like this:

`[imagen omitida: wiki id 23613]`

The following code is associated with the Web Panel button:

```
Event 'ToXml'
   &Customer.Load(&CustomerId)
   &xml=&Customer.ToXml()
Endevent
```

In run-time, suppose you enter the value: 1 in the &CustomerId variable and then press the button. The customer data is loaded in the &Customer variable and converted to XML format, as the following image shows:

<Customer xmlns=“knowledgeBase”>  
    <CustomerId>1</CustomerId>  
    <CustomerName>Jack Smith </CustomerName>  
    <CustomerAddress>2300 East Avenue </CustomerAddress>  
    <CustomerPhone>12103110700 </CustomerPhone>  
    <CustomerEmail>jsmith@gmail.com</CustomerEmail>  
    <CustomerAddedDate>2020-02-04</CustomerAddedDate>  
    <Mode>UPD</Mode>  
    <Initialized>0</Initialized>  
    <CustomerId\_Z>1</CustomerId\_Z>  
    <CustomerName\_Z> Jack Smith </CustomerName\_Z>  
    <CustomerAddress\_Z>2300 East Avenue </CustomerAddress\_Z>  
    <CustomerPhone\_Z>12103110700 </CustomerPhone\_Z>  
    <CustomerEmail\_Z>jsmith@gmail.com</CustomerEmail\_Z>  
    <CustomerAddedDate\_Z>2020-02-04</CustomerAddedDate\_Z>  
</Customer>

### [See Also](#See+Also)

[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component FromXml method](https://wiki.genexus.com/commwiki/wiki?23633) |

---
