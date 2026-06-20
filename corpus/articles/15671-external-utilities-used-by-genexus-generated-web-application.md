---
title: "External utilities used by GeneXus-generated web applications"
source_id: 15671
source_url: https://wiki.genexus.com/commwiki/wiki?15671
genexus_version: "18"
---

# External utilities used by GeneXus-generated web applications

Here is a list of third-party utilities distributed by GeneXus which are used by the [GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892), [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) and [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) generated applications. In addition, references to the license terms for each one are included.

## [Business Logic](#Business+Logic)

| Utility | Purpose | Usage | License type | Website | Generators |
| --- | --- | --- | --- | --- | --- |
| iText | PDF files handling | Used when [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) are generated in the application | .NET (iText 4.x)   * LGPL / MPL | <https://github.com/schourode/iTextSharp-LGPL> | Java (iText.jar,iTextAsian.jar)  .Net Framework & .NET (iTextAsian.dll, itextsharp.dll) |
| Java (iText 2.1.7)   * MPL 1.1 | <https://mvnrepository.com/artifact/com.lowagie/itext/2.1.7> |
| Java or .NET (iText 8.x)   * AGPL * Commercial | <https://itextpdf.com/> |
| Lucene | Full Text search tool | Used when Full text search feature is used. (ref.: [Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)) | Apache License, Version 2.0 | <http://lucene.apache.org/>  <https://www.nuget.org/packages/Lucene.Net/> | Java (is-core-2.2.0.jar, lucene-highlighter-2.2.0.jar, lucene-spellchecker-2.2.0.jar,tm-extractors-0.4.jar)  .Net Framework (Lucene.Net.dll, GxSearch.dll, Highlighter.Net.dll, Lucene.Net.dll, SpellChecker.Net.dll)  .NET |
| jSrvAny | Install java applications as service | Used when Java applications are installed as a windows service. [See details](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,10834) | BSD-style License | <http://sourceforge.net/projects/jsrvany/> | Java |
| POI | Excel files handling | Used when ExcelDocument datatype are defined in the application [Generating Microsoft Excel and Word Documents](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2101,,)  Is distributed with Java Generator | Apache License, Version 2.0 | <http://poi.apache.org/> | Java (poi-4.1.2.jar, poi-scratchpad-4.1.2.jar, poi-ooxml-4.1.2.jar, poi-ooxml-schemas-4.1.2.jar, commons-compress-1.21.jar, commons-math3-3.6.1.jar, curvesapi-1.06.jar, SparseBitSet-1.2.jar, commons-codec-1-9-jar, xmlbeans-3.1.0.jar)  .Net Framework (GxExcelI.dll) |
| EPPlus | Excel files handling | Used when ExcelDocument data type is defined in the application [Generating Microsoft Excel and Word Documents](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2101,,)  Is distributed with the .NET Generator | LGPL | [EPPlus 4.5.3.2](https://github.com/JanKallman/EPPlus /4.5.3.2) | .Net Framework  .NET |
| Jayrock-JSON | JSON library | JSON Serialization | LGPL | <https://code.google.com/archive/p/jayrock/> | Java  .Net Framework  .NET |
| log4net, log4j | Logging functions | Used for logging: [Log external object](https://wiki.genexus.com/commwiki/wiki?37872), [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) | Apache License, Version 2.0 | <http://logging.apache.org/log4net/> | Java  .Net Framework  .NET |
| NetComponents Internet Protocol Library | Network protocols implementations | Used when ftp functions are used.[FTP functions](https://wiki.genexus.com/commwiki/wiki?8393) | Apache License, Version 2.0 | <http://www.savarese.org/oro/index.html#NetComponents> | Java |
| NetTopologySuite | Geography types | Used to manipulate geography data types | BSD-3-Clause | <https://www.nuget.org/packages/NetTopologySuite> | .NET |
| GeographicLib | Geography types | Used to manipulate geography data types | MIT/X11 | <https://github.com/oldrev/GeographicLib> | .NET |
| Stubble.Core | User Controls (Server-side) | Used by [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) in .NET Applications. | MIT | <https://github.com/stubbleorg/stubble> | .NET |
| Nustache | UserControls (Server-side) | Used by [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) in .NET Applications | MIT | <https://github.com/jdiamond/Nustache> | .Net Framework |
| OpenPop | SMTP and Pop3 | Used by Applications manipulating Pop3 emails | [PUBLIC-DOMAIN License](http://unlicense.org/) | <https://www.nuget.org/packages/OpenPop.NET> | .Net Framework, .NET |
| MailKit | SMTP and Pop3 | Used by Applications manipulating Pop3 and SMTP emails | MIT license | <https://github.com/jstedfast/MailKit> | .Net Framework, .NET |
| MimeKit | SMTP and Pop3 | Used by Applications manipulating Pop3 and SMTP emails | MIT license | <https://github.com/jstedfast/MimeKit> | .Net Framework, .NET |
| JakartaMail | SMTP and Pop3 | Used by Applications manipulating Pop3 and SMTP emails | [Multiple](https://projects.eclipse.org/projects/ee4j.mail) | <https://jakartaee.github.io/mail-api/> | Java |
| StackExchange.Redis | Cache on Redis | Used by Applications with caching enabled on Redis cache server | MIT license | <https://github.com/StackExchange/StackExchange.Redis> | .Net Framework, .NET |
| Ntidy.dll | HtmlPreview in FullTextSearch | Used when .NET Applications HtmlPreview and [HTMLClean function](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5224,,) functions are used. [Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292) |  |  | Java (Tidy.jar)  .Net (NTidy.dll) |
| Apache Commons IO Bundle | Internal Usage for IO | GX Standard Classes internal usage | Apache License, Version 2.0 | <http://commons.apache.org/proper/commons-io/> | Java (commons-io-1.4.jar) |
| Apache Commons Codec | Internal Usage for Encoding & Decoding | GX Standard Classes internal usage | Apache License, Version 2.0 | <https://commons.apache.org/proper/commons-codec/> | Java (commons-codec-1.9.jar) |
| Apache Commons Lang | Internal Usage for String manipulation | GX Standard Classes internal usage | Apache License, Version 2.0 | <http://commons.apache.org/lang/> | Java (commons-lang-2.4.jar) |
| Xerces | XML Reading & Writing | Used by the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) and [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |  |  | Java (xercesImpl.jar) |
| Apache Commons FileUpload | File Upload to the server | Used for uploading Blobs |  |  | Java (commons-fileupload-1.3.2.jar) |
| Apache commons NET | Gives support for FTP |  |  |  | Java (commons-net-3.3.jar) |
| Joda Time | Date and Time API | Datetime management with timezone | Apache License, Version 2.0 | <http://joda-time.sourceforge.net/license.html> | Java (joda-time-2.8.2.jar) |
| Jersey | Rest webservices | Support for RESTful Web services in Java | [Eclipse Public License 2.0](https://github.com/eclipse-ee4j/jersey?tab=License-1-ov-file) | <https://jersey.github.io/> | Java (Jersey 2.x for JavaX or 3.x for Jakarta ) |
| Bouncy Castle | Cryptography | Support for Cryptography data type in JAVA | MIT | https://www.bouncycastle.org/licence.html | JAVA (bcpkix-jdk15on-160.jar, bcprov-jdk15on-160.jar) |
| Xml Security | Cryptography | Support for Cryptography (XML Signature) data type in JAVA | Apache License, Version 2.0 | http://santuario.apache.org/ | JAVA (xmlsec.jar) |
| WebSocket support | WebNotifications | Support for Web Sockets in DotNet Applications |  | https://www.microsoft.com/web/webpi/eula/net\_library\_eula\_enu.htm | .Net Framework (Microsoft.WebSockets.dll) |
| AWS Amazon S3 | External Blob Storage | Support for storing blobs outside Database using Microsoft Azure Storage | Apache License, Version 2.0 | https://github.com/aws/aws-sdk-net | Net Framework and .NET   * AWSSDK.Core.dll * AWSSDK.S3.dll   JAVA   * aws-java-sdk-1.11.62.jar * httpclient-4.4.1.jar * httpcore-4.4.1.jar |
| Microsoft Azure Storage | External Blob Storage | Support for storing blobs outside Database using AWS S3 | Apache License, Version 2.0 | https://github.com/Azure/azure-storage-net/blob/master/LICENSE.txt | .Net Framework:   * Microsoft.WindowsAzure.Storage.dll * Microsoft.Data.Services.Client.dll   .NET:   * Microsoft.WindowsAzure.Storage.dll * Microsoft.Data.Services.Client.dll   JAVA   * azure-storage-4.2.0.jar |
| IBM Cloud Object Storage | External Blob Storage | Support for storing blobs outside Database using IBM COS | Apache License, Version 2.0 | <https://github.com/IBM/ibm-cos-sdk-java/blob/master/LICENSE.txt> | JAVA   * ibm-cos-java-sdk-s3 |
| Google Cloud Platform Storage | External Blob Storage | Support for storing blobs outside Database using Google Cloud Platform Storage | Apache License, Version 2.0 | https://github.com/google/google-api-dotnet-client | .Net Framework:   * Google.Apis.Auth.dll * Google.Apis.Auth.PlatformServices.dll * Google.Apis.Core.dll * Google.Apis.dll * Google.Apis.PlatformServices.dll * Google.Apis.Storage.v1.dll * Google.Cloud.Storage.V1.dll * Google.Api.Gax.dll * Google.Api.Gax.Rest.dll   .NET packages:   * Google.Apis.Auth * Google.Apis.Core * Google.Apis * Google.Apis.AndroidPublisher.v3   JAVA   * google-api-client-1.22.0 * google-api-services-storage- * google-auth-library-credentials-0.6.0 * google-auth-library-oauth2-http-0.6.0 * google-cloud-0.8.1-alpha * google-cloud-core-0.8.1-alpha * google-cloud-storage-0.8.1-beta * google-http-client-1.22.0 * google-http-client-appengine-1.22.0 * google-http-client-jackson-1.22.0 * google-http-client-jackson2-1.22.0 * google-oauth-client-1.22.0 |
| PDFBox | Printserver | Client side web printing | Apache License, Version 2.0 | <https://pdfbox.apache.org/> | pdfbox-2.0.18.jar, fontbox-2.0-18.jar |
| PDF files handling | Used to generate PDF reports in the application, when [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844) = PDFBox. |
| PdfPig | Indexing PDF files | Used when Full text search feature is used. (ref.: [Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)) | Apache License, Version 2.0 | <https://github.com/UglyToad/PdfPig> | Only used in .NET and .NET Framewor generators (pdfpig.dll) |
| httpclient, httpcore | httpclient | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) & http connections in general | Apache License, Version 2.0 | <https://hc.apache.org/> |  |
| TOTP | Two Factor Authentication | Used when TOTP Authenticator is enabled | .NET   * Apache License, Version 2.0 * MIT | <https://www.nuget.org/packages/GoogleAuthenticator/>  <https://www.nuget.org/packages/QRCoder/> | Java (commons-codec-1.9.jar, commons-net-3.3.jar, core-3.4.0.jar, javase-3.4.0.jar, jcommander-1.72.jar, totp-1.7.1.jar)  .Net Framework (Google.Authenticator.dll, QRCoder.dll)  .NET |
| Java   * Apache License, Version 2.0 * MIT | <https://mvnrepository.com/artifact/commons-codec/commons-codec>  <https://mvnrepository.com/artifact/commons-net/commons-net>  <https://mvnrepository.com/artifact/com.google.zxing/core>  <https://mvnrepository.com/artifact/com.google.zxing/javase>  <https://mvnrepository.com/artifact/com.beust/jcommander>  <https://mvnrepository.com/artifact/dev.samstevens.totp/totp-parent> |

## [**Web Client-Side Libraries**](#Web+Client-Side+Libraries)

|  |  |  |  |
| --- | --- | --- | --- |
| **Library** | **Purpose** | **License Type** | **Files** |
| jQuery | Client-Side Rendering (Javascript) | MIT License | jquery.js |
| jQuery UI | Client-Side Rendering (Javascript) | MIT License | Included in gxgral.js |
| Modernizr | Detect HTML5 and CSS3 features in various browsers | MIT License | Included in gxgral.js |
| Bootstrap | Front-end framework | MIT License | bootstrap, npm.js |
| howler.js | Support for Audio API for Web | MIT License | howler.js |
| DHTML Calendar | Date & Datetime Picker, Used when Enable DatePicker = yes [Enable Datepicker property](https://wiki.genexus.com/commwiki/wiki?13339) | LGPL 3 |  |
| [Highcharts](https://www.highcharts.com) | Reporting (Charts): [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | OEM |  |
| [ECharts](https://echarts.apache.org/) | Reporting (Maps): [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | Apache License | echarts.js |
| [ECharts maps](https://github.com/genexuslabs/echarts-countries-js/tree/maps-branch/echarts-countries-js) | Reporting (Maps): [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | ODC Open Database License |  |
| OAT Pivot | Reporting (Pivot): [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | GNU General Public License |  |
|  | Mustache (for templating) |  | gxgral.js |
| [jstimezonedetect](https://github.com/pellepim/jstimezonedetect/) | Helps with the timezone | MIT License | Included in the gxtimezone.js |
| CK Editor 3.x | [FCK HTML Editor Control](https://wiki.genexus.com/commwiki/wiki?4858) | GPL, LGPL, MPL, Commercial ([ref](https://docs-old.ckeditor.com/CKEditor_3.x/Howto/License)) |  |

## [Data Access](#Data+Access)

**JDBC Drivers**  
These are the default JDBC driver, you could deploy others.

| Driver | License type | Website |
| --- | --- | --- |
| jt400.jar | IBM Public License Version 1.0 | <http://sourceforge.net/projects/jt400/> |
| mssql-jdbc-10.2.0.jre8.jar | MIT License | <https://github.com/microsoft/mssql-jdbc> |
| mysql-connector-java-5.1.49-bin.jar | GPLv2  Commercial License | <https://dev.mysql.com/downloads/connector/j/> |
| postgresql-42.2.14.jar | BSD License | <http://jdbc.postgresql.org/> |
| ojdbc8.jar version 12.2..0.1 | OTN License | <https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html> |

**ADO.NET Drivers**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Oracle.ManagedDataAccess.Core | Oracle ADO.NET provider | Used when .NET Applications connect to Oracle DBMS | OTN License Agreement | [https://www.nuget.org/packages/Oracle.ManagedDataAccess.Core](https://www.nuget.org/packages/Oracle.ManagedDataAccess.Core/) | .NET |
| MySql.Data | MySQL ADO.NET provider | Used when .NET Applications connects to MySQL DBMS | GPLv2 | [https://www.nuget.org/packages/MySql.Data](https://www.nuget.org/packages/MySql.Data/) | .NET |
| MySQLDriverCS | MySQL ADO.NET provider | Used when .NET Applications connects to MySQL DBMS | GNU GPL | <http://sourceforge.net/projects/mysqldrivercs/> | .Net Framework |
| Npgsl | Postgre SQL ADO.NET provider | Used whe .NET Applications connects to PostgreSQL DBMS | [License terms](https://github.com/npgsql/npgsql/blob/master/LICENSE) | <http://www.npgsql.org/> | .Net Framework  .NET |

### [See Also](#See+Also)

[External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094)


|  |
| --- |
| **Backlinks** |
| [Table of contents:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [External utilities used by GeneXus generated applications](https://wiki.genexus.com/commwiki/wiki?25151) | [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094) |
| [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) |
| [Offline scenario of the .NET Generator](https://wiki.genexus.com/commwiki/wiki?53793) | [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844) |
| [PDF Reports Library property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55459) | [PDF Reports Library property (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55933) | [PDF Reports Library property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57550) | [PDF Reports Library property (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57946) |

---
