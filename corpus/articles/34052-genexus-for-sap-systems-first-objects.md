---
title: "GeneXus for SAP Systems - First Objects"
source_id: 34052
source_url: https://wiki.genexus.com/commwiki/wiki?34052
genexus_version: "18"
---

# GeneXus for SAP Systems - First Objects

Once the [Knowledge Base has been created](https://wiki.genexus.com/commwiki/wiki?34041) and [the Fiori resources were initialized](https://wiki.genexus.com/commwiki/wiki?54721), the next step is to describe the objects of reality using [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866).

[Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s allow you to describe the entities and associated attributes of the application in a declarative manner, using database tables in [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713) automatically created by GeneXus. Transaction objects also create responsive web forms (pages) to insert, update and delete records. The default web forms created by Transaction objects can be customized.

### [Use case](#Use+case)

It is desired to have a travel agency application, which shows: recommended tourist attractions, countries and cities where they offer tours.

To achieve this, the following entities (reality actors) will be defined in the Travel Agency Knowledge Base, using Transaction objects:

* Customers
* Tours attractions
* Countries
* Cities

All entities have attributes that provide detailed information about the entity. For example, a customer has attributes: first name, last name, email address, and phone number.

For each entity, you will have to create a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

To create a new object, go to Toolbar and select **File > New > Object.**

Once you select the option to create a new object, you can choose the type of object that will be created from the dialog box.

Select Data Management in the categories section of the dialog box and select the Transaction object type.  Name it “Customer” and click on the ‘Create’ button.

When a Transaction object is created, the Structure section is open by default:

`[imagen omitida: wiki id 53036]`

In the Transaction object Structure, you have to specify the name and data type of each attribute of the Transaction.

A customer has attributes such as first name, last name, phone, email, and address.

```
Customer
{
   CustomerId*
   CustomerName
   CustomerLastName
   CustomerAddress
   CustomerPhone
   CustomerEmail
}
```

Note that the first line is already created to enter the first attribute.

In every Transaction object, an attribute or set of attributes must be able to uniquely identify each record. In other words, one cannot enter two customers with the same identifier value. For this reason, a key icon that distinguishes the identifier attribute from other attributes is associated with the first line.

Customer’s passport number or ID card numbers could be candidates for identifier roles. Since the application is not required to store passport number or ID card number, you can create an attribute called "CustomerId". You can configure the identifier attribute to automatically increment in steps of 1 for every record added to the Transaction by setting the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) of the attribute to True.

If you press the “dot” key on the keyboard, GeneXus automatically shows the Transaction name as a prefix in the attribute name field.

`[imagen omitida: wiki id 53037]`

You only have to type "Id" after the "Customer" prefix.

`[imagen omitida: wiki id 53038]`

After entering the name of the attribute, press the Tab key and choose the data type.

`[imagen omitida: wiki id 53039]`

Clicking on the arrow displays the data types available in GeneXus. For this attribute, leave the default data type: Numeric of 4 digits (with no decimals).

Press ENTER and start creating the second attribute.

A new line will open.

The second attribute to be entered is ‘CustomerName’.

`[imagen omitida: wiki id 53040]`

Once again, type “.” and complete the attribute name by typing “Name”.

`[imagen omitida: wiki id 53041]`

In the data type section for the CustomerName attribute, type ‘Character’.

Note that if you type an opening bracket, the default length is 20 characters; you can leave it unchanged.

Follow the same steps to enter the ‘CustomerLastName’ attribute, which will also be of Character type, length 20.

Now, add the CustomerAddress attribute. In this case, the data type ‘Address’ was automatically assigned. GeneXus realized that you want to create an attribute whose name partially matches the name of the existing data type ‘Address’.

`[imagen omitida: wiki id 53042]`

Continue with ‘CustomerPhone’. GeneXus will automatically assign it the data type ‘Phone’.

Lastly, enter the ‘CustomerEmail’ Attribute, which is automatically assigned the Email data type by GeneXus. In particular, the data types Address, Phone and Email are special data types called semantic domains. [Semantic Domains](https://wiki.genexus.com/commwiki/wiki?17227) include features that are specific to an address, a phone number, or an email address, respectively.

`[imagen omitida: wiki id 53043]`

Note that an asterisk is being displayed in the Customer Transaction tab.

This means that the Transaction is being edited. When you save the changes, the asterisk will disappear, and the Transaction object will be displayed in the KB Explorer window. Click on File > Save or press Ctrl + S to save the Transaction.

`[imagen omitida: wiki id 53047]`

Select the “Web Layout” section.

`[imagen omitida: wiki id 53045]`

For web applications, GeneXus automatically designs responsive Web Forms according to the defined structure. This form allows users to add, change and delete customers.

Form Preview shows you how the web form will look at runtime according to the screen size. To open the Form Preview window, click on **View > Other Tool Windows > Form Preview**.

`[imagen omitida: wiki id 53046]`

Note that the Form Preview window shows the screen size for the preview in the footer of the window.

GeneXus supports the following screen size categories.

1. Large size devices that have width more than 1200px
2. Medium size devices that have width more than 992 px but less than 1200 px.
3. Small size devices that have width more than 768 px but less than 992 px.
4. Extra small size devices that have width less than 768 px

`[imagen omitida: wiki id 53048]`

You can change the size of the preview by enlarging or reducing the size of the Form Preview window.

When you change the screen size, the controls will be adapted to show the data according to that size.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) | [GeneXus for SAP Systems - First Build and Run](https://wiki.genexus.com/commwiki/wiki?34179) | [GeneXus for SAP Systems First Build and Run (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54669) |

---
