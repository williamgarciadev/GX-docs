---
title: "The last reorganization has failed and you are trying to execute a different reorganization"
source_id: 11005
source_url: https://wiki.genexus.com/commwiki/wiki?11005
genexus_version: "18"
---

# The last reorganization has failed and you are trying to execute a different reorganization

When running a [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288), the following error could eventually be displayed:

```
The last reorganization has failed and you are trying to execute a different reorganization.
Unexpected errors may occur if you don't try to finalize previous reorganization before running this one.
If you want to run this reorganization anyway, use 'ignoreresume' parameter.
```

### [Cause](#Cause)

Suppose you executed a reorganization (let's call it r*eorg1*) and it failed. After that, you made some changes in the [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661)s that imply updating the database (probably trying to 'fix' the *reorg1* failure). Therefore, a new reorganization (let's call it *reorg2*) is required and the displayed error occurs.

The reason is that GeneXus performs the reorganizations consecutively. If one reorganization fails and you try to perform another one, the previous reorganization will still be missing. 

### [Possible solutions](#Possible+solutions)

When a reorganization fails (in this case both *reorg1* and *reorg2* failed) you can check the following options:

* Try to understand why the reorganization failed. Avoid modifying the Transaction Structures and run the reorganization again.  
  In this case, several reorganization generations will execute the same GeneXus Code. A sample of this error is a login or connection problem with the DBMS. Generally, you modify the Database preferences and the reorganization is regenerated and executed until it succeeds.
* Figure out why the reorganization failed, modify the Transaction Structures to solve the problem, and execute the reorganization again. In this case, the reorganization may display the above error because there is a mismatch between the GeneXus Schema model and the database one. The error message suggests you add the -ignoreresume parameter in the [Reorganization Options property](https://wiki.genexus.com/commwiki/wiki?36454) to bypass the default validation done by GeneXus and run the reorganization process from the very beginning. To do so, follow these steps:   
  + Select the Preferences tab.
  + Select your back-end generator.
  + Look for the [Reorganization Options property](https://wiki.genexus.com/commwiki/wiki?36454).
  + Add the -ignoreresume parameter and save your KB.

`[imagen omitida: wiki id 50685]`

Note: If the *reorg1* reorganization made a change in the database and you use the -ignoreresume parameter, your reorganization may still not work because the target database has a change that GeneXus is not aware of. So, you will have to restore a Database Backup and rerun the reorganization.
