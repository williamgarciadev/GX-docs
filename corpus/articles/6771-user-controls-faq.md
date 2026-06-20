---
title: "User Controls - FAQ"
source_id: 6771
source_url: https://wiki.genexus.com/commwiki/wiki?6771
genexus_version: "18"
---

# User Controls - FAQ

In this article you can find some frequently asked questions and its answers about User Controls.

#### [**1. Is it necessary to execute Genexus.exe /install every time I make changes to my user control?**](#1.+Is+it+necessary+to+execute+Genexus.exe+%2Finstall+every+time+I+make+changes+to+my+user+control%3F)

No, Genexus.exe /install should only be executed when making changes to the UC structure, that is, when changing its properties or events.  
  
On the other hand, if you just make changes to the javascript render file and the version of the control is not updated (tag <Version>0</Version> in .control file) then you need to delete file named <ucname>.<version>.VER from the web folder of your model and generate the object that uses the UC in order to get the files of your UC copied to the relevant folder eg: \web\<UserControlName>.

#### [**2. How do I get the container name (div id) at runtime?**](#2.+How+do+I+get+the+container+name+%28div+id%29+at+runtime%3F)

In order to get the container name at runtime you can use "this.ContainerName" inside the control's scope. E.g: var name = this.ContainerName;

#### [**3. How do I get a reference to the container control?**](#3.+How+do+I+get+a+reference+to+the+container+control%3F)

In order to get a reference to the container control, you can use "this.getContainerControl()" inside the control's scope. E.g: var name = this.getContainerControl();

#### [**4. How do I get a reference to the user control instance (at runtime) after the user control has already been loaded?**](#4.+How+do+I+get+a+reference+to+the+user+control+instance+%28at+runtime%29+after+the+user+control+has+already+been+loaded%3F)

In many cases your user control will have to generate html like this: *<a href="*[*www.genexus.com*](http://www.genexus.com)*" onclick="someFunction(z)">text</a>*. In those cases you will want the onclick event to be attended by a function of your user control and not a global function (because that would be a problem if you have multiple instances of you control in the same web page). In those cases you will have to use the "this.me()" function within the scope of your user control as follows:

```
<a href="'+ this.MenuData[i].MenuURL + '" onclick="' + this.me() + '.JSDolphinItemClicked(\'' + this.ControlName + '\',' + i +');" title="' + this.MenuData[i].MenuDescription + '"> + this.MenuData[i].MenuTitle + '</a>
```

The example above is taken from the Dolphin Style Menu user control, downloadable [here](https://marketplace.genexus.com/product.aspx?dolphinstylemenu,en).

#### [**5. How do I detect if the user control is being loaded for the first time or if there is a postback?**](#5.+How+do+I+detect+if+the+user+control+is+being+loaded+for+the+first+time+or+if+there+is+a+postback%3F)

Use "this.IsPostback" to detect if the control is being loaded for the first time or not. E.g.:

```
this.show = function()
{
   if (!this.IsPostBack)
   {
      // draw control
   }
}
```

#### [**6. How do I suscribe a function to the onload event?**](#6.+How+do+I+suscribe+a+function+to+the+onload+event%3F)

The recommended way of subscribing user controls functions to the onload event is using:

```
gx.evt.on_ready( window,<myFunction>);
```

where myFunction is the function you want to subscribe to the onload event. Using this you will avoid possible incompatibilities that may happen when using different javascript frameworks (jquery, dojo, scriptaculous).


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
