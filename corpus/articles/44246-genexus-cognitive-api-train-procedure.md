---
title: "GeneXus Cognitive API - Train procedure"
source_id: 44246
source_url: https://wiki.genexus.com/commwiki/wiki?44246
genexus_version: "18"
---

# GeneXus Cognitive API - Train procedure

Creates and starts training a custom model from a given dataset.

## [Parameters](#Parameters)

* **in**:&definition :: [Definition, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44427)  
  The definition of your custom model.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Model :: [Model data type](https://wiki.genexus.com/commwiki/wiki?44240)  
  Model information.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |
| --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Key** |
| **Alibaba** | - |
| **Amazon** | - |
| **Baidu** | - |
| **Google** | Service Account JSON |
| **IBM** | Visual Recognition Key |
| **Microsoft** | Custom Vision Training Key |
| **SAP** | - |
| **Tencent** | - |

## [Sample](#Sample)

Suppose you want to create a model to classify different types of flowers.

First, you must get your tagged data. In this case, we will use the [Mamaevs' Flowers Recognition dataset](https://www.kaggle.com/alxmamaev/flowers-recognition).

Then, you must provide a GeneXus' 'generator' object that must satisfy two conditions:  
1) Returns a collection of [Data data type](https://wiki.genexus.com/commwiki/wiki?44237).  
2) Allows pagination through two input parameters: page number and page size.

In this context, you have two alternatives:

1. Use a Data Provider  
   e.g. if you load the dataset in a Transaction object, you can create a Data Provider object using [Skip/Count clauses](https://wiki.genexus.com/commwiki/wiki?25410).

   ```
   Properties:
     Output = Data
     Collection = True

   Rules:
     parm(in:&pageNum, in:&pageSize);

   Variables:
     &pageSize: Numeric(4.0)
     &pageNum: Numeric(4.0)
     &inputMediaBlob: Blob
     &outputCategory: VarChar(40)

   Source:
     DataCollection [COUNT = &pageSize] [SKIP = (&pageNum - 1) * &pageSize]
     { 
         Dummy [NoOutput]
         {
             // get dataset involved attributes
             &inputMediaBlob = TransactionImage 
             &outputCaregory = TransactionCategory.ToString() 
             
             // load item
             Data
             {
                 Input
                 {
                    Features
                    {
                         Value = &inputMediaBlob
                    }
                 }
                 Output
                 {
                    Label = &outputCaregory
                 }
             }
         }
   ​​​​​  }
   ```
2. Use a Procedure  
   e.g. if you have your dataset in a directory and every image follows the format '{category}\_{index}.png', you can scan the directory with the following Procedure object.

   ```
   Rules:
     parm(in:&pageNum, in:&pageSize, out:&DataCollection);

   Variables:
     &pageSize: Numeric(4.0) 
     &pageNum: Numeric(4.0)
     &i: Numeric(4.0)
     &BTM: Numeric(4.0)
     &TOP: Numeric(4.0)
     &directory: Directory
     &file: File
     &mediaFilePath: VarChar(512)
     &mediaCategory: VarChar(32)
     &data: Data, GeneXusAI.Custom
     &DataCollection: Data, GeneXusAI.Custom (collection)

   Source:
     &i = 0
     &BTM = (&pageNum - 1) * &pageSize + 1
     &TOP = &pageSize * &pageNum
     &directory.Source = !"{path}/dataset" 

     // look for every image in directory
     for &file in &directory.GetFiles()
        &i += 1
        do case

           case &i > &TOP // exclude upper index in range [&BTM,&TOP]
              exit 

           case &i < &BTM // exclude lower index in range [&BTM,&TOP]
              // skip

           otherwise
             
             // get dataset involved values
             &mediaFilePath = &file.GetAbsoluteName()
             &mediaCategory = &file.GetName()
                 .ReplaceRegEx(!"_\d+\.png$",!"") // e.g. "cat1_0001.png" --> "cat1"
             
             // load item
             &data = new()
             &data.Input.Featrues.Add(&mediaFilePath)
             &data.Output.Label = &mediaCategory
             &DataCollection.Add(&data)

        endCase
     endFor
   ```

Finally, you can define your model and start the training process as follows:

```
&definition = new()

// define model name
&definition.Name = !"Flowers model"

// define model dataset (link to generator object previously defined)
&definition.Dataset.Loader = link(MyGeneratorObject)

// define model input
&feature = new()
&feature.Name = !"IMAGE"
&feature.Type = DataInputType.Media
&definition.Input.Features.Add(&feature)

// define model output
&definition.Output.Type = DataOutputType.Label

// call train process
&Model = GeneXusAI.Custom.Train(&definition, &provider, &Messages)
```

**Note**: Don not forget to include at least **10 samples** per class: 8 for  training, 1 for testing and 1 for validation.  
In case you don't have enaugh samples on your dataset, it is most probably you do not satisfy the mentioned conditions. You can use the Purpose field of [Data data type](https://wiki.genexus.com/commwiki/wiki?44237) to achieve this aim when you code your generator object.

## [Requirments](#Requirments)

### [Google provider](#Google+provider)

1. Your *service-account.json* file must be accessible from the web app in case you set the Provider's Key property with its file path.
2. You must install [OpenSSL command-line tool](https://www.openssl.org/).  
   Check the successful installation by typing the following command in the command-line interface.  
   > openssl version  
   Do not forget to add the directory containing the *openssl.exe* to your PATH environment variable in case you are working on Windows OS.
3. You must set the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) to '*Google Cloud Storage*' and set [the associated properties](https://wiki.genexus.com/commwiki/wiki?31121) according to your *service-account.json* file. Ensure your bucket region is '*us-central1*'; otherwise, you must create it and recreate your *service-account.json* file.

## [Notes](#Notes)

* This process executes silently (in the provider's server). You can poll the training status by calling the [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242).
* The training process time may vary depending on your input dataset.
* It is highly important your 'generator' object follows these two rules:  
  1) Returns a collection of [Data data type](https://wiki.genexus.com/commwiki/wiki?44237).  
  2) Allows pagination through two input parameters: page number and page size.  
  Also, your 'generator' object must be reachable from your main object because it will be [dynamically called](https://wiki.genexus.com/commwiki/wiki?8260) from GeneXusAI.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)  
  -  Google Auto ML is available.

## [See also](#See+also)

* [Data data type](https://wiki.genexus.com/commwiki/wiki?44237)
* [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242)
* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Data data type](https://wiki.genexus.com/commwiki/wiki?44237) | [Definition data type](https://wiki.genexus.com/commwiki/wiki?44427) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) |
| [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |
| [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |

---
