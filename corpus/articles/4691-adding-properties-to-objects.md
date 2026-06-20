---
title: "Adding Properties to Objects"
source_id: 4691
source_url: https://wiki.genexus.com/commwiki/wiki?4691
genexus_version: "18"
---

# Adding Properties to Objects

Many classes in GeneXus' object model use a powerful and extensible way of defining custom properties. The most notable examples include classes like Model, KBObject (Transaction, Web Panel, Procedure, etc.), and controls in many of the visual editors. Any of these classes can be extended making them incorporate additional properties.

### [Goal](#Goal)

Suppose that you want the Transactions in the KnowledgeBase to be subject to some kind of inspection. This might be a process executed by a person or automatically, but the point is that you will want to keep track of whether each particular object was already inspected (a bool property), and what the result of the inspection was (say, a numeric value). This tutorial will show you how to do that with just a few lines of code.

### [Implementation](#Implementation)

The AbstractPackage class that serves as base for every package class includes a method that you can use when you want to extend an object type with one or more properties of your own. This method has the following signature:

```
public bool AddPropertiesDefinition(string type, PropertiesDefinition definition)
```

The first parameter (type) is the key used to refer to the collection of properties' definitions for a particular kind of object. The key for Transactions is "TRN", for Procedures is "PRC", and so on, but you'd better not trust that. Rather than hard-coding those strings into your code, the proper way to obtain the keys you need is through the DefinitionsHelper class:

```
using Artech.Common.Properties;

...

  string transactionKey = DefinitionsHelper.GetPropertiesDefinitionKey<Transaction>();
```

Once you have the key, you can add your own PropertiesDefinition as follows:

```
  public class MyPackage : AbstractPackage

{

...

private void SomeMethod()

{

string transactionKey = DefinitionsHelper.GetPropertiesDefinitionKey<Transaction>();

PropertiesDefinition myDefinitions = CreateMyPropertiesDefinition(transactionKey);

AddPropertiesDefinition(transactionKey, myDefinitions);

}

private PropertiesDefinition CreateMyPropertiesDefinition()

{

// TODO: create and return an instance of PropertiesDefinition

}

}
```

But then of course, you'll need to create your properties definition, that is, put some code inside the CreateMyPropertiesDefinition() method.

There are many ways in which you can achieve this. PropertiesDefinition, as its name implies, is a collection of definitions for properties. The most basic constructor for this class receives what it's called an objectClass, which is no other than the properties definition key discussed above; you already know how to obtain that. There are also constructors that take an XmlDocument or a file name from which to populate the collection of definitions, but these constructors are intended for more advanced uses, and thus will not be discussed here. In any case, as long as you want to add only a few properties, it's easier to do it as we'll show here.

After creating your PropertiesDefinition object, you can simply add the definition for each of the properties with which you want to extend the object, namely "Inspected" and "InspectionResult". The method used for this, not surprisingly, is called AddDefinition and it's fairly easy to use.

```
private PropertiesDefinition CreateMyPropertiesDefinition(string objectClass)

{

PropertiesDefinition myProperties = new PropertiesDefinition(objectClass);

myProperties.AddDefinition("Inspected", typeof(bool), false, null);

myProperties.AddDefinition("InspectionResult", typeof(int), 0, null);

return myProperties;

}
```

As you can see in the code fragment above, the first two parameters in these calls to AddDefinition are the name and type of the property, while the next parameter is a default value. There is also a fourth parameter named "attributes" for which we simply passed null in this example. This parameter is an array not of GeneXus attributes but rather of objects of the [System.Attribute](http://msdn2.microsoft.com/en-us/library/system.attribute.aspx) class in the .NET Framework. Examples of the attributes you may want to use are [System.ComponentModel.ReadOnlyAttribute](http://msdn2.microsoft.com/en-us/library/system.componentmodel.readonlyattribute.aspx) and [System.ComponentModel.BrowsableAttribute](http://msdn2.microsoft.com/en-us/library/system.componentmodel.browsableattribute.aspx), which will display the property as read-only in the Properties window or hide it entirely, respectively.

### [Sample](#Sample)

```
public class MyPackage: AbstractPackage

   {
      public override string Name
      {
         get { return "MyPackage"; }
      }
      public override void PostInitialize()
      {
          base.PostInitialize();
          AddMyProperties();
      }
      private void AddMyProperties()
      {
          string transactionKey = DefinitionsHelper.GetPropertiesDefinitionKey<Transaction>();
          PropertiesDefinition myDefinitions = CreateMyPropertiesDefinition(transactionKey);
          AddPropertiesDefinition(transactionKey, myDefinitions);
      }
      private PropertiesDefinition CreateMyPropertiesDefinition(string objectClass)
      {
          PropertiesDefinition myProperties = new PropertiesDefinition(objectClass);
          myProperties.AddDefinition("Inspected", typeof(bool), false, null);
          myProperties.AddDefinition("InspectionResult", typeof(int), 0, null);
          return myProperties;
      }
```

### [Advanced Use of Properties](#Advanced+Use+of+Properties)

There are many more powerful and interesting ways in which you can configure your properties, but they fall beyond the scope of this introductory article. Just so you can have a taste, let's simply mention that you might specify custom editors, and your own way to display the values. Or that you might use "resolvers" to dynamically calculate the default value, or whether a property should become read-only, or be hidden. There's even the possibility of declaring properties and their behavior rules in a powerful declarative language, which once compiled, allows you to control all of this. In a sense, the support for custom properties in GeneXus X is a platform in itself!
