---
title: "User Control Object - Definition of properties (GeneXus 18 Upgrade 1 or prior)"
source_id: 53689
source_url: https://wiki.genexus.com/commwiki/wiki?53689
genexus_version: "18"
---

# User Control Object - Definition of properties (GeneXus 18 Upgrade 1 or prior)

You have to identify the properties you want to define for your [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) with {{ }} inside the **Screen Template** tab. Even though in general, GeneXus infers all the correct definition for the properties directly from the **Screen Template**, since ambiguities may exist, they can be modified in the Properties section of the object.

## [Properties](#Properties)

As detailed previously, the most basic tag type is the property. A {{name}} tag in a basic template will try to find the *name* key in the current context. If there is no name key, the parent contexts will be checked recursively. If the top context is reached and the name key is still not found, nothing will be rendered.

All properties are HTML escaped by default. If you want to return unescaped HTML, use the triple mustache.

A property "miss" returns an empty string.

## [Types of properties](#Types+of+properties)

The types of properties available are the following:

* [Character](https://wiki.genexus.com/commwiki/wiki?6777)
* [Numeric](https://wiki.genexus.com/commwiki/wiki?6793)
* Decimal
* [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207)
* [Boolean](https://wiki.genexus.com/commwiki/wiki?4374)
* [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)

## [How to define properties](#How+to+define+properties)

By default, GeneXus uses the following conventions when interpreting the **Screen Template** section:

* {{Test}} --> Defines the Test property as a string.
* {{Test:one|two|three}} --> Defines the Test property as an enumerated value and defines its possible values as one, two, three.
* {{#Test}} --> Defines the Test property as custom; basically, any SDT is accepted.
* --> Defines the Test property as a string with the specific purpose of assigning raw HTML code to it.

### [Defining a property](#Defining+a+property)

To define a property, this syntax {{ }} is used. For example, to add a property called "Make," the syntax is as follows:

{{Make}}

GeneXus will assume it is a property of string type because its type hasn't been explicitly declared.

### [Defining a property of declared type](#Defining+a+property+of+declared+type)

Continuing with the previous example, to define a type for the "Make" property, the syntax is as follows:

{{Make:<data type>}}

Where <data type> must be one of the data types available.

The mappings between GeneXus data types and User Control's <data type> are the following:

* Character --> string
* Numeric --> numeric
* Decimal --> numeric with decimals
* Boolean --> boolean
* SDT --> sdt

In addition, to define enumerated values of Make, the declaration must be:

{{Make:Fiat|Volkswagen|Toyota|Peugeot|Renault}}

### [Defining a property with default value](#Defining+a+property+with+default+value)

An initial value can be assigned to a Property; to do so, the operator = (equals) must be used. The definition looks as follows:

* {{Test="HELLO"}} --> the Test property takes the default value "HELLO"
* {{Test:one|two|three=one}} --> the Test property, within the enumerated values that have been declared, takes the default value "one"
* {{IsActive=true}} --> the IsActive property takes the default value "true"

### [Defining a collection property](#Defining+a+collection+property)

To define elements in iterative blocks, it is possible to set a property as a Collection.  
So, to define for example a list of category values, the declaration would be:

```
 <UL>
 {{#Categories}}
    <LI>{{Name}}</LI>
 {{/Categories}}
 </UL>
```

The Categories property preceded by the # (sharp) character allows indicating that it is an element that can be iterated (and within this iterative element the items with their corresponding names are defined using the {{Name}} property).

If you are using a Collection of Basic types such as Character, Numeric, Date (and so on) use the syntax {{.}} to reference the element within the simple collection, for example:

```
{{#SimpleCollection}}
{{.}}
{{/SimpleCollection}}
```

### [Defining a property to which be able to assign Raw HTML](#Defining+a+property+to+which+be+able+to+assign+Raw+HTML)

You can define a property with triple mustache syntax to include raw HTML to the object.

For example, if you want to create an HTML button that contains a title, you can define the property in the Screen Template of the User Control. After that, you can assign the value of the property with the HTML code in some GeneXus event:

myButton.customData = '<h2> The Button Element </ h2> <button type = "button"> I'm a button! </ button>'

The result in execution will be a Header with the title and a button with a text.

### [Applying a condition to the value of a property](#Applying+a+condition+to+the+value+of+a+property)

If for some reason you want to omit a certain output if a certain property has no value, a condition must be applied to the property to achieve this behavior. Properties accept the use of conditionals to achieve the above behavior. Conditionals are represented with a question mark (?).

For example:

```
{{AdditionalComments?}} text to include {{/AdditionalComments}}
```

In this case, the AdditionalComments property can be empty; therefore, it is conditioned so that if it is empty, it is not shown.

## [Example 1 - applying condition in a property](#Example+1+-+applying+condition+in+a+property)

The following Alert control is to be implemented:

`[imagen omitida: wiki id 39545]`

Its variations simply differ in the class (CSS style); it is, therefore, reasonable to think of creating a single control with an enumerated property that indicates the desired type of Alert: warning, info, success or danger. This is modeled as shown below in the Screen Template of the control:

```
  <div {{OnClick}} class="Alert Alert--{{Type:info|warning|success|danger}}">
  {{Text}} 
  </div>
```

Then, when you place the control on the screen, you can choose the type of Alert to use.

`[imagen omitida: wiki id 39546]`

If you pay attention to the image above, you can see that there are 5 types of Alerts. However, 4 values have been defined. The reason is that the empty value is also a possible value, and in this case, the Alert-- class doesn't have to be concatenated.  
To achieve this, a condition has to be applied to the Type property value:

```
  <div {{OnClick}} class="Alert {{Type?}}Alert--{{Type:info|warning|success|danger}}{{/Type}}">
  {{Text}} 
  </div>
```

As a result of applying a condition to this property, the Alert--{{Type}} class will be ignored, with only the Alert class remaining in the control.

## [Example 2 - iterating a multi-level SDT](#Example+2+-+iterating+a+multi-level+SDT)

Let's suppose you need to iterate the following SDT in the User Control:

`[imagen omitida: wiki id 46537]`

As you see, the SDT has a collection of Rooms and each Room has a collection of Speakers and Tracks.  
To achieve this, the following properties definition template should be used:

```
{{#SDTConferences}} 
    {{#Rooms}}
        <!-- properties of room -->
           
        {{#Speakers}}
            <!-- properties of speaker -->
        {{/Speakers}}
                
        {{#Tracks}}            
            <!-- properties of track -->                
        {{/Tracks}}
    {{/Rooms}}
{{/SDTConferences}}
```
