---
title: "User Control Object - Scripts definition and usage"
source_id: 40598
source_url: https://wiki.genexus.com/commwiki/wiki?40598
genexus_version: "18"
---

# User Control Object - Scripts definition and usage

It is a good practice to include your base Javascript as much as possible in one or more base Javascripts and specify these files by using a Base Library in GeneXus. Thus, every time a user control is used in some [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), GeneXus includes it automatically.

Anyway, sometimes you want to include some Javascript code before showing the control, and sometimes after showing the control. To achieve this in GeneXus, you should use the Script tag in the Properties tab of a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356).  
  
Imagine that you want to create the rendering of the following markup for your control:

```
<div class="ui-widget">
  <label for="tags">Tags:
  </label> <input id="tags">
</div>
```

And after that, you want to execute the following script:

```
$("#tags").autocomplete({
source: availableTags});
```

To allow the creation of this kind of controls, GeneXus User Controls provide a way to declare a Script Tag in their Properties tab. So, you should define the following in the Properties tab of your User Control object:

```
<Script Name="Autocomplete" When="AfterShow">
  $("#tags").autocomplete({ source: availableTags});
</Script>
```

Also, depending on when your script should execute, there are two possibles values for When property:

* AfterShow: The Script will be executed after the control is rendered on the page.
* BeforeShow: The Script will be executed before the control is on the page; you should not manipulate the Document Object Model ([DOM](https://www.w3schools.com/js/js_htmldom.asp)) at this stage.

Additionally, the User Control object accepts Public and Private methods. Public methods are those that can be called from the code while Private methods are simply defined to be generated.

If the Script does not have the When property, then it is a public method:

```
<script Name="MyMethod" Parameters="myparm, otroparm">
     alert (myparm + otroparm);
</script>
```

Notes:  
- Methods with return are not supported. To solve that, you can use a property and assign it there and then consult it.  
- There is no type checking by the specifier, so Parameters is simply the list of parameter names.

If you want to define a private method simply put an \_ at the beginning of the name of the script:

```
<script Name = "_ myPrivateMethod"> ....
```

Sometimes using just the {{DataElement}} to specify what is the element of the DOM that is holding the value of your control is not enough because you are based in more complex controls that hold the value in other places.  
In those cases there is a way to participate in the set and get data operations over your control, so each time GeneXus assign a value to your control you can participate and every time GeneXus get the value of your control you can participate, too.

So, in this cases, you can define a Script tag with the When="beforegetdata" and When="beforesetdata".

See below a sample of a control based on the [Ace Editor](https://ace.c9.io/):

First of all you define the AceEditorControl and set the properties IsControlType=true DataTypeFilter=varchar,longvarchar,character. In this way, you are defining that the AceEditorControl can be selected as a control type for [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371) and [Character](https://wiki.genexus.com/commwiki/wiki?6777) attributes and variables.

The problem here is that the AceEditorControl is not maintaining the value in the HTML DOM, so you need to do some extra work defining Script Tags in the Properties Tab:

```
<Definition auto="false">
  <Property Name="Width" Type="Numeric" Default="600"/>
  <Property Name="Height" Type="Numeric" Default="400"/>
  <script Name="GetValue" When="BeforeGetData">
          return this.myEditor.getValue();  
  </script> 
  <script Name="SetValue" When="BeforeSetData">
        if (this.myEditor)
              this.myEditor.setValue(valueObject.value); 
  </script>
  <script Name="Show" When="AfterShow">  
   
this.myEditor = ace.edit("aceeditor");        
  
this.myEditor.setOptions({
    theme: "ace/theme/xcode",
            autoScrollEditorIntoView: true,
            maxLines: Math.trunc(($(window).height()-60)/16),
            minLines: Math.trunc(($(window).height()-60)/16),
    mode: "ace/mode/javascript"
 
  });  
this.myEditor.setValue(valueObject.value);

  </script>
</Definition>
```


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
