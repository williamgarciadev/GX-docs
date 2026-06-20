---
title: "Transactions Diagrams"
source_id: 8926
source_url: https://wiki.genexus.com/commwiki/wiki?8926
genexus_version: "18"
---

# Transactions Diagrams

Display all relations between the selected transactions. Each transaction within the diagram is represented by a rectangle and arrows are used to indicate relations. Only direct relations are represented.

### [Description](#Description)

Let us suppose that we have an invoicing model consisting of the following transactions: Clients, Invoices and Products. The type of arrows used are:  
  
**Arrow 1-N** (`[imagen omitida: wiki id 8933]`). This type of arrow is used between the Clients and Invoices transactions. This means that a client can have many invoices and an invoice can only belong to one client.  
  
**Arrow M-N** (`[imagen omitida: wiki id 8934]`). This type of arrow is used between the Invoices and Products transactions. This arrow indicates that an invoice can have many products and that a product can be found in many invoices.  
  
**Arrow 1-1** (`[imagen omitida: wiki id 8935]`). Used to indicate 'parallel' transactions (it has the same identifier).  
  
To include Transactions in a Diagram you must drag and drop the transactions desired from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) container. It is interesting to note that the user only has to choose the transactions because GeneXus will automatically draw the arrows.

The Delete button removes the Transaction from the diagram (attention: only Transaction Diagrams are deleted, not the Knowledge Base).

To edit a transaction displayed on the diagram you must Double-click over it.

`[imagen omitida: wiki id 8932]`

### [See Also](#See+Also)

[Tables Diagrams](https://wiki.genexus.com/commwiki/wiki?8927)


|  |
| --- |
| **Backlinks** |
| [Category:Diagram object](https://wiki.genexus.com/commwiki/wiki?23941) | [Diagrams](https://wiki.genexus.com/commwiki/wiki?8925) | [Table Diagrams](https://wiki.genexus.com/commwiki/wiki?8927) |

---
