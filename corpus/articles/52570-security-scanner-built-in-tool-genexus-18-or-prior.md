---
title: "Security Scanner built-in tool (GeneXus 18 or prior)"
source_id: 52570
source_url: https://wiki.genexus.com/commwiki/wiki?52570
genexus_version: "18"
---

# Security Scanner built-in tool (GeneXus 18 or prior)

**Note**: This tool replaces the [GeneXus Security Scanner extension](https://wiki.genexus.com/commwiki/wiki?39951,,) available in the GeneXus Marketplace. You need to be familiar with the OWASP security issues to use it.

The Security Scanner tool scans/checks objects within a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) looking for potential security issues according to OWASP's Top 10 Security Risks.

You can open the Security Scanner Configuration Window by selecting the following options from the GeneXus IDE toolbar: Tools > Security > Security Scanner

`[imagen omitida: wiki id 46438]`

or apply it to a particular object or a subset of them using the "Security Scanner" Contextual Menu:

`[imagen omitida: wiki id 46439]`

The Environment rules will be applied only when a full scan is triggered. When a partial scan is executed (using the Contextual Menu) the Environment rules will not be applied.

### [Scan configuration](#Scan+configuration)

The tool will scan the following types of objects:

* Environment (rules #136 and #137)
* Generator (rule #106)
* [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)
* [Transactions](https://wiki.genexus.com/commwiki/wiki?1908)
* [Procedures](https://wiki.genexus.com/commwiki/wiki?6293)
* [Attributes](https://wiki.genexus.com/commwiki/wiki?7240)
* [Domains](https://wiki.genexus.com/commwiki/wiki?7221)

The tool will not scan the following types of objects:

* Referenced module objects
* Unit test objects

### [Output](#Output)

When the scan is performed using the IDE the result will be shown on a new Output Section called Security Scanner.

`[imagen omitida: wiki id 47877]`

### [Rules configuration](#Rules+configuration)

For every rule, you can configure its level of severity or disable it in the Configuration Window.

`[imagen omitida: wiki id 46440]`

### [Parameter encryption #100](#Parameter+encryption+%23100)

*Security Scanner* analyzes objects to check if their parameters are encrypted; that is, if their [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) is set to "*Session key*" or "*Site key.*"  
If a *<Parameter encryption>* issue is found, *Security Scanner* will show the following message:

```
error 100: Parameters encryption is not set
```

### [HTML format #101](#HTML+format+%23101)

*Security Scanner* analyzes attributes, variables, and textblocks checking if their [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) has been set to "*HTML*" or "*Raw HTML.*"  
If an *<HTML format>* issue is found, *Security Scanne*r will show a message like this:

```
error 101: HTML Textblock detected in WebForm (Name 'htmltxtblock' Type 'HTML'. Name 'rawhtmltxtblock' Type 'Raw HTML'. )
```

### [Authorization #102](#Authorization+%23102)

Security Scanner analyzes Web Panels and Transactions in the KB checking if they call an Authorization program (procedure). This rule does not apply to Master Pages and Web Components.  
If an *<Authorization>* issue is found, *Security Scanner* will show a message like this:

```
error 102: No access control configured for this object
```

When using Xev2, the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) is checked ([GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) usage).

### [SQL Command #103](#SQL+Command+%23103)

*Security Scanner* analyzes KB objects looking for [SQL commands](https://wiki.genexus.com/commwiki/wiki?8623).  
If a *<SQL Command>* issue is found, *Security Scanner* will show a message like this:

```
error 103: SQL Command usage found in source
```

i.e.: **SQL UPDATE UserInfo SET UserWelcomeMessage='[!&UserWelcomeMessage!]' WHERE UserId=[!&UserId!]**

### [Link Command #104](#Link+Command+%23104)

*Security Scanner* analyzes KB objects to check if there is a dynamic command link without parameters.  
If a *<Link command>* issue is found, *Security Scanner* will show a message like this:

```
error 104: Parameterless LINK command usage found in source
```

i.e.: **Link(&SomeWebPanel)**

### [Http Protocol #105](#Http+Protocol+%23105)

*Security Scanner* analyzes Web Panels and Procedures checking if HTTPS protocol has been specified. This means checking if the [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) has been set to “*Secure (HTTPS).*”

In the case of a SOAP Procedure, it will inherit the protocol specification from the environment so it will trigger the rule when an insecure protocol specification is configured on the environment. This apply since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).  
If an *<Http protocol>* issue is found, *Security Scanner* will show a message like this:

```
error 105: HTTP protocol is not Secure
```

### [Javascript Debug Mode #106](#Javascript+Debug+Mode+%23106+)

Security Scanner analyzes the [Javascript debug mode property](https://wiki.genexus.com/commwiki/wiki?17384) at generator level; when enabled, the following message will be displayed:

```
error 106: Javascript Debug Mode is enabled
```

### [Web Components URL Access #107](#Web+Components+URL+Access+%23107)

*Security Scanner* analyzes KB objects set as Web Components checking if URL Access for them has been enabled. This means checking if the [URL Access property](https://wiki.genexus.com/commwiki/wiki?7868) has been set to “*Yes.*”  
If a *<WC URL Access>* issue is found, *Security Scanner* will show a message like this:

```
error 107: Web Component with URL Access enabled 
```

### [C#, Java, Ruby native code usage #108](#C%23%2C+Java%2C+Ruby+native+code+usage+%23108)

*Security Scanner* analyzes KB objects' source section checking for the Java or C-Sharp command.  
The following message is displayed:

```
error 108: Native Code usage found in source
```

### [HttpResponse data type usage #109](#HttpResponse+data+type+usage+%23109)

*Security Scanner* analyzes KB objects' variables section checking for [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) usage.  
The following message is displayed:

```
error 109: HttpResponse Data Type usage in variables (Name 'HttpResponse' Type 'HttpResponse'. )
```

### [LDAPClient GetAttribute method usage #110](#LDAPClient+GetAttribute+method+usage+%23110)

*Security Scanner* analyzes KB objects' source section checking for [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) GetAttribute method usage.  
The following message is displayed:

```
error 110: LDAPClient.GetAttribute() pattern detected in source 
```

### [Directory data type usage #111](#Directory+data+type+usage+%23111)

*Security Scanner* analyzes KB objects' variables section checking for [Directory data type](https://wiki.genexus.com/commwiki/wiki?6567) usage.  
The following message is displayed:

```
error 111: Directory Data Type usage in variables (Name 'Directory' Type 'Directory'. )
```

### [File data type usage #112](#File+data+type+usage+%23112)

*Security Scanner* analyzes KB objects' variables section checking for [File data type](https://wiki.genexus.com/commwiki/wiki?6915) usage.  
The following message is displayed:

```
error 112: File Data Type usage in variables (Name 'File' Type 'File'. )
```

### [XMLReader ValidationType property usage #113](#XMLReader+ValidationType+property+usage+%23113)

*Security Scanner* analyzes KB objects' source section checking for [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) ValidationType property usage.  
The following message is displayed:

```
error 113: XmlReader Validation type property misconfiguration 
```

### [Shell function #114](#Shell+function+%23114)

*Security Scanner* analyzes KB objects' source section checking for [Shell function](https://wiki.genexus.com/commwiki/wiki?8502) usage.  
The following message is displayed:

```
error 114: Shell function usage found in source
```

### [Random function #115](#Random+function+%23115)

*Security Scanner* analyzes KB objects' source section checking for [Random function](https://wiki.genexus.com/commwiki/wiki?8479) usage.  
The following message is displayed:

```
error 115: Random function usage found in source
```

### [SetCookie function #116](#SetCookie+function+%23116)

*Security Scanner* analyzes KB objects' source section checking for [SetCookie function](https://wiki.genexus.com/commwiki/wiki?6878) usage.  
The following message is displayed:

```
error 116: SetCookie function usage found in source 
```

Whenever possible, use the [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) and enable the HttpOnly property.

### [Form.HeaderRawHTML property #117](#Form.HeaderRawHTML+property+%23117)

*Security Scanner* analyzes the source section of WebPanels and Transactions checking for Form.HeaderRawHTML property usage.  
The following message is displayed:

```
error 117: HeaderRawHTML method usage found in source
```

### [Form.JScriptSrc property #118](#Form.JScriptSrc+property+%23118)

*Security Scanner* analyzes the source section of WebPanels and Transactions checking for Form.JScriptSrc property usage.  
The following message is displayed:

```
error 118: JScriptSrc method usage found in source
```

### [IsPassword property #119](#IsPassword+property+%23119)

*Security Scanner* analyzes the source section of WebPanels and Transactions checking for IsPassword property usage.  
The following message is displayed:

```
error 119: IsPassword Property enabled in WebForm
```

### [External Object usage #120](#External+Object+usage+%23120)

*Security Scanner* analyzes KB objects' source section checking for [External object](https://wiki.genexus.com/commwiki/wiki?5669) usage.  
The following message is displayed:

```
error 120: External Object usage in variablesName 'CustomType' Type 'CustomType'. 
```

For Xev2; GAM and GXflow External Objects are excluded.

### [User Control usage #121](#User+Control+usage+%23121)

*Security Scanner* analyzes the WebForm section of [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) and [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) for [User Controls](https://wiki.genexus.com/commwiki/wiki?5273) usage.  
The following message is displayed:

```
error 121: UserControl detected in WebForm Name 'CustomControl' Type 'CustomControl'.
```

### [Cookie data type usage #124](#Cookie+data+type+usage+%23124)

*Security Scanner* analyzes KB objects' variables section checking for [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) usage.  
The following message is displayed:

```
error 124: Cookie Data Type usage in variables (Name 'Cookie' Type 'cookie'. )
```

Whenever possible, enable the HttpOnly property.

### [XmlWriter WriteRawText method usage #125](#XmlWriter+WriteRawText+method+usage+%23125)

*Security Scanner* analyzes KB objects' source section checking for the [XMLWriter](https://wiki.genexus.com/commwiki/wiki?6938) [WriteRawText method](https://wiki.genexus.com/commwiki/wiki?7075) usage.  
The following message is displayed:

```
error 125: XmlWriter.WriteRawText() pattern detected in source 
```

### [SDT.FromXml() pattern usage (#126)](#SDT.FromXml%28%29+pattern+usage+%28%23126%29)

*Security Scanner* analyzes KB objects' source section checking for the [FromXml method - SDT](https://wiki.genexus.com/commwiki/wiki?8788) usage.  
The following message is displayed:

```
error 126: SDT.FromXml() pattern detected in source
```

### [SDT.FromJson() pattern usage (#127)](#SDT.FromJson%28%29+pattern+usage+%28%23127%29)

*Security Scanner* analyzes KB objects' source section checking for the [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) usage.  
The following message is displayed:

```
error 127: SDT.FromJson() pattern detected in source
```

### [XMLReader ReadRawXML method usage (#128)](#XMLReader+ReadRawXML+method+usage+%28%23128%29)

*Security Scanner* analyzes KB objects' source section checking for the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)'s [ReadRawXML method](https://wiki.genexus.com/commwiki/wiki?7099) usage.  
The following message is displayed:

```
error 128: XmlReader.ReadRawXML() pattern detected in source 
```

### [Blob usage (#129)](#Blob+usage+%28%23129%29)

*Security Scanner* analyzes KB objects' variables section checking for [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) usage.  
The following message is displayed:

```
error 129: Blob usage detected in object (Variable: blob) 
```

### [JSEvent usage (#130)](#JSEvent+usage+%28%23130%29)

*Security Scanner* analyzes KB objects' source section checking for the [JSEvent method](https://wiki.genexus.com/commwiki/wiki?8809) usage.  
The following message is displayed:

```
error 130: JSEvent usage found in source 
```

### [SoapHeaderRaw (#131)](#SoapHeaderRaw+%28%23131%29)

*Security Scanner* analyzes KB objects' source section checking for the [SoapHeaderRaw](https://wiki.genexus.com/commwiki/wiki?33708,,) nonstandard function usage.  
The following message is displayed:

```
error 131: soapHeaderRaw usage found in source
```

### [PathToURL usage (#132)](#PathToURL+usage+%28%23132%29)

*Security Scanner* analyzes KB objects' source section checking for the [PathToURL function](https://wiki.genexus.com/commwiki/wiki?9563) usage.  
The following message is displayed:

```
error 132: PathtoUrl usage found in source
```

### [XMLReader ReadExternalEntities (#133)](#XMLReader+ReadExternalEntities+%28%23133%29)

*Security Scanner* analyzes KB objects' source section checking for the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) [ReadExternalEntities Property](https://wiki.genexus.com/commwiki/wiki?6967) usage.  
The following message is displayed:

```
error 133: XmlReader ReadExternalEntities pattern detected in source
```

### [SDT.FromXmlFile() pattern usage (#134)](#SDT.FromXmlFile%28%29+pattern+usage+%28%23134%29)

*Security Scanner* analyzes KB objects' source section checking for the [FromXmlFile method](https://wiki.genexus.com/commwiki/wiki?24070) usage.  
The following message is displayed:

```
error 134: SDT.FromXmlFile() pattern detected in source
```

### [SDT.FromJsonFile() pattern usage (#135)](#SDT.FromJsonFile%28%29+pattern+usage+%28%23135%29)

*Security Scanner* analyzes KB objects' source section checking for the [FromJsonFile method](https://wiki.genexus.com/commwiki/wiki?24070) usage.  
The following message is displayed:

```
error 135: SDT.FromJsonFile() pattern detected in source
```

### [Parameter encryption (Environment) #136](#Parameter+encryption+%28Environment%29+%23136)

*Security Scanner* analyzes the KB Environment to check if its parameters are encrypted; that is, if its [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) is set to "*Session key*" or "*Site key.*"  
If a *<Parameter encryption>* issue is found, *Security Scanner* will show the following message:

```
error #136: Parameters encryption is not set (Environment)
```

### [Http Protocol #137](#Http+Protocol+%23137)

*Security Scanner* analyzes the KB Environment checking if HTTPS protocol has been specified. This means checking if the [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) has been set to “*Secure (HTTPS).*”  
If an *<Http protocol>* issue is found, *Security Scanner* will show a message like this:

```
error #137: Http protocol is not Secure
```

### [SameSite Cookie Attribute (#138)  (This rule is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,))](#SameSite+Cookie+Attribute+%28%23138%29+%28This+rule+is+available+since+wiki%3F48247%2CGeneXus%2B17%2BUpgrade%2B5+GeneXus+17+Upgrade+5%29)

*Security Scanner* analyzes the KB Environment checking if [SameSite cookie attribute property](https://wiki.genexus.com/commwiki/wiki?47685) is configured with the value None.

If that is the case *Security Scanner* will show a message like this:

```
error: Code: 138 - SameSite Cookie Attribute is set to None
```

### [Advanced configuration](#Advanced+configuration)

#### [Security objects Whitelist](#Security+objects+Whitelist)

`[imagen omitida: wiki id 46418]`

Using this field, you can select objects and rules to be whitelisted on the analysis.

`[imagen omitida: wiki id 46419]`

`[imagen omitida: wiki id 46420]`

#### [Authorization Procedure](#Authorization+Procedure)

`[imagen omitida: wiki id 46418]`

If you are not using GAM, this field allows you to insert a Procedure or Master Page that contains the authorization logic. The scan will signal with an error the objects that do not contain the call for the authentication Procedure or use the Master Page selected.

`[imagen omitida: wiki id 46421]`

If you put some other type of object (not Master Page and not Procedure) the scan will ignore this configuration.

### [Running Security Scanner using MsBuild task](#Running+Security+Scanner+using+MsBuild+task)

Define a new Task called Scan that allows you to run the scanner in an MSBuild script. This task can be included in any server-side pipeline of CI/CD.

This task will execute the configuration previously set through the Security Scanner Configuration Window.

```
<Project DefaultTargets="SecurityScan" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

    <Import Project="$(GXInstall)\genexus.tasks.targets"/>
    <Import Project="$(GXInstall)\security.tasks.targets"/>

    <Target Name="SecurityScan">
        <OpenKnowledgeBase Directory="$(KBDir)"    />
        <SecurityScan XmlOutputFile="securityTest.xml"/>
    </Target>
</Project>
```

By specifying the XmlOutputFile you get Errors and Warnings in XML format.

### [Running the Scanner from the command line](#Running+the+Scanner+from+the+command+line)

```
msbuild securityscantest.msbuild /verbosity:minimal /t:SecurityScan /p:KBDir=c:\mykbpath /p:GXInstall=c:\genexusinstalldir
```

### [Availability](#Availability)

This tool is available since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).
