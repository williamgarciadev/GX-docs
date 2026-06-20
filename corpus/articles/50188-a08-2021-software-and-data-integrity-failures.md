---
title: "A08:2021 - Software and data integrity failures"
source_id: 50188
source_url: https://wiki.genexus.com/commwiki/wiki?50188
genexus_version: "18"
---

# A08:2021 - Software and data integrity failures

This document describes the Software and data integrity failures of applications and how to prevent them.

This category relates to code and infrastructure that do not protect against integrity violations. It also focuses on making assumptions related to, among other things, software updates, critical data, and continuous integration/development pipelines without verifying integrity.

Read more at: [Software and Data Integrity Failures - OWASP Documentation](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)

The following are general prevention scenarios:

* **Code review:** Ensuring that there is a review process for code and configuration changes minimizes the possibility of malicious code or configurations being introduced into the development and deployment process.
* **Malicious downloads:** It is vital to verify the source from which you are downloading resources from the Internet. In the case of GeneXus and other components (User Controls, extensions), always make sure that the source comes from the official GeneXus channels (Download Center, marketplace, wiki).
* **Trusted dependencies:** Following the previous item, it also applies to the libraries and dependencies to be used. In [Java](https://wiki.genexus.com/commwiki/wiki?12258)/[.NET](https://wiki.genexus.com/commwiki/wiki?38604) external objects, you should always check that they come from reliable sources and publishers (Maven Central, NuGet).
* **CI/CD security:** In case of having continuous integration/deployment pipelines, secrets and access control must be properly configured to ensure code integrity during the compilation and deployment process.

### [Insecure deserialization](#Insecure+deserialization)

[Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus brings serialization/deserialization secure mechanisms such as [FromJson](https://wiki.genexus.com/commwiki/wiki?37809), [ToJson](https://wiki.genexus.com/commwiki/wiki?37817), [FromXML](https://wiki.genexus.com/commwiki/wiki?8788) & [ToXML](https://wiki.genexus.com/commwiki/wiki?8789).
* When the [SDT](https://wiki.genexus.com/commwiki/wiki?2427)'s ToXML or ToJSON functions are used, GeneXus encodes the entries for the corresponding context.
* When the XML is manually read/written, [XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938) and [XMLReader](https://wiki.genexus.com/commwiki/wiki?6928) functions code/decode the entries and values accordingly.

#### [Actions by Developers](#Actions+by+Developers)

* Sanitize user entries if they are concatenated to an XML and loaded using FromXML function.

  + Security Scanner helps to detect this scenario with case code #126.
  + The use of System.Security.SecurityElement.Escape from [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), and org.owasp.esapi.Encoder.encodeForXML from [ESAPI](https://owasp.org/www-project-enterprise-security-api/) or org.apache.commons.text.StringEscapeUtils.encodeXml10 for Java is advised.
* If the function [WriteRawText](https://wiki.genexus.com/commwiki/wiki?7075) of [XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938) is used, the developer must sanitize user entries.

  + Security Scanner helps to detect this scenario with case code  #128.
  + The use of System.Security.SecurityElement.Escape from .NET Framework, and org.owasp.esapi.Encoder.encodeForXML from [ESAPI](https://owasp.org/www-project-enterprise-security-api/) or org.apache.commons.text.StringEscapeUtils.encodeXml10 for Java is advised.
  + Use [ValidationType](https://wiki.genexus.com/commwiki/wiki?6969) property to validate XML format.

    - Security Scanner helps to detect this scenario with case code #113.
* Sanitize user entries if they are concatenated to a JSON and loaded using FromJSON function.

  + Security Scanner helps to detect this scenario with case code #127.
  + The use of System.Web.Serialization.JavaScriptSerializer.Serialize from .NET Framework or org.owasp.esapi.Encoder.encodeForJavascript from [ESAPI](https://owasp.org/www-project-enterprise-security-api/) for Java is advised.
* Security Scanner - Detections:

  + Checking use of SDT.FromXml() method (#126), checking use of SDT.FromJson() method (#127), checking use of SDT.FromXmlFile() method (#134), checking use of SDT.FromJsonFile() method (#135).

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
