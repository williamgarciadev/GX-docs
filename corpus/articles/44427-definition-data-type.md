---
title: "Definition data type"
source_id: 44427
source_url: https://wiki.genexus.com/commwiki/wiki?44427
genexus_version: "18"
---

# Definition data type

Represents the complete definition of a model in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Name**: VarChar(64) -- Model's name
* **Dataset**(structure)
  + **Loader**: ObjectName, GeneXus -- Fully qualified object name that generates training data samples.
  + **Option** (Structure)
    - **Batch**: Numeric(4.0) -- Describes how many elements will be processed time by time.
    - **Size**: (structure) -- Proportion reservation in range [0,1].
      * **Training**: Numeric(5.3)
      * **Testing**: Numeric(5.3)
    - **Seed**: Numeric(4.0) -- Useful when you want to repeat an experiment (same random splitting).
* **Input** (structure)
  + **Features** (collection) -- Defines every data input by name and type (i.e. every column names/types).
    - **Feature** (structure)
      * **Name**: VarChar(64) -- Optional feature's name (e.g. "PET PHOTO").
      * **Type**: [DataInputType, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44423)
* **Output** (structure)
  + **Type**: [DataOutputType, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44424)

## [Notes](#Notes)

* Dataset.Loader field must be set with the fully-qualified name of your dataset 'generator' object (Procedure or Data Provider).
* Features' field count in the Input field must be equal to every [Data.Input Features' field](https://wiki.genexus.com/commwiki/wiki?44237) count of your data-set.
* Features' field in [Definition.Input](https://wiki.genexus.com/commwiki/wiki?44427) and [Data.Input](https://wiki.genexus.com/commwiki/wiki?44237) must be correlative in order to describe the name and type of every feature of your data item (i.e. the k-th element of Data.Input.Feature should have the Type of the k-th element of Definition.Input.Feature).
* If Data.Input.Features field has more items than Definition.Input.Features field, remain items in Data.Input.Features will be ignored.
* If Data.Input.Features field has fewer items than Definition.Input.Features, means you have undefined Data.Input.Features and will produce an error.
* When Name field is omitted in Data.Input.Features' item, the column name will be the Type field name, enumerated in order of appearance (e.g. "MEDIA\_1"). In order to data summary being human readable, it is recommended to do not omit the Name field.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [DataInput data type](https://wiki.genexus.com/commwiki/wiki?44425) | [DataOutput data type](https://wiki.genexus.com/commwiki/wiki?44426) | [Definition data type](https://wiki.genexus.com/commwiki/wiki?44427) |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |

---
