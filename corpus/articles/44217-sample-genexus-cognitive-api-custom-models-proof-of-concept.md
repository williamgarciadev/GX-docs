---
title: "Sample: GeneXus Cognitive API Custom-Models proof of concept"
source_id: 44217
source_url: https://wiki.genexus.com/commwiki/wiki?44217
genexus_version: "18"
---

# Sample: GeneXus Cognitive API Custom-Models proof of concept

This article refers to the proof of concept made during the [GeneXus Meeting #29 conference](https://meetings.genexus.com/2019/session/genexusai-past-present-y-future/ENG) about GeneXusAI.

## [Sample download](#Sample+download)

`[imagen omitida: wiki id 40856]` [Sample - GeneXusAI PoC - Custom Model](https://wiki.genexus.com/commwiki/wiki?44218,,).

**Note**: It is highly important to install GeneXusAI built-in module **before importing** the *GeneXusAI\_Custom\_Model\_Sample.xpz* file into your Knowledge Base.

## [GeneXusAI built-in module installation](#GeneXusAI+built-in+module+installation)

1. Go to Knowledge Base option from the GeneXus Toolbar.  
2. Click on [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172).  
3. Look for GeneXusAI module on the displayed list.  
4. Click on the "Install" button.

You could see the installation process on the 'General' option of the output section. Once installed, you can import the *GeneXusAI\_Sample.xpz* file using the [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179).

## [Sample content](#Sample+content)

The Knowledge Base includes:

* **gxai procedure**  
  A command-line procedure that implements a utility for training a custom model, predict an output based on a new (unseen) input and delete the model.
* **GenerateDataset**  
  A procedure to generate the dataset by scanning the content of a directory.

## [Runtime execution](#Runtime+execution)

The application is a simple command-line tool for training a custom model and predict based on it by using with GeneXusAI. For sampling purposes, we had used a subsample of [Flowers dataset](https://www.kaggle.com/alxmamaev/flowers-recognition) (you can download here: [FlowersDatasetSubsample.zip](https://wiki.genexus.com/commwiki/wiki?44296,,)).

|  |  |
| --- | --- |
|  | **agxai -help**  Displays a message explaining how to use the command-line utility.   The command has three option:  > *help*: Display the message  > *train*: For training a custom model  > *predict*: For predicting an output based on a new (unseen) input.  > *delete*: For deleting a custom model previously created/trained. |
|  | **agxai train -name "{your\_model\_name}" - dataset {dataset\_dir} -provider {provider\_file}**  Creates a new custom model, starts the training process and check for the status until it is ready (or aborted). |
|  | **agxai predict -model {model\_id} -data {input\_file} -provider {provider\_file}**  Given a new input (image) returns a prediction label for the custom model previously trained. |
| - | **agxai delete -model {model\_id} -provider {provider\_file}**  Deletes a custom model previously trained. |

**Note**: Before you call **agxai** **tool** by the command-line, ensure you are positioned in the directory containing it or you had set such directory on your Path environment variable.

## [See also](#See+also)

* [GeneXusAI: Past, Present and Future, GX #28, Proof of concept video](https://youtu.be/U1OjVVbSZ0E?t=8227).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) |

---
