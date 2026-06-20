---
title: "HowTo: Create a Three Step Wizard with Panels for Native Mobile applications"
source_id: 18718
source_url: https://wiki.genexus.com/commwiki/wiki?18718
genexus_version: "18"
---

# HowTo: Create a Three Step Wizard with Panels for Native Mobile applications

Many times information needs to be exchanged between [Panels](https://wiki.genexus.com/commwiki/wiki?24829), this document explains how to do so.

This article shows an example of how to exchange variables between Panels by creating a Three Step Wizard application. Three Panels are going to be created in order to do this example.

### [Step 1 - Create the Transaction](#Step+1+-+Create+the+Transaction)

Create the following
[Transaction](https://wiki.genexus.com/commwiki/wiki?1908) and apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) (see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

```
Country
{
    CountryId*
    CountryName
    CountryDescription
    CountryArea
    CountryWaterPercentage
    CountryPopulationEstimate
    CountryGDPNominalTotal
    CountryGDPNominalPerCapita
}
```

**Note**: The [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) property should be set to True

### [Step 2 - Create the three Panels](#Step+2+-+Create+the+three+Panels)

**1.** Create the first of the three Panels (called *FirstPanel* in this case), and add the following variables:

`[imagen omitida: wiki id 54810]`

Add the variables to the layout and, as this [Panel](https://wiki.genexus.com/commwiki/wiki?24829) calls the next one, also add a *Next* button (by dragging and dropping the 'Button' control from the toolbox)

`[imagen omitida: wiki id 54811]`

Define the action for the button as follows:

```
Event 'Next'
    SecondPanel(&CountryDescription,&CountryName)

Endevent
```

**2.** Define the second Panel (called *SecondPanel*).

Define the Parm Rule as follows:

```
Parm(in:&CountryDescription,
     in:&CountryName);
```

Add the following variables to the Panel:

`[imagen omitida: wiki id 54815]`

Add the variables and a *Next* button to the layout:

`[imagen omitida: wiki id 54816]`

Define the action for the button as follows:

```
Event 'Next'
    ThirdPanel(&CountryDescription,&CountryName, &CountryArea, &CountryWaterPercentage)

Endevent
```

**3.** Define the third Panel (called *ThirdPanel*).

Define the Parm rule as follows:

```
Parm(in:&CountryDescription,
     in:&CountryName,
     in:&CountryArea,
     in:&CountryWaterPercentage);
```

Create the following variables:

`[imagen omitida: wiki id 54818]`

**Note**: The variable *&Country*comes from turning the *Country* 

[Transaction](https://wiki.genexus.com/commwiki/wiki?1908) into a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)

Add the variables and a *Finish* button to the layout:

`[imagen omitida: wiki id 54819]`

Define the action for the button as follows:

```
Event 'Finish'
    Composite
        &Country.CountryName = &CountryName
        &Country.CountryDescription = &CountryDescription
        &Country.CountryArea = &CountryArea
        &Country.CountryWaterPercentage = &CountryWaterPercentage
        &Country.CountryPopulationEstimate = &CountryPopulationEstimate
        &Country.CountryGDPNominalTotal = &CountryGDPNominalTotal
        &Country.CountryGDPNominalPerCapita = &CountryGDPNominalPerCapita
        &Country.Save()
        BasicWizard()
    EndComposite
Endevent
```

**4.** Create a [Menu](https://wiki.genexus.com/commwiki/wiki?16321) called *BasicWizard* and add the [Work With](https://wiki.genexus.com/commwiki/wiki?15974) of the *Country*[Transaction](https://wiki.genexus.com/commwiki/wiki?1908) and the *FirstPanel* 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829) to it.  
  
`[imagen omitida: wiki id 54821]`

**Note**: you can add the items to the Menu by dragging and dropping the *FirstPanel* Panel and the Work With of the *Country*Transaction from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210).

### Step 3. Done!

All the objects needed for this example have been created.

Press F5 and see the results.

### [Samples](#Samples)

#### [**Android**](https://wiki.genexus.com/commwiki/wiki?14453)

`[imagen omitida: wiki id 54823]`

Pressing next:

`[imagen omitida: wiki id 54824]`

Pressing next:

`[imagen omitida: wiki id 54825]`

Pressing finish and going to the country's work with item:

`[imagen omitida: wiki id 32604]`
