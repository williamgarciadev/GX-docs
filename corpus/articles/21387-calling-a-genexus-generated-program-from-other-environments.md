---
title: "Calling a GeneXus generated program from other Environments"
source_id: 21387
source_url: https://wiki.genexus.com/commwiki/wiki?21387
genexus_version: "18"
---

# Calling a GeneXus generated program from other Environments

If you want to execute a GeneXus program from other environments using the generated objects, you will need to understand the generation conventions in the selected platform:

* the generated object name.
* how the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) parameters are resolved.
* how to use *In*, *InOut* and *Out* type [parameters](https://wiki.genexus.com/commwiki/wiki?8220).
* extra parameters if needed.
* [platform specific data type mappings](https://wiki.genexus.com/commwiki/wiki?21392) and Structured Data Type mapping.

Suppose you have the GeneXus object "calltype01" with the following parm rule

```
parm(in:&c01,inout:&c02,out:&c03); // &c01 to &c03 are character data type
```

### [C#](#C%23)

From C#, you need to instantiate the class associated to the GeneXus object, call the *execute* method taking into account the parameter type. *In* parameters will be passed by value and the rest by reference.

* *In*: use the parameter by reference.
* *InOut*: use the C# ref keyword.
* *Out*: use the C# out keyword.

Following the example, you can call the object as follows:

```
String c01 = "csharp_c01" ;
String c02 = "csharp_c02" ;
String c03 = "csharp_c03" ;
new calltype01().execute(  c01, ref  c02, out  c03) ;  // c01 to c03 are strings
```

In this case the object is generated using the .Net Application namespace property.

If you use Collection data types, you will need to cast the element to *IGxCollection*.

### [Java](#Java)

When using Java, you need to instantiate the class associated to the GeneXus object with a context initializer, you can use "-1" to create a new context. Call the *execute* method taking into account the parameter type. All parameters are passed by value, for *InOut* and *Out* parameters you will need to do an extra handling before and after executing the method to set and retrieve the returned values.

* *In*: set the Java variable as is.
* *InOut*|*Out*: Create a 1 element array for each parameter type. Before and after calling the object you will need to assign and retrieve its value from the first position.

Following the example, you can call the object as follows:

```
String c01 = "java_c01" ;
String c02 = "java_c02" ;
String c03 = "java_c03" ;
String GXv_char02[] = new String [1] ;
String GXv_char03[] = new String [1] ;
GXv_char02[0] = c02 ;
GXv_char03[0] = c03 ;
new calltype01(-1).execute( c01, GXv_char02, GXv_char03) ;
String c022 = GXv_char02[0] ;  // c02 return value
String c033 = GXv_char03[0] ;  // c03 return value
```

Check the [Java Package Name Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9111,,) to locate the generated java and class files; you will need to qualify the call if you use this property.

If you use Collection data types, you will need to use the *GxObjectCollection* class.

### [Ruby](#Ruby)

When using Ruby, you need to instantiate the class associated to the GeneXus object with a context initializer, you can use *nil* to create a new context. Call the *execute* method taking into account that *In* and *InOut* parameters should be method arguments and *InOut* and *Out* parameters must be assigned as return values.

* *In*|*InOut*: set the Ruby variable as is in the method argument section.
* *InOut*|*Out*: assign them as return values.

Following the example, you can call the object as follows:

```
c01 = 'c01'
c02 = 'c02'
c03 = 'c03'
c02, c03 = Calltype01.new(nil).execute( c01, c02)
```

If you use Collection data types, you will need to use the *GX::Collection* class.

### [Considerations](#Considerations)

Depending on the case, you will need to add the [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) and other generated objects in your project.

When using Extended data types and [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)s in the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862), you will need to check the GeneXus generated code objects to do a correct data type mapping and add these references to the project.

For standard GeneXus SDT objects, you need to find the associated generated class. For example, if you create a *UserSDT* object, the generator will create a *SdtUserSDT* class in the target language.

### [See Also](#See+Also)

[Attribute and Variable Data types mapping by Generator](https://wiki.genexus.com/commwiki/wiki?21392)  
[Definition of type of parameters received (in, out, inout)](https://wiki.genexus.com/commwiki/wiki?8220)
