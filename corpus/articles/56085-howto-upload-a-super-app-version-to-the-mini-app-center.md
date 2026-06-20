---
title: "HowTo: Upload a Super App version to the Mini App Center"
source_id: 56085
source_url: https://wiki.genexus.com/commwiki/wiki?56085
genexus_version: "18"
---

# HowTo: Upload a Super App version to the Mini App Center

In this article, you can learn how to upload a new Super App version to the Mini App Center.

The **Provisioning Administrator** and members with the **Organization Administrator** or **Super App Administrator** role can define a new [Super App](https://wiki.genexus.com/commwiki/wiki?50900,,) version.

To upload a new Super App version, click on the Super Apps option and select the name of the Super App for which you want to upload a new version.

`[imagen omitida: wiki id 56213]`

Go to the **Versions** tab and click on the **NEW VERSION** button.

`[imagen omitida: wiki id 56214]`

The following data is required:

* **Platform**: Select among the available options.
* **Version Name**. When uploading a Mini App version, this name will appear to select their corresponding Super App version.
* **Enabled**: Indicates if the Super App version is available for [Mini Apps](https://wiki.genexus.com/commwiki/wiki?50900,,) to be assigned.

### [**Private And Public Key**](#Private+And+Public+Key)

You will notice that a pair of RSA (private and public) keys is automatically generated, designed to facilitate secure operations between your Super App and its associated Mini Apps.

**Private Key**  
The generated private key serves the purpose of signing each new version of a Mini App published for that Super App. This cryptographic process ensures the integrity and authenticity of your Mini Apps, confirming they haven't been altered during deployment or distribution.

**Public Key**  
At runtime, when loading a Mini App from the Super App, the public key is utilized to validate the Mini App. You'll need to download a .crt file containing this public key and place it within the resources or properties of the Super App. This ensures the Super App can validate and authorize the Mini Apps correctly.

You may generate a new key by pressing Generate new **KeyPair**.

Click on the **CONFIRM** button to save this information.


|  |
| --- |
| **Backlinks** |
| [Toc:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) |

---
