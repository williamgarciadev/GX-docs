---
title: "Hello World Container User Control"
source_id: 5387
source_url: https://wiki.genexus.com/commwiki/wiki?5387
genexus_version: "18"
---

# Hello World Container User Control

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

**Introduction**

One of the types of controls you can create when creating user controls (UC) are container controls. Container controls are controls that can have other controls inside them. This allows you to create very powerful controls, such as tab controls, accordions and so on.

Creating a container UC is just as easy as creating any other control. However, when you create a container UC you need two things:

·         a way of indicating a container region in your control (you can have as many as you wish). This will allow you to drop other controls within the container region at design time.

·         a way of retrieving the container region contents at runtime.

**Example**

|  |
| --- |
|  |

In this case, we have an accordion control which is, of course, a container control.  The control was defined with 3 container areas:

·         Region 1: used to place an icon

·         Region 2: used to place a title (in this case ?Second option?)

·         Region 3: used to place any panel content. In this case there is a button and a table.

In the following example, we will be creating a simple HelloWorldContainer control. The HelloWorldContainer control is almost identical to the basic HelloWorld control (explained [here](https://wiki.genexus.com/commwiki/wiki?4880)), except that it also defines an area where you can drop any other controls. This sample control makes no sense in practical terms, of course, but it is useful for learning purposes.  This sample will teach you how to create any kind of container controls.

The objective of this sample is to explain:

·         How to define a container area

·         How to retrieve the controls inside a container area

**Creating a HelloWorldContainer user control**

The HelloWorldContainer user control will be simply a table composed of two rows. The first row will display the ?Hello World Container? text, and the second row will have the container area where you can put any other controls. When it's finished, it will look as follows:

|  |
| --- |
|  |

 

Let's begin!

**1) Initial steps**

> 1.1) Download the latest version of the basic HelloWorld user control from [here](http://www.gxopen.com/gxopen/servlet/projectinformation?632) and copy it to the UserControls directory under GeneXus install.
>
> 1.2) Open the HelloWorld user control using the User Control Designer (UserControlEditor.exe), which is in the GX installation directory.
>
> |  |
> | --- |
> |  |
>
> When you open the control, you will see the following:
>
> |  |
> | --- |
> |  |
>
>  
>
> The HelloWorld container user control will only require changes in the ?Xsl Design Render tab? and the ?Jscript Runtime Render tab? , so there are no changes in the other tabs.
>
> **2) Defining a container area**
>
> 2.1) Open the XSL design render tab and look for this code:
>
> ```
>  <!-- HelloWorld design render -->
> ```
>
> <!-- /////////////////// Implement your render here ///////////////////-->
>
> <xsl:template name="RenderHelloWorld">
>
> <table cellSpacing="0" cellPadding="0" background="">
>
> <xsl:call-template name="AddTableStyleAttribute"/>
>
> <tbody>
>
> <tr>
>
> <td>
>
> <span>
>
> <xsl:call-template name="AddHelloWorldStyleAttribute"/>
>
> Hello World Container
>
> </span>
>
> </td>
>
> </tr>
>
> </tbody>
>
> </table>
>
> </xsl:template>
>
>  
>
> 2.2) Replace the above code with the one below:
>
> ```
> <!-- HelloWorldContainer design render -->
> ```
>
> <!-- /////////////////// Implement your render here ///////////////////-->
>
> <xsl:template name="RenderHelloWorld">
>
> <table cellSpacing="0" cellPadding="0" background="">
>
> <xsl:call-template name="AddTableStyleAttribute"/>
>
> <tbody>
>
> <tr>
>
> <td>
>
> <span>
>
> <xsl:call-template name="AddHelloWorldStyleAttribute"/>
>
> Hello World Container
>
> </span>
>
> </td>
>
> </tr>
>
> <tr>
>
> <td containerId="Container1">
>
> </td>
>
> </tr>
>
> </tbody>
>
> </table>
>
> </xsl:template>
>
> As you may have noticed, the code above creates a table for the control's design render. As explained before, the table has only two rows, one to place the ?Hello World Container? text and the other for the container area. So, where is the container area defined?
>
> To define a container area all you have to do is add the **ContainerId** attribute (and its value) to any HTML tag. After this, if you start GX and use the HelloWorld control you will be able to drop controls inside the second row of the table drawn before, which was defined as a container area.
>
> You will then use the specified ContainerId value to retrieve the container content at runtime. Take into account that you can define as many container areas as you wish but you will have to use different ContainerId values to identify each area.
>
> **3) Getting the container contents at runtime**
>
> 3.1) Open the Jscript Runtime Render tab
>
> 3.2) Replace the Show method with the following:
>
> this.show = function()
>
> {
>
> ///UserCodeRegionStart:<show> (do not remove this comment.)
>
> var buffer="<table width=" + this.Width + " height=" + this.Height + " border=1>";
>
> buffer+="<tr><td>";
>
> buffer+= '<a id="hworld1" href="#" style="color:rgb(' + this.FontColor.R + ',' + this.FontColor.G + ',' + this.FontColor.B + ')' + '; font-family:' + this.FontFace+ ';font-size:' + this.FontSize + 'pt;">Hello World!!!</a>';
>
> buffer+="</tr></td>";
>
> buffer+="<tr><td id='**UCrowContainer1**'></tr></td>";
>
> buffer+="</table>";
>
> this.setHtml(buffer);
>
> var childContainer = this.getChildContainer("Container1");
>
> gx.fn.setVisible(childContainer,1);
>
> gx.dom.el('**UCrowContainer1**').appendChild(childContainer);
>
> document.getElementById("hworld1").onclick = this.HelloWorldContainerClicked;
>
> ///UserCodeRegionEnd: (do not remove this comment.)
>
> }
>
> As you can see, ?this.getChildContainer("Container1")? is used to retrieve the content of 'Container1'. Consequently you will be using this function to retrieve the HTML contents of the container areas that you will be defining in your controls.
>
> The content inside 'Container1' is not visible at startup, thats why it's needed set as visible. Then we move the content inside 'Container1' inside the HTML Control we want. In this case inside the UC Main container. 
>
> *this.getChildContainer(<ContainerId>)*
>
> As you may have guessed, ?*this.getChildContainer*? is defined in a parent class so you DO NOT need to define it.
>
> **4) Try it!**
>
> 4.1) Open GeneXus
>
> 4.2) Drop the user HelloWorld user control in a web panel and drop some controls in the container area.
>
> |  |
> | --- |
> |  |
>
> 4.3) Now run it!
>
> **Download**
>
> Click [here](http://www.gxopen.com/gxopen/servlet/projectinformation?678) to download the sample.


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
