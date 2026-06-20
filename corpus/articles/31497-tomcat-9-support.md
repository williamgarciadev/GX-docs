---
title: "Tomcat 9 support"
source_id: 31497
source_url: https://wiki.genexus.com/commwiki/wiki?31497
genexus_version: "18"
---

# Tomcat 9 support

The [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) Java generated applications, run on Tomcat 9.

### [Software Requirements](#Software+Requirements)

* Java 8 or higher

### Details on the implementation

#### [At development time](#At+development+time)

[Use annotations for servlet definition property](https://wiki.genexus.com/commwiki/wiki?29399) must be set to Yes, at prototyping time.

For optimization purposes (reducing annotation searches during application deployment), content similar to the following is automatically added to the context.xml file:

```
<Context reloadable="true" privileged="true">
    <WatchedResource>WEB-INF/web.xml</WatchedResource>
    <JarScanner><JarScanFilter pluggabilitySkip="*" tldSkip="*" pluggabilityScan="GXWebSocket.jar"/></JarScanner>
</Context>
```

Reference [here](https://tomcat.apache.org/tomcat-8.0-doc/config/jar-scan-filter.html).

**Note:** For Tomcat 8, the same entry is included in the context.xml file. In the case of Tomcat 7, the [GXJarScanner](https://www.genexus.com/developers/websac?en,,,37610) is used.

#### [At production time](#At+production+time)

When taken to production, build the deployment package using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092). In that case, it isn't necessary to generate annotated servlets, so it isn't mandatory to generate using [Use annotations for servlet definition property](https://wiki.genexus.com/commwiki/wiki?29399) = Yes. The reason is that the descriptor file (web.xml) declares all the servlets explicitly.


|  |
| --- |
| **Backlinks** |
| [HowTo: Change Windows Registry values for Tomcat](https://wiki.genexus.com/commwiki/wiki?21926) |

---
