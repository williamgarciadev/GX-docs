---
title: "Mini App Center - API Reference - Platform"
source_id: 57761
source_url: https://wiki.genexus.com/commwiki/wiki?57761
genexus_version: "18"
---

# Mini App Center - API Reference - Platform

The Mini App Center offers an API that provides endpoints for accessing and modifying data within the Platform. This article contains an overview of these endpoints.

Check the [generic variables](https://wiki.genexus.com/commwiki/wiki?57742) required to use the API.

## [Endpoints](#Endpoints)

Below is a summary of the available endpoints for this API:

| Method | Path | Description |
| --- | --- | --- |
| GET | [/platforms](https://wiki.genexus.com/commwiki/wiki?57761) | Gets a list of Platforms. |
| GET | [/platforms/{id}](https://wiki.genexus.com/commwiki/wiki?57761) | Gets Platform details. |
| POST | [/platforms](https://wiki.genexus.com/commwiki/wiki?57761) | Creates a Platform. |
| PUT | [/platforms/{id}](https://wiki.genexus.com/commwiki/wiki?57761) | Updates a Platform. |
| DELETE | [/platforms/{id}](https://wiki.genexus.com/commwiki/wiki?57761) | Deletes a Platform. |

**Note**: This endpoint requires a Mini App Center API token related to the **Provisioning Administrator User** scope. Read more at: [How to create API Key as a Provisioning Administrator User](https://wiki.genexus.com/commwiki/wiki?57935).

### [GET /platforms](#GET+%2Fplatforms)

This endpoint allows you to obtain a list of all available Platforms.

### [Response](#Response)

```
{
    "data": [
        {
            "id": "string",
            "name": "string"
        },
        ...
    ]
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/platforms" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

Pay close attention to the returned ID element that is needed for other related APIs.

### [GET /platforms/{id}](#GET+%2Fplatforms%2F%7Bid%7D)

This endpoint allows you to retrieve details about a specific Platform identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Platform ID (required) |

### [Response](#Response)

```
{
    "data": {
        "id": "string",
        "name": "string"
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/platforms/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /platforms](#POST+%2Fplatforms)

This endpoint is used to create a new Platform.

### [Request Body](#Request+Body)

```
{
    "id": "string",
    "name": "string"
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP StatusCode "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/platforms" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "id": "TST",
            "name": "Testing"
        }'
```

### [PUT /platforms/{id}](#PUT+%2Fplatforms%2F%7Bid%7D)

This endpoint updates an existing Platform, identified by the id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Platform ID (required) |

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
curl -X PUT "$BASE_URL/v1/platforms/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Testing"
        }'
```

### [DELETE /platforms/{id}](#DELETE+%2Fplatforms%2F%7Bid%7D)

This endpoint is used to delete a Platform with a specific id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | string | Platform ID (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/platforms/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Mini App Center - API Reference - Platform](https://wiki.genexus.com/commwiki/wiki?57761) |

---
