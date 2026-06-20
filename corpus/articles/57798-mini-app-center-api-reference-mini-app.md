---
title: "Mini App Center - API Reference - Mini App"
source_id: 57798
source_url: https://wiki.genexus.com/commwiki/wiki?57798
genexus_version: "18"
---

# Mini App Center - API Reference - Mini App

The Mini App Center offers an API that provides endpoints for retrieving and modifying data from the Mini App. This article offers an overview of these Endpoints.

Check the [generic variables](https://wiki.genexus.com/commwiki/wiki?57742) required to use the API.

## [Endpoints](#Endpoints)

Below is a summary of the available endpoints for this API:

| Method | Path | Description |
| --- | --- | --- |
| GET | [/miniapps/{id}](https://wiki.genexus.com/commwiki/wiki?57798) | Gets Mini App details. |
| POST | [/miniapps/upload](https://wiki.genexus.com/commwiki/wiki?57798) | Creates a Mini App with additional attributes and locations. |
| POST | [/miniapps](https://wiki.genexus.com/commwiki/wiki?57798) | Creates a Mini App. |
| PUT | [/miniapps/{id}](https://wiki.genexus.com/commwiki/wiki?57798) | Updates a Mini App. |
| DELETE | [/miniapps/{id}](https://wiki.genexus.com/commwiki/wiki?57798) | Deletes a Mini App. |
| POST | [/miniapps/{id}/attributes](https://wiki.genexus.com/commwiki/wiki?57798) | Assigns a value to an additional attribute of the Mini App. |
| DELETE | [/miniapps/{id}/attributes/{field}](https://wiki.genexus.com/commwiki/wiki?57798) | Deletes a value to an additional attribute of the Mini App. |
| GET | [/miniapps/{id}/locations](https://wiki.genexus.com/commwiki/wiki?57798) | Gets a list of locations of Mini App. |
| POST | [/miniapps/{id}/locations](https://wiki.genexus.com/commwiki/wiki?57798) | Creates a location for Mini App. |
| PUT | [/miniapps/{id}/locations/{location\_id}](https://wiki.genexus.com/commwiki/wiki?57798) | Updates the location of Mini App. |
| DELETE | [/miniapps/{id}/locations/{location\_id}](https://wiki.genexus.com/commwiki/wiki?57798) | Deletes location of Mini App. |
| GET | [/miniapps/{id}/versions/{version\_id}](https://wiki.genexus.com/commwiki/wiki?57798) | Gets Mini App version details. |
| POST | [/miniapps/{id}/versions/upload](https://wiki.genexus.com/commwiki/wiki?57798) | Creates a version of Mini App with compatibilities. |
| POST | [/miniapps/{id}/versions](https://wiki.genexus.com/commwiki/wiki?57798) | Creates a version of a Mini App. |
| PUT | [/miniapps/{id}/versions/{version\_id}](https://wiki.genexus.com/commwiki/wiki?57798) | Updates a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/compatibility](https://wiki.genexus.com/commwiki/wiki?57798) | Adds Super App version compatibility to a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/compatibility/delete](https://wiki.genexus.com/commwiki/wiki?57798) | Deletes Super App version compatibility to a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/send\_to\_review](https://wiki.genexus.com/commwiki/wiki?57798) | Sends to review a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/in\_review](https://wiki.genexus.com/commwiki/wiki?57798) | Sets in review a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/rejected](https://wiki.genexus.com/commwiki/wiki?57798) | Rejects a version of a Mini App. |
| POST | [/miniapps/{id}/versions/{version\_id}/ready](https://wiki.genexus.com/commwiki/wiki?57798) | Sets as ready a version of a Mini App. |

**Note**: This endpoint requires a Mini App Center API token related to **Member Organization User** scope. Read more at: [How to create API Key as an Organization Administrator User](https://wiki.genexus.com/commwiki/wiki?57935).

### [GET /miniapps/{id}](#GET+%2Fminiapps%2F%7Bid%7D)

This endpoint gets details about a specific Mini App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |

### [Response](#Response)

```
{
    "data": {
        "id": "string",
        "organization_id": "GUID",
        "name": "string",
        "description": "string",
        "superapp_id": "string",
        "type": "string",
        "keywords": "string",
        "icon": "URL",
        "card": "URL",
        "banner": "URL",
        "additional_attributes": [
            {
                "field": "string",
                "value": "string"
            },
            ...
        ]
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/miniapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /miniapps/upload](#POST+%2Fminiapps%2Fupload)

Uploads a Bundle file to create a Mini App with additional attributes and locations. Note that the file extension must be ".mac" or the one indicated in the "File Types" parameter.

### [Request Body](#Request+Body)

The supported option is binary. It is useful for its simplicity and encodes the binary data directly in the request body.

It is mandatory to set a filename header value with the document name and extension. For example:

```
filename: MiniApp.mac
```

**Note**: To learn how to create the MiniApp.mac file, read [HowTo: Create Mini App Bundle](https://wiki.genexus.com/commwiki/wiki?57803).

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/upload" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H 'filename: MiniApp.mac' \
    -d '@/C:/temp/MiniApp.mac'
```

### [POST /miniapps](#POST+%2Fminiapps)

Creates a Mini App.

### [Request Body](#Request+Body)

```
{
    "id": "string",
    "organization_id": "GUID",    /*Only with Site Admin API token*/
    "name": "string",
    "description": "string",
    "superapp_id": "string",
    "type": "string",             /*Native, WEB*/
    "keywords": "string",
    "icon": "object_id",
    "icon_url": "string",         /*For WEB image*/
    "card": "object_id",
    "card_url": "string",         /*For WEB image*/
    "banner": "object_id",
    "banner_url": "string".       /*For WEB image*/
}
```

To learn how to generate an "object\_id" read [HowTo: Upload an image, video, or audio file via an API object Using Postman](https://wiki.genexus.com/commwiki/wiki?51411).

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "id": "com.genexus.verdant.coffeemuffins",
            "name":"Coffee & Muffins",
            "superapp_id":"com.genexus.verdantbank",
            "type":"native",
            "description":"Coffee & Muffins Mini App",
            "keywords":"coffee cafe muffins breakfast",
            "icon":"gxupload:fe4602263a224b68a6cdd8c5533e5700"
        }'
```

### [PUT /miniapps/{id}](#PUT+%2Fminiapps%2F%7Bid%7D)

Updates details of a specific Mini App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |

### [Request Body](#Request+Body)

```
{
    "organization_id": "GUID",    /*Only with Site Admin API token*/
    "name": "string",
    "description": "string",
    "superapp_id": "string",
    "type": "string",             /*Native, WEB*/
    "keywords": "string",
    "icon": "object_id", 
    "icon_url": "string",         /*For WEB image*/
    "card": "object_id", 
    "card_url": "string",         /*For WEB image*/
    "banner": "object_id",
    "banner_url": "string".       /*For WEB image*/ 
}
```

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/miniapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name":"Coffee & Muffins",
            "superapp_id":"com.genexus.verdantbank",
            "type":"native",
            "description":"Coffee & Muffins Mini App",
            "keywords":"coffee cafe muffins breakfast",
            "icon":"gxupload:fe4602263a224b68a6cdd8c5533e5700",
            "card":"gxupload:32d77315af2a45aea39b99bb7b5a07a9"
        }'
```

### [DELETE /miniapps/{id}](#DELETE+%2Fminiapps%2F%7Bid%7D)

Deletes a Mini App identified by its id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/miniapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /miniapps/{id}/attributes](#POST+%2Fminiapps%2F%7Bid%7D%2Fattributes)

Assigns a value to an additional attribute of a Mini App identified by its id.

### [Request Body](#Request+Body)

```
{
    "field": "string",
    "value": "string"
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/attributes" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "field": "COUNTRY",
            "value": "Uruguay"
        }'
```

### [DELETE /miniapps/{id}/attributes/{field}](#DELETE+%2Fminiapps%2F%7Bid%7D%2Fattributes%2F%7Bfield%7D)

Deletes an additional attribute of a Mini App identified by its id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| field | string | Field (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/miniapps/{id}/attributes/{field}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [GET /miniapps/{id}/locations](#GET+%2Fminiapps%2F%7Bid%7D%2Flocations)

This endpoint gets a list of locations associated with a Mini App identified by its id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| location\_id | string | Location ID (required) |

### [Response](#Response)

```
{
    "data": [
        {
            "id": "int",
            "name": "string",
            "geo_point": "GeoPoint"
        },
        ...
    ]
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/miniapps/{id}/locations/{location_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /miniapps/{id}/locations](#POST+%2Fminiapps%2F%7Bid%7D%2Flocations)

Creates a new location associated with a Mini App identified by its id.

### [Request Body](#Request+Body)

```
{
    "name": "string",
    "geo_point": "GeoPoint"
}
```

> GeoPoint: Geography object represented by the WKT text (<https://en.wikipedia.org/wiki/Well-known_text>).  
> Sample: "POINT(-56.163740158081055 -34.92478600243492)"

### [Response](#Response)

```
{
    "data": {
        "id": "int"
    }
}
```

If the creation is successful, it will return HTTP response Status "201 Created". Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/locations" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Central",
            "geo_point": "POINT(-56.163740158081055 -34.92478600243492)"
        }'
```

### [PUT /miniapps/{id}/locations/{location\_id}](#PUT+%2Fminiapps%2F%7Bid%7D%2Flocations%2F%7Blocation_id%7D)

Updates the details of a specific location associated with a Mini App.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| location\_id | string | Location ID (required) |

### [Request Body](#Request+Body)

```
{
    "name": "string",
    "geo_point": "GeoPoint"
}
```

> GeoPoint: Geography object represented by the WKT text (<https://en.wikipedia.org/wiki/Well-known_text>).  
> Sample: "POINT(-56.163740158081055 -34.92478600243492)"

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/miniapps/{id}/locations/{location_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Central",
            "geo_point": "POINT(-56.163740158081055 -34.92478600243492)"
        }'
```

### [DELETE /miniapps/{id}/locations/{location\_id}](#DELETE+%2Fminiapps%2F%7Bid%7D%2Flocations%2F%7Blocation_id%7D)

Deletes a specific location associated with a Mini App.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| location\_id | string | Location ID (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/miniapps/{id}/locations/{location_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [GET /miniapps/{id}/versions/{version\_id}](#GET+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D)

Gets details about a specific version of a Mini App.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

```
{
    "data": {
        "id": "int",
        "code": "string",
        "platform_id": "string",
        "metadata": "URL",
        "integrated_security": "boolean",
        "main_name": "string",
        "main_type": "string",
        "service_url": "URL"
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/miniapps/{id}/versions/{version_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /miniapps/{id}/versions/upload](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2Fupload)

Uploads a Bundle file to create a version of mini app {id}. Note that the file extension must be ".mac" or the one indicated in the "File Types" parameter.

### [Request Body](#Request+Body)

The supported option is binary. It is useful for its simplicity and encodes the binary data directly in the request body.

It is mandatory to set a filename header value with the document name and extension. For example:

```
filename: MiniAppVersion.mac
```

**Note**: To learn how to create the MiniAppVersion.mac file, read [HowTo: Create Mini App Version Bundle](https://wiki.genexus.com/commwiki/wiki?57804).

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/upload"\
    -H "APIKey-Auth: $API_TOKEN" \
    -H 'filename: MiniAppVersion.mac' \
    -d '@/C:/temp/MiniAppVersion.mac'
```

### [POST /miniapps/{id}/versions](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions)

This endpoint creates a new version of the Mini App identified by its id.

### [Request Body](#Request+Body)

```
{
    "code": "string",
    "platform_id": "string",
    "metadata": "object_id",
    "integrated_security": "boolean",
    "main_name": "string",
    "main_type": "string",    /*Panel, Menu*/
    "service_url": "URL"
}
```

To learn how to generate an "object\_id" read [HowTo: Upload an image, video, or audio file via an API object Using Postman](https://wiki.genexus.com/commwiki/wiki?51411).

### [Response](#Response)

```
{
    "data": {
        "id": "int",
        "code": "string",
    }
}
```

If the creation is successful, it will return HTTP response Status "201 Created". Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "platform_id": "iOS",
            "metadata": "gxupload:f292ef3f9ac94294a66cc353c4802c35",
            "integrated_security": true,
            "main_name": "startObject",
            "main_type": "Panel",
            "service_url": "https://apps6.genexus.com/Id555317f4080a0da816dc4eb15d69bc1b/"
        }'
```

### [PUT /miniapps/{id}/versions/{version\_id}](#PUT+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D)

Updates an existing version of a Mini App.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Request Body](#Request+Body)

```
{
    "platform_id": "string",
    "metadata": "object_id",
    "integrated_security": "boolean",
    "main_name": "string",
    "main_type": "string",    /*Panel, Menu*/
    "service_url": "URL"
}
```

To learn how to generate an "object\_id" read [HowTo: Upload an image, video, or audio file via an API object Using Postman](https://wiki.genexus.com/commwiki/wiki?51411).

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/miniapps/{id}/versions/{version_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "platform_id": "iOS",
            "metadata": "gxupload:f292ef3f9ac94294a66cc353c4802c35",
            "integrated_security": true,
            "main_name": "startObject",
            "main_type": "Panel",
            "service_url": "https://apps6.genexus.com/Id555317f4080a0da816dc4eb15d69bc1b/"
        }'
```

### [POST /miniapps/{id}/versions/{version\_id}/compatibility](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Fcompatibility)

Adds compatibility with the version of a Super App in the Mini App version.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Request Body](#Request+Body)

```
{
    "superapp_version": "int"
}
```

### [Response](#Response)

If the compatibility is successfully added, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/compatibility" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "superapp_version": 1
        }'
```

### [POST /miniapps/{id}/versions/{version\_id}/compatibility/delete](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Fcompatibility%2Fdelete)

Deletes compatibility with the version of a Super App in the Mini App version.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Request Body](#Request+Body)

```
{
    "superapp_version": "int"
}
```

### [Response](#Response)

If the compatibility is successfully deleted, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/compatibility/delete" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "superapp_version": 1
        }'
```

### [POST /miniapps/{id}/versions/{version\_id}/send\_to\_review](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Fsend_to_review)

Sends to review a particular version of a Mini App identified by its id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If status setting is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/send_to_review" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
```

### [POST /miniapps/{id}/versions/{version\_id}/in\_review](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Fin_review)

Sets a version of a Mini App as "in review".

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If status setting is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/in_review" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
```

### [POST /miniapps/{id}/versions/{version\_id}/rejected](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Frejected)

This endpoint sets a version of a Mini App identified by its id and as "rejected".

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If status setting is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/rejected" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
```

### [POST /miniapps/{id}/versions/{version\_id}/ready](#POST+%2Fminiapps%2F%7Bid%7D%2Fversions%2F%7Bversion_id%7D%2Fready)

Sets a version of a Mini App identified by its id as "ready".

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Mini app ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If status setting is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/miniapps/{id}/versions/{version_id}/ready" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Mini App Center - API Reference - Mini App](https://wiki.genexus.com/commwiki/wiki?57798) |

---
