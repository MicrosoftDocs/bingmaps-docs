---
title: "Location and Recognition Entity types | Microsoft Docs"
description: "Describes location and recognition entity types and provides the businessAtLocation field, an example, and business entity types."
ms.date: "06/18/2018"
ms.topic: "reference"
author: "v-chrfr"
ms.author: "eriklind"
ms.service: "bing-maps"
---

# Location and Recognition Entity Types

[!INCLUDE [bing-maps-location-recognition-api-retirement](../../includes/bing-maps-location-recognition-api-retirement.md)]

The response returned by the Location Recognition API contains one or more entity types. This article provides descriptions of the various fields associated with each entity type.

## Businesses at Location

Entities like local businesses, offices, museums, parks, and points of interest are grouped under the `businessesAtLocation` element in the response. Each `businessesAtLocation` element contains the following fields.

|Field Name              |Description                                                                      |  
|------------------------|---------------------------------------------------------------------------------|
|`BusinessLocationEntity`|Container element (XML only) for the `businessAddress` and `businessInfo` fields.|
|`businessesAddress`     |Address of the business entity. Multiple entities can be situated at the input location, in such cases each entity has its own address.|
|`businessInfo`          |Name, type and other information about the business entity.                      |

## Example

The following example shows a `businessesAtLocation` element in the Location Recognition API response.

```json
"businessesAtLocation": [
{
              "businessAddress": {
                "latitude": 47.6427448210338,
                "longitude": -122.12949670889715,
                "addressLine": "1 Microsoft Way",
                "locality": "Redmond",
                "adminDivision": "WA",
                "countryIso2": "US",
                "postalCode": "98052",
                "formattedAddress": "1 Microsoft Way, Redmond, WA 98052, US"
              },
              "businessInfo": {
                "id": "873x2278110160718493824",
                "entityName": "Microsoft",
                "url": "https://www.microsoft.com/en-us/",
                "phone": "(425) 882-8080",
                "typeId": 91600,
                "otherTypeIds": [
                  91046,
                  90100
                ],
                "type": "IndustrialStructure",
                "otherTypes": [
                  "Information Technology Companies",
                  "B2B Business Services",
                  "Business-to-Business"
                ]
              }
}
```

### Business Address

A `businessAddress` element contains the following fields.

|Field Name|Description|
|----------------|-----------|
|`latitude,longitude`|Latitude and longitude of the business or location.<br><br>Note that business locations are approximate and aren't guaranteed to be accurate.|

> [!NOTE]
> For the other fields in business address refer to [Location and Area Types](location-and-area-types.md).

### Business Information

A `businessInfo` element contains the following fields.

|Field Name|Description|
|----------------|-----------|
|`entityName`|Name of the business entity.|
|`url`|Website URL of the business entity.|
|`phone`|Phone number of the business entity.|
|`type`|Type of business entity representing the primary nature of business of the entity. Refer to the [Business Entity Types](#business-entity-types) list for a full list of supported types.|
|`otherTypes`|List of types that represent the secondary nature of business of the entity.|

### Business Entity Types

The list of supported entity types.

- Arts & entertainment
- Automotive
- Banking & finance
- Beauty & spa
- Business-to-business
- Education
- Food & drink
- Government
- Healthcare
- News & media
- Professional services
- Real estate
- Religion
- Retail
- Sports & recreation
- Travel

> [!NOTE]
> Granular categories are available under these top-level categories (e.g. different cuisines are available under ‘restaurants’ which itself is under ‘Food & drink’).

### Natural Points of Interest at Location

Natural entities like beaches, etc., are placed in the `naturalPOIAtLocation` element. Each natural entity has the following fields.

|Field Name|Description|
|----------------|-----------|
|`entityName`|Name of the natural entity or point of interest.|
|`latitude,longitude`|Location coordinates of the entity.|
|`type`|Type of natural entity. See the following list of supported types.|

The complete list of supported _natural entity_ types.

- Bay
- Beach
- Canal
- Forest
- Island
- Lake
- Mountain
- Plateau
- Reserve
- River
- Sea
- Valley
