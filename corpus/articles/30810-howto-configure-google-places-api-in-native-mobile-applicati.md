---
title: "HowTo: Configure Google Places API in Native Mobile applications"
source_id: 30810
source_url: https://wiki.genexus.com/commwiki/wiki?30810
genexus_version: "18"
---

# HowTo: Configure Google Places API in Native Mobile applications

This document explains how to configure the Google Places API in Native Mobile applications and provides a brief overview about it.

[Google Places API](https://developers.google.com/places/) is a popular service that allows finding [geographic locations](https://wiki.genexus.com/commwiki/wiki?14644) near a site indicated by the end user.

When this feature is applied, a location point can be chosen in three different ways:

1. By tapping an icon on a map
2. By looking for a place by its name on a search engine
3. By selecting it from a list

Every site registered on Google includes its photos, reviews, and other relevant information for each one of them. These features enhance the possibility for the end users to find places of interest, such as hospitals, restaurants, business, shops, hotels, etc.

For example, what happens if your application allows consulting those hotels near the user, but they only know its name? Google Places allows searching for its address and see its references in an easy way.

The use of Google Places preserves compatibility with their respective [control](https://wiki.genexus.com/commwiki/wiki?16756) for Google Maps.

### Step 1 - Create or select a project in the Developer Console

**1.** Go to the [Google Developer Console](http://console.developers.google.com/), log in and search for the Google Places link.  
`[imagen omitida: wiki id 30811]`

**2.** If you don't have any projects created at the moment, Google prompts you to create one. Next, continue to step 4.  
`[imagen omitida: wiki id 30824]`

**3.** If you already have projects created, select one of them or create a new one to apply Google Places to.   
`[imagen omitida: wiki id 30825]`

**4.** If you choose (or have) to create a new project, Google asks you to select a name for it.  
`[imagen omitida: wiki id 30826]`

### [Step 2 - Enable Google Places API](#Step+2+-+Enable+Google+Places+API)

Simply click on the "Enable" button.  
`[imagen omitida: wiki id 30812]`

### [Step 3 - Create and retrieve a Google Places API Key](#Step+3+-+Create+and+retrieve+a+Google+Places+API+Key)

Follow the steps explained in [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055).

### Step 4 - Set Maps API Key in the IDE

In the GeneXus IDE, navigate to *Preferences > Knowledge Base > Environment > Front end > Android*.

`[imagen omitida: wiki id 54714]`

Under *Generator: Android*, there is a property called [Android Maps API Key](https://wiki.genexus.com/commwiki/wiki?19115). Paste the Google Places API Key obtained in Step 2 here.  

### [Step 5 - Run the application](#Step+5+-+Run+the+application)

If your application has attributes or variables based on the [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644), Google Places will be displayed with all the features it offers whenever you want to choose a location, .  
`[imagen omitida: wiki id 30816]`

### [Scope](#Scope)

**Objects**: [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Domain:** [Geolocation](https://wiki.genexus.com/commwiki/wiki?14644)  
**Generators:** 
[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Availability](#Availability)

This feature is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)
