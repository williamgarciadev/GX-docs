---
title: "Google OAuth 2.0 process for emails: Generation and data collection by the Administrator"
source_id: 50408
source_url: https://wiki.genexus.com/commwiki/wiki?50408
genexus_version: "18"
---

# Google OAuth 2.0 process for emails: Generation and data collection by the Administrator

In this article, you will find the necessary steps to provide data to connect to the mailbox through [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2).

Example: Application administrators have to provide the necessary data to programmers so that they can connect to their mailboxes.

## [Steps](#Steps)

Follow these steps to provide data to connect to a mailbox with Google OAuth 2.0:

1. Enter this link: <https://console.developers.google.com/apis/credentials>.

2. Create a **New Project:**

`[imagen omitida: wiki id 50421]`

Name it and click on "Create".

Once you have created the New Project, select it in order to work with it.

3. Go to the **OAuth** **Consent screen** option in the left menu and [Configure a OAuth consent](https://support.google.com/cloud/answer/10311615#user-type&zippy=%2Cexternal%2Cinternal%2Ctesting%2Cin-production).

To do so, follow the next steps:

* Select the **User Type** as **External**and click on the **Create** button.
* Fill in the sections as applicable to your application and click on the **Save and continue** button.
* Click again on the **OAuth** **Consent screen** option and check that your application is in Publishing status = Testing (if you set the Publishing status = Production, a verification of the app will take place. For more information, check this link: [Testing in production](https://support.google.com/cloud/answer/10311615#user-type&zippy=%2Cexternal%2Cinternal%2Ctesting%2Cin-production)):

`[imagen omitida: wiki id 50422]`

4. Go to the **Credentials** option in the left menu and click on the **+ Create Credentials**. Then select **OAuth client ID**.

5. Select the application type necessary for your project. Since, in this example, the focus is on the process for emails, it is common to use "**Application type = Web application**" or "**Application type = Desktop app**." Then click on the **Create** button.

6. Now the OAuth client has been created:

`[imagen omitida: wiki id 50423]`

Save the ClientId and ClientSecret that will be used later.

7. Go to the **Library** option in the Google Cloud Platform and search for the **Gmail API** (use the search engine to help you out) and enable it.

8. Go back to the **OAuth consent screen** option, where you will have to enter the scope of the Gmail API app that you just activated in the previous step. For this, click on the **Edit App** button to enter the form.

9. In the **Scopes**section, add the necessary scope to be able to use the email services with Google. To do so, press the **Add or remove scopes** button as shown in the image:

`[imagen omitida: wiki id 50425]`

10. Select "https://mail.google.com/" and click on the **Update** button.

11. For this step, you don't need to stay on the Google Cloud Console. It is necessary to make a GET request to a URL. For simplicity, it is recommended to do it from the browser.

The URL is constructed as follows:

* *https://accounts.google.com/o/oauth2/auth?client\_id=**{CLIENT\_ID}**&redirect\_uri=**{REDIRECT\_URI}**&scope=**{SCOPE}**&response\_type=code*

Where:

* **{SCOPE}:**refers to the level of access required. As in this case, you want authorization to send emails, you will have to enter the following value: "https://mail.google.com/".
* **{REDIRECT\_URI}:**refers to the page where you want to redirect after authorizing the application.
* **{CLIENT\_ID}**refers to the ClientId that was obtained in step 6.

**Notes:**

* If your application has not been verified yet, you may get an "Error 403: access\_denied. In that case, first, add test users to your Application as explained in <https://stackoverflow.com/questions/65184355/error-403-access-denied-from-google-authentication-web-api-despite-google-acc/65186291#65186291>.
* If you selected **Application type = Desktop app** in the step 5, it is recommended to place the following as Redirect URI: "**urn:ietf:wg:oauth:2.0:oob**", which redirects to the same browser.
* If you selected **Application type = Web** in step 5, it is necessary to place a different Redirect URI. In this example, if you select a Web application, it is recommended to add **http://localhost:1** as a Redirect URI.
* If you selected **Application type = Web,** it is necessary to Add the URI in the **Credentials** option (it needs to have a URL format), specifically clicking in the Edit button of the **OAuth 2.0 Client IDs** section:

`[imagen omitida: wiki id 50678]`

### [Example of a Desktop Application type URL](#Example+of+a+Desktop+Application+type+URL)

```
https://accounts.google.com/o/oauth2/auth?access_type=offline&prompt=consent&client_id=xxx.apps.googleusercontent.com&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=https://mail.google.com/&response_type=code
```

After having made the request in the previous step, an Authorization Code will be obtained as shown in the image below. This code is necessary for the following steps.

`[imagen omitida: wiki id 50426]`

Next, it is necessary to make a POST request, where the Authorization Code obtained in the previous step is used.

As shown in the image in Curl format below, you have to make a request to the **https://accounts.google.com/o/oauth2/token** URL. Also, you need to pass, using x-www-form-urlencoded format (which must be specified as the value for the Content-Type header), the keys with their corresponding values:

* client\_id --> Client ID **obtained in step 6.**
* client\_secret --> Client **Secret obtained in step 6.**
* code --> Authorization Code **obtained in step 11.**
* grant\_type --> ***"authorization\_code"***
* redirect\_uri --> ***"urn:ietf:wg:oauth:2.0:oob"***
* access\_type --> offline
* prompt --> consent

**curl -X POST https://accounts.google.com/o/oauth2/token -H "Content-Type: application/x-www-form-urlencoded" -d "access\_type=offline&prompt=consent&client\_id=xxx&client\_secret=xxx&code=xxx&grant\_type=authorization\_code&redirect\_uri=xxx"**

**Note:** Take into account that the previous POST request must be written as shown on a single line.

The response obtained after executing the previous request is as follows:

`[imagen omitida: wiki id 50428]`

As you can see in this last answer, the refresh token is already obtained (in addition, the first active access token is also obtained, which can already be used by the programmer).

The next step would be to pass the Client ID, Client Secret, and Refresh Token to the programmer.

He/she will be in charge of calculating the access tokens when they expire, using the three recently mentioned metadata.

### [Example of a Web Application type URL](#Example+of+a+Web+Application+type+URL)

```
https://accounts.google.com/o/oauth2/auth?access_type=offline&prompt=consent&client_id=xxx-xxx.apps.googleusercontent.com&redirect_uri=http://localhost:1&scope=https://mail.google.com/&response_type=code&access_type=offline
```

If you request the Authorization Code of a Web Application, you have to copy the code from the browser as shown in this image:

`[imagen omitida: wiki id 50668]`

Next, it is necessary to make a POST request, where the Authorization Code obtained in the previous step is used.

As shown in the image in Curl format below, you have to make a request to the **https://accounts.google.com/o/oauth2/token** URL. Also, you need to pass, using x-www-form-urlencoded format (which must be specified as the value for the Content-Type header), the keys with their corresponding values:

* client\_id --> Client ID **obtained in step 6.**
* client\_secret --> Client **Secret obtained in step 6.**
* code --> Authorization Code **obtained in step 11.**
* grant\_type --> ***"authorization\_code"***
* redirect\_uri --> ***"*http://localhost:1*"***
* access\_type --> offline
* prompt --> consent

**curl -X POST https://accounts.google.com/o/oauth2/token -H "Content-Type: application/x-www-form-urlencoded" -d "access\_type=offline&prompt=consent&client\_id=xxx&client\_secret=xxx&code=xxx&grant\_type=authorization\_code&redirect\_uri=xxx"**

The response obtained after executing the previous request is as follows:

`[imagen omitida: wiki id 50428]`

As you can see in this last answer, the refresh token is already obtained (in addition, the first active access token is also obtained, which can already be used by the programmer).

The next step would be to pass the Client ID, Client Secret, and Refresh Token to the programmer.

He/she will be in charge of calculating the access tokens when they expire, using the three recently mentioned metadata.

### [See also](#See+also+)

[Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227)  
[Microsoft Exchange OAuth 2.0 for Mails](https://wiki.genexus.com/commwiki/wiki?50396)  
[OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438)


|  |
| --- |
| **Backlinks** |
| [Microsoft Exchange OAuth 2.0 for emails: Generation and data collection from the Administrator](https://wiki.genexus.com/commwiki/wiki?50396) | [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) |

---
