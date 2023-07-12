---
title: "Geocoding Japanese Addresses | Microsoft Docs"
description: Learn the complexities of Japanese address geocoding including handling addresses that can be expressed in four different character sets and the Japanese address system and how to implement using The Bing Maps REST API and Bing Spatial Data Services.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 55ae69d1-c46b-4e0e-b5c5-a1785444233d
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocoding Japanese Addresses
Japanese geocoding is complex because addresses can be expressed using four different character sets – three native sets (Kanji, Hiragana, Katakana) as well as the Latin (western) alphabet. Also, Japan uses the Japanese address system which is different from the western address system.  The [Bing Maps REST Services](../rest-services/index.md) and [Bing Spatial Data Services](../spatial-data-services/index.md) offer flexibility to handle the custom needs of Japanese address geocoding and support these key features:  
  
-   **Use of Kanji and Kana (Katakana and Hiragana) character sets**: You can specify Japanese addresses in Kanji, Katakana or Hiragana or a combination of any of these. When you reverse-geocode, the response is returned in either Katakana or Hiragana. See **Japanese and Latin (Hepburn Romanization) Character Sets** below for more details  
  
-   **Use of Hepburn Romanization Latin character set and variants**: You can specify Japanese addresses using the Hepburn character set that uses Latin characters. Some variants are also supported. See the **Hepburn Romanization (Latin character set) and its variants** section below for more details.  
  
-   **Support for western and Japanese address systems**: You can specify a Japanese address using either the Japanese or western address system. See **Japanese and Western Address Systems** below for more details.  
  
-   **Support for addresses with mixed character sets**: You can specify a Japanese address using a combination of characters sets. For example, you can specify an address specified using both Kanji and Latin (Hepburn) characters.  
  
-   **Support for addresses that do not follow standard Japanese address conventions**: You can geocode non-standard Japanese addresses. See **Custom address support** below for more details.  
  
-   **Support for the historical Kyoto Toorina address system**: You can geocode addresses using the Kyoto Toorina address system.  
  
 The Bing Maps APIs are designed to look for and handle the complexity of Japanese geocoding, and will return results for a great variety of situations. However, note that there can be situations where due to the complexity, geocoding may not be successful.  
  
## Geocode using the Bing Maps REST Services Locations API  
 You can use the [Locations](../rest-services/locations/index.md) (part of the Bing Maps REST Services) to geocode Japanese addresses. Each address component can be specified as a separate URL parameter or you can specify the entire address string.  
  
> [!IMPORTANT]
> Japanese address values in native character sets (Kanji, Katakana, Hiragana) must be base-64 encoded UTF-8 strings.  
  
### Geocode using URL address parameters  
 If you know the parsed address, you can specify each component separately using the following URL template and the URL parameters in the table. This type of request will give the best result because the address string does not need to be parsed.  
  
```url
https://dev.virtualearth.net/REST/v1/Locations?countryRegion=countryRegion&adminDistrict=adminDistrict&locality=  
locality&postalCode=postalCode&addressLine=addressLine&culture=ja&key=YourBingMapsKey  
```  
  
 **Address URL parameters with Japanese examples**  
  
 The following table lists the address parameters that you can set in the URL  
  
|URL parameter|Japanese address examples|  
|-----------------------|-----------------------------------|  
|CountryRegion|CountryRegion=JP|  
|PostalCode|PostalCode=〒100-0000<br /><br /> PostalCode=100-0000<br /><br /> **Note**: The symbol 〒 is optional even though it is required by the Japanese addressing system.|  
|AdminDistrict|AdminDistrict=東京都 : Tokyo prefecture<br /><br /> AdminDistrict=北海道 : Hokkaido prefecture<br /><br /> AdminDistrict=大阪府 : Osaka prefecture<br /><br /> AdminDistrict=福岡県 : Other prefectures<br /><br /> **Note**: It is acceptable to include Japan as part of the AdminDistrict by putting it in front of the prefecture. For example: AdminDistrict= 日本、東京都.|  
|Locality|Locality=港区 : Tokyo and other special designated cities<br /><br /> Locality=西多摩郡 : Prefectures with gun<br /><br /> Locality=那覇市 : Other municipals|  
|AddressLine|港区2: Address within the locality|  
|Culture [**REQUIRED**]|Culture=ja OR c=ja<br /><br /> This parameter must be included in all Japanese geocoding requests.|  
  
### Geocode using a single query string  
 If it’s not possible or convenient to separate out the components of the address, you can specify a single address string in the request:  
  
```url
https://dev.virtualearth.net/REST/v1/Locations?q=addressString&culture=ja&key=YourBingMapsKey  
```  
  
### Reverse-geocode  
 To reverse-geocode a Japanese address, specify the latitude and longitude of the location in the request.  
  
```url
https://dev.virtualearth.net/REST/v1/Locations/latitudeIinDegrees,longitudeInDegrees?key=YourBingMapsKey  
```  
  
### Japanese Geocode and Reverse-Geocode URL Examples  
The following examples show how to use these URLs to geocode Japanese addresses. Before trying out these examples, make sure you replace the placeholder YourBingMapsKey with your Bing Maps Key. These URLs will produce an XML response because the output parameter “o=xml” is specified. If you do not specify the output parameter, a JSON response is returned.  

|Request type|Address values, strings or coordinates|Example URL|  
|----|----|----|  
|Geocode an address using URL address parameters|AdminDistrict = 東京都<br /><br /> Locality = 港区<br /><br /> AddressLine = 港南２－１６－３|https://dev.virtualearth.net/REST/v1/Locations?countryRegion=JP&adminDistrict=%E6%9D%B1%E4%BA%AC%E9%83%BD&locality=%e6%b8%af%e5%8c%ba&addressLine=%e6%b8%af%e5%8d%97%ef%bc%92%e2%88%92%ef%bc%91%ef%bc%96%e2%88%92%ef%bc%93&o=xml&key=YourBingMapsKey|  
|Geocode an address using a single address string|Query = 〒108-0075東京都港区港南２－１６－３|https://dev.virtualearth.net/REST/v1/Locations?query=%e3%80%92108%2d0075%e6%9d%b1%e4%ba%ac%e9%83%bd%e6%b8%af%e5%8c%ba%e6%b8%af%e5%8d%97%ef%bc%92%e2%88%92%ef%bc%91%ef%bc%96%e2%88%92%ef%bc%93&o=xml&c=ja&key=YourBingMapsKey|  
|Geocode a postal code using URL address parameters|PostalCode = 108-0075|https://dev.virtualearth.net/REST/v1/Locations?countryRegion=JP&postalCode=108-0075&o=xml&key=YourBingMapsKey&c=ja|  
|Geocode a postal code using a single address string|Query = 〒108-0075|https://dev.virtualearth.net/REST/v1/Locations?countryRegion=JP&postalCode=%e3%80%92108%2d0075&o=xml&key=YourBingMapsKey&c=ja|  
|Reverse-geocode a latitude and longitude|Latitude=35<br /><br /> Longitude=139|https://dev.virtualearth.net/REST/v1/Locations/35,139?o=xml&key=YourBingMapsKey|  
  
### Geocode Response  
 When you make a geocode request using the Locations API URLs and a location is found that matches the address, a response is returned with the latitude and longitude, a confidence and other information. The following is an example of an XML response returned by a Locations API geocode request. For more information about the fields returned in a Locations API response and the equivalent JSON response format, see [Location Data](../rest-services/locations/location-data.md).  
  
 Japanese address information in the response is returned using Japanese native character sets only (Kanji, Katakana, Hiragana). Latin character representations of Japanese addresses are not returned in the response.  
  
```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.  
<Response xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns="https://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>  
    https://dev.virtualearth.net/Branding/logo_powered_by.png  
  </BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    c6b9f2cdc5bf4145873fe1b60616600c  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>108-0075 東京都港区港南２丁目１６－３</Name>  
          <Point>  
            <Latitude>35.6265754699707</Latitude>  
            <Longitude>139.74099731445313</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>35.623880524118341</SouthLatitude>  
            <WestLongitude>139.73768180735172</WestLongitude>  
            <NorthLatitude>35.629270415823065</NorthLatitude>  
            <EastLongitude>139.74431282155447</EastLongitude>  
          </BoundingBox>  
          <EntityType>Address</EntityType>  
          <Address>  
            <AddressLine>港南２丁目１６－３</AddressLine>  
            <AdminDistrict>東京都</AdminDistrict>  
            <CountryRegion>日本</CountryRegion>  
            <FormattedAddress>108-0075 東京都港区港南２丁目１６－３</FormattedAddress>  
            <Locality>港区</Locality>  
            <PostalCode>108-0075</PostalCode>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>35.6265754699707</Latitude>  
            <Longitude>139.74099731445313</Longitude>  
            <CalculationMethod>Rooftop</CalculationMethod>  
            <UsageType>Display</UsageType>  
          </GeocodePoint>  
        </Location>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
## Geocoding with Bing Spatial Data Services  

 You can geocode a set of addresses using the Bing Spatial Data Services using the [Geocode Dataflow API](../spatial-data-services/index.md). Like the Locations API, the Geocode Dataflow API allows you to geocode a Japanese address by identifying its components or by specifying a single address string. The Geocode Dataflow data schema includes the following input values.  
  
```Values
Id  
GeocodeRequest/Culture  
GeocodeRequest/Query  
GeocodeRequest/Address/AddressLine  
GeocodeRequest/Address/AdminDistrict  
GeocodeRequest/Address/CountryRegion   
GeocodeRequest/Address/AdminDistrict2  
GeocodeRequest/Address/FormattedAddress  
GeocodeRequest/Address/Locality  
GeocodeRequest/Address/PostalCode  
GeocodeRequest/Address/PostalTown  
GeocodeRequest/ConfidenceFilter/MinimumConfidence  
```  
  
 To specify individual components, use the same address definitions as defined above for the Locations API (such as GeocodeRequest/Address/AddressLine and GeocodeRequest/Address/AdminDistrict). To specify a single address query string use GeocodeRequest/Query. For more information about this data schema and how to use the Geocode Dataflow, see [Geocode Dataflow API](../spatial-data-services/index.md),  [Data Schema  v2.0](../spatial-data-services/geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md), and [Walkthrough](../spatial-data-services/geocode-dataflow-api/geocode-dataflow-walkthrough.md).  
  
## Japanese and Western Address Systems  
 The Japanese address system formats addresses in the opposite order of western addresses. In the western address system, you begin with the address details and then proceed to the larger categories such as city and state and postal code. In the Japanese system, the larger categories are listed first and finish with the address details. The Bing Maps REST Services and the Bing Spatial Data Services support geocoding for addresses that use either the Japanese or western address system for all character sets.  For example, you can specify an address using Kanji in the western address system or you can specify an address in Latin characters using the Japanese address system and the API will detect the order.  For best results, specify the values in the exact order shown below for each system.  
  
### Japanese Address System  
 (postcode}{prefecture){city/municipality/ward}{location in city/municipality/ward}{address details)  
  
 Example: 〒108-0075東京都港区港南2-16-3  
  
 Using Latin characters: 108-0075 Tokyo-to Minato-ku Konan 2-16-3  
  
### Western Address System  
 (address details)(location in city/municipality/ward) (city/municipal/ward)(prefIecture)(postcode){country}  
  
 Example: 2-16-3 Konan Minato-ku, Tokyo 108-0075 Japan  
  
## Japanese and Latin (Hepburn/Hebon) Character Sets  
 When you geocode a Japanese address, you can specify the address using any of the native character sets -- Kanji, Hiragana, Katakana – as well as [Hepburn Romanization](https://en.wikipedia.org/wiki/Hepburn_romanization). Hepburn Romanization, also known as Hebon, is a system for writing the Japanese language using the Latin alphabet.  
  
 You can also geocode an address that uses more than one characters set. For example, you can specify different parts of an address in Kanji and the Latin Hepburn system or Kanji and Katakana and still geocode the address. The following example shows an address written using Kanji and Hepburn Romanization.  
  
 Kanji + Heburn Romanization: 東京都Minato-ku Kounan 2-16-3  
  
 Kanji + Katakana: 東京都ミナト区  
  
 Note that when you reverse-geocode, the address is returned in the native Japanese character sets (Kanji, Katakana and Hiragana) only. Hepburn Romanization (Latin characters) are not supported for reverse-geocoding.  
  
## Hepburn (Hebon) Romanization (Latin character set) and its variants  
 Many of the Hepburn Romanization variants can be used when you geocode a Japanese address. Examples of supported variants include:  
  
-   Using suffixes that come from phonetic sounds. The following example contains the suffixes “-ku” and “-to” which are suffixes that come from the phonetic sounds that mean ward and prefecture respectively.  
  
     2-16-3 Kounan Minato-ku, Tokyo-to 108-0075 Japan  
  
-   Using multiple forms of Japanese Hepburn spelling. For example, you can specify  “Konan” instead of the Japanese phonetic spelling “Kounan”.  
  
     2-16-3 Konan, Minato Ward, Tokyo-to, Japan  
  
-   Using special Unicode characters that are part of Hepburn such as a Latin character “o” with macron ō:  
  
     2-16-3 Kōnan, Minato-ku, Tōkyō, Japan  
  
## Custom Address Support  
 You can also geocode custom or unofficial addresses. For example, if an address contains additional information that is not part of the official address, you may still be able to geocode the address.  
  
 Address alone: 長野県長野市南長野  
  
 Address with extra value: 長野県長野市大字南長野  
  
 Note that while the Bing Maps geocoding APIs are designed to try to handle custom addresses, there may be some custom addresses that are not successfully geocoded.