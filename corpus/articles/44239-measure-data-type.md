---
title: "Measure data type"
source_id: 44239
source_url: https://wiki.genexus.com/commwiki/wiki?44239
genexus_version: "18"
---

# Measure data type

Represents the main metric for evaluating a model in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Score**: [Score, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40190)
* **Additional** (collection) -- Additional metrics
  + ***Key***: VarChar(32)
  + ***Value***: Numeric (10.5)
* **Local**: Boolean

## [Description](#Description)

The Score field is the main metric based on your model type (e.g. for a classification model will be the F1-measure). The Additional field displays a set of additional measures that can help you to decide if your model meets your requirements. The following subsections describe some of these additional fields when metrics are locally calculated by GeneXusAI and their semantic.

### [Confusion Matrix key](#Confusion+Matrix+key)

The Confusion Matrix information is displayed in the Additional field as follows:

|  |  |
| --- | --- |
| Key | = ConfusionMatrix[{true-class},{predicted-class}] |
| Value | = {value} |
|  |  |

where {true-class} is the class (or label) defined in the test-data and {predicted-class} is the class (or label) predicted by your trained model. The meaning of this output is that your model predicts {value} times that {true-class} was a {predicted-class}.

For example, if you have 'ConfusionMatrix[DOG,CAT]' key associated with 3 value, it means that your model predicts 3 times that a DOG was a CAT.

### [Macro Measures key](#Macro+Measures+key)

The Macro Measures information is displayed in the Additional field as follows:

|  |  |
| --- | --- |
| Key | = {metric}*@*{threshold} |
| Value | = {value} |
|  |  |

being {metric} one of Accuracy, Precision, Recall or FScore; and {threshold} a numeric value between 000 and 100.The {value} is the macro-measure (average value) of every value defined by {metric} for each category when it exceeds the {threshold} value (otherwise, it counts as 0).

For example, if you have three categories (DOG, CAT, PARROT), the value 0.897 associated with the 'F1Score@80' key means that 0.897 is the average of the F1-Score for DOG, CAT and PARROT which exceeds 80% (or 0.80) threshold.

## [Notes](#Notes)

* Examples of additional metrics.
  + [Precision](https://en.wikipedia.org/wiki/Precision_and_recall#Precision)
  + [Recall](https://en.wikipedia.org/wiki/Precision_and_recall#Recall)
  + [F-Score](https://en.wikipedia.org/wiki/Precision_and_recall#F-measure).
  + [Accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision#In_binary_classification) (for Binary classification)
  + [Intersection-over-Union (IoU)](https://en.wikipedia.org/wiki/Jaccard_index) (for Region identification)
  + [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix).
* When you use a cloud-provider and it does not provide evaluation metrics of your model (e.g. IBM), the *Local field* is set to True and Measure's results were calculated locally. In order to execute a local evaluation your model must be deployed (i.e. [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) must be executed before call this task) because internally it will call to [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) for each test-data in your dataset (available in [Model.Dataset field](https://wiki.genexus.com/commwiki/wiki?44240)).
* The Main Score for an Image Classification problem will be the F1-Score (or the average over all thresholds).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,):  
  - Local evaluation has been added.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |

---
