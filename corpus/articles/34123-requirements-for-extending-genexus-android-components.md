---
title: "Requirements for Extending GeneXus Android components"
source_id: 34123
source_url: https://wiki.genexus.com/commwiki/wiki?34123
genexus_version: "18"
---

# Requirements for Extending GeneXus Android components

## [Environment setup](#Environment+setup)

1. Install:
   * [Android SDK](https://developer.android.com/studio/index.html) (please check [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449))
   * [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html) (Version 8 or later)
2. Set the required environment variables:
   * **ANDROID\_HOME**: Location of your Android SDK directory (e.g. C:\Users\%USERNAME%\AppData\Local\Android\Sdk).
   * **JAVA\_HOME**: Location of your JDK directory (e.g. C:\Program Files\Java\jdk1.8.0\_65).

**Tip**: If you are going to be compiling the sources often, you'll probably want to set these environment variables permanently in your system by going to **System Properties > Advanced > Environment Variables** on Windows.

Notice that to develop extensions you need internet connection; otherwise some components from the public repositories (such as Maven or Gradle) will not be able to be downloaded.
