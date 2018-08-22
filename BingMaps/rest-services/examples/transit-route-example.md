---
title: "Transit Route Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ff91d581-63c5-4c4c-a93a-572813e825e3
caps.latest.revision: 13
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Transit Route Example
The following example shows how to request a transit route between the Golden Gate Bridge and Fisherman’s Wharf in San Francisco for 3 PM on the current day. Responses are shown for both XML and JSON formats.  
  
```  
http://dev.virtualearth.net/REST/V1/Routes/Transit?wp.0=Golden%20Gate%20Bridge&wp.1=Fishermans%20Wharf&timeType=Departure&dateTime=3:00:00PM&output=xml&key=BingMapsKey  
```  
  
 **JSON Response**  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  37.798622,  
                  -122.478302,  
                  37.818314,  
                  -122.414979  
               ],  
               "id":"v65,h885817486,i0,a0,cen-US,dANjhgdIm0Qg1,y1,s1,m4,o1,t0,wjpNcA2HvHPU1~AaComJlxLwkCAADgAYhnAD8B0~R29sZGVuIEdhdGUgQnJpZGdlLCBDQQ2~~~,wYFlcAxFhHvU1~AaComJkTpAkCAADgAfHx_z4A0~RmlzaGVybWFuJ3MgV2hhcmYsIENB0~~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           37.808316,  
                           -122.414979  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           37.818314,  
                           -122.478302  
                        ]  
                     },  
                     "alternateVias":[  
  
                     ],  
                     "cost":0,  
                     "endLocation":{  
                        "bbox":[  
                           37.779341,  
                           -122.46385,  
                           37.837282,  
                           -122.366106  
                        ],  
                        "name":"Fisherman's Wharf, CA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              37.808311,  
                              -122.414978  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"CA",  
                           "adminDistrict2":"San Francisco Co.",  
                           "countryRegion":"United States",  
                           "formattedAddress":"Fisherman's Wharf, CA",  
                           "locality":"San Francisco",  
                           "landmark":"Fisherman's Wharf"  
                        },  
                        "confidence":"High",  
                        "entityType":"NauticalStructure",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 37.808311,  
                                 -122.414978  
                              ],  
                              "calculationMethod":"Rooftop",  
                              "usageTypes":[  
                                 "Display"  
                              ]  
                           }  
                        ],  
                        "matchCodes":[  
                           "Good"  
                        ]  
                     },  
                     "endTime":"\/Date(1397602707000-0700)\/",  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"",  
                           "details":[  
                              {  
                                 "endPathIndices":[  
                                    7  
                                 ],  
                                 "maneuverType":"Walk",  
                                 "mode":"Transit",  
                                 "roadType":"NotApplicable",  
                                 "startPathIndices":[  
                                    0  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"DepartStart",  
                              "text":"Walk: From Golden Gate Bridge, CA to Golden Gate Bridge Toll Plaza Southbound"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 37.818314,  
                                 -122.478302  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":1.35,  
                           "travelDuration":972,  
                           "travelMode":"Transit"  
                        },  
                        {  
                           "childItineraryItems":[  
                              {  
                                 "compassDirection":"",  
                                 "details":[  
                                    {  
                                       "maneuverType":"TransitDepart",  
                                       "mode":"Transit",  
                                       "names":[  
                                          "Golden Gate Bridge Toll Plaza Southbound"  
                                       ],  
                                       "roadType":"None"  
                                    }  
                                 ],  
                                 "exit":"",  
                                 "iconType":"None",  
                                 "instruction":{  
                                    "formattedText":null,  
                                    "maneuverType":"TransitDepart",  
                                    "text":"Depart: Golden Gate Bridge Toll Plaza Southbound"  
                                 },  
                                 "maneuverPoint":{  
                                    "type":"Point",  
                                    "coordinates":[  
                                       0,  
                                       0  
                                    ]  
                                 },  
                                 "sideOfStreet":"Unknown",  
                                 "time":"\/Date(1397600460000-0700)\/",  
                                 "tollZone":"",  
                                 "transitStopId":1186806,  
                                 "transitTerminus":"",  
                                 "travelDistance":0,  
                                 "travelDuration":0,  
                                 "travelMode":"Transit",  
                                 "tripId":517611  
                              },  
                              {  
                                 "compassDirection":"",  
                                 "details":[  
                                    {  
                                       "maneuverType":"TransitArrive",  
                                       "mode":"Transit",  
                                       "names":[  
                                          "Van Ness Av & Union St"  
                                       ],  
                                       "roadType":"None"  
                                    }  
                                 ],  
                                 "exit":"",  
                                 "iconType":"None",  
                                 "instruction":{  
                                    "formattedText":null,  
                                    "maneuverType":"TransitArrive",  
                                    "text":"Arrive: Van Ness Av & Union St"  
                                 },  
                                 "maneuverPoint":{  
                                    "type":"Point",  
                                    "coordinates":[  
                                       0,  
                                       0  
                                    ]  
                                 },  
                                 "sideOfStreet":"Unknown",  
                                 "time":"\/Date(1397601360000-0700)\/",  
                                 "tollZone":"",  
                                 "transitStopId":1186800,  
                                 "transitTerminus":"",  
                                 "travelDistance":0,  
                                 "travelDuration":0,  
                                 "travelMode":"Transit",  
                                 "tripId":517611  
                              }  
                           ],  
                           "compassDirection":"",  
                           "details":[  
                              {  
                                 "endPathIndices":[  
                                    28  
                                 ],  
                                 "maneuverType":"TakeTransit",  
                                 "mode":"Transit",  
                                 "roadType":"NotApplicable",  
                                 "startPathIndices":[  
                                    7  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "hints":[  
                              {  
                                 "hintType":null,  
                                 "text":"Previous stop is Lombard St & Fillmore St"  
                              },  
                              {  
                                 "hintType":null,  
                                 "text":"If you reach Van Ness Av & Pacific Av, you've gone too far"  
                              }  
                           ],  
                           "iconType":"Bus",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TakeTransit",  
                              "text":"Bus: Take 10 - South"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 37.807011,  
                                 -122.47567  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitLine":{  
                              "abbreviatedName":"10",  
                              "agencyId":1178,  
                              "agencyName":"Golden Gate Transit",  
                              "lineColor":3368703,  
                              "lineTextColor":16777215,  
                              "phoneNumber":"(415) 455-2000)",  
                              "providerInfo":"Service Provider: Golden Gate Transit, Phone: (415) 455-2000)",  
                              "uri":"http:\/\/www.goldengate.org",  
                              "verboseName":"Strawberry - Marin City - San Francisco",  
                              "version":"Mar 30 2014 10:06PM"  
                           },  
                           "transitTerminus":"South",  
                           "travelDistance":5.094,  
                           "travelDuration":900,  
                           "travelMode":"Transit"  
                        },  
                        {  
                           "compassDirection":"",  
                           "details":[  
                              {  
                                 "endPathIndices":[  
                                    38  
                                 ],  
                                 "maneuverType":"Walk",  
                                 "mode":"Transit",  
                                 "roadType":"NotApplicable",  
                                 "startPathIndices":[  
                                    28  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"ArriveFinish",  
                              "text":"Walk: From Van Ness Av & Union St to Fisherman's Wharf, CA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 37.798622,  
                                 -122.424179  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":1.87,  
                           "travelDuration":1347,  
                           "travelMode":"Transit"  
                        }  
                     ],  
                     "routeRegion":"Transit-WD",  
                     "routeSubLegs":[  
                        {  
                           "endWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 37.808311,  
                                 -122.414978  
                              ],  
                              "description":"Fisherman's Wharf, CA",  
                              "isVia":false,  
                              "locationIdentifier":"1|160|168|152|153|19|164|9|2|0|0|224|1|241|241|255|62|0|37.808316,-122.414979",  
                              "routePathIndex":38  
                           },  
                           "startWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 37.818298,  
                                 -122.478439  
                              ],  
                              "description":"Golden Gate Bridge, CA",  
                              "isVia":false,  
                              "locationIdentifier":"1|160|168|152|153|113|47|9|2|0|0|224|1|136|103|0|63|1|37.818314,-122.478302",  
                              "routePathIndex":0  
                           },  
                           "travelDistance":8.314,  
                           "travelDuration":3219  
                        }  
                     ],  
                     "startLocation":{  
                        "bbox":[  
                           37.810162,  
                           -122.47979,  
                           37.82608,  
                           -122.476936  
                        ],  
                        "name":"Golden Gate Bridge, CA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              37.818298,  
                              -122.478439  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"CA",  
                           "adminDistrict2":"San Francisco Co.",  
                           "countryRegion":"United States",  
                           "formattedAddress":"Golden Gate Bridge, CA",  
                           "landmark":"Golden Gate Bridge"  
                        },  
                        "confidence":"High",  
                        "entityType":"TouristStructure",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 37.818298,  
                                 -122.478439  
                              ],  
                              "calculationMethod":"Rooftop",  
                              "usageTypes":[  
                                 "Display"  
                              ]  
                           }  
                        ],  
                        "matchCodes":[  
                           "Good"  
                        ]  
                     },  
                     "startTime":"\/Date(1397599488000-0700)\/",  
                     "travelDistance":8.314,  
                     "travelDuration":3219  
                  }  
               ],  
               "travelDistance":8.314,  
               "travelDuration":3219  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"9e61674cf15a41af9b30f92d191872cc "  
}  
```  
  
 **XML Response**  
  
 Set output=xml to the URL to get an XML response.  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>313a7161f7404f18b3c39f0187017881|CH10023745</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Route>  
          <Id>v65,h-1816995113,i0,a0,cen-US,dAAAAAAAAAAA1,y0,s1,m2,o2,t0,w-81XBGczNAA1~A5QlvVABsgEYAADgAfQb-j4A0~RWlmZmVsIFRvd2VyLCBQYXJpcywgRnJhbmNl0~~~,w-uVXBIcjNQA1~A5QlvVDDAAYYAADgAQAAAAAA0~TG91dnJlLCBQYXJpcywgRnJhbmNl0~~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>48.858623</SouthLatitude>  
            <WestLongitude>2.293761</WestLongitude>  
            <NorthLatitude>48.862928</NorthLatitude>  
            <EastLongitude>2.335222</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>3.627</TravelDistance>  
          <TravelDuration>2611</TravelDuration>  
          <TravelDurationTraffic>2611</TravelDurationTraffic>  
          <RouteLeg>  
            <TravelDistance>3.627</TravelDistance>  
            <TravelDuration>2611</TravelDuration>  
            <Cost>0</Cost>  
            <ActualStart>  
              <Latitude>48.858623</Latitude>  
              <Longitude>2.293965</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>48.86274</Latitude>  
              <Longitude>2.335222</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>Eiffel Tower, Paris, France</Name>  
              <Point>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>48.82963</SouthLatitude>  
                <WestLongitude>2.235303</WestLongitude>  
                <NorthLatitude>48.887571</NorthLatitude>  
                <EastLongitude>2.352657</EastLongitude>  
              </BoundingBox>  
              <EntityType>Monument</EntityType>  
              <Address>  
                <AdminDistrict>IdF</AdminDistrict>  
                <AdminDistrict2>Paris</AdminDistrict2>  
                <CountryRegion>France</CountryRegion>  
                <FormattedAddress>Eiffel Tower, Paris, France</FormattedAddress>  
                <Locality>Paris</Locality>  
                <Landmark>Eiffel Tower</Landmark>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </StartLocation>  
            <EndLocation>  
              <Name>Louvre, Paris, France</Name>  
              <Point>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>48.859371</SouthLatitude>  
                <WestLongitude>2.33046</WestLongitude>  
                <NorthLatitude>48.863522</NorthLatitude>  
                <EastLongitude>2.33995</EastLongitude>  
              </BoundingBox>  
              <EntityType>Museum</EntityType>  
              <Address>  
                <AdminDistrict>IdF</AdminDistrict>  
                <AdminDistrict2>Paris</AdminDistrict2>  
                <CountryRegion>France</CountryRegion>  
                <FormattedAddress>Louvre, Paris, France</FormattedAddress>  
                <Locality>Paris</Locality>  
                <Landmark>Louvre</Landmark>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.07</TravelDistance>  
              <TravelDuration>50</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.858623</Latitude>  
                <Longitude>2.293965</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart from Eiffel Tower, Paris, France</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>DepartStart</ManeuverType>  
                <StartPathIndex>0</StartPathIndex>  
                <EndPathIndex>2</EndPathIndex>  
                <CompassDegrees>54</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <TowardsRoadName>Allée Jean Paulhan</TowardsRoadName>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.16</TravelDistance>  
              <TravelDuration>114</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.85905</Latitude>  
                <Longitude>2.293761</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRightThenTurnLeft">Turn right, and then immediately turn left onto Allée Paul Deschanel</Instruction>  
              <CompassDirection>northwest</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>2</StartPathIndex>  
                <EndPathIndex>4</EndPathIndex>  
                <CompassDegrees>54</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>4</StartPathIndex>  
                <EndPathIndex>5</EndPathIndex>  
                <Name>Allée Paul Deschanel</Name>  
                <CompassDegrees>303</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.557</TravelDistance>  
              <TravelDuration>401</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.860123</Latitude>  
                <Longitude>2.295011</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Quai Branly</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>5</StartPathIndex>  
                <EndPathIndex>10</EndPathIndex>  
                <Name>Quai Branly</Name>  
                <CompassDegrees>53</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>1.302</TravelDistance>  
              <TravelDuration>937</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862263</Latitude>  
                <Longitude>2.301518</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepStraight">Keep straight onto Quai d'Orsay</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>10</StartPathIndex>  
                <EndPathIndex>17</EndPathIndex>  
                <Name>Quai d'Orsay</Name>  
                <CompassDegrees>84</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
                <LocationCode>F32-51763</LocationCode>  
                <LocationCode>F32-51762</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.416</TravelDistance>  
              <TravelDuration>299</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862579</Latitude>  
                <Longitude>2.319033</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RoadNameChange">Road name changes to Quai Anatole France</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>RoadNameChange</ManeuverType>  
                <StartPathIndex>17</StartPathIndex>  
                <EndPathIndex>19</EndPathIndex>  
                <Name>Quai Anatole France</Name>  
                <CompassDegrees>100</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
                <LocationCode>F32-51762</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.196</TravelDistance>  
              <TravelDuration>140</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861131</Latitude>  
                <Longitude>2.324182</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto Passerelle Léopold Sédar Senghor</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>19</StartPathIndex>  
                <EndPathIndex>21</EndPathIndex>  
                <Name>Passerelle Léopold Sédar Senghor</Name>  
                <CompassDegrees>36</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.247</TravelDistance>  
              <TravelDuration>177</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862703</Latitude>  
                <Longitude>2.325368</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Terrasse du Bord de l'Eau</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>21</StartPathIndex>  
                <EndPathIndex>24</EndPathIndex>  
                <Name>Terrasse du Bord de l'Eau</Name>  
                <CompassDegrees>108</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.165</TravelDistance>  
              <TravelDuration>118</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.86171</Latitude>  
                <Longitude>2.32841</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto path</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>24</StartPathIndex>  
                <EndPathIndex>28</EndPathIndex>  
                <CompassDegrees>41</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.239</TravelDistance>  
              <TravelDuration>171</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862799</Latitude>  
                <Longitude>2.329579</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Jardin du Carrousel</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>28</StartPathIndex>  
                <EndPathIndex>30</EndPathIndex>  
                <CompassDegrees>108</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>30</StartPathIndex>  
                <EndPathIndex>32</EndPathIndex>  
                <Name>Jardin du Carrousel</Name>  
                <CompassDegrees>107</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.038</TravelDistance>  
              <TravelDuration>27</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861861</Latitude>  
                <Longitude>2.332529</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepStraight">Keep straight onto path</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>32</StartPathIndex>  
                <EndPathIndex>35</EndPathIndex>  
                <CompassDegrees>107</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.026</TravelDistance>  
              <TravelDuration>18</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861861</Latitude>  
                <Longitude>2.33298</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepLeft">Keep left onto path</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepLeft</ManeuverType>  
                <StartPathIndex>35</StartPathIndex>  
                <EndPathIndex>37</EndPathIndex>  
                <CompassDegrees>40</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.041</TravelDistance>  
              <TravelDuration>29</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862048</Latitude>  
                <Longitude>2.33313</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepRight">Keep right onto path</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepRight</ManeuverType>  
                <StartPathIndex>37</StartPathIndex>  
                <EndPathIndex>40</EndPathIndex>  
                <CompassDegrees>90</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.125</TravelDistance>  
              <TravelDuration>90</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862118</Latitude>  
                <Longitude>2.333581</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepRight">Keep right toward Place du Carrousel</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepRight</ManeuverType>  
                <StartPathIndex>40</StartPathIndex>  
                <EndPathIndex>44</EndPathIndex>  
                <CompassDegrees>82</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.045</TravelDistance>  
              <TravelDuration>32</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862419</Latitude>  
                <Longitude>2.3349</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto Place du Carrousel</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>44</StartPathIndex>  
                <EndPathIndex>45</EndPathIndex>  
                <Name>Place du Carrousel</Name>  
                <CompassDegrees>45</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>MajorRoad</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.86274</Latitude>  
                <Longitude>2.335222</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Louvre, Paris, France</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Hint>If you reach Rue de Rohan, you've gone too far</Hint>  
              <Detail>  
                <ManeuverType>ArriveFinish</ManeuverType>  
                <StartPathIndex>45</StartPathIndex>  
                <EndPathIndex>45</EndPathIndex>  
                <Name>Place du Carrousel</Name>  
                <CompassDegrees>45</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>MajorRoad</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <RouteSubLeg>  
              <TravelDistance>3.627</TravelDistance>  
              <TravelDuration>2611</TravelDuration>  
              <StartWaypoint>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
                <Description>Eiffel Tower, Paris, France</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>3|148|37|189|80|1|178|1|24|0|0|224|1|244|27|250|62|0|48.858623,2.293965</LocationIdentifier>  
                <RoutePathIndex>0</RoutePathIndex>  
              </StartWaypoint>  
              <EndWaypoint>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
                <Description>Louvre, Paris, France</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>3|148|37|189|80|195|0|6|24|0|0|224|1|0|0|0|0|0|48.86274,2.335222</LocationIdentifier>  
                <RoutePathIndex>45</RoutePathIndex>  
              </EndWaypoint>  
            </RouteSubLeg>  
            <StartTime>0001-01-01T00:00:00</StartTime>  
            <EndTime>0001-01-01T00:00:00</EndTime>  
            <Description />  
            <RouteRegion>EU</RouteRegion>  
          </RouteLeg>  
        </Route>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
## See Also  
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../json-data-contracts.md)   
 [Bing Maps Transit Coverage](http://msdn.microsoft.com/en-us/library/hh441739.aspx)