---
title: "HowTo: Obtain a Super App Version Public Key"
source_id: 57522
source_url: https://wiki.genexus.com/commwiki/wiki?57522
genexus_version: "18"
---

# HowTo: Obtain a Super App Version Public Key

In this article, you can learn how to download Super App public keys from the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).

When you create a new version for a Super App in the Mini App Center, a set of keys is generated to ensure that the Super App can only load Mini Apps published for that specific version of the Super App (refer to [Super App's Private And Public Key](https://wiki.genexus.com/commwiki/wiki?56085) for more information).

You will need to download the public key and place it as part of your Super App's resources.

Follow these steps to download the public key:

1. Log in to the Mini App Center with a user that has the role of Super App Administrator or (Super App) Organization Administrator.
2. Click on the **Super Apps** option in the Main Menu. The list of the Super Apps available will be displayed. Next, select the name of the Super App for which you want to obtain the key.

`[imagen omitida: wiki id 57530]`

      3. Go to the **Versions** section and click on the **PUBLIC KEY** link to download the file containing the public key corresponding to the version you need.

`[imagen omitida: wiki id 57523]`

      4. Optionally, you can click on the version to display the key in text format.

      5. Store the downloaded file within your Super App project. The specific location may vary depending on the technology used for Super App development:

* GeneXus Super App: See [Android & iOS Public Key File properties](https://wiki.genexus.com/commwiki/wiki?53457)
* [Non-GeneXus Android Super App](https://github.com/genexus-books/gx-super-app/tree/main/Android#setting)
* [Non-GeneXus Apple Super App](https://github.com/genexus-books/gx-super-app/blob/main/iOS/README.md#setting)


|  |
| --- |
| **Backlinks** |
| [Android Public Key File property](https://wiki.genexus.com/commwiki/wiki?53602) | [How to create a Super App?](https://wiki.genexus.com/commwiki/wiki?50906) | [iOS Public Key File property](https://wiki.genexus.com/commwiki/wiki?53603) |
| [Toc:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) |

---
