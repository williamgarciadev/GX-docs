---
title: "Compiler Options property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54275
source_url: https://wiki.genexus.com/commwiki/wiki?54275
genexus_version: "18"
---

# Compiler Options property (GeneXus 18 Upgrade 2 or prior)

Compiler options to send when GeneXus automatically calls the Java compiler.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The default value is -J-Xms512m -J-Xmx1024m. This means that the starting memory is 512 MB and can be up to 1 GB.

However, you can include any valid property for the Java compiler, depending on its version. To learn more, read the [Java documentation](https://docs.oracle.com/javase/9/tools/javac.htm#JSWOR627).
