---
title: "WorkflowApplicationData"
source_id: 7562
source_url: https://wiki.genexus.com/commwiki/wiki?7562
genexus_version: "18"
---

# WorkflowApplicationData

This object allows representing specific application data, associated to a specific process instance.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Name | Character | Read | Name |
| Type | Character | Read | Datatype (Character, Numeric, Date, DateTime) |
| Length | Numeric | Read | Length |
| Value | Character | Read/Write | Value |
| NumericValue\* | Numeric | Read/Write | Numeric Value |
| CharacterValue | Character | Read/Write | Character Value |
| DateValue | Date | Read/Write | Date Value |
| DateTimeValue | DateTime | Read/Write | Date/Time Value |
| Dimension | Numeric(WorkFlowDimension) | Read/Write | It returns value 0 if the relevant data is a scale and 1 if it is an array |
| Count | Numeric | Read | It returns the number of elements in an array of relevant data |
| Error | WorkflowError | Read | Error |

### [Methods](#Methods)

#### [SetValue](#SetValue)

It adds the value indicated in the &value parameter in the position indicated by the &index parameter. The value must be transferred as character string, regardless of the type of relevant data.

#### [SetValue (&index, &value)](#SetValue+%28%26index%2C+%26value%29)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | &index | Numeric | Input | Position where the value will be added |
| 2 | &value | Character | Input | Value to be added |

#### [Add](#Add)

It adds the value indicated in the &value parameter, at the end of the values collection. The value must be transferred as character string, regardless of the type of relevant data.

#### [Add (&value)](#Add+%28%26value%29)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | &value | Character | Input | Value to be added at the end of the collection |

#### [GetValue](#GetValue)

It obtains the value contained in the position indicated by the &index parameter. The value is stored in the &value parameter as a character string.

#### [GetValue (&index): &value](#GetValue+%28%26index%29%3A+%26value)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | &index | Numeric | Input | Position of the value to be obtained |
