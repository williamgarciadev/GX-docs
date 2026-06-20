---
title: "HowTo: Request data from Facebook using Graph API and Access Token"
source_id: 38437
source_url: https://wiki.genexus.com/commwiki/wiki?38437
genexus_version: "18"
---

# HowTo: Request data from Facebook using Graph API and Access Token

This document presents an example of how to use [Facebook's GraphAPI](https://developers.facebook.com/docs/graph-api) in Smart Device applications using GeneXus.

### [Step 1: Register your application](#Step+1%3A+Register+your+application)

You must register your application on the Facebook developer site and get your *Facebook App Id*.  
Refer to [HowTo: Register a Facebook App](https://wiki.genexus.com/commwiki/wiki?19399) for detailed information.

### [Step 2: Integrate Facebook's login and request access token](#Step+2%3A+Integrate+Facebook%27s+login+and+request+access+token)

Use [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841) to allow the end user to log in to the GeneXus app using Facebook's credentials. This action will allow you to get the user's Access Token and use the Graph API for retrieving user data.

For example, you can use the *OnUserInfoUpdated*event and request the [access token](https://wiki.genexus.com/commwiki/wiki?38432) as follows:

```
Event &SDFacebookButton.OnUserInfoUpdated
    &FacebookAccessToken = Facebook.AccessToken
Endevent
```

where &FBAccessToken is based on [FacebookAccessToken SDT](https://wiki.genexus.com/commwiki/wiki?38432).

In this case, we will use the Graph API for getting the [user's posts](https://developers.facebook.com/docs/facebook-login/permissions/#reference-user_posts). To do so, the developer must ensure that "user\_posts" tag is added to [Read Permission property](https://wiki.genexus.com/commwiki/wiki?31841). When the end user logs in, **Facebook will inform**him/her about your purpose (in this case, get his/her posts).

### [Step 3: Request data from Facebook using Graph API](#Step+3%3A+Request+data+from+Facebook+using+Graph+API)

Write an online Procedure for requesting the GraphAPI data by using [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932). This procedure should receive in its parm rule the access token and user identifier strings obtained from the device.

For example, suppose the procedure is called GetUserPosts, and it has defined the following parm rule:

```
parm(in:&AccessToken, in:&UserId, out:&FBJson);
```

You can write a source code as follows:

```
&FBVersion = !"v2.12" // Change it if it is necessary
&Url = !"https://graph.facebook.com/%version/%user_id/feed?access_token=%access_token"
&Url = &Url.Replace("%version",&FBVersion)
&Url = &Url.Replace("%user_id",&UserId)
&Url = &Url.Replace("%access_token",&AccessToken)
&HttpClient.Execute(HttpMethod.Get,&Url)
&FBJson = &HttpClient.ToString()
```

Then, in a user event, you can invoke this procedure as follows:

```
Event 'Get My Posts'
    &FBJson = GetUserPosts(&FacebookAccessToken.AccessToken, &FacebookAccessToken.UserId)
Endevent
```

As a result, after the user has logged in, the &FBJson string-based variable will have the following value:

```
{
   "data": [
      {
         "story": "Damian Salvia is with Pablo Martinez and 5 others.",
         "created_time": "2018-05-07T16:13:21+0000",
         "id": "<id>"
      },
      {
         "story": "Stella Marys Pereira Larrosa added a new photo \u2014 with Nicolas Mechulam and 2 others.",
         "created_time": "2019-07-11T15:12:25+0000",
         "id": "<id>"
      },
      ...
      ], 
   "paging": {
      "previous": "https://graph.facebook.com/v2.12/<user_id>/feed?since=<datetime>&access_token=<token>&limit=<number>&__paging_token=<token>&__previous=1",
      "next": "https://graph.facebook.com/v2.12/<user_id>/feed?access_token=<token>&limit=<number>&until=<datetime>&__paging_token=<token>"
}
```

It's your responsibility to parse the result to meet your requirements.

## [Availability](#Availability)

Full Graph API integration is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,).

## [See also](#See+also)

* [Graph API Reference](https://developers.facebook.com/docs/graph-api/reference)
* [HowTo: Register a Facebook App](https://wiki.genexus.com/commwiki/wiki?19399)
* [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841)


|  |
| --- |
| **Backlinks** |
| [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |

---
