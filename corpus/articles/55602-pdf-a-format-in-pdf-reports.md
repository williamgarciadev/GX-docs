---
title: "PDF/A format in PDF reports"
source_id: 55602
source_url: https://wiki.genexus.com/commwiki/wiki?55602
genexus_version: "18"
---

# PDF/A format in PDF reports

Today, the conservation and preservation of information is vital. To achieve this, the PDF/A standard, defined by ISO as a subcategory of the PDF format, guarantees the integrity and readability of documents over time. In this context, GeneXus excels at enabling the generation of reports in PDF/A format, ensuring adherence to long-term preservation standards, and guaranteeing that documents maintain their usefulness and accessibility in the future.

### [What is PDF/A?](#What+is+PDF%2FA%3F)

PDF/A is a standardized variant of PDF (Portable Document Format/Archival) developed by ISO for a specific purpose: to ensure the long-term preservation and accessibility of digital documents. It focuses on maintaining the visual representation and structure of page-based documents over time. This format, defined by the ISO 19005 family of standards, acts as a safeguard against technological changes, ensuring that documents can be read and used in the future.

The primary goal of PDF/A is to ensure that the visual appearance of documents remains consistent as time progresses. To achieve this, PDF/A-compliant files must encapsulate all the necessary information within the document itself. This includes fonts, colors, content, and layout instructions. Unlike regular PDFs, PDF/A documents are not allowed to reference external resources, ensuring self-sufficiency.

PDF/A mandates adherence to a set of guidelines:

1. No Audio or Video Content: PDF/A files cannot contain audio or video elements, focusing solely on the visual aspects of the document.
2. No Executable Content: JavaScript and executable file launches are prohibited, enhancing security and preventing potential vulnerabilities.
3. Embedded Fonts: All fonts used in the document must be embedded to ensure accurate rendering regardless of the system or software.
4. Device-Independent Color Spaces: Color information should be defined in a way that remains consistent across various devices and platforms.
5. No Encryption: Encryption is not allowed in PDF/A files to facilitate long-term accessibility and prevent encryption-related issues.
6. Standards-Based Metadata: Metadata must adhere to recognized standards, enabling proper indexing and searchability.
7. No Transparent Objects or Layers: Transparency features are excluded to ensure consistent visual reproduction.
8. Image Compression Restrictions: Certain image compression models, such as LZW and JPEG2000, are prohibited due to potential compatibility issues.

### [Compliance Levels](#Compliance+Levels)

PDF/A standards have evolved over time. Each version introduced refinements to the standard, ensuring better archival capabilities.

PDF/A-1: This version includes two compliance levels:

* PDF/A-1a: Level A (accessible). This level of compliance focuses on ensuring that the content of the document is fully readable and actionable in the future. To meet this level, the PDF must contain metadata and a structure that enables search and retrieval of the content. In other words, it ensures that the content can be searched and reused, which is especially useful for documents where information needs to be extracted in the future.
* PDF/A-1b: Level B (basic). This level focuses on preserving the visual appearance of the document over time. It ensures that fonts, colors, and layout remain intact when the document is viewed in the future. Content does not need to be fully reusable or meet certain search requirements, but its appearance must remain consistent.

### [Using PDF/A in GeneXus](#Using+PDF%2FA+in+GeneXus)

To generate reports in PDF/A format using GeneXus, follow these steps:

1. Access the [PDFReport.ini file](https://wiki.genexus.com/commwiki/wiki?27500).
2. Add one of the following lines according to your preference or need:  
   ComplianceLevel=pdf\_a1a  
   ComplianceLevel=pdf\_a1b
3. Save the "PDFReport.ini" file with the corresponding configuration line.

Note that the value of "ComplianceLevel" in the PDFReport.ini file only affects runtime. This means that it does not change the generated code, so you can directly change the PDFReport.ini file and, when re-running, the system will take the new value you have set. This flexibility allows you to adjust the generation of PDF/A files according to your needs without modifying the underlying code.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [PDFReport.ini file format](https://wiki.genexus.com/commwiki/wiki?27500) |

---
