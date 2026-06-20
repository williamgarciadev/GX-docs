---
title: "Dictionary External Object"
source_id: 58246
source_url: https://wiki.genexus.com/commwiki/wiki?58246
genexus_version: "18"
---

# Dictionary External Object

The Dictionary [External Object](https://wiki.genexus.com/commwiki/wiki?5669) provides a way to store and retrieve key-value pairs. It allows you to manage a collection of data where each item is identified by a unique key.

`[imagen omitida: wiki id 58217]`

You can find the Dictionary External Object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the Common module, which in turn is located within the GeneXus module.

## [Types](#Types)

### [KeyType type](#KeyType+type)

The type of the keys used in the dictionary. You can set this type at design time. The default data type is [VarChar](https://wiki.genexus.com/commwiki/wiki?6778)(255), but it can be any of the following data types: [Character](https://wiki.genexus.com/commwiki/wiki?6777), [Date](https://wiki.genexus.com/commwiki/wiki?7373), [Guid](https://wiki.genexus.com/commwiki/wiki?31772), [Boolean](https://wiki.genexus.com/commwiki/wiki?4374), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), [Numeric](https://wiki.genexus.com/commwiki/wiki?6793), or [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221) based on these types.

### [ValueType type](#ValueType+type)

The type of the values stored in the dictionary. You can set this type at design time. The default data type is VarChar(255), but it can be any data type.

## [Properties](#Properties)

### [Values property](#Values+property)

Returns a collection of all values stored in the dictionary. This property is read-only at runtime and contains elements of the type specified by ValueType.

### [Keys property](#Keys+property)

Returns a collection of all keys used in the dictionary. This property is read-only at runtime and contains elements of the type specified by KeyType.

### [Count property](#Count+property)

Returns the number of items stored in the dictionary. This property is read-only at runtime.

## [Methods](#Methods)

### [Set method](#Set+method)

Adds a new key-value pair to the dictionary or updates the value associated with an existing key.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Key: KeyType, Value: ValueType |

### [SetDictionary method](#SetDictionary+method)

Adds or updates multiple key-value pairs from another dictionary.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Dictionary: Dictionary, GeneXus.Common |

### [Remove method](#Remove+method)

Removes the item associated with the specified key from the dictionary.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | Key: KeyType |

### [RemoveKeys method](#RemoveKeys+method)

Removes multiple items from the dictionary based on a collection of keys.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Keys: KeyType (Collection) |

### [RemoveAll method](#RemoveAll+method)

Removes all items from the dictionary based on the keys of another dictionary.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Dictionary: Dictionary, GeneXus.Common |

### [Clear method](#Clear+method)

Removes all items from the dictionary.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [Get method](#Get+method)

Retrieves the value associated with the specified key.

|  |  |
| --- | --- |
| **Return value** | ValueType |
| **Parameters** | Key: KeyType |

### [Contains method](#Contains+method)

Checks if the dictionary contains an item with the specified key.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | Key: KeyType |

### [FromJson method](#FromJson+method)

Parses a JSON string and populates the dictionary with the key-value pairs from the JSON data.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Json: VarChar(255) |

### [ToJson method](#ToJson+method)

Returns a JSON string representation of the dictionary.

|  |  |
| --- | --- |
| **Return value** | VarChar(255) |
| **Parameters** | None |

## [Events](#Events)

The Dictionary External Object does not have any events.

## [Samples](#Samples)

#### [Iterating through dictionary elements](#Iterating+through+dictionary+elements)

This sample shows you how to iterate through all dictionary elements using the [For in command](https://wiki.genexus.com/commwiki/wiki?6359) and the Keys property of the dictionary.

**Step 1: Create the Procedure Object**

You can define a variable of Dictionary type in any GeneXus object; however, a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) is created for this example.

**Step 2: Define the Dictionary type variable**

Create a variable named &MyDictionary of Dictionary type. Set the Key Type property to Varchar and the Value Type property to Numeric.  
`[imagen omitida: wiki id 58247]`

**Step 3: Initialize the Dictionary**

Add some elements to the dictionary:

```
&MyDictionary.Set("Name", 1)
&MyDictionary.Set("Age", 30)
&MyDictionary.Set("City", 2)
```

**Step 4: Iterate Through the Dictionary**

Use the For in command to iterate over the Keys property of the dictionary:

```
for &Key in &MyDictionary.Keys
    &Value = &MyDictionary.Get(&Key)
    msg(&Key.ToString() + ": " + &Value.ToString())
endfor
```

Where &Key is of VarChar type and &Value is of Numeric type.

**Step 5: Execute**

Press F5 to run. The result is as follows:

```
Name:    1
Age:   30
City:    2
```

## [Considerations](#Considerations)

* Converting a Dictionary to or from XML, JSON, or String is only possible if the underlying types have the corresponding functions implemented. If these functions are not available, runtime exceptions will occur. For example, the File data type does not have a ToJson() method. Therefore, if you have a Dictionary with values of File type, you cannot serialize it to JSON.
* You cannot define variables that are collections of dictionaries.
* The [Properties data type](https://wiki.genexus.com/commwiki/wiki?31606) is a special case of a Dictionary where both KeyType and ValueType are of VarChar type. Unlike the Properties Data Type, a member of a [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) can be a Dictionary. This means you can create an SDT that has a field that stores a Dictionary.

  **Example:**

  Suppose you're creating an SDT to represent a customer with the following structure:

  ```
  Customer
      Name: Varchar(40)
      Address: Address, GeneXus
      Preferences: Dictionary<Varchar, Varchar> // This is a Dictionary member
  ```

  In this example, the Preferences member of the Customer SDT is a Dictionary. This allows you to store key-value pairs representing the customer's preferences, as shown below:

  + **Key:** "FavoriteColor" **Value:** "Blue"
  + **Key:** "NewsletterSubscription" **Value:** "Yes"So, while you can't directly use the Properties data type within an SDT, you can use a Dictionary, which gives you more flexibility in storing data within your custom data structures.

## [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular (since v18 u13)](https://wiki.genexus.com/commwiki/wiki?42550)

## [Availability](#Availability)

This External Object is available as of [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

## [See Also](#See+Also)

[Fundamentals of data structures: Dictionaries](https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_1/Fundamentals_of_data_structures/Dictionaries)  
[External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |

---
