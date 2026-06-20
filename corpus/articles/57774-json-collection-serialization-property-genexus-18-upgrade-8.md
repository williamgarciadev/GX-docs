---
title: "Json Collection Serialization property (GeneXus 18 Upgrade 8 or prior)"
source_id: 57774
source_url: https://wiki.genexus.com/commwiki/wiki?57774
genexus_version: "18"
---

# Json Collection Serialization property (GeneXus 18 Upgrade 8 or prior)

Specifies the way collections are serialized in Json format.

### [Values](#Values)

|  |  |
| --- | --- |
| **Sequence** | Serializes as a plain sequence of collection elements. |
| **Wrapped** | Includes the collection name item. This is the default value. |

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** SDT level node

### [Description](#Description)

The JSON Collection Serialization property is available in the SDT node which has been defined as a collection by clicking on the Is Collection checkbox.

`[imagen omitida: wiki id 57755]`

**Note**: This property is taken into account only when the [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) is a parameter of an [API object](https://wiki.genexus.com/commwiki/wiki?46151). It is not taken into account in [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270) exposed as REST.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

Suppose you have defined an SDT called Countries, as shown in the image above.

Next, you define a Procedure object called CountryList as follows:

Variables:

```
Countries     (Type:Countries)
country       (Type:Countries.Country)
```

Rules:

```
Parm(out:&Countries);
```

Source

```
&country = new()
&country.CountryName = "UY"
&Countries.Country.Add(&country)

&country = new()
&country.CountryName = "BR"
&Countries.Country.Add(&country)
```

And then you define in the Service Source of the API object the following:

```
Countries{
    [RestVerb(GET)]
    ListCountries(out:&Countries) => ListCountries(&Countries);
    }
```

When executing by pressing F5, you will be able to display one of the following, depending on the value set in the J**son Collection Serialization property**:

* Wrapped:

  ```
   {
    "Countries": [
      {
        "CountryName": "UY"
      },
      {
        "CountryName": "BR"
      }
    ]
  }
  ```

* Sequence:

  ```
  [
    {
      "CountryName": "UY"
    },
    {
      "CountryName": "BR"
    }
  ]
  ```

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

[Procedures as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?21467)  
[Data Providers as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28216)
