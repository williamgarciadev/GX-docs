---
title: "HowTo: Build a custom model for GeneXus Cognitive API"
source_id: 43665
source_url: https://wiki.genexus.com/commwiki/wiki?43665
genexus_version: "18"
---

# HowTo: Build a custom model for GeneXus Cognitive API

This article explains how you can create your own custom model and integrate it into your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

**Warning**: Custom models are available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,) only for **image classification problem**. However, the process described in this document is more general, and it is applicable to any **prediction problem** (e.g. predict the price of a house in term of the features it has). GeneXusAI will cover more scenarios in future updates.

### [Introduction](#Introduction)

When you create an Artificial Intelligence model you are 'teaching' your computer to make predictions based on the experience. In this context, *experience* means to be *historical data* from which your computer can infer patterns in order to make inferences over new (unseen) data with a certain confidence. The learning process involves two main steps: Training (see data and learn) and Testing (how well the model behaves).

**Note**: Custom models can't make inferences that humans can't. Thus, if a person cannot be trained to assign tags for a certain input (audio, image, text, video, etc.), don't expect a computer to do it (nor better).

The complete cycle for creating and using a custom model is described in [Image 1](https://wiki.genexus.com/commwiki/wiki?43665).

|  |
| --- |
|  |
| [**Image 1**: Artificial Intelligence flowchart](#Image+1%3A+Artificial+Intelligence+flowchart) |

First, you must **acquire tagged data** for training your model. Sometimes, it may be helpful to split your dataset in two: training-set (80%) and test-set (20%) as it is shown in [Image 2](https://wiki.genexus.com/commwiki/wiki?43665). Either way, if you don't do it, the provider automatically splits your dataset.

|  |
| --- |
|  |
| [**Image 2**: Dataset containing training, validation and test sets.](#Image+2%3A+Dataset+containing+training%2C+validation+and+test+sets.) |

Then, you must **train and test your model** until you are satisfied with how well your model behaves (see [Evaluation importance section](https://wiki.genexus.com/commwiki/wiki?43665)). Once you consider you achieve a good score, you are able to deploy it.

Finally, with your deployed model, you will be able to **input new data and get a prediction** for it (also, you can delete your model or retrain it if you wish).

### [Building process](#Building+process)

#### [**1.** Acquire and tag your data](#1.+Acquire+and+tag+your+data)

You must:

1. Get data for achieving your aim (e.g. images of dogs/cats).
2. Choose your output classes (e.g. 'dog' and 'cat').
3. Start tagging your data (e.g. "image1.jpg > dog", "image2.png > cat", etc.).

After this step, you will get your **training dataset**.

**Notes: Tips and good practices**

1. Training data should be as similar as possible to the data on which predictions will be made.
2. Provide at least 10 samples per class you want to predict (1000 samples per class are recommended) including, at least, 1 for testing and 1 for validation.
3. Avoid low-frequent classes (join them in a general class or discard them).
4. Include a "NONE" tag as a miscellaneous category to improve your model behavior

#### [**2.** Create your custom model](#2.+Create+your+custom+model)

You must:

1. Train your model from your input dataset (asynchronously, may take a long time).
2. Test your model in order to decide if it behaves as you expect or not.
3. Deploy your model in order to use it.

You can do these three steps in two ways:

**A) By using your provider's back-office**

1. Go to your [provider's back-office](https://wiki.genexus.com/commwiki/wiki?43665).
2. Upload your dataset following their requirements.
3. Start your training (and go for a coffee).
4. Once trained, look for evaluation metrics.
5. If you are satisfied, deploy your model.
6. Get model identifier, version, and credentials to be able to use it.

**B) By using an SDK (Standard Development Kit)**

1. Use GeneXusAI.Custom module (or an official SDK) for training, testing and deployment processes.
2. Get model identifier, version, and credentials to be able to use it.

If you are going to use the alternative (B) with GeneXusAI.Custom module, you can take the following code as an implementation example for the flowchart described in the [Image 1](https://wiki.genexus.com/commwiki/wiki?43665) (details about how can you load &definition variable can be found in [this sample](https://wiki.genexus.com/commwiki/wiki?44246)).

```
// trigger training process
&model = GeneXusAI.Custom.Train(&definition, &provider, &Messages)

// check for the progress
do while True
    &ret = sleep(60) // wait 1 min until re-poll
    &state = GeneXusAI.Custom.Check(&model,&provider,&Messages)
    if &state <> GeneXusAI.Custom.State.Training OR &Messages.Count > 0
        exit // break the loop
    endIf
endDo

// evaluate your model
&Measure = GeneXusAI.Custom.Evaluate(&model, &provider, &Messages)
if &Measure.Score < 0.85 // threshold
    return
endIf

// deploy your model
GeneXusAI.Custom.Deploy(&model, &provider, &Messages)
```

After this step, you will get a reference to your **custom model**.

**Notes: Tips and good practices**

1. Always evaluate your model before deploying it.
2. If your model predicts unexpected values, recheck your training data.
3. Higher precision does not guarantee you good predictions. Your model may fall over the *[overfitting problem](https://en.wikipedia.org/wiki/Overfitting)*

#### [**3.** Use your custom model](#3.+Use+your+custom+model)

You must:

1. Load your provider with your model properties (identifier, version, and/or credential).
2. Call to the appropriate GeneXusAI's task.  
   e.g. if you train your model for image classification, call to [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) or, if you train your model using GeneXusAI.Custom module, you can call to [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245).
3. Start making predictions over new data.

As simple as that!

### [Evaluation importance](#Evaluation+importance)

Imagine you want to train a classifier that distinguishes between two classes:

* **Positive** (P)
* **Negative** (N)

Ideally, you want your classifier to predict exactly the real value (i.e., predict P when it really was a P, analogous for N). This idea is shown in [Image 3a](https://wiki.genexus.com/commwiki/wiki?43665). But, as you are training a model from biased data (data from the real world), sometimes it may fail. So, your real classifier will be 'deviated' from the classifier you expect (exemplified in the [Image 3b](https://wiki.genexus.com/commwiki/wiki?43665)).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | |  |  | | [**(a)** Ideal classifier with two classes](#%28a%29+Ideal+classifier+with+two+classes) | [**(b)** Real classifier with outcomes](#%28b%29+Real+classifier+with+outcomes) | |
| [**Image 3**: ideal vs real classifier](#Image+3%3A+ideal+vs+real+classifier) |

Take into account that this 'deviation' is not a bad thing, since your model will be used for predicting values from new data (unseen during the training). Otherwise, you may fall into the well-known *[overfitting problem](https://en.wikipedia.org/wiki/Overfitting)*. The fact that matters is 'how much' your model is 'deviated' from your expectation.

So, when you evaluate a model, you will get four outcomes:

* **True Positives** (TP)   
  How many positive values were correctly classified as positive.
* **True Negatives** (TN)  
  How many negative values were correctly classified as negative.
* **False Positive** (FP)  
  How many negative values were misclassified as positive.
* **False Negative** (FN)  
  How many positive values were misclassified as negative.

These values determine what we know as a [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix), and from it you will be able to perform calculations that allow you to decide how well your model behaves. For instance, the most used metrics are calulated as follows:

* **Accuracy** (ACC)

  |  |  |
  | --- | --- |
  | ACC = | TP + TN |
  | TP + TN + FP + FN |
* **Precision** (P)

  |  |  |
  | --- | --- |
  | P = | TP |
  | TP +  FP |
* **Recall** (R)

  |  |  |
  | --- | --- |
  | R = | TP |
  | TP +  FN |
* **F1-Score** (F1, armonic mean of precision and recall)

  |  |  |
  | --- | --- |
  | F1 = | 2 · P · R |
  | P  +  R |

This same idea can be generalized to a multiclass classifier. So, don't be strict, a 100% accuracy does not guarantee that your model behaves correctly when classifies new data (data that it has never seen before).

### [Provider back-office](#Provider+back-office)

The following table tells you where can you find the online training website for each supported provider.

|  |  |  |
| --- | --- | --- |
| **Provider** | **Online training** | **Documentation** |
| **Google** | [AutoML Vision UI](https://cloud.google.com/automl/ui/vision) | [Read](https://cloud.google.com/vision/automl/docs/how-to) |
| **Microsoft** | [Custom Vision AI](https://www.customvision.ai/projects?mostRecentDirectory) | [Read](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier) |
|  |  |  |

**Note**: Google provider does not work with .NET Core Generator.

### [Availability](#Availability)

Since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [DataInputType domain](https://wiki.genexus.com/commwiki/wiki?44423) | [DataOutputType domain](https://wiki.genexus.com/commwiki/wiki?44424) |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) | [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) |
| [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |
| [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665) |
| [Purpose domain](https://wiki.genexus.com/commwiki/wiki?44234) | [State domain](https://wiki.genexus.com/commwiki/wiki?44235) |

---
