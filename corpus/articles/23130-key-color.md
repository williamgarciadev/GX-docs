---
title: "Key Color"
source_id: 23130
source_url: https://wiki.genexus.com/commwiki/wiki?23130
genexus_version: "18"
---

# Key Color

### [[Previous version (X Evolution 2)](https://wiki.genexus.com/commwiki/wiki?27445,,)](#wiki%3F27445%2CKey%2BColor%2B%2528X%2BEvolution%2B2%2529+Previous+version+%28X+Evolution+2%29)

The Key Color is considered important for developing [iOS 7 Overview](https://wiki.genexus.com/commwiki/wiki?23121,,) apps. The concept behind this is:

### [Color can enhance communication](#Color+can+enhance+communication)

So Apple is recommending to use a Key Color for their applications following some guidelines:

**Consider defining a key color**. The built-in apps use key colors—such as yellow in Notes—to indicate interactivity and element state.

**Color communicates, but not always in the way you intend.** Everyone sees color differently and many cultures differ in how they assign meanings to colors. Spend the time to research how your use of color might be perceived in other countries and cultures. As much as possible, you want to be sure that the colors in your app send the appropriate message.

**In most cases, don’t let color distract users.** Unless the color is essential to your app’s purpose, it usually works well to use color as a subtle enhancement."

### [Usage](#Usage)

In the [Colors Tab of Theme Object](https://wiki.genexus.com/commwiki/wiki?22256) users can define new semantic colors and these colors can be referenced from other classes.

In iOS themes, define a new semantic color named 'Key Color'. In the GeneXus theme for iOS7 there are several properties internally referencing this Key Color. So if you want to change the Key Color of your application you only need to change it in one single place.

Steps to Change Key Color:

* Open iOS 7 Theme
* Select Color Tab
* On Color Palette right-click and select 'New Color'
* Define it with Name 'Key Color' and change the color

`[imagen omitida: wiki id 23137]`

Even though in previous versions of iOS the key color concept didn't exist, in GeneXus you can have the same behavior for previous versions of iOS by setting the same Fore Color property for Buttons and Texts that have some kind of interactivity.

### [Considerations for iOS8 applications](#Considerations+for+iOS8+applications)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,), if the selected Key Color is a light color, for instance White, WhiteSmoke or any other light color, the action's color of the following dialogs are set to the platform default blue color:

* Alert view messages: Appears when errors occur or when using the Msg command
* [Action group sheets](https://wiki.genexus.com/commwiki/wiki?25106)
* [Send Mail dialog](https://wiki.genexus.com/commwiki/wiki?18193)
* [Send SMS dialog](https://wiki.genexus.com/commwiki/wiki?17310)
* Image or Video picker
* Calendar or Contacts

### [Availability](#Availability)

This property is available as from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)
