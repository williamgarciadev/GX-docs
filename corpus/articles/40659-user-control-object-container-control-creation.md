---
title: "User Control Object - Container control creation"
source_id: 40659
source_url: https://wiki.genexus.com/commwiki/wiki?40659
genexus_version: "18"
---

# User Control Object - Container control creation

Continuing with the example shown [here](https://wiki.genexus.com/commwiki/wiki?39356) regarding the UI control "Card" provided by Semantic UI CSS Framework, and upon supposing the case where instead of having a fixed content in the extra content section you want to have the freedom to include whatever you wish there (slot), what should you do?

The GeneXus [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) enables the modeling of the referred scenario by using an HTML 5 standard element known as slot with which you have a placeholder for any content that you might want to add in a specific HTML structure. Additionally, the slot is reusable, so you may define structures once and then use them as many times as necessary.

In order to define the slot, a slot must be added to the extra content section (which is an html div element inside the User Control) for it to be filled out by those willing to use the control.

Considering [the same example](https://wiki.genexus.com/commwiki/wiki?39356) (control Card), the code will be as follows:

```
<div class="ui card" {{Click}} > 
   <div class="image"> 
      <img src="{{ImageUrl}}"> </div> 
      <div class="content">
         <a class="header">{{Title}}</a> 
         <div class="meta"> <span class="date">{{MetaInfo}}</span> </div>
         <div class="description"> {{Description}} </div> 
     </div> 
   <div class="extra content">
       <a> <i class="user icon"></i> {{ExtraContent}} </a> 
       <slot name="extraContent" />
   </div> 
</div>
```

As you open the [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), you will see that inside the User Control you now have a table called "extraContent" over which you may drag and drop any element from the toolbox.   
In this case, it will simply bee added a TextBlock to define a new caption:

`[imagen omitida: wiki id 39393]`

When you execute the change afterward, you will see that the footer changed and now shows the text defined in the added TextBlock:

`[imagen omitida: wiki id 39394]`


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
