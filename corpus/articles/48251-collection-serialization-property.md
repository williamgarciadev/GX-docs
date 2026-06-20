---
title: "Collection Serialization property"
source_id: 48251
source_url: https://wiki.genexus.com/commwiki/wiki?48251
genexus_version: "18"
---

# Collection Serialization property

Specifies the way collections are serialized in XML format.

### [Values](#Values)

|  |  |
| --- | --- |
| **Sequence** | Serializes as a plain sequence of collection elements. |
| **Wrapped** | Includes the collection start/end tag. This is the default value. |

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

 A collection of Cities inside the Country [Structured Data Type object](https://wiki.genexus.com/commwiki/wiki?10021) could be serialized as follows:

* Wrapped:

  ```
  <Country>
           <Cities>
               <CityName>City1</CityName>
               <CityName>City2</CityName>
              ...
           </Cities>
   </Country>
  ```

* Sequence:

  ```
    <Country>
       <CityName>City1</CityName>
       <CityName>City2</CityName>
       ...
    </Country>
  ```
