---
title: "Application Registration in Azure Active Directory"
source_id: 42055
source_url: https://wiki.genexus.com/commwiki/wiki?42055
genexus_version: "18"
---

# Application Registration in Azure Active Directory

When you need to authenticate to [Office 365 using GAM](https://wiki.genexus.com/commwiki/wiki?39166), you will first have to create an application in Azure portal.  
Following the steps explained here, you will have all the information necessary to configure the [GAM OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) for using Office 365.

The steps below should be followed to create an Application within the Azure Portal:

**Important note**: the following screens capture can be different depending on the Azure Portal version that you are using. We recommend seeing the document [Register an app with the Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v1-add-azure-ad-app)

1. Sign in to your Azure Account through the [Azure portal](https://portal.azure.com/).
2. Select Azure Active Directory -> App registrations.  
   `[imagen omitida: wiki id 42383]`
3. Select New application registration.  
   `[imagen omitida: wiki id 42384]`
   * Fill Name Application Name, Type and Sign-on URL  
       
     `[imagen omitida: wiki id 42386]`  
       
     Note: The Sign-on URL is not used for the callback after the login. The URL used for that purpose should be configured in Step 5 (Reply URLs)
4. Click on Settings.  
   `[imagen omitida: wiki id 42387]`
5. Select the section Reply URLs and configure accordingly (by default, you have the same URL specified in Step 3.) This URL is used for the callback. You may specify more than one if you have more than one app using the same Azure application.  
   `[imagen omitida: wiki id 42388]`
6. Go through "Required Permissions" to configure at least the following permissions:  
     
   - Microsoft Graph  
   - Windows Azure Directory  
     
   Each of them must include the following settings (access to Delegated Permissions: "Sign in and read user profile" and "Read all user's basic profiles" ).  
     
   `[imagen omitida: wiki id 42389]`  
   `[imagen omitida: wiki id 42390]`  
   So, you will have:  
   `[imagen omitida: wiki id 42391]`
7. Configure the client secret of the application. Go through "Keys", and add a new key, whose description should be "client\_secret" (with that casing). Configure the expiration and the value (it should be a valid GUID).  
   `[imagen omitida: wiki id 42392]`  
   Note the warning: Copy the key value. You will not be able to retrieve it after leaving this blade.
8. Done! If needed, the Manifest with the application detail is available.

Note: You will need the Application Id (= Client Id), the client\_secret, and the Reply URL for configuring the GAM OAuth 2.0 authentication type.

### [See Also](#See+Also)

[Register an app with the Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v1-add-azure-ad-app)  
[HowTo: Authenticate to Microsoft Entra ID using GAM](https://wiki.genexus.com/commwiki/wiki?48906)


|  |
| --- |
| **Backlinks** |
| [HowTo: Authenticate to Office 365 using GAM](https://wiki.genexus.com/commwiki/wiki?39166) |

---
