---
title: "GeneXus SDK for SAP Leonardo: Similarity Scoring"
source_id: 41791
source_url: https://wiki.genexus.com/commwiki/wiki?41791
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Similarity Scoring

The Similarity Scoring service(API) allows you to compare vectors using a similarity score (cosine distance) ranging from -1 to 1.

## [How to use the Similarity Scoring API](#How+to+use+the+Similarity+Scoring+API)

To use the Similarity Scoring API on GeneXus you have to use the PostInferenceSync procedure:

```
GeneXusSAPLeonardo.SimilarityScoring.PostInferenceSync(&options,&File, &Response, &Messages, &IsSuccess)
```

Where: 

* &options: Options parameters must be in json format. Possible values are: - numSimilarVectors - Required. Number of most similar vectors to return in response
* &File: the file containing the vectors to compare.
  + Archive file: zip, tar, gz, tgz.
  + Vector files in archive file: txt.
  + What a vector file should include: (number, number, number, ..., number)
  + Example: (0.20161056518554688, 1.0347602367401123, ..., 1.5012381076812744)
* &Response
* &Messages:is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess:is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

[Read more about the Similarity Scoring API.](https://api.sap.com/api/similarity_scoring_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
