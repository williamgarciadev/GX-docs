---
title: "HowTo: Configure Single Sign-On (SSO) between a Super App and Mini App using GAM"
source_id: 58884
source_url: https://wiki.genexus.com/commwiki/wiki?58884
genexus_version: "18"
---

# HowTo: Configure Single Sign-On (SSO) between a Super App and Mini App using GAM

This article explains how to configure Single Sign-On (SSO) between a [Super App and Mini App](https://wiki.genexus.com/commwiki/wiki?50899) using [GAM](https://wiki.genexus.com/commwiki/wiki?24746). By following these steps, you will enable users to authenticate once in the Super App and access the Mini App without the need to re-enter their credentials.

**Note**: If your Super App or Mini App is not developed using GeneXus or GAM, see the following document: [Authentication between Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59284,,).

### [Super App configuration at GAM Backoffice](#Super+App+configuration+at+GAM+Backoffice)

**1.** Create a new [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910).

**1.1.** Complete the **Name** and **Description**fields (in the General section), as well as the other fields that you consider necessary (they are optional).

`[imagen omitida: wiki id 58891]`

**1.2.** In the Configuration section (OAuth Authentication tab) set the **Client ID** and **Client Secret** of your Super App.

**1.3.** Select the **Allow REST v2.0 authentication?** check box.

**1.4.** Finally, select the User Scopes that your Super App will share with your Mini App. For example: **User Data**.  
To view the scopes that can be shared, follow this link: [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

`[imagen omitida: wiki id 58892]`

**2.** Go to the **MiniApp** tab and select the **Enable work as MiniApp?** check box.

`[imagen omitida: wiki id 58886]`

**2.1.** Select **Server** in the **Mode** Combo Box.

**2.2.** Finally, set the **MiniApp client URL** field with your MiniApp service URL.

If your MiniApp was not developed using GeneXus or GAM, select **Custom MiniApp client URL**.

If you are using a [Multi - Tenant](https://wiki.genexus.com/commwiki/wiki?18682) scenario, you must specify your **MiniApp client repository GUID.**

### [Mini App configuration at GAM Backoffice](#Mini+App+configuration+at+GAM+Backoffice)

**1.** Create a new [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910).

**1.1.** Complete the **Name** and **Description** fields (in the General section) and the other fields that you consider necessary (they are optional).

`[imagen omitida: wiki id 58894]`

**1.2.** In the Configuration section (OAuth Authentication tab), set the **Client ID** and **Client Secret** of your MiniApp. They must be the same as those specified in Step 1.2 of the Super App configuration.

`[imagen omitida: wiki id 58895]`

**1.3.** Select the **Allow REST v2.0 authentication?** check box.

**1.4.** Select the User Scopes that your Mini App will request to the Super App.

To view the scopes that can be shared, follow this link: [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

**2.** Go to the **MiniApp** tab and select the **Enable work as MiniApp?** check box.

`[imagen omitida: wiki id 58888]`

**2.1.** Select **Client** in the Mode combo box.

**2.2.** In the **User authentication type name in this client** combo box, select the Authentication Type with which the user will be registered once authenticated in the Mini App.

**2.3.** Finally, set the **SuperApp server URL** field with your Super App service URL.

Requests to achieve SSO will be made to endpoints as follows:

* To obtain the **access token:**  

  ```
  https://<superapp_domain>/<superapp_virtualdirectory>/oauth/gam/v2.0/access_token
  ```
* To obtain **user information:**  

  ```
  https://<superapp_domain>/<superapp_virtualdirectory>/oauth/gam/v2.0/user_info
  ```

If your **SuperApp is not developed using GeneXus or GAM**, select **Custom SuperApp server URL**, in this case endpoints will be:

* To obtain the **access token:**  

  ```
  https://<superapp_domain>/<superapp_virtualdirectory>/access_token
  ```
* To obtain **user information:**  

  ```
  https://<superapp_domain>/<superapp_virtualdirectory>/user_info
  ```

In a [Multi-Tenant](https://wiki.genexus.com/commwiki/wiki?18682) scenario, make sure to specify your **SuperApp repository GUID**.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |

---
