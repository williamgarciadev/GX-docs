---
title: "Creation and configuration of a bot in Telegram"
source_id: 48340
source_url: https://wiki.genexus.com/commwiki/wiki?48340
genexus_version: "18"
---

# Creation and configuration of a bot in Telegram

First of all, it is important to highlight what Telegram offers you in terms of conversational interfaces and how they work. To this end, the BotFather concept should be mentioned.

BotFather is a bot managed by Telegram that centralizes the creation and configuration of bots. It is a user with @botfather username that allows you to access your bot's settings by following some commands. In short, Telegram bots are special accounts that do not require a phone number to be set up.

Telegram does not treat bots as ordinary users, but rather distinguishes them. Here are some important considerations:

* Bots do not have “online” or “last login” status; instead, they have a “bot” label.
* They have limited cloud storage space.
* Bots cannot initiate conversations with users. A user must either add them to a group or send them a message first.
* Bot usernames always end with the word "bot."

**Steps to create and configure a bot in Telegram**:

First, in the Telegram search engine, find the ¨BotFather¨ and send the command /newbot. After sending the /newbot command, it will ask you for a name and username for the bot; this username is what identifies your bot and cannot be repeated in the system.

Once the registration of the new bot is completed, you will be issued a token. You must keep this token safe because it will identify your bot and you will have to configure it in the [Telegram Bot Token property](https://wiki.genexus.com/commwiki/wiki?48120).

The image below shows the previous steps:

`[imagen omitida: wiki id 48342]`

Once the bot has been created, you will be able to perform several actions from the Botfather of your choice, such as changing the bot's profile picture and description:

`[imagen omitida: wiki id 48343]`

Next, go to the Telegram search engine and confirm that it has been created correctly.

`[imagen omitida: wiki id 48344]`

Finally, from Telegram, start a conversation with the bot using the /start command:

`[imagen omitida: wiki id 48345]`

### [See also](#See+also)

[Enable Telegram property](https://wiki.genexus.com/commwiki/wiki?48119)  
[Telegram Bot Token property](https://wiki.genexus.com/commwiki/wiki?48120)


|  |
| --- |
| **Backlinks** |
| [HowTo: Chatbots using Telegram](https://wiki.genexus.com/commwiki/wiki?48339) |

---
