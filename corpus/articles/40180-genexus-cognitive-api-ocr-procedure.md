---
title: "GeneXus Cognitive API - OCR procedure"
source_id: 40180
source_url: https://wiki.genexus.com/commwiki/wiki?40180
genexus_version: "18"
---

# GeneXus Cognitive API - OCR procedure

Extracts text from an image. The acronym OCR means 'Optical Character Recognition'.

## [Parameters](#Parameters)

* **in**:&image :: [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)  
  An image to extract text.
* **in**:&language :: [Language, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40453)  
  The language of the text to be recognized.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputRegions:: [OutputRegion, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40194)  
  A set of labels with their confidence describing the image's scenario.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | ***Id*** | ***Key*** | ***SecretKey*** |
| **Alibaba** | - | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Rekognition | Rekognition |
| **Baidu** | 视觉技术 | 视觉技术 | 视觉技术 |
| **Google** | - | Cloud Vision API | - |
| **IBM** | - | Visual Recognition  (deprecated, dark-beta) | - |
| **Microsoft** | - | Computer Vision | - |
| **MLKit** | ML Kit API | ML Kit API | - |
| **SAP** | - | Sandbox Environment  (Deprecated) | - |
| **Tencent** | 通用OCR | 通用OCR | - |

## [Sample](#Sample)

Taking the following image input, the table below shows the text are identified for each provider (as a JSON structure) and the time it takes for processing it.

|  |
| --- |
|  |

|  |  |  |  |
| --- | --- | --- | --- |
| **Provider** | **Output** |  | **Benchmark** |
| **Alibaba** | ``` [{ 	"label": "LevI'S", 	"confidence": 0.999, 	"top": 651, 	"left": 424, 	"width": 128, 	"height": 40 }] ``` |  | 3156ms |
| **Amazon** | ``` [{     "label": "LEVI'S",     "confidence": 0.977,     "top": 668,     "left": 428,     "width": 127,     "height": 31 }] ``` |  | 13531ms |
| **Baidu** | ``` [{ 	"label": "evIs", 	"confidence": 1, 	"top": 664, 	"left": 453, 	"width": 108, 	"height": 30, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\":453,\"y\":664},{\"x\":476,\"y\":664}, 				 ...,{\"x\":453,\"y\":669}]" // 16 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": "[{\"x\":453,\"y\":664},{\"x\":559,\"y\":664}, 				 {\"x\":559,\"y\":692},{\"x\":453,\"y\":692}]" 	}] }] ``` |  | 4335ms |
| **Google** | ``` [{     "label": "Levi'S",     "confidence": 1,     "top": 821,     "left": 535,     "width": 139,     "height": 40,     "Info": [{             "property": "Language",             "value": "en"         }     ] }] ``` |  | 8305ms |
| **IBM** | ``` [{     "label": "vrs",     "confidence": 0.697,     "top": 241,     "left": 153,     "width": 8,     "height": 25,     "Info": [{         "property": "line_number",         "value": "0.00000"     }] }, {     "label": "le",     "confidence": 0.668,     "top": 247,     "left": 162,     "width": 35,     "height": 14,     "Info": [{         "property": "line_number",         "value": "0.00000"     }] }] ``` |  | 9251ms |
| **Microsoft** | ``` [{     "label": "Levrs",     "confidence": 0.0,     "top": 823,     "left": 538,     "width": 147,     "height": 36,     "Info": [{         "property": "Angle",         "value": "0.00000"     }, {         "property": "Language",         "value": "tr"     }, {         "property": "Orientation",         "value": "Up"     }] }] ``` |  | 8496ms |
| **MLKit** | ``` [{     "label": "Levrs",     "confidence": 1,     "top": 806,     "left": 516,     "width": 200,     "height": 75 }] ``` |  | 978ms |
| **SAP** | ``` [{     "label": "Levis",     "confidence": 0.955528974533081,     "top": 820,     "left": 534,     "width": 156,     "height": 39 }] ``` |  | 8595ms |
| **Tencent** | ``` [{     "label": "LeVi's",     "confidence": 0.795,     "top": 668,     "left": 436,     "width": 121,     "height": 28 }] ``` |  | 7582ms |

Another example, when the input image has clean text (reduced noise).

|  |
| --- |
|  |

|  |  |  |  |
| --- | --- | --- | --- |
| **Provider** | **Output** |  | **Benchmark** |
| **Alibaba** | ``` [{ 	"label": "GeneXus", 	"confidence": 0.999, 	"top": 52, 	"left": 20, 	"width": 63, 	"height": 24 }, { 	"label": "LEGACY", 	"confidence": 0.999, 	"top": 70, 	"left": 355, 	"width": 107, 	"height": 25 }, { 	"label": "MODERNIZATION", 	"confidence": 0.999, 	"top": 103, 	"left": 356, 	"width": 230, 	"height": 25 }, { 	"label": "WITH GENEXUSTM15", 	"confidence": 0.999, 	"top": 138, 	"left": 357, 	"width": 204, 	"height": 22 }, { 	"label": "DOWNLOAD THE EBOOK!", 	"confidence": 0.999, 	"top": 228, 	"left": 378, 	"width": 149, 	"height": 14 }] ``` |  | 4171ms |
| **Amazon** | ``` [{     "label": "LEGACY",     "confidence": 0.999,     "top": 103,     "left": 546,     "width": 161,     "height": 41 }, {     "label": "MODERNIZATION",     "confidence": 0.999,     "top": 158,     "left": 550,     "width": 340,     "height": 38 }, {     "label": "WITH",     "confidence": 0.999,     "top": 211,     "left": 546,     "width": 86,     "height": 31 }, {     "label": "15",     "confidence": 0.998,     "top": 211,     "left": 821,     "width": 42,     "height": 35 }, {     "label": "EBOOK!",     "confidence": 0.997,     "top": 350,     "left": 736,     "width": 77,     "height": 20 }, {     "label": "THE",     "confidence": 0.996,     "top": 352,     "left": 695,     "width": 40,     "height": 20 }, {     "label": "ATES",     "confidence": 0.992,     "top": 289,     "left": 364,     "width": 42,     "height": 17 }, {     "label": "GENEXUSTN",     "confidence": 0.983,     "top": 211,     "left": 638,     "width": 167,     "height": 34 }, {     "label": "DOWNLOAD",     "confidence": 0.973,     "top": 350,     "left": 580,     "width": 113,     "height": 20 }, {     "label": "illsion",     "confidence": 0.945,     "top": 95,     "left": 270,     "width": 32,     "height": 11 }, {     "label": "3LD",     "confidence": 0.944,     "top": 308,     "left": 362,     "width": 29,     "height": 15 }, {     "label": "3ut it is!",     "confidence": 0.938,     "top": 134,     "left": 263,     "width": 32,     "height": 8 }, {     "label": "is",     "confidence": 0.933,     "top": 112,     "left": 293,     "width": 9,     "height": 7 }, {     "label": "Genekus:",     "confidence": 0.872,     "top": 92,     "left": 28,     "width": 101,     "height": 24 }, {     "label": "'condinve",     "confidence": 0.863,     "top": 121,     "left": 261,     "width": 38,     "height": 10 }, {     "label": "ian",     "confidence": 0.837,     "top": 98,     "left": 257,     "width": 16,     "height": 7 }] ``` |  | 2418ms |
| **Baidu** | ``` [{ 	"label": "Genexus", 	"confidence": 1.000, 	"top": 83, 	"left": 30, 	"width": 97, 	"height": 34, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\":30,\"y\":83},{\"x\":56,\"y\":83}, 				   ...,{\"x\":30,\"y\":90}]" // 38 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": "[{\"x\":30,\"y\":83},{\"x\":126,\"y\":83}, 				   {\"x\":126,\"y\":116},{\"x\":30,\"y\":116}]" 	}] }, { 	"label": "uE it is", 	"confidence": 1.000, 	"top": 134, 	"left": 267, 	"width": 45, 	"height": 11, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\":267,\"y\":134},{\"x\":273,\"y\":134}, 				   ...,{\"x\":267,\"y\":135}]" // 38 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": "[{\"x\":267,\"y\":134},{\"x\":311,\"y\":134}, 				   {\"x\":311,\"y\":144},{\"x\":267,\"y\":144}]" 	}] }, { 	"label": "EGACY", 	"confidence": 1.000, 	"top": 107, 	"left": 571, 	"width": 143, 	"height": 42, 	"Info": [{ 			"property": "finegrained_vertexes_location", 			"value": "[{"x":571,"y":107},{"x":602,"y":107}, 					   ...,{"x":571,"y":116}]" // 38 points 		}, { 			"property": "min_finegrained_vertexes_location", 			"value": "[{\"x\":570,\"y\":107},{\"x\":711,\"y\":107}, 			           {\"x\":711,\"y\":147},{\"x\":570,\"y\":147}]" 		} 	] }, { 	"label": "MODERNIZATION", 	"confidence": 1.000, 	"top": 157, 	"left": 545, 	"width": 363, 	"height": 44, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\":545,\"y\":157},{\"x\":577,\"y\":157}, 				  ...,{\"x\":545,\"y\":168}]" // 38 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": "[{\"x\":545,\"y\":157},{\"x\":906,\"y\":157}, 				   {\"x\":906,\"y\":199},{\"x\":545,\"y\":199}]" 	}] }, { 	"label": "WITH GENEXUSM 15", 	"confidence": 1.000, 	"top": 213, 	"left": 545, 	"width": 322, 	"height": 35, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\":545,\"y\":213},{\"x\":571,\"y\":213}, 		          ...,{\"x\":545,\"y\":220}]" // 38 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": "[{\"x\":545,\"y\":213},{\"x\":865,\"y\":213}, 				   {\"x\":865,\"y\":247},{\"x\":545,\"y\":247}]" 	}] }, { 	"label": "DOWNLOAD THE EBOOK!", 	"confidence": 1.000, 	"top": 354, 	"left": 583, 	"width": 232, 	"height": 21, 	"Info": [{ 		"property": "finegrained_vertexes_location", 		"value": "[{\"x\": 583,\"y\": 354},{\"x\": 598,\"y\": 354}, 				  ...,{\"x\": 583,\"y\": 359}]" // 38 points 	}, { 		"property": "min_finegrained_vertexes_location", 		"value": [{\"x\":582,\"y\":353},{\"x\":812,\"y\":353}, 		          {\"x\":812,\"y\":373},{\"x\":582,\"y\":373}]" 	}] }] ``` |  | 2418ms |
| **Google** | ``` [{     "label": "LEGACY",     "confidence": 1,     "top": 110,     "left": 551,     "width": 155,     "height": 34,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "MODERNIZATION",     "confidence": 1,     "top": 162,     "left": 553,     "width": 347,     "height": 35,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "WITH",     "confidence": 1,     "top": 216,     "left": 553,     "width": 77,     "height": 29,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "GENEXUS",     "confidence": 1,     "top": 216,     "left": 641,     "width": 150,     "height": 29,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "15",     "confidence": 1,     "top": 216,     "left": 823,     "width": 31,     "height": 29,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "Mlusion",     "confidence": 1,     "top": 99,     "left": 274,     "width": 24,     "height": 7,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "GeneXus",     "confidence": 1,     "top": 96,     "left": 34,     "width": 85,     "height": 3,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "it",     "confidence": 1,     "top": 136,     "left": 279,     "width": 4,     "height": 5,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "is!",     "confidence": 1,     "top": 136,     "left": 287,     "width": 8,     "height": 7,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "(0S",     "confidence": 1,     "top": 262,     "left": 291,     "width": 9,     "height": 7,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "430",     "confidence": 1,     "top": 263,     "left": 304,     "width": 9,     "height": 7,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "ees",     "confidence": 1,     "top": 263,     "left": 318,     "width": 16,     "height": 8,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "ATES",     "confidence": 1,     "top": 295,     "left": 369,     "width": 31,     "height": 18,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "RLD",     "confidence": 1,     "top": 313,     "left": 367,     "width": 20,     "height": 13,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "DOWNLOAD",     "confidence": 1,     "top": 356,     "left": 586,     "width": 106,     "height": 15,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "THE",     "confidence": 1,     "top": 356,     "left": 698,     "width": 36,     "height": 15,     "Info": [{             "property": "Language",             "value": ""         }     ] }, {     "label": "EBOOK!",     "confidence": 1,     "top": 356,     "left": 741,     "width": 69,     "height": 15,     "Info": [{             "property": "Language",             "value": ""         }     ] }] ``` |  | 2716ms |
| **IBM** | ``` [{     "label": "gene",     "confidence": 0.7228,     "top": 92,     "left": 35,     "width": 62,     "height": 27,     "Info": [{         "property": "line_number",         "value": "0.00000"     }] }, {     "label": "nexus",     "confidence": 0.8237,     "top": 80,     "left": 62,     "width": 68,     "height": 32,     "Info": [{         "property": "line_number",         "value": "0.00000"     }] }, {     "label": "legacy",     "confidence": 0.9684,     "top": 111,     "left": 553,     "width": 158,     "height": 37,     "Info": [{         "property": "line_number",         "value": "1.00000"     }] }, {     "label": "modernization",     "confidence": 0.9898,     "top": 163,     "left": 553,     "width": 351,     "height": 37,     "Info": [{         "property": "line_number",         "value": "2.00000"     }] },  ... }] ``` |  | 12898ms |
| **Microsoft** | ``` [{     "label": "GeneXus",     "confidence": 0,     "top": 94,     "left": 0,     "width": 126,     "height": 76,     "Info": [{             "property": "Angle",             "value": "0.00000"         }, {             "property": "Language",             "value": "en"         }, {             "property": "Orientation",             "value": "up"         }     ] }, {     "label": "WITH GENEXUSTM 15",     "confidence": 0,     "top": 216,     "left": 0,     "width": 862,     "height": 215,     "Info": [{             "property": "Angle",             "value": "0.00000"         }, {             "property": "Language",             "value": "en"         }, {             "property": "Orientation",             "value": "up"         }     ] }, {     "label": "DOWNLOAD THE EBOOK!",     "confidence": 0,     "top": 353,     "left": 0,     "width": 813,     "height": 352,     "Info": [{             "property": "Angle",             "value": "0.00000"         }, {             "property": "Language",             "value": ""         }, {             "property": "Orientation",             "value": ""         }     ] }, ... ] ``` |  | 8496ms |
| **MLKit** | ``` [] ``` | N/A | -ms |
| **SAP** | ``` [{ 	"label": "MODERNIZATION", 	"confidence": 0.995006024837494, 	"top": 159, 	"left": 562, 	"width": 322, 	"height": 41 }, { 	"label": "LEGACY", 	"confidence": 0.953990995883942, 	"top": 109, 	"left": 551, 	"width": 161, 	"height": 37 }, { 	"label": "Genexus", 	"confidence": 0.974162995815277, 	"top": 79, 	"left": 30, 	"width": 99, 	"height": 40 }, { 	"label": "DOWNLOAD", 	"confidence": 0.931997001171112, 	"top": 355, 	"left": 586, 	"width": 106, 	"height": 18 }, { 	"label": "GENEXUS", 	"confidence": 0.976303994655609, 	"top": 216, 	"left": 641, 	"width": 155, 	"height": 30 }, { 	"label": "WITH", 	"confidence": 0.947585999965668, 	"top": 217, 	"left": 550, 	"width": 83, 	"height": 27 }, { 	"label": "RATES", 	"confidence": 0.932789027690888, 	"top": 294, 	"left": 364, 	"width": 39, 	"height": 19 }, { 	"label": "EBOOK!", 	"confidence": 0.912930011749268, 	"top": 354, 	"left": 742, 	"width": 71, 	"height": 19 }, { 	"label": "RLD", 	"confidence": 0.899074018001556, 	"top": 310, 	"left": 362, 	"width": 28, 	"height": 18 }, { 	"label": "THE", 	"confidence": 0.899158000946045, 	"top": 356, 	"left": 698, 	"width": 39, 	"height": 16 }, { 	"label": "15", 	"confidence": 0.925707995891571, 	"top": 217, 	"left": 826, 	"width": 36, 	"height": 29 }] ``` |  | 3780ms |
| **Tencent** | ``` [{     "label": "15",     "confidence": 0.99,     "top": 232,     "left": 856,     "width": 37,     "height": 34 }, {     "label": "MODE",     "confidence": 0.975,     "top": 242,     "left": 577,     "width": 96,     "height": 70 }, {     "label": "RLD",     "confidence": 0.96,     "top": 480,     "left": 452,     "width": 22,     "height": 13 }, {     "label": "RATES",     "confidence": 0.955,     "top": 461,     "left": 447,     "width": 36,     "height": 17 }, {     "label": "GENF",     "confidence": 0.943,     "top": 277,     "left": 685,     "width": 63,     "height": 46 }, {     "label": "THEE",     "confidence": 0.873,     "top": 396,     "left": 780,     "width": 38,     "height": 44 }, {     "label": "ERi",     "confidence": 0.868,     "top": 229,     "left": 675,     "width": 52,     "height": 50 }, {     "label": "NEXUS\"",     "confidence": 0.863,     "top": 242,     "left": 746,     "width": 89,     "height": 68 }, {     "label": "NZATON",     "confidence": 0.848,     "top": 159,     "left": 735,     "width": 180,     "height": 103 }, {     "label": "LEGAER",     "confidence": 0.828,     "top": 174,     "left": 559,     "width": 149,     "height": 94 }, {     "label": "?",     "confidence": 0.775,     "top": 350,     "left": 120,     "width": 29,     "height": 42 }, {     "label": "Gene",     "confidence": 0.775,     "top": 369,     "left": 68,     "width": 46,     "height": 37 }, {     "label": "EBDON",     "confidence": 0.759,     "top": 372,     "left": 823,     "width": 67,     "height": 46 }, {     "label": "MITHC",     "confidence": 0.712,     "top": 300,     "left": 591,     "width": 87,     "height": 59 }, {     "label": "auters",     "confidence": 0.71,     "top": 318,     "left": 288,     "width": 33,     "height": 12 }, {     "label": "OMCOO",     "confidence": 0.614,     "top": 411,     "left": 677,     "width": 97,     "height": 58 }, {     "label": "HhIsion",     "confidence": 0.602,     "top": 308,     "left": 294,     "width": 27,     "height": 9 }] ``` |  | 1827ms |

## [Notes](#Notes)

* The label assigned for an object depends on the provider used (i.e. string detection accuracy). Additional information can be found on the OutputRegion.Info field if it is given by the provider.
* Some providers are more accurate with noisy images than others (e.g. stamps on shirts). All of them work fine with clean text on the image (e.g. a scanned text).
* Maximum image file size is 10MB.
* GeneXusAI does not provide support for drawing a rectangle over an image. This action is the responsibility of the developer.  
  **TIP**: For Web applications, a good alternative can be combining [HTML5 Canvas control with JavaScript](https://www.w3schools.com/tags/ref_canvas.asp) with [User Control object](https://wiki.genexus.com/commwiki/wiki?39356). On the other hand, for Smart Devices you could use [Image Map control](https://wiki.genexus.com/commwiki/wiki?17823) on which you can set the processed image as background and 'draw' square regions (i.e. set a border color on the table item of the grid).
* **IBM provider**: Deprecated as of September 12 (2019). Check [IBM Visual Recognition's Release Notes](https://cloud.ibm.com/docs/services/visual-recognition?topic=visual-recognition-release-notes#12-de-septiembre-de-2019). Before deprecation, GeneXusAI sses the dark beta feature of Visual Recognition and you had to [request access](https://datasciencex.typeform.com/to/nU6efl).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Android, Apple, Angular |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

* As of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,):  
  - Google Cloud AI is available.  
  - SAP Leonardo supports noise images
* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,):  
  - Amazon WS and Tencent AI are available.
* As of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,):  
  - Baidu AI is available.
* As of [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,):  
  - Alibaba AI is available.
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,):  
  - SAP Leonardo has been deprecated
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  - Firebase ML Kit is available for Android.


|  |
| --- |
| **Backlinks** |
| [Confidence domain](https://wiki.genexus.com/commwiki/wiki?40189) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [OutputRegion data type](https://wiki.genexus.com/commwiki/wiki?40194) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) |

---
