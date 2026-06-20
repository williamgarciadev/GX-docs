---
title: "GeneXus Cognitive API - Evaluate procedure"
source_id: 44244
source_url: https://wiki.genexus.com/commwiki/wiki?44244
genexus_version: "18"
---

# GeneXus Cognitive API - Evaluate procedure

Evaluates a custom model behavior (i.e. 'how well' it makes new predictions).

## [Parameters](#Parameters)

* **in**:&model :: [Model, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44240)  
  The model information to be evaluated.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Measure :: [Measure data type](https://wiki.genexus.com/commwiki/wiki?44239)  
  Measure obtained before the evaluation.

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

After training your model with [Mamaevs' Flowers Recognition dataset](https://www.kaggle.com/alxmamaev/flowers-recognition), the table below shows the evaluation made for each provider and the time it takes for processing it.

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Amazon** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Baidu** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Google** | ``` {     "Score": 1,     "Additional": [         {             "Key": "auPrc",             "Value": 1         },         {             "Key": "auRoc",             "Value": 0         },         {             "Key": "F1Score@000",             "Value": 0.922         },         {             "Key": "Precision@000",             "Value": 0.915         },         {             "Key": "Recall@000",             "Value": 0.918         },         ...         {             "Key": "ConfusionMatrix[DAISY,DAISY]",             "Value": 1         },         ...         {             "Key": "ConfusionMatrix[ROSE,ROSE]",             "Value": 1         }     ],     "Local": false } ``` | 1299ms |
| **IBM** | ``` {     "Score": 0.823,     "Additional": [         {             "Key": "ConfusionMatrix[TULIP,TULIP]",             "Value": 10         },         ...         {             "Key": "ConfusionMatrix[ROSE,TULIP]",             "Value": 2         },         ...         {             "Key": "Precision@000",             "Value": 0.922         },         {             "Key": "Recall@000",             "Value": 0.915         },         {             "Key": "FScore@000",             "Value": 0.918         },         ...         {              "Key": "Precision@100",              "Value": 0.4         },         {             "Key": "Recall@100",             "Value": 0.4         },         {             "Key": "Precision@100",             "Value": 0.4         }     ],     "Local": True } ``` | 156ms |
| **Microsoft** | ``` {     "Score": 0.999,     "Additional": [         {             "Key": "Precision",             "Value": 1.000         },         {             "Key": "PrecisionSdtDeviation",             "Value": 0.000         },         {             "Key": "Recall",             "Value": 0.998         },         {             "Key": "RecallSdtDeviation",             "Value": 0.000         },         {             "Key": "AveragePrecision",             "Value": 1.000         },         {             "Key": "AverageRecall",             "Value": 0,998         }     ],     "Local": False } ``` | 215ms |
| **SAP** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Tencent** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |

## [Notes](#Notes)

* When you get higher score values you may fall in the [Overffiting problem](https://en.wikipedia.org/wiki/Overfitting).
* When you have [Precision](https://en.wikipedia.org/wiki/Precision_and_recall#Precision) and [Recall](https://en.wikipedia.org/wiki/Precision_and_recall#Recall) measures in the Additional field, the main score (Score field) will be the [F1-Measure](https://en.wikipedia.org/wiki/Precision_and_recall#F-measure).
* In case your cloud-provider does not give information about the evaluation (e.g. IBM), this task locally calculates some [standard metrics](https://wiki.genexus.com/commwiki/wiki?44239) once your model has been deployed. In this scenario, the [Measure.Local field](https://wiki.genexus.com/commwiki/wiki?44239) is set to True. Despite the fact that it does not require any credentials for making the calculations, you need to indicate the access credentials for checking the deployed status (i.e. [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242)) and for predicting every test-data on your dataset (i.e. [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245)) in order to compare the true-value with the predicted-value. Also, the Evaluation task must know which model has to use (Id/Version fields), which type of model are you evaluating (Type field) because the metrics depend on it, and where is the dataset information (Dataset field with the csv file path) because the task needs to know which are the testing-data. So, your [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) input must be fully set.
* When the evaluation is locally performed and you had enabled log level in Debug mode, GeneXusAI will log the confusion matrix, outcomes, metrics and macros. For example:

  ```
  Matrix    | TULIP | SUNFLOWER | DANDELION | ROSE | DAISY
  ----------+-------+-----------+-----------+------+-------
  TULIP     |    10 |         0 |         0 |    0 |     0
  SUNFLOWER |     0 |         8 |         1 |    0 |     0
  DANDELION |     0 |         1 |         8 |    0 |     0
  ROSE      |     2 |         0 |         0 |    8 |     0
  DAISY     |     0 |         0 |         0 |    0 |     9

  Outcomes | TULIP | SUNFLOWER | DANDELION | ROSE | DAISY
  ---------+-------+-----------+-----------+------+-------
  TP       |    10 |         8 |         8 |    8 |     9
  TN       |    35 |        37 |        37 |   37 |    38
  FP       |     2 |         1 |         1 |    0 |     0
  FN       |     0 |         1 |         1 |    2 |     0
  POP      |    47 |        47 |        47 |   47 |    47
  P        |    10 |         9 |         9 |   10 |     9
  N        |    37 |        38 |        38 |   37 |    38
  TOP      |    12 |         9 |         9 |    8 |     9
  TON      |    35 |        38 |        38 |   39 |    38

  Metrics | TULIP | SUNFLOWER | DANDELION |  ROSE | DAISY
  --------+-------+-----------+-----------+-------+-------
  ACC     | 0.957 |     0.957 |     0.957 | 0.957 |     1
  ERR     | 0.043 |     0.043 |     0.043 | 0.043 |     0
  PPV (P) | 0.833 |     0.889 |     0.889 |     1 |     1
  TPR (R) |     1 |     0.889 |     0.889 |   0.8 |     1
  F0.5    | 0.862 |     0.889 |     0.889 | 0.952 |     1
  F1      | 0.909 |     0.889 |     0.889 | 0.889 |     1
  F2      | 0.962 |     0.889 |     0.889 | 0.833 |     1
  J       | 0.833 |       0.8 |       0.8 |   0.8 |     1
  TNR     | 0.946 |     0.974 |     0.974 |     1 |     1
  NPV     |     1 |     0.974 |     0.974 | 0.949 |     1
  AUC     | 0.973 |     0.932 |     0.932 |   0.9 |     1
  MCC     | 0.888 |     0.863 |     0.863 | 0.871 |     1

  Macros  |  MEAN | VARIANCE | STD DEV | STD ERR
  --------+-------+----------+---------+---------
  ACC     | 0.966 |  0.00037 | 0.01924 | 0.00837
  ERR     | 0.034 |  0.00037 | 0.01924 | 0.00837
  PPV (P) | 0.922 |  0.00557 | 0.07463 | 0.03332
  TPR (R) | 0.916 |  0.00726 | 0.08521 | 0.03808
  F0.5    | 0.918 |  0.00317 |  0.0563 |  0.0251
  F1      | 0.915 |  0.00232 | 0.04817 | 0.02145
  F2      | 0.915 |  0.00438 | 0.06618 | 0.02966
  J       | 0.847 |  0.00756 | 0.08695 | 0.03886
  TNR     | 0.979 |  0.00051 | 0.02258 |    0.01
  NPV     | 0.979 |  0.00046 | 0.02145 | 0.00949
  AUC     | 0.947 |  0.00154 | 0.03924 | 0.01761
  MCC     | 0.897 |  0.00342 | 0.05848 | 0.02608
  ```

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,):  
  - Evaluation is made locally when the provider does not give evaluation information.
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)  
  -  Google AutoML is available.

## [See also](#See+also)

* [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246)
* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Measure data type](https://wiki.genexus.com/commwiki/wiki?44239) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |

---
