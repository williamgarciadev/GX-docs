---
title: "Deployment Unit object"
source_id: 38886
source_url: https://wiki.genexus.com/commwiki/wiki?38886
genexus_version: "18"
---

# Deployment Unit object

Defines the set of objects to be deployed together.

Only Main objects, File objects, and Business Process Diagram objects are available for selection in a Deployment Unit.

To deploy the objects defined by a Deployment Unit, you may use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

Typically, for an application that has a front office, back-end, and Services layer, you create a Deployment Unit for each, but you are free to define the ones you need.

### [Sample](#Sample)

In the [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,) Sample, clearly you need to deploy the Home (LightCRM Web), the Services required for the LightCRM Android and iOS App, and the Android and iOS App itself.

If you want to deploy the Web and the Services separately (for example, to https://example.com/Main and https://example.com/Services), you can define two Deployment Units: The 'Site' with the Home object (and its called objects) and the 'Services' defined by the LightCRM object.

`[imagen omitida: wiki id 38888]`

Then, deploy each of them.  
To Deploy a Deployment Unit you have two options: Right-click on a Deployment Unit (which opens the Application Deployment Toolwindows ready to deploy the selected Deployment Unit), or open Build-> Application Deployment and then select the desired Deployment Unit.

### [Availability](#Availability)

Since [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,).
