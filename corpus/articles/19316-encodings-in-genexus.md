---
title: "Encodings in GeneXus"
source_id: 19316
source_url: https://wiki.genexus.com/commwiki/wiki?19316
genexus_version: "18"
---

# Encodings in GeneXus

The encodings used in the standard functions that require it are unified for all generators. To this end, a domain called Encoding and of type Character(255) is distributed with [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756).  
This makes the code more portable and helps you to choose valid values.

For example, you can write: &xmlreader.SetDocEncoding(Encoding.UTF-8)

In addition to this method of XML data types, there are these other functions and methods that also receive as parameter a string with the encoding name.

The functions and methods that use encoding are as follows:

* [ByteCount](https://wiki.genexus.com/commwiki/wiki?2455)(CharacterExpression:Att|Var|Cons, Encoding:Att|Var|Cons): Numeric
* [DFWOpen](https://wiki.genexus.com/commwiki/wiki?8372)(FileName: Character, FieldDelimiter: Character, StringDelimiter: Character, Append: Numeric, Encoding:Character) : Numeric
* [DFROpen](https://wiki.genexus.com/commwiki/wiki?8369)(FileName: Character, RegLength: Numeric, FieldDelimiter: Character, StringDelimiter:Character, Encoding:Character): Numeric
* &xmlreader.[SetDocEncoding](https://wiki.genexus.com/commwiki/wiki?7054)(Encoding:Character)
* &xmlreader.[SetNodeEncoding](https://wiki.genexus.com/commwiki/wiki?7055)(Encoding:Character)
* &xmlwriter.[WriteStartDocument](https://wiki.genexus.com/commwiki/wiki?7083)(Encoding:Character, <Standalone:Boolean>)

### [Encoding Domain (Unified encoding list)](#Encoding+Domain+%28Unified+encoding+list%29)

|  | .NET | Java |
| --- | --- | --- |
| ASCII | Yes | Yes |
| Big5 | Yes | Yes |
| Big5-HKSCS | **No** | Yes |
| EUC-JP | Yes | Yes |
| EUC-KR | Yes | Yes |
| GB18030 | Yes | Yes |
| GB2312 | Yes | Yes |
| GBK | Yes | Yes |
| IBM850 | Yes | Yes |
| ISO-2022-JP | Yes | Yes |
| ISO-8859-1 | Yes | Yes |
| ISO-8859-10 | **No** | **No** |
| ISO-8859-13 | Yes | Yes |
| ISO-8859-15 | Yes | Yes |
| ISO-8859-16 | **No** | **No** |
| ISO-8859-2 | Yes | Yes |
| ISO-8859-3 | Yes | Yes |
| ISO-8859-4 | Yes | Yes |
| ISO-8859-5 | Yes | Yes |
| ISO-8859-6 | Yes | Yes |
| ISO-8859-7 | Yes | Yes |
| ISO-8859-8 | Yes | Yes |
| ISO-8859-9 | Yes | Yes |
| KOI8-R | Yes | Yes |
| KOI8-U | Yes | **No** |
| KSC\_5601 | Yes | Yes |
| Shift\_JIS | Yes | Yes |
| TIS-620 | Yes | Yes |
| US-ASCII | Yes | Yes |
| UTF-16BE BOM | Yes | Yes |
| UTF-16LE BOM | Yes | Yes |
| UTF-32 | Yes | **No** |
| UTF-32 BOM | Yes | **No** |
| UTF-32BE BOM | Yes | **No** |
| UTF-32LE BOM | Yes | **No** |
| UTF-8 | Yes | Yes |
| UTF-8 BOM | Yes | Yes |
| Windows-1250 | Yes | Yes |
| Windows-1251 | Yes | Yes |
| Windows-1252 | Yes | Yes |
| Windows-1253 | Yes | Yes |
| Windows-1254 | Yes | Yes |
| Windows-1255 | Yes | Yes |
| Windows-1256 | Yes | Yes |
| Windows-1257 | Yes | Yes |
| Windows-1258 | Yes | Yes |
| Windows-31J | **No** | Yes |
| Windows-874 | Yes | Yes |

### [BOM (Byte Order Mark)](#BOM+%28Byte+Order+Mark%29)

UTF\* BOM encodings are used to indicate that a byte order mark is to be used at the beginning of the file or stream to specify the Unicode type in which the text in the file or stream is encoded.

For UTF-8, the BOM is represented by the sequence 0xEF, 0xBB, 0xBF.

For UTF-16BE, the sequence is 0xFE, 0xFF

For UTF-16LE, the sequence is 0xFF, 0xFE

For UTF-32BE, the sequence is 0x00, 0x00, 0xFE, 0xFF

For UTF-32LE, the sequence is 0xFF, 0xFE, 0x00, 0x00

### [See Also](#See+Also)

[Encoding Management](https://wiki.genexus.com/commwiki/wiki?43502)


|  |
| --- |
| **Backlinks** |
| [File data type: Text file handling](https://wiki.genexus.com/commwiki/wiki?24070) |

---
