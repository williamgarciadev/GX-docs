---
title: "PDFReport.ini file format (GeneXus 18 Upgrade 4 or prior)"
source_id: 55599
source_url: https://wiki.genexus.com/commwiki/wiki?55599
genexus_version: "18"
---

# PDFReport.ini file format (GeneXus 18 Upgrade 4 or prior)

The PDFReport.ini file is a configuration file used to generate PDF files. It is located in the directory where the report is executed (webapp\WEB-INF folder for Java) and is automatically generated when executing a report in case it is not present. Make sure the file encoding is UTF8 otherwise it may cause problems reading font parameters.

It includes the following configuration entries:

|  |  |
| --- | --- |
| Barcode128AsImage | Boolean indicating whether to generate a Barcode128 font type as an Image (Default value true). |
| Embeed Fonts | Boolean indicating whether to embed the fonts; check 'Embedded Fonts' Section (Default *false*). |
| SearchNewFonts | Boolean indicating whether the fonts must be searched if they are not in the INI when embedding them (Default *false*). |
| SearchNewFontsOnce | Boolean indicating that the fonts must be searched just once if they are not found (Default *true*). |
| Version | Defines the PDFReport version (a.b.c.d format) (Default 1.0.0.0). |
| FontsLocation | Defines the fonts location (Default "."). |
| LeftMargin | Defines the left margin associated to the document (in centimeters) (Default 0.75). |
| TopMargin | Defines the top margin associated to the document (in centimeters) (Default 0.75). |
| BottomMargin | Defines the bottom margin associated to the document (in centimeters) (Default 6). |
| OutputFileDirectory | If the path is not specified in GeneXus report output\_File, the outputDirectory is considered (Default "."). |
| DottedStyle | Dotted Style value (Default 1;2). |
| LineCapProjectingSquare | Line position in reports as design (Default *true*). |
| LongDotDashedStyle | Long dot Dashed Style value (Default 6;2;1;2). |
| ServerPrinting | Boolean indicating whether to print the PDF in the application server (Default *false*). |
| AdjustToPaper | Boolean indicating whether fit to page is enabled (Default *true*). |
| Leading | Defines the separation between each row (Default 2). |
| DashedStyle | Dashed Style value (Default value 4;2). |
| LongDashedStyle | Long Dashed Style value (Default value 6;2). |
| DEBUG | DEBUG information will be added to the Standard Output (stdout)  (Default *false*)  It shows information such as the following:  *GxSetDocName: 'report.pdf'*  *setPageLines: 999*  *setLineHeight: 15*  *GxAttris:*  *\-> Font: Helvetica (8) BOLD*  *\-> Fore (0, 0, 0)*  *\-> Back (255, 255, 255)*  *GxEndDocument!* |

### ['Embedd Fonts' Section](#%27Embedd+Fonts%27+Section)

A boolean is associated to each font name. This boolean defines whether to embed the font or not (for finest General Property granularity). To embed a font, the generalProperty and the property of this section must have 'true' value. To setup the fonts to embedded you can execute 'com.genexus.reports.PDFReportConfig' utility class.

Notice that a Font and its Bold type (or other variations) are considered different so you need to reference both separately if you want to embeed them.

#### [Example](#Example)

```
[Embeed Fonts]
Microsoft Sans Serif= true
Microsoft Sans Serif,Bold= true
```

### ['Fonts Location (Sun)' Section](#%27Fonts+Location+%28Sun%29%27+Section)

The 'FontName= location of the associated .ttf' mappings are stored. These mappings are automatically created; when you use non standard fonts make sure to check the correct configuration.

#### [Java Example](#Java+Example)

```
[Fonts Location (Sun)]
Microsoft Sans Serif= c:\windows\fonts\micross.ttf
```

.NET Example

```
[Fonts Location (MS)]
Microsoft Sans Serif= c:\windows\fonts\micross.ttf
Microsoft Sans Serif,Bold= c:\windows\fonts\micross.ttf
```

### ['Fonts Substitutions' Section](#%27Fonts+Substitutions%27+Section)

'Font= Font' pairs mapping a font within other are stored. E.g.: you can put 'Impact= Courier' to map one TrueTypeFont within another one. You can also map a font in a Type1; e.g.: 'Impact= Helvetica'. These mappings can be performed by the user.

### [Considerations](#Considerations)

Every time you modify the pdfreport.ini file make sure to restart the application server as this configuration is read only once at application startup. For C# you can modify the web.config file so the application is recycled; for Tomcat or any other application server restart the service.

### [How to deploy a custom "PDFReport.ini", "GXPRN.ini" or "PDFReport.template"?](#How+to+deploy+a+custom+%22PDFReport.ini%22%2C+%22GXPRN.ini%22+or+%22PDFReport.template%22%3F)

If you want to make sure GeneXus is including in the deploy process a modified: ReportPDF.ini**,** GXPRN.ini or PDFReport.template, add it as a kb file. Then set the property "Extract for ... generator" to "true".

That way, the files will be included in the deploy even if you don't add them to a DeploymentUnit.
