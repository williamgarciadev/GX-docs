---
title: "Treeview Control"
source_id: 5055
source_url: https://wiki.genexus.com/commwiki/wiki?5055
genexus_version: "18"
---

# Treeview Control

The treeview control provides a rich visual presentation of hierarchical data. It can be fully customized at design time or runtime (if necessary) through a vast set of properties that allow you to configure how the tree will be displayed. The control is based on Yahoo! Treeview.

Key features:

* Unlimited number of levels
* Supports all major browsers
* Alternative images for each node
* Raises server event when the selected nodes changes
* Supports populate on demand.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Custom icons | Modern style | Menu style |

### [Using the control](#Using+the+control)

After dragging and dropping a treeview control into a web panel or transaction you will notice that the following variables are created:

|  |  |
| --- | --- |
| **&treeNodeCollectionData:** | Based on TreeNodeCollection SDT (collection of TreeNodeCollection.TreeNode) |
| **&treeNode:** | Based on TreeNodeCollection.TreeNode SDT |
| **&parent:** | Based on TreeNodeCollection.TreeNode SDT |
| **&selectedTreeNode:** | Based on TreeNodeCollection.TreeNode SDT |

&treeNodeCollectionData and &selectedTreeNode are automatically assigned to the control's TreeNodeCollectionData and SelectedTreeNode properties, respectively. &treeNodeCollection data will hold the tree structure, while &selectedTreeNode will be used to hold the currently selected node of the treeview when handling events. &parentNode and &treeNode, for their part, are auxiliary variables used in the code snippet to create a sample tree. The snippet looks as follows:

```
Sub 'TreeViewSample'
  &treeNode.Id = "Some GeneXus Sites"
  &treeNode.Name = "GeneXus Sites"
  &treeNodeCollectionData.Add(&treeNode)

  &treeNode = new()
  &treeNode.Id = "GeneXus Home Page"
  &treeNode.Name = "GeneXus Home Page"
  &parent = &treeNodeCollectionData.Item(1)
  &parent.Nodes.Add(&treeNode)

  &treeNode = new()
  &treeNode.Id = "Developer Resources"
  &treeNode.Name = "Developer Resources"
  &parent = &treeNodeCollectionData.Item(1)
  &parent.Nodes.Add(&treeNode)

  &treeNode = new()
  &treeNode.Id = "GXTechnical"
  &treeNode.Name = "GXTechnical"
  &parent = &treeNodeCollectionData.Item(1).Nodes.Item(2)
  &parent.Nodes.Add(&treeNode)

  &treeNode = new()
  &treeNode.Id = "GXSearch"
  &treeNode.Name = "GXSearch"
  &parent = &treeNodeCollectionData.Item(1).Nodes.Item(2)
  &parent.Nodes.Add(&treeNode)
EndSub

//Event treeview1.NodeClicked
//    textBlock1.Caption = &selectedTreeNode.Name
//EndEvent

//Event treeview1.PopulateNode
//    &treeNode = new()
//    &treeNode.Id = "Server Node"
//    &treeNode.Name = "Server Node"
//    &selectedTreeNode.Nodes.Add(&treeNode)
//EndEvent
```

This snippet creates the treeview shown below. In addition, you will notice that there's a snippet that shows you how to manage the NodeClicked event and how to populate a treeNode on demand (both topics will be covered later).

|  |
| --- |
|  |
| Default tree |

### [Control Properties](#Control+Properties)

|  |  |
| --- | --- |
| LinkTarget | Default target for all nodes |
| **Appearance** |  |
| Style | Only one node within a parent can be expanded at the same time. |
| **Appearance/CustomImages** |  |
| ParentIcon | Image for all parent nodes |
| ParentSelectedIcon | Image for all parent nodes when selected |
| LeafIcon | Image for all leaf nodes |
| LeafSelectedIcon | Image for all leaf nodes when selected |
| **DataBindings** |  |
| TreeNodeCollectionData | TreeNodeCollection SDT instance containing the tree structure |
| SelectedTreeNode | TreeNode SDT for the selected treeNode |

Control properties allow you (among other things) to set icons for the diferent types of nodes of the control. This of course applies to the entire treeview, but if you also define some special icons for a specific treeNode at runtime, the special icons will have precedence over the icons defined for the control (ParentIcon, ParentSelectedIcon, LeafIcon, LeafSelectedIcon).

There are also are some predefined styles that can be applied to the treeview. These styles can be extended, but in order to do so, you need to change certain css and js codes. The list of available styles is:

|  |  |
| --- | --- |
| Default | Lines |
| DefaultWithDefaultIcons | Lines + default icon set |
| Modern | Lines (big plus and minus icons) |
| ModernWithDefaultIcons | Lines (big plus and minus icons) + default icon set |
| Menu | Menu style |
| NoLines | No lines, no icons |
| NoLinesWithDefaultIcons | No lines + default icon set |

### [TreeNode SDT fields](#TreeNode+SDT+fields)

When creating a new treeNode (TreeNodeCollection.TreeNode), there are several fields that allow you to specify how the treeNode behaves and how it should be displayed. These field are:

|  |  |
| --- | --- |
| **Id (character):** | Internal id, useful for event handling. |
| **Name (character):** | Text of the treenode. |
| **Link (character), (optional):** | URL that is called when the node is clicked. |
| **LinkTarget (character):** | Same as the html anchors target. |
| **Expanded (boolean):** | Specifies if the tree node should be opened by default after the treenode has been loaded. |
| **DynamicLoad (boolean):** | Sets whether the treenode should load its children on demand. |
| **Icon:** | Image icon representing the tree node. If it is left empty, a default image will be used. |
| **IconWhenSelected:** | Image icon representing the tree node when it's open. If it is left empty, a default image will be used. |
| **Nodes:** | TreeNodeCollection |

Some considerations concerning the fields listed above:

1. When creating a node you can specify a link or not. Either way, the NodeClicked event will be triggered, but if there is a link, the browser will then navigate to the specified url (according to the linkTarget).
2. When DynamicLoad = true for a treeNode, the PopulateNode event will be triggered if there is code to handle the event.

#### [Handling the NodeClicked event](#Handling+the+NodeClicked+event)

When a node is clicked, a NodeClicked event will be triggered every time you have a code to handle that event from the server side. An example of a code for handling that event would be:

```
Event treeview1.NodeClicked
    textBlock1.Caption = &selectedTreeNode.Name
EndEvent
```

It should be noted that the NodeClicked event is raised every time you click the node but not when the node is expanded or collapsed using the plus/minus icons.

#### [Dynamic Load (load on demand)](#Dynamic+Load+%28load+on+demand%29)

Nodes can be loaded on demand, that is, you can add children to a node at runtime. In order to do this you have to set the dynamicLoad property of the treeNode to True.

```
&treeNode = new()
&treeNode.Id = "SampleNode"
&treeNode.Name = "SampleNode"
&treeNode.DynamicLoad = true
```

Consequently, when "SampleNode" is expanded for the first time, you can add children to it. This can be accomplished by handling the PopulateNode event of the treeview as follows:

```
Event treeview1.PopulateNode
    &treeNode = new()
    &treeNode.Id = "Server Node"
    &treeNode.Name = "Server Node"
    &selectedTreeNode.Nodes.Add(&treeNode)
EndEvent
```

The &selectedTreeNode variable represents the node that has been expanded. This is because we have previously bound the &selectedTreeNode variable to the SelectedTreeNode property of the treeview (this is done automatically when you drop the treeview control in a form, but you can change this).

`[imagen omitida: wiki id 5237]`

### [Loading a Treeview control using a [Recursive Data Providers](https://wiki.genexus.com/commwiki/wiki?4891)](#Loading+a+Treeview+control+using+a+wiki%3F4891%2CRecursive%2BData%2BProviders+Recursive+Data+Providers)

Suppose you have the following entities:

`[imagen omitida: wiki id 5238]`

CategoryFatherId and CategoryFatherName are obviously subtypes of CategoryId and CategoryName, respectively. Consequently, each Category has a "Category Father". Moreover, each Item is related to a Category through the CategoryItem transaction.

Now suppose that you want to create a Data Provider that recursively loads the treeview structures using the entities described above. That data provider should start loading the "top parent category" (the category that has 0 as the CategoryFatherID) and then go on to load all its children recursively (that is, it should load its child categories and items). In addition, remember that the TreeNodeDataCollection structures look as follows:

`[imagen omitida: wiki id 5239]`

The data provider will look as follows:

```
TreeNodeCollection
where CategoryFatherId = &CategoryFatherId
{
  Id = str(CategoryId)
  Name = CategoryName
  Link = ViewCategory.Link(CategoryId)
  Nodes = Catalog(CategoryId)
}
TreeNodeCollection
where CategoryId = &CategoryFatherId
{
  Id = str(ItemId)
  Name = ItemName
  Link = ViewItem.Link(ItemId)
}
```

You should then call this data provider as follows:

```
Event Start
    &treeNodeCollectionData = Catalog(0)
EndEvent
```

...where &treeNodeCollection data is a TreeNodeCollection SDT-based variable. Note that we call the data provider passing 0 as a parameter because we want to start loading the nodes whose CategoryFatherID is 0 (that is, the Categories that have no "parent").

## [Licensing](#Licensing)

This user control automatically distributed with GeneXus uses the following components:

* Yahoo! Treeview from the [YUI Library](https://github.com/yui/yui3/wiki/YUI-Documentation); open license (BSD).
* Syntax Highlighter from <https://github.com/syntaxhighlighter/>; MIT license.


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) |

---
