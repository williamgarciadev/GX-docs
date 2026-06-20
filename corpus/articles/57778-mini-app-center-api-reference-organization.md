---
title: "Mini App Center - API Reference - Organization"
source_id: 57778
source_url: https://wiki.genexus.com/commwiki/wiki?57778
genexus_version: "18"
---

# Mini App Center - API Reference - Organization

The Mini App Center offers an API that provides endpoints for retrieving and modifying data from the Organization. This article contains an overview of these endpoints.

Check the [generic variables](https://wiki.genexus.com/commwiki/wiki?57742) required to use the API.

## [Endpoints](#Endpoints)

Below is a summary of the available endpoints for this API:

| Method | Path | Description |
| --- | --- | --- |
| GET | [/organizations](https://wiki.genexus.com/commwiki/wiki?57778) | Gets a list of Organizations. |
| GET | [/organizations/{id}](https://wiki.genexus.com/commwiki/wiki?57778) | Gets Organization details. |
| POST | [/organizations](https://wiki.genexus.com/commwiki/wiki?57778) | Creates an Organization. |
| PUT | [/organizations/{id}](https://wiki.genexus.com/commwiki/wiki?57778) | Updates an Organization. |
| DELETE | [/organizations/{id}](https://wiki.genexus.com/commwiki/wiki?57778) | Deletes an Organization. |
| POST | [/organizations/{id}/member/invite](https://wiki.genexus.com/commwiki/wiki?57778) | Invites a member of the Organization. |
| POST | [/organizations/{id}/member/resendinvite](https://wiki.genexus.com/commwiki/wiki?57778) | Resends the invitation to the member. |
| POST | [/organizations/{id}/member/delete](https://wiki.genexus.com/commwiki/wiki?57778) | Deletes the invitation to the member. |
| PUT | [/organizations/{id}/member/suspend](https://wiki.genexus.com/commwiki/wiki?57778) | Suspends a member of the Organization. |
| PUT | [/organizations/{id}/member/reactivate](https://wiki.genexus.com/commwiki/wiki?57778) | Reactivates a member of the Organization. |
| POST | [/organizations/{id}/superapp/permission](https://wiki.genexus.com/commwiki/wiki?57778) | Adds permission on the Super App in the Organization. |
| POST | [/organizations/{id}/superapp/permission/delete](https://wiki.genexus.com/commwiki/wiki?57778) | Deletes permission on the Super App in the Organization. |

**Note**: This endpoint requires a Mini App Center API token related to the **Provisioning Administrator User** scope. Read more at: [How to create API Key as a Provisioning Administrator User](https://wiki.genexus.com/commwiki/wiki?57935).

### [GET /organizations](#GET+%2Forganizations)

This endpoint is used to retrieve a list of Organizations.

### [Response](#Response)

```
{
    "data": [
        {
            "id": "GUID",
            "name": "string"
        },
        ...
    ]
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/organizations" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

Pay close attention to the returned ID element that is needed for other related APIs.

### [GET /organizations/{id}](#GET+%2Forganizations%2F%7Bid%7D)

This endpoint allows you to retrieve details about a specific Organization identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Response](#Response)

```
{
    "data": {
        "id": "GUID",
        "name": "string",
        "can_create_miniapps": "boolean",
        "can_create_superapps": "boolean"
    }
}
```

If an error has occurred, it will return HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X GET "$BASE_URL/v1/organizations/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /organizations](#POST+%2Forganizations)

This endpoint is used to create a new Organization.

### [Request Body](#Request+Body)

```
{
    "name": "string",
    "can_create_miniapps": "boolean",
    "can_create_superapps": "boolean"
}
```

### [Response](#Response)

If the creation is successful, it will return HTTP response Status "201 Created" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/organizations" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Testing"
            "can_create_miniapps": true,
            "can_create_superapps": false
        }'
```

### [PUT /organizations/{id}](#PUT+%2Forganizations%2F%7Bid%7D)

This endpoint updates details about a specific Organization identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "name": "string",
    "can_create_miniapps": "boolean",
    "can_create_superapps": "boolean"
}
```

### [Response](#Response)

If the update is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/organizations/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "name": "Testing"
            "can_create_miniapps": true,
            "can_create_superapps": true
        }'
```

### [DELETE /organizations/{id}](#DELETE+%2Forganizations%2F%7Bid%7D)

This endpoint deletes a specific Organization identified by its unique id.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X DELETE "$BASE_URL/v1/organizations/{id}" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json"
```

### [POST /organizations/{id}/member/invite](#POST+%2Forganizations%2F%7Bid%7D%2Fmember%2Finvite)

This endpoint is used to invite a member of the Organization.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "email": "string",
    "role": "string"    /* "OrgAdm":Organization Administrator, "SuperAppAdm":Super App Administrator, "MiniAppReview":Mini App Review, "MiniAppDev":Mini App Developer*
}
```

### [Response](#Response)

If the invitation is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/organizations/{id}/member/invite" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "email": "member1@organization.com"
            "role": "OrgAdm"
        }'
```

### [POST /organizations/{id}/member/resendinvite](#POST+%2Forganizations%2F%7Bid%7D%2Fmember%2Fresendinvite)

This endpoint is used to resend the invitation to the member.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "email": "string"
}
```

### [Response](#Response)

If the invitation is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/organizations/{id}/member/resendinvite" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "email": "member1@organization.com"
        }'
```

### [POST /organizations/{id}/member/delete](#POST+%2Forganizations%2F%7Bid%7D%2Fmember%2Fdelete)

This endpoint is used to delete the invitation to the member.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "email": "string"
}
```

### [Response](#Response)

If the deletion is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/organizations/{id}/member/delete" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "email": "member1@organization.com"
        }'
```

### [PUT /organizations/{id}/member/suspend](#PUT+%2Forganizations%2F%7Bid%7D%2Fmember%2Fsuspend)

This endpoint suspends a member of the Organization.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "email": "string"
}
```

### [Response](#Response)

If the suspension is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/organizations/{id}/member/suspend" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "email": "member1@organization.com"
        }'
```

### [PUT /organizations/{id}/member/reactivate](#PUT+%2Forganizations%2F%7Bid%7D%2Fmember%2Freactivate)

This endpoint reactivates a member of the Organization.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "email": "string"
}
```

### [Response](#Response)

If the reactivation is successful, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/organizations/{id}/reactivate" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "email": "member1@organization.com"
        }'
```

### [POST /organizations/{id}/superapp/permission](#POST+%2Forganizations%2F%7Bid%7D%2Fsuperapp%2Fpermission)

This endpoint adds permission to the Super App in the Organization.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "superapp_id": "string"
}
```

### [Response](#Response)

If the permission is successfully added, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X POST "$BASE_URL/v1/organizations/{id}/superapp/permission" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "superapp_id": "com.genexus.verdantbank"
        }'
```

### [POST /organizations/{id}/superapp/permission/delete](#POST+%2Forganizations%2F%7Bid%7D%2Fsuperapp%2Fpermission%2Fdelete)

Deletes permission on the Super App in the Organization.

### [Parameters](#Parameters)

| Name | Type | Description |
| --- | --- | --- |
| id | GUID | Organization ID (required) |

### [Request Body](#Request+Body)

```
{
    "superapp_id": "string"
}
```

### [Response](#Response)

If the permission is successfully deleted, it will return HTTP response Status "204 No Content" and no body. Otherwise, it will show HTTP StatusCode 40x and the body as [errors](https://wiki.genexus.com/commwiki/wiki?57742).

### [cURL Sample](#cURL+Sample)

```
curl -X PUT "$BASE_URL/v1/organizations/{id}/superapp/permission/delete" \
    -H "APIKey-Auth: $API_TOKEN" \
    -H "Accept: application/json" \
    -d '{
            "superapp_id": "com.genexus.verdantbank"
        }'
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Mini App Center - API Reference - Organization](https://wiki.genexus.com/commwiki/wiki?57778) |

---
