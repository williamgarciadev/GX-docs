---
title: "Java Generator Requirements"
source_id: 54302
source_url: https://wiki.genexus.com/commwiki/wiki?54302
genexus_version: "18"
---

# Java Generator Requirements

This article outlines the Java Generator requirements for development work.

### [Java SDK](#Java+SDK)

To build Java applications, keep in mind the relationship between [Gradle and Java](https://wiki.genexus.com/commwiki/wiki?52359) versions, which is available here: [Compatibility Table](https://docs.gradle.org/current/userguide/compatibility.html).

### [DBMS Drivers](#DBMS+Drivers+)

At build time, an internet connection to gradle.org is required in several cases; for example, to get the required version of a DBMS driver.

However, in the case of the [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713), the necessary drivers are not available, so you must download the files from the [SAP Hana Client for Windows](https://tools.hana.ondemand.com/#hanatools) and copy the JAR file to the "lib" folder of the model's web folder.

The same is true for [DB2 Universal Database](https://wiki.genexus.com/commwiki/wiki?1961). Therefore, you must perform the same procedure.

### [Troubleshooting](#Troubleshooting)

The following error will be displayed if there are version compatibility problems between Gradle and Java:

Could not open proj generic class cache for build file

The solution is to install a newer version of Gradle. To do this, follow the steps below:

1. Check the [Compatibility Table](https://docs.gradle.org/current/userguide/compatibility.html) and select the minimum version of Gradle that supports the JDK you want to use.
2. Download the latest major version of Gradle that has been released according to the previous step.  
   You can check these pages for the available version: [Gradle Distribution](https://services.gradle.org/distributions/) and [Gradle Installation](https://gradle.org/install/).
3. Open the command line (CMD) and navigate to the GeneXus installation folder on your computer, specifically to the gxjava directory. For example: "c:\Program Files (x86)\GeneXus\GeneXus18\gxjava". Run the following command:

   ```
   gradlew wrapper --gradle-version=<enter version> --distribution-type=bin
   ```

   When you run this command, the Gradle version that you downloaded will be configured to be used in the next action performed in the folder. This allows the new version of Gradle to be available for any [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB) construction in GeneXus.
4. To update the Gradle configuration in the KB directory that gave the error, in the GeneXus Toolbar select Tools >CMD Environment Directory, and open the Windows command console (CMD). Next, navigate to the Web folder of the model that uses the Java Generator and execute the command from the previous step.

#### [Sample](#Sample)

Suppose you want to use JDK 19, for which the minimum Gradle version supported is 7.6. After checking the Gradle distribution, you realize that version 7.6.1 exists and you install it. Go to the cmd and navigate to the GeneXus installation folder and execute the command:

```
gradlew wrapper --gradle-version=7.6.1 --distribution-type=bin
```

Now go to GeneXus, open the Web folder of the model (C:\KB\LightCRM\JavaEnv\web), and execute the same line. If everything is OK, you will get a message like the following:

```
Configure project :
apply services.webnotifications.genexus.gradle

BUILD SUCCESSFUL in 10s
1 actionable task: 1 executed

c:\KB\LightCRM\JavaEnv\web>gradlew getDeps
Downloading https://services.gradle.org/distributions/gradle-7.6.1-bin.zip
...........10%............20%...........30%............40%............50%...........60%............70%............80%...........90%............100%

Welcome to Gradle 7.6.1!

Here are the highlights of this release:
 - Added support for Java 19.
 - Introduced `--rerun` flag for individual task rerun.
 - Improved dependency block for test suites to be strongly typed.
 - Added a pluggable system for Java toolchains provisioning.

For more details see https://docs.gradle.org/7.6.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)
```

### [See Also](#See+Also)

[GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) | [Category:GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) |
| [Toc:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) |

---
