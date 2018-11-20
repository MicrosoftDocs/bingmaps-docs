# Location Recognition

Given a pair of location coordinates (latitude, longitude), the Location Recognition API returns a list of entities ranked by their proximity to that location. The URL response contains three components: local business entities near that location (e.g. restaurants, hotels, office buildings, transit stations, etc.), natural points of interest near that location (e.g. beaches, valleys, etc.), and a reverse geocoded address of that location. See [Location Recognition Entity Types](../common-parameters-and-types/location-and-recognition-entity-types.md) for a list of supported entity types. You can specify the type of entities you want to receive by setting the `includeEntityTypes` parameter in the URL.


> [!NOTE]
>- This template supports both HTTP and HTTPS protocols
>- Search by query is not supported
>- Only USA locations are supported, other countries will be added soon

## API Parameters

|Parameters|Alias|Description|Values|  
|----|:----:|----|----|
|`point`| |**Required.** The coordinates of the location for which you want the entities situated at that location. A point is specified by a latitude and a longitude. See the definition of point in [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|Use the following value ranges: <br /> Latitude (degrees): `[-90, +90]` <br /> Longitude (degrees): `[-180, +180]` <br /> <br /> Example: `47.610679194331169,-122.10788659751415`| 
|`radius`|`r` |**Optional.** Search radius in kilometers (KM). Search is performed within a circle with the specified radius and centered at the location point. Only those entities that fall within this search circle are returned.|Default search radius is 0.25 KM. The maximum supported radius is 2 KM.|
|`top`||**Optional.** The maximum number of entities returned.|Default value is 10. The maximum value is 20.|
|`dateTime`||**Optional.** Date and time at which the location is visited, in UTC format. When this parameter is specified, entities closed at that day and/or time are ranked lower than entities which are open.|Example: `2018-05-09 13:34:42Z`| 
|`distanceUnit`||**Optional.** Unit for the radius parameter. |Use one of the following values: <br />- `kilometer`, or `km`<br />- `mile`, or `mi` <br /><br /> Default value is `km`.|  
|`verboseplacenames`||**Optional.** Either `true` or `false`.<br><br/>- If `false`: "admin1" & country names will be in their official form (e.g.: “WA” for Washington state in USA and full name, e.g. "Occitanie" in France).<br/><br/>-If `true`: "admin1" names will be in expanded form (e.g. Washington), and "countryRegion" field with full name is added to address.|Default value is `false`.| 
|`includeEntityTypes`||**Optional.** Specifies the entity types returned in the response. Only the specified types will be returned. If no entity types are found at the location point, then no location information is returned in the response.<br /><br /> See [Location Recognition Entity Types](../common-parameters-and-types/location-and-recognition-entity-types.md) for a description of the values.|A comma separated list of entity types selected from the following options:<br>- `businessAndPOI`<br>- `naturalPOI`<br>- `address` <br><br>Default value is `businessAndPOI`.| 
|`output`|`o`|**Optional.** Output format for the response.|The following values are supported:<br>- `JSON` <br>- `XML`<br><br>Default value is `JSON`.|

## Include Entity Types

|Entity Type|Description|Example|  
|----------------|-----------|-----------------|  
|`businessAndPOI`|Local businesses and points of interest.|Restaurants, hotels, hospitals, airports, train & bus stations <br /> Office buildings <br /> Municipal & national parks <br /> Landmarks or popular buildings|
|`naturalPOI`|Points of interest, including natural entities.|Lakes, beaches, mountains, valleys, and forests|
|`address`|Reverse geocoded address of the input location. For a description of the address fields, refer to [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|1 Microsoft Way, Redmond, WA 98052, US|

For more information about the location entity types, see  [Location Recognition Entity Types](../common-parameters-and-types/location-and-recognition-entity-types.md).

## Response

One or more entities are returned in the response when you make a request using this URL 
|Field Name|Description|  
|----------------|-----------|
|`businessesAtLocation`|List of businessAddress & businessInfo elements representing the businesses or named venues found within the specified search radius.|
|`naturalPOIAtLocation`|Natural entities or points of interest. For a complete list of supported natural entity types see  [Location Recognition Entity Types](../common-parameters-and-types/location-and-recognition-entity-types.md).|
|`addressOfLocation`|Reverse geocoded address of the input location.|

For more information about the location entity types, see  [Location Recognition Entity Types](../common-parameters-and-types/location-and-recognition-entity-types.md). For information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md).

## Examples

### Find all entities at point on Earth in XML.

This example gets entities situated at a specified location and requests the response in xml format.

```url
http://dev.virtualearth.net/REST/v1/locationrecog/47.640068,-122.129860?key={BingMapsAPIKey}&output=xml
```

Here is the XML Response (truncated for brevity):

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
   xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>7f3146adab974e9b95a665b7099eb692|CO30276242|7.7.0.0</TraceId>
    <ResourceSets>
      <ResourceSet>
        <EstimatedTotal>1</EstimatedTotal>
        <Resources>
          <Resource xsi:type="LocationRecog">
            <IsPrivateResidence>False</IsPrivateResidence>
            <BusinessesAtLocation>
              <BusinessLocationEntity>
                <BusinessAddress>
                  <Latitude>47.640155</Latitude>
                  <Longitude>-122.129788</Longitude>
                  <AddressLine>1 Microsoft Way Bldg 98</AddressLine>
                  <Locality>Redmond</Locality>
                  <AdminDivision>WA</AdminDivision>
                  <CountryIso2>US</CountryIso2>
                  <PostalCode>98052</PostalCode>
                  <FormattedAddress>1 Microsoft Way Bldg 98, Redmond, WA 98052, US</FormattedAddress>
                </BusinessAddress>
                <BusinessInfo>
                  <Id>873x131243969</Id>
                  <EntityName>Eastside Ski & Sport</EntityName>
                  <Url>http://www.eastsideskiandsport.com/</Url>
                  <Phone>(425) 885-3000</Phone>
                  <TypeId>90628</TypeId>
                  <OtherTypeIds>
                    <int>91518</int>
                    <int>91517</int>
                    <int>90826</int>
                  </OtherTypeIds>
                  <Types>Retail</Types>
                  <OtherTypes>
                    <string>Outdoor Recreational Equipment Stores</string>
                    <string>Bicycle Shops</string>
                    <string>Sports & Outdoors</string>
                  </OtherTypes>
                </BusinessInfo>
              </BusinessLocationEntity>
              <BusinessLocationEntity>
                <BusinessAddress>
                  <Latitude>47.640012</Latitude>
                  <Longitude>-122.129756</Longitude>
                  <AddressLine>1 Microsoft Way</AddressLine>
                  <Locality>Redmond</Locality>
                  <AdminDivision>WA</AdminDivision>
                  <CountryIso2>US</CountryIso2>
                  <PostalCode>98052</PostalCode>
                  <FormattedAddress>1 Microsoft Way, Redmond, WA 98052, US</FormattedAddress>
               </BusinessAddress>
               <BusinessInfo>
                 <Id>873x8648196069879702717</Id>
                 <EntityName>Microsoft Alumni Network</EntityName>
                 <Url>http://microsoftalumni.com/</Url>
                 <Phone>(425) 885-3500</Phone>
                 <TypeId>91254</TypeId>
                 <OtherTypeIds>
                   <int>90298</int>
                 </OtherTypeIds>
                 <Types>Charitable Organizations</Types>
                 <OtherTypes>
                   <string>Government & Community</string>
                 </OtherTypes>
               </BusinessInfo>
             </BusinessLocationEntity> 
             
             <!-- * * * -->

           </BusinessesAtLocation>
           <AddressOfLocation>
             <AddressInfo>
             <Latitude>47.640068</Latitude>
             <Longitude>-122.12986</Longitude>
             <AddressLine>1 Microsoft Way</AddressLine>
             <Locality>Redmond</Locality>
             <Neighborhood>Overlake</Neighborhood>
             <AdminDivision>WA</AdminDivision>
             <CountryIso2>US</CountryIso2>
             <PostalCode>98052</PostalCode>
             <FormattedAddress>1 Microsoft Way, Redmond, WA 98052, US</FormattedAddress>
           </AddressInfo>
         </AddressOfLocation>
         <VendorIds>
           <int>3</int>
           <int>208</int>
           <int>224</int>
           <int>225</int>
         </VendorIds>
       </Resource>
     </Resources>
   </ResourceSet>
 </ResourceSets>
</Response>
```

### Find natural entities situated at a specified point on Earth.

This example uses the `includeEntityTypes` parameter to search for natural entities at a point in JSON format.

```url
http://dev.virtualearth.net/REST/v1/locationrecog/47.640068,-122.129860?key={BingMapsAPIKey}&output=json
```

HTTP response in JSON:

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
    "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
      {
        "estimatedTotal": 1,
        "resources": [
          {
            "__type": "LocationRecog:http://schemas.microsoft.com/search/local/ws/rest/v1",
            "naturalPOIAtLocation": [
              {
                "entityName": "Alki Beach Park",
                "latitude": 47.595383,
                "longitude": -122.38659,
                "type": "Beach"
              }
            ]
          }
        ]
      }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "288b508676fb497db1b5cb6525aa0b10|CO30275836|7.7.0.0"
  }
```

### Find the address for a point on Earth.

This URL request gets the address for a point in Downtown Seattle in the JSON format.

```url
http://dev.virtualearth.net/REST/v1/locationrecog/47.609722,-122.333056?key={BingMapsAPIKey}&includeEntityTypes=address&output=json
```

HTTP Request in JSON:

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",
    "copyright": "Copyright c 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 1,
            "resources": [
                {
                    "__type": "LocationRecog:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
                    "isPrivateResidence": "True",
                    "businessesAtLocation": [],
                    "addressOfLocation": [
                        {
                            "latitude": 47.60975,
                            "longitude": -122.33287,
                            "addressLine": "1314 6th Ave",
                            "locality": "Seattle",
                            "neighborhood": "Central Business District",
                            "adminDivision": "WA",
                            "countryIso2": "US",
                            "postalCode": "98101",
                            "formattedAddress": "1314 6th Ave, Seattle, WA 98101, US"
                        }
                    ]
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "6503238c004d4d9384a77d6bd61de26d|CO3035AD45|7.7.0.0"
}
```

This example gets entities situated at a specified location and requests the response in xml format.

This example gets entities for a specified latitude and longitude and requests the results in XML format.

```url
http://dev.virtualearth.net/REST/v1/LocationRecog/47.640068,-122.129860?key={BingMapsAPIKey}&output=xml
``` 

We can also make the same request, but this time searching for business entities within half a mile of the point:

```url
http://dev.virtualearth.net/REST/v1/locationrecog/47.609722,-122.333056?key={BingMapsAPIKey}&r=.5&distanceUnit=mi&includeEntityTypes=address&output=json
```

## HTTP Status Codes

[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]

When the request is successful, the following HTTP status code is returned:
- 200

When the request is not successful, the response returns one of the following errors:
- 204
- 400