---
title: "Prncmd command"
source_id: 14274
source_url: https://wiki.genexus.com/commwiki/wiki?14274
genexus_version: "18"
---

# Prncmd command

Sends control sequences to a printer.

### [Syntax](#Syntax)

**Prncmd** {\0nn | ‘*string’*}

**Where:**

*\0nn*  
    A 3 digit ASCII code preceded by a '\' (backslash)

*string*  
    A string containing characters (letters/digits).

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3)

### [Samples](#Samples)

To set the emphasize mode, most printers use the command ESC E 1; where ESC is the ASCII code 027. The Prncmd command should be:

```
Prncmd \027 E 1
```

Most printers will be set to condensed mode when they receive the 015 ASCII character. To send it, write the following printer command:

```
Prncmd \015
```

**Note**: The command's parameters depend on each printer's particularities, so refer to the printer manual to know which parameters you must send to your printer.
