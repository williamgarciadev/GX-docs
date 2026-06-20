---
title: "GeneXus SDK for SAP Leonardo: Optical Character Recognition (OCR)"
source_id: 41767
source_url: https://wiki.genexus.com/commwiki/wiki?41767
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Optical Character Recognition (OCR)

Optical Character Recognition(OCR) service takes an uploaded file and returns the text characters detected in the input.

## [How to use the OCR API](#How+to+use+the+OCR+API)

The OCR API retrieves the text out of an image. There are two ways to do it :

1. the synchronous way
2. the asynchronous way

**1. Using the synchronous way**

You have to use the PostOcr procedure that you have available after having imported the API:

```
PostOcr
GeneXusSAPLeonardo.OCR.PostOcr(&OCRFile, &options, &Response_ok, &ResponseError, &HttpMessage, &IsSuccess)
```

Where:

* &OCRFile: is the route of the file to be processed.
  + images: jpeg, jpe, png.
  + PDF
* &options: is a JSON that contains the specifications for the file processing.
  + Language: The language of the text submitted separated by commas. A maximum of 3 languages can be set. It can be:
    - en (English) - **Default**
    - de (German)
    - fr (French)
    - es (Spanish)
    - ru (Russian).
  + The output type: The output type of the result. It can be:
    - txt  - **Default**
    - XML
  + The page segmentation mode:
    - 0 - Orientation and script detection (OSD) only
    - 1 - Automatic page segmentation with OSD **(Default)**
    - 3 - Fully automatic page segmentation, but no OSD
    - 4 - Assume a single column of text of variable sizes
    - 5 - Assume a single uniform block of vertically aligned text
    - 6 - Assume a single uniform block of text
    - 7 - Treat the image as a single text line
    - 8 - Treat the image as a single word
    - 9 - Treat the image as a single word in a circle
    - 10 - Treat the image as a single character
    - 11 - Sparse text. Find as much text as possible in no particular order
    - 12 - Sparse text with OSD
    - 13 - Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific
  + The model type: the type of machine learning model for OCR
    - lstmPrecise - precise model with LSTM cells
    - lstmFast - fast model with LSTM cells
    - lstmStandard - standard model with lstm cells **(Default)**
    - noLstm - model without LSTM cells
    - all - model with LSTM cells and standard processing algorithms

```
Example: {"lang": "en", "output_type": "xml", "page_seg_mode": "13", "model_type": "lstmStandard"}
```

* &Response\_ok: is based on the following [SDT](https://wiki.genexus.com/commwiki/wiki?2427) and it is loaded with the result if no errors are found.

  `[imagen omitida: wiki id 41783]`
* &ResponseError: is based on the following [SDT](https://wiki.genexus.com/commwiki/wiki?2427) and it is loaded with an error code, error message, and some details of an error that may occur.

  `[imagen omitida: wiki id 41784]`
* &HttpMessage: is based on the [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335) and it contains information about the request.
* &IsSuccess: is based on a [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) and its value will be True if no errors are found.

**2. Using the asynchronous way**

You have to use the PostOcrJobs and the GetOcrJobs procedures:

```
PostOcrJobs
GeneXusSAPLeonardo.OCR.PostOcrJobs(&OCRFile, &options, &Response_pending, &ResponseError, &HttpMessage, &IsSuccess)
```

Where

* &Response\_pending: is based on the following [SDT](https://wiki.genexus.com/commwiki/wiki?2427) that contains the id and the status of the request that is used to get the result.

`[imagen omitida: wiki id 41785]`

The other variables are based on the same types as the PostOcr procedure ones.

```
GetOcrJobs
GeneXusSAPLeonardo.OCR.GetOcrJobs(&Id, &Response_ok, &ResponseError, &HttpMessage, &IsSuccess)
```

Where

* &Id: is the id retrieved from the PostOcrJobs procedure.

The other variables are based on the same types as the PostOcr procedure ones.

[Read more information about the OCR API](http://api.sap.com/api/ocr_api/resource).


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
