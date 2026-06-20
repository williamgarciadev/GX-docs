---
title: "Compile options property"
source_id: 14015
source_url: https://wiki.genexus.com/commwiki/wiki?14015
genexus_version: "18"
---

# Compile options property

Defines compile options for the generation of programs when automatically called by GeneXus.

### [Scope](#Scope)

**Generators:** Cobol, RPG  
**Level:** Generator

### [Description](#Description)

For each program generated for the iSeries environment, an additional program called "compilation program" is also generated (in the CL language). Its function is to establish an environment for the compilation of the generated program and then compile it.

When the compilation program is generated, the current compilation options are "present" in the generated program (compiled immediately after the actual program).

The values that this property can take are listed in the table below.

|  |  |
| --- | --- |
| **SRC               NOSRC** | Specifies whether or not the compilation list includes the generated program source. When SRC is specified, the spool file that results from the compilation is NOT deleted. If NOSRC is specified, the spool file is eliminated if the compilation was successful. When SRC is specified, the compilation is a little slower because of the printing. |
| **XREF         NOXREF** | Indicates whether or not the compiler prints out a cross-reference report at the end of the compilation report. |
| **MAP             NOMAP** | Indicates whether or not the compiler prints out the data correlation used in the program, at the end of the compilation report. |
| **LIST           NOLIST** | Indicates whether or not the compiler prints out the generated program code. |
| **OPTIMIZE     NOOPTIMIZE** | The compiler will or will not try to optimize both the memory that is used and the program's execution time. This optimization noticeably increases compilation time. |
| **DEBUG NODEBUG** | This option eliminates or not all information that enables its debugging after the program has been compiled. This option turns out to be important because the size of the program is greatly reduced. |

**Note:** All desired values should be specified separated by one or more spaces, ensuring that contradictory values are not simultaneously indicated. If contradictory options are selected, only the first option will be considered.

### [Samples](#Samples)

`[imagen omitida: wiki id 22299]`
