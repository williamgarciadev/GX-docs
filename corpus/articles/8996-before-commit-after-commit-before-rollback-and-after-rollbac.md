---
title: "Before Commit, After Commit, Before Rollback and After Rollback Generator properties"
source_id: 8996
source_url: https://wiki.genexus.com/commwiki/wiki?8996
genexus_version: "18"
---

# Before Commit, After Commit, Before Rollback and After Rollback Generator properties

The Before commit, After commit, Before rollback and After rollback properties indicate the procedure to be executed before and after each [commit](https://wiki.genexus.com/commwiki/wiki?7964) or [rollback](https://wiki.genexus.com/commwiki/wiki?7998) commands.

The main advantage is that this allows "signing" the actions executed in the database when finishing the [LUW](https://wiki.genexus.com/commwiki/wiki?2424) and **leave this information available for auditing purposes**.

### Description

The idea is that the user can call a GeneXus procedure to carry out any desired operation at any of these execution "moments": Before commit, After commit, Before rollback and After rollback.

To use these properties, you have to enter the name of the procedure (GeneXus) you want to call. This procedure must receive a Char(40) as a parameter, which has the name of the object which conducted the operation (or Commit Rollback). The parameter information is relevant data that should be recorded in the database.

### How to apply changes

Build any object.

### Notes

It is not possible for this procedure to receive other parameters and cannot do this procedure Commit or Rollback.

The application will stop with an error when the procedure is not found in the execute moment.

### Scope

**Languages** .NET, Java
