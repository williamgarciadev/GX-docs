---
title: "Parameters Style property for Environments"
source_id: 46404
source_url: https://wiki.genexus.com/commwiki/wiki?46404
genexus_version: "18"
---

# Parameters Style property for Environments

Determines that the generated application will be using the standard URL query component style (identifying each parameter by its name) or another supported style.

### [Values](#Values)

|  |  |
| --- | --- |
| **Named** | Parameters in the URL are named and separated by an ampersand (&) |
| **Positional** | Parameters in the URL are positional and separated by a comma (,) |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

Parameters are named by default in new Environments. This is to follow common or standard URL writing styles and to simplify Web Application Firewall (WAF) configuration, among other benefits.

When the Parameters Style is Named, the parameters will appear in the query string of the URL as shown below:

```
?ParameterName1=value1&ParameterName2=value2...&ParameterNameN=valueN
```

In addition, the order of appearance in the query string is not relevant. The code below:

```
?ParameterName1=value1&ParameterName2=value2
```

is equivalent to:

```
?ParameterName2=value2&ParameterName1=value1
```

When the Parameters Style is Positional, the parameters will appear in the query of the URL as shown below:

```
?value1,value2,..valueN
```

#### [Notes](#Notes)

* Programs can read parameters received in a positional style even if the property is set to Named.
* [Dynamic calls](https://wiki.genexus.com/commwiki/wiki?8260) or [Dynamic links](https://wiki.genexus.com/commwiki/wiki?8446) use or create URLs in a positional style; they are not affected by this property.
* URLs of programs with [encrypted parameters](https://wiki.genexus.com/commwiki/wiki?8068) are not affected by this property.

#### Considerations when changing from Positional to Named

When you change this property from Positional to Named, all the code you wrote in GeneXus should keep working as usual.   
This doesn't apply if you already expected a named parameter in the query string (See Sample 2 - Compatibility issue when changing from Positional to Named).  
Other possible aspects to consider:

* Configuration of rules in the WAF
* UI Tests that verify the query string of the URL
* Length of the URL (since it is longer now).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

#### [Sample 1 - A typical case](#Sample+1+-+A+typical+case)

Consider the 'Client' object with this rule:

```
Parm(&Mode,&ClientId);
```

It is running on example.com and called by another object with:

```
Client('UPD',1)
```

It will appear in the URL as:

* "http://www.example.com/Client?Mode=UPD&ClientId=1", when using Parameters Styles set to Named, and as:
* "http://www.example.com/Client?UPD,1", when using Parameters Style set to Positional.

#### Sample 2 - Compatibility issue when changing from Positional to Named

Suppose you have two objects, and one calls the other with a line like the following:

```
MyWebObject(!"Parm1=MyValue")
```

MyWebObject:

```
parm(in:&MyParameter);
```

Source:

```
&ParameterValueStartPosition =  &MyParameter.IndexOf(!"=");
&ParameterValue = &MyParameter.SubString(&ParameterValueStartPosition+1)
msg(&ParameterValue)
```

When the Parameters Style is Positional, you get the message "MyValue." With Named parameters, to get "MyValue" again, you need to change the code on the caller to the following:

```
MyWebObject(!"Parm1%3DMyValue")
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

* [URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523)


|  |
| --- |
| **Backlinks** |
| [Link command](https://wiki.genexus.com/commwiki/wiki?8446) | [Link Function](https://wiki.genexus.com/commwiki/wiki?8444) |
| [Category:URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523) |

---
