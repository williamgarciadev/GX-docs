---
title: "Locale domain"
source_id: 40450
source_url: https://wiki.genexus.com/commwiki/wiki?40450
genexus_version: "18"
---

# Locale domain

Enumerated domain representing a locale (or [language localization](https://en.wikipedia.org/wiki/Language_localisation )) in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

## [Values](#Values)

|  |  |  |
| --- | --- | --- |
| **None** | None |  |
| **Arabic\_Arabic** | Arabic (Arabic) | *ar-AR* |
| **Arabic\_Egypt** | Arabic (Egypt) | *ar-EG* |
| **Arabic\_SaudiArabia** | Arabic (Saudi Arabia) | *ar-SA* |
| **Bulgarian** | Bulgarian (Bulgaria) | *bg-BG* |
| **Cantonese\_HongKong** | Cantonese (Traditional, Hong Kong) | *yue-HK* |
| **Cantonese\_Macao** | Cantonese (Traditional, Macao) | *yue-MO* |
| **Catalan** | Catalan (Spain) | *ca-ES* |
| **Chinese** | Chinese (Simplified, Mainland) | *zh-CN* |
| **Chinese\_HongKong** | Chinese (Traditional, Hong Kong) | *zh-HK* |
| **Chinese\_Singapore** | Chinese (Traditional, Singapore) | *zh-SG* |
| **Chinese\_Taiwan** | Chinese (Traditional, Taiwan) | *zh-TW* |
| **Croatian\_BosniaAndHerzegovina** | Croatian (Bosnia And Herzegovina) | *hr-BA* |
| **Croatian\_Croatia** | Croatian (Croatia) | *hr-HR* |
| **Czech** | Czech (Czech Republic) | *cs-CZ* |
| **Danish** | Danish (Denmark) | *da-DK* |
| **Dutch\_Belgium** | Dutch (Belgium) | *nl-BE* |
| **Dutch\_Netherlands** | Dutch (Netherlands) | *nl-NL* |
| **English\_Australia** | English (Australia) | *en-AU* |
| **English\_Canada** | English (Canada) | *en-CA* |
| **English\_India** | English (India) | *en-IN* |
| **English\_Ireland** | English (Ireland) | *en-IE* |
| **English\_Jamaica** | English (Jamaica) | *en-JM* |
| **English\_NewZeland** | English (New Zeland) | *en-NZ* |
| **English\_UnitedKingdom** | English (United Kingdom) | *ca\_GB* |
| **English\_UnitedStates** | English (UnitedStates) | *en-US* |
| **Finnish** | Finnish (Finland) | *fi-FI* |
| **French\_Canada** | French (Canada) | *fr-CA* |
| **French\_France** | French (France) | *fr-FR* |
| **French\_Switzerland** | French (Switzerland) | *fr-CH* |
| **German\_Austria** | German (Austria) | *de-AT* |
| **German\_Germany** | German (Germany) | *de-DE* |
| **German\_Switzerland** | German (Switzerland) | *de-CH* |
| **Greek** | Greek (Greece) | *el-GR* |
| **Hebrew** | Hebrew (Israel) | *he-IL* |
| **Hindi** | Hindi (India) | *hi-IN* |
| **Hungarian** | Hungarian (Hungria) | *hu-HU* |
| **Icelandic** | Icelandic (Iceland) | *is-IS* |
| **Indonesian** | Indonesian (Indonesia) | *id-ID* |
| **Italian** | Italian (Italy) | *it-IT* |
| **Japanese** | Japanese (Japan) | *ja-JP* |
| **Korean** | Korean (Korea) | *ko-KR* |
| **Malay** | Malay (Malasia) | *ms-MY* |
| **Mandarin** | Mandarin (Simplified, Mainland) | *cmn-CN* |
| **Mandarin\_Singapore** | Mandarin (Simplified, Singapore) | *cmn-SG* |
| **Norwegian** | Norwegian (Norway) | *nb-NO* |
| **Polish** | Polish (Poland) | *pl-PL* |
| **Portuguese\_Brasil** | Portuguese (Brasil) | *pt-BR* |
| **Portuguese\_Portugal** | Portuguese (Portugal) | *pt-PT* |
| **Romanian** | Romanian (Romania) | *ro-RO* |
| **Russian** | Russian (Russia) | *ru-RU* |
| **Slovak** | Slovak (Slovakia) | *sk-SK* |
| **Slovenian** | Slovenian (Slovenia) | *sl-SI* |
| **Spanish\_LatinAmerica** | Spanish (Latin America) | *es-LA* |
| **Spanish\_Mexico** | Spanish (Mexico) | *es-MX* |
| **Spanish\_Spain** | Spanish (Spain) | *es-ES* |
| **Spanish\_UnitedStates** | Spanish (United States) | *es-US* |
| **Swedish** | Swedish (Sweden) | *sv-SE* |
| **Tamil** | Tamil (India) | *ta-IN* |
| **Thai** | Thai (Thailand) | *th-TH* |
| **Turkish** | Turkish (Turkey) | *tr-TR* |
| **Vietnamese** | Vietnamese (Viet Nam) | *vi-VN* |
| **Welsh** | Welsh (United Kindom) | *cy-GB* |

## [Notes](#Notes)

* This domain is more specific than [Language domain](https://wiki.genexus.com/commwiki/wiki?40453).
* Not every locale is available for every [Provider](https://wiki.genexus.com/commwiki/wiki?40195). In such case, GeneXusAI will raise an [GXAI4017 code](https://wiki.genexus.com/commwiki/wiki?40188) with the information needed.
* If some locale is not available on the domain definition for your upgrade installation, you can add it at runtime by using [FromString method](https://wiki.genexus.com/commwiki/wiki?12694).  
  e.g.: &locale.FromString(!"xx-XX"), being *xx-XX* a valid locale code.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169), [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170), [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This domain is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

## [See also](#See+also)

* [Language domain](https://wiki.genexus.com/commwiki/wiki?40453)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) |
| [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
