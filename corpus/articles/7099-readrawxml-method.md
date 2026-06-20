---
title: "ReadRawXML method"
source_id: 7099
source_url: https://wiki.genexus.com/commwiki/wiki?7099
genexus_version: "18"
---

# ReadRawXML method

Obtains flat XML text from the start of an element.

### [Syntax](#Syntax)

**&***VarBasedOnXmlReader***.ReadRawXML()**  
  
**Type Retruned:**  
Character

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Allows obtaining flat XML text from the start of an element.

**Note**: It is valid only for nodes of the Element type.

XML

```
<NFe xmlns="http://www.portalfiscal.inf.br/nfe">
    <infNFe>
        <cobr>
            <fat>
                <nFat>13111</nFat>
                <vOrig>1731.65</vOrig>
                <vLiq>1731.65</vLiq>
            </fat>
            <dup>
                <nDup>0/</nDup>
                <dVenc>2016-08-08</dVenc>
                <vDup>1731.64</vDup>
            </dup>
            <dup>
                <nDup>0/</nDup>
                <dVenc>2016-08-08</dVenc>
                <vDup>1731.65</vDup>
            </dup>
            <dup>
                <nDup>0/</nDup>
                <dVenc>2016-08-08</dVenc>
                <vDup>1731.66</vDup>
            </dup>
        </cobr>
</NFe>
```

Code

```
&XMLReader.OpenFromString(&dadosxml)

// &AuxXML - Varchar
// &SubXml - Varchar
// &XMLReader - XMLReader
// &Sucess - Number

&sucess = &XMLReader.ReadType(NodeType.Element, 'infNFe')
&sucess = &XMLReader.ReadType(NodeType.Element, 'cobr')
&sucess = &XMLReader.ReadType(NodeType.Element, 'dup')

Do While (true)
    &AuxXML = &XMLReader.ReadRawXML()
    If (&AuxXML.Trim().Length() > 0)
        &SubXml.Add(&AuxXML)
    Else
        Exit
    EndIf
EndDo

&XMLReader.Close()
```

Output:

&SubXml will have 3 items with

Item1

```
<dup>
    <nDup>0/</nDup>
    <dVenc>2016-08-08</dVenc>
    <vDup>1731.64</vDup>
</dup>
```

Item2

```
<dup>
    <nDup>0/</nDup>
    <dVenc>2016-08-08</dVenc>
    <vDup>1731.65</vDup>
</dup>
```

Item3

```
<dup>
    <nDup>0/</nDup>
    <dVenc>2016-08-08</dVenc>
    <vDup>1731.66</vDup>
</dup>
```

### [Security Tips](#Security+Tips)

This method does not sanitize inputs. Proper sanitization is advised.

### [See Also](#See+Also)

[Read](https://wiki.genexus.com/commwiki/wiki?7049)  
[ReadType](https://wiki.genexus.com/commwiki/wiki?7048)  
[SetDocEncoding.htm](https://wiki.genexus.com/commwiki/wiki?7054)[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
