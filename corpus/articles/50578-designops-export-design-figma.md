---
title: "DesignOps - Export design - Figma"
source_id: 50578
source_url: https://wiki.genexus.com/commwiki/wiki?50578
genexus_version: "18"
---

# DesignOps - Export design - Figma

Designers can send designs made in [Figma format](https://www.figma.com/) to developers. Then, developers can import these designs using the [Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) in the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

### [How to send a Figma design](#How+to+send+a+Figma+design)

When a designer sends a design, it should include a Figma URL and provide an [Access Token](https://www.figma.com/developers/api#access-tokens) in case the developer does not have an account in Figma or cannot access the Figma project.

The Figma URL must have the following format:  
https://www.figma.com/file/:key/:title[?version-id=:version]

### [How to get a Figma token](#How+to+get+a+Figma+token)

1. [Log in](https://www.figma.com/login) into your Figma account
2. From the file browser, click on your profile icon in the top-left corner and select Settings.
3. Go to the Security tab.
4. In the Personal access tokens section, click Generate new token.
5. Set a description, choose an expiration period and enable the file content scope so GeneXus can read the design file.
6. Click Generate token.
7. Copy the token immediately and store it in a secure place. You won’t be able to view it again.
8. If you lose it, you can always revoke the token and generate a new one.

### [How to save a Figma version](#How+to+save+a+Figma+version)

It is highly recommended to save a **snapshot** of the Figma file before sharing the Figma URL, which includes the version-id parameter.

The snapshot can be saved by going to **File > Save to Version History** in Figma, and Figma will ask you for a revision title and revision description as follows.

|  |  |  |
| --- | --- | --- |
|  |  |  |

Finally, you can get the snapshot URL by going to **File > Show Version History**, selecting your snapshot, and clicking on the Copy Link option.

|  |  |  |
| --- | --- | --- |
|  |  |  |

Now you can share your link with a developer who can use the [Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) for importing your design into GeneXus.

### [How to include custom fonts](#How+to+include+custom+fonts)

If you are using Figma fonts, GeneXus will try to get them from Google Fonts but this process might not work in every case. In case the developer had experienced issues with the font files while importing the design file into GeneXus or if you are using custom fonts (not provided by Figma), you have to deliver the font files to the developer and the developer must install them on the development machine (in Windows, installation have to be done by right-clicking and selecting "Install for all users" option).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917). |

### [See also](#See+also)

[Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)  
[Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Sample - Home Decor](https://wiki.genexus.com/commwiki/wiki?50970) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |
| [GeneXus Design Prototyper for Figma](https://wiki.genexus.com/commwiki/wiki?56683) |
| [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
