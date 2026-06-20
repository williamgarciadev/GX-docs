---
title: "Create Transaction from Attributes command"
source_id: 26553
source_url: https://wiki.genexus.com/commwiki/wiki?26553
genexus_version: "18"
---

# Create Transaction from Attributes command

In the transaction editor you can select several attributes and use this command to create a new transaction with them.

`[imagen omitida: wiki id 26554]`

This command is enabled when you select one or more attributes in the Transaction editor.

It creates a new [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) taking the first of the selected attributes as the key. The name of the new Transaction is taken from the name of the first selected attribute.

For example, if you select CustomerId and CustomerName and execute this command over them, you will have a new "Customer" Transaction with the following structure:

```
CustomerId*
CustomerName
```

`[imagen omitida: wiki id 26555]`

### [See also](#See+also)

* [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)
