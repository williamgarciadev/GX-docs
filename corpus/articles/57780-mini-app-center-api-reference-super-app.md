---
title: "Mini App Center - API Reference - Super App"
source_id: 57780
source_url: https://wiki.genexus.com/commwiki/wiki?57780
genexus_version: "18"
---

# Mini App Center - API Reference - Super App

The Mini App Center offers an API that provides endpoints for retrieving and modifying data from the Super App. This article contains an overview of these Endpoints.

Check the [generic variables](https://wiki.genexus.com/commwiki/wiki?57742) required to use the API.

## [Endpoints](#Endpoints)

Below is a summary of the available Endpoints for this API:

| Method | Path | Description |
| --- | --- | --- |
| GET | [/superapps/{id}](https://wiki.genexus.com/commwiki/wiki?57780) | Gets Super App details. |
| POST | [/superapps](https://wiki.genexus.com/commwiki/wiki?57780) | Creates a Super App. |
| PUT | [/superapps/{id}](https://wiki.genexus.com/commwiki/wiki?57780) | Updates a Super App. |
| DELETE | [/superapps/{id}](https://wiki.genexus.com/commwiki/wiki?57780) | Deletes a Super App. |
| GET | [/superapps/{id}/attributes/{field}](https://wiki.genexus.com/commwiki/wiki?57780) | Gets details of additional Super App attributes. |
| POST | [/superapps/{id}/attributes](https://wiki.genexus.com/commwiki/wiki?57780) | Creates an additional attribute to the Super App. |
| PUT | [/superapps/{id}/attributes/{field}](https://wiki.genexus.com/commwiki/wiki?57780) | Updates an additional attribute to the Super App. |
| DELETE | [/superapps/{id}/attributes/{field}](https://wiki.genexus.com/commwiki/wiki?57780) | Deletes an additional attribute to the Super App. |
| GET | [/superapps/{id}/versions/{platform\_id}/{version\_id}](https://wiki.genexus.com/commwiki/wiki?57780) | Gets Super App version details. |
| POST | [/superapps/{id}/versions](https://wiki.genexus.com/commwiki/wiki?57780) | Creates a version of Super App. |
| PUT | [/superapps/{id}/versions/{platform\_id}/{version\_id}](https://wiki.genexus.com/commwiki/wiki?57780) | Updates a version of Super App. |
| POST | [/superapps/{id}/versions/{platform\_id}/{version\_id}/disable](https://wiki.genexus.com/commwiki/wiki?57780) | Disables a version of Super App. |
| POST | [/superapps/{id}/versions/{platform\_id}/{version\_id}/enable](https://wiki.genexus.com/commwiki/wiki?57780) | Enables a version of Super App. |
| GET | [/superapps/{id}/versions/{platform\_id}/{version\_id}/public\_key](https://wiki.genexus.com/commwiki/wiki?57780) | Gets Public Key of Super App version. |

**Note**: This endpoint requires a Mini App Center API token related to the **Member Organization User** scope. Read more at: [How to create API Key as an Organization Administrator User](https://wiki.genexus.com/commwiki/wiki?57935).

### [GET /superapps/{id}](#GET+%2Fsuperapps%2F%7Bid%7D)

 This endpoint allows you to retrieve details about a Super App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |

### [Response](#Response)

```
{
    "data": {
        "id": "string",
        "name": "string",
        "organization_id": "GUID",
        "security": "boolean"
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/superapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /superapps](#POST+%2Fsuperapps)

Creates a Super App.

### [Request Body](#Request+Body)

```
{
    "id": "string",
    "name": "string",
    "organization_id": "GUID",    /*Only with Site Admin API token*/
    "security": "boolean"
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/superapps" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "id": "com.genexus.verdantbank",
            "name": "Verdant Bank",
            "security": true
        }'
```

### [PUT /superapps/{id}](#PUT+%2Fsuperapps%2F%7Bid%7D)

This endpoint updates a specific Super App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |

### [Request Body](#Request+Body)

```
{
    "name": "string",
    "security": "boolean"
}
```

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/superapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Verdant Bank",
            "security": false
        }'
```

### [DELETE /superapps/{id}](#DELETE+%2Fsuperapps%2F%7Bid%7D)

Deletes a Super App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/superapps/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [GET /superapps/{id}/attributes/{field}](#GET+%2Fsuperapps%2F%7Bid%7D%2Fattributes%2F%7Bfield%7D)

Invites a member of the Super App.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| field | string | Field (required) |

### [Response](#Response)

```
{
    "data": {
        "superapp_id": "string",
        "field": "string",
        "required": "boolean",
        "type": "string",    /*CHR:Character, NUM:Number, VAL:Values*/,
        "values": [
            "string",
            ...
        ]
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/superapps/{id}/attributes/{field}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /superapps/{id}/attributes](#POST+%2Fsuperapps%2F%7Bid%7D%2Fattributes)

Creates an additional attribute to the Super App identified by its unique id.

### [Request Body](#Request+Body)

```
{
    "field": "string",
    "required": "boolean",
    "type": "string",    /*CHR:Character, NUM:Number, VAL:Values*/,
    "values": [
        "string",
        ...
    ]
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/superapps/{id}/attributes" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "field": "COUNTRY",
            "required": false,
            "type": "VAL",
            "values": [
                "Argentina",
                "Uruguay",
                "Chile",
                "Bolivia"
            ]
        }'
```

### [PUT /superapps/{id}/attributes/{field}](#PUT+%2Fsuperapps%2F%7Bid%7D%2Fattributes%2F%7Bfield%7D)

Updates an additional attribute of a specific Super App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| field | string | Field (required) |

### [Request Body](#Request+Body)

```
{
    "required": "boolean",
    "type": "string",    /*CHR:Character, NUM:Number, VAL:Values*/,
    "values": [
        "string",
        ...
    ]
}
```

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/superapps/{id}/attributes/{field}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "field": "COUNTRY",
            "required": true,
            "type": "CHR"
        }'
```

### [DELETE /superapps/{id}/attributes/{field}](#DELETE+%2Fsuperapps%2F%7Bid%7D%2Fattributes%2F%7Bfield%7D)

Deletes an additional attribute of a Super App identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| field | string | Field (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/superapps/{id}/attributes/{field}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [GET /superapps/{id}/versions/{platform\_id}/{version\_id}](#GET+%2Fsuperapps%2F%7Bid%7D%2Fversions%2F%7Bplatform_id%7D%2F%7Bversion_id%7D)

Gets details about a specific version of a Super App on a particular platform.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| platform\_id | string | Platform ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

```
{
    "data": {
        "superapp_id": "string",
        "id": "int",
        "name": "string"
    }
}
```

if an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/superapps/{id}/versions/{platform_id}/{version_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /superapps/{id}/versions](#POST+%2Fsuperapps%2F%7Bid%7D%2Fversions)

This endpoint creates a new version for a specific Super App identified by its unique id.

### [Request Body](#Request+Body)

```
{
    "platform_id": "string",
    "name": "string"
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/superapps/{id}/versions" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "platform_id": "iOS",
            "name": "Version for iOS"
        }'
```

### [PUT /superapps/{id}/versions/{platform\_id}/{version\_id}](#PUT+%2Fsuperapps%2F%7Bid%7D%2Fversions%2F%7Bplatform_id%7D%2F%7Bversion_id%7D)

Updates a specific version of a Super App on a particular platform.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| platform\_id | string | Platform ID (required) |
| version\_id | int | Version ID (required) |

### [Request Body](#Request+Body)

```
{
    "name": "string"
}
```

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/superapps/{id}/versions/{platform_id}/{version_id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Version for iOS 1.0"
        }'
```

### [POST /superapps/{id}/versions/{platform\_id}/{version\_id}/disable](#POST+%2Fsuperapps%2F%7Bid%7D%2Fversions%2F%7Bplatform_id%7D%2F%7Bversion_id%7D%2Fdisable)

Disables a specific version of a Super App on a particular platform.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| platform\_id | string | Platform ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If the disabling is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/superapps/{id}/versions/{platform_id}/{version_id}/disable" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Version for iOS 1.0"
        }'
```

### [POST /superapps/{id}/versions/{platform\_id}/{version\_id}/enable](#POST+%2Fsuperapps%2F%7Bid%7D%2Fversions%2F%7Bplatform_id%7D%2F%7Bversion_id%7D%2Fenable)

Enables a specific version of a Super App on a particular platform.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| platform\_id | string | Platform ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

If the enabling is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/superapps/{id}/versions/{platform_id}/{version_id}/enable" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Version for iOS 1.0"
        }'
```

### [GET /superapps/{id}/versions/{platform\_id}/{version\_id}/public\_key](#GET+%2Fsuperapps%2F%7Bid%7D%2Fversions%2F%7Bplatform_id%7D%2F%7Bversion_id%7D%2Fpublic_key)

Gets the public key file associated with a specific version of a Super App on a particular platform.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Super app ID (required) |
| platform\_id | string | Platform ID (required) |
| version\_id | int | Version ID (required) |

### [Response](#Response)

Gets the .crt file with the Public Key of the Super App version. If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/superapps/{id}/versions/{platform_id}/{version_id}/public_key" \
    -H "APIKey-Auth: $API_TOKEN" \
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Mini App Center - API Reference - Super App](https://wiki.genexus.com/commwiki/wiki?57780) |

---
