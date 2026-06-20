---
title: "Generate strong named assemblies property"
source_id: 8950
source_url: https://wiki.genexus.com/commwiki/wiki?8950
genexus_version: "18"
---

# Generate strong named assemblies property

This causes the assemblies generated and compiled with this feature to have a unique name.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | It determines the programs that don’t have a strong name. This is the default value. |
| **Yes** | It determines the programs that have a strong name. |

### [Description](#Description)

It determines whether the generated main and DLL programs have ‘strong names’ or not.

It gives access to a series of important advantages provided by the .Net Framework, such as, Deployment in the GAC (Global Assembly Cache), Security configuration for the assembly (it allows configuring the security to run assemblies coming from unsafe zones).

To generate the Key identifying the object, the generator searches for a key.snk at compilation time (typically dataxxx). If it does not find the key.snk, it generates one.

This is useful if a company has a generated key, as it can keep using it for all its products (for this, you must copy the file with the key as key.snk in the model directory). All the standard programs provided by the generator are already distributed with a ‘strong name’.

When the Generated Strong Name Assemblies value is set to Yes, the following values are configured in the assembly's file:

-  Assembly Description = Empty  
-  Assembly Product = “Design”  
-  Assembly Version = The same as “Assembly version number” generator property  
-  Assembly Title = “GxAssembly”

#### [Note](#Note)

To use this feature, you must install the **.net framework SDK 1.1** in the development environment, to be able to execute the sn.exe and generate the file with the Key.  Besides, in the ‘PATH’ environment variable, you must configure the path to the required tools so that the compiler finds them (the path is similar to the following one: <PROGRAM FILES\MICROSOFT.NET\SDK\V1.1\bin" ).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Platforms:** Web(.Net)

### [See Also](#See+Also)

[Assembly version number property](https://wiki.genexus.com/commwiki/wiki?9226)  
[http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpguide/html/cpconstrong-namedassemblies.asp


|  |
| --- |
| **Backlinks** |
| [Assembly version number property](https://wiki.genexus.com/commwiki/wiki?9226) |

---
