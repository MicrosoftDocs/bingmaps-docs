---
title: "Map Style Sheet Entries | Microsoft Docs"
description: "This article lists map style sheet entries that can be used to customize the appearance of a map in various Microsoft map controls."
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: C22745F9-7DD9-4348-8476-DC1AC0F7AC98
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Entries

The entries listed below can be used in a [map style sheet](map-style-sheets.md) to customize the appearance of a map in various [Microsoft map controls](map-style-sheet-support.md). They can also be used to define how overlaid geometry on a map should be represented.

> [!TIP]
> Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

## Settings and Elements

The entries shown below are a hierarchy where a [property](map-style-sheet-entry-properties.md) on a parent entry will override child entry properties.  This table uses ">" to represent levels in the entry hierarchy.  The properties available to each entry can be found in the entry's property group.

| Name                                | Property Group | Web      | Style | Description |
|-------------------------------------|----------------|----------|-------|-------------|
| version                             | [Version]      | version  | [1.0] | The style sheet version that you want to use. |
| settings                            | [Settings]     | g        | [1.0] | The settings that apply to the whole style sheet. |
| baseMapStyle                        | [BaseMapStyle] |          | [1.4] | Map style from which this map style is derived. |
| mapElement                          | [MapElement]   | me       | [1.0] | The parent entry to all map entries. |
| > baseMapElement                    | [MapElement]   | bme      | [1.0] | The parent entry to all non-user entries. |
| >> area                             | [MapElement]   | ar       | [1.0] | Areas describing land use. These should not to be confused with the physical buildings which are under the structure entry. |
| >>> airport                         | [MapElement]   | ap       | [1.0] | Areas that encompass airports. |
| >>> areaOfInterest                  | [MapElement]   | ai       | [1.1] | Areas in which there are a high concentration of businesses or interesting points. |
| >>> cemetery                        | [MapElement]   | cm       | [1.0] | Areas that encompass cemeteries. |
| >>> continent                       | [MapElement]   | ct       | [1.0] | Continent area labels. |
| >>> education                       | [MapElement]   | ed       | [1.0] | Areas that encompass schools and other educational facilities. |
| >>> indigenousPeoplesReserve        | [MapElement]   | ipr      | [1.0] | Areas that encompass indigenous peoples reserves. |
| >>> industrial                      | [MapElement]   | ind      | [1.1] | Areas that are used for industrial purposes. |
| >>> island                          | [MapElement]   | is       | [1.0] | Island area labels. |
| >>> medical                         | [MapElement]   | md       | [1.0] | Areas that are used for medical purposes (For example: a hospital campus). |
| >>> military                        | [MapElement]   | ima      | [1.0] | Areas that encompass military bases or have military uses. |
| >>> nautical                        | [MapElement]   | nt       | [1.0] | Areas that are used for nautical related purposes. |
| >>> neighborhood                    | [MapElement]   | nh       | [1.0] | Neighborhood area labels. |
| >>> runway                          | [MapElement]   | rw       | [1.0] | Areas that is used as an airplane runway. |
| >>> sand                            | [MapElement]   | sn       | [1.0] | Sandy areas like beaches. |
| >>> shoppingCenter                  | [MapElement]   | sct      | [1.0] | Areas of ground allocated for malls or other shopping centers. |
| >>> stadium                         | [MapElement]   | sta      | [1.0] | Areas that encompass stadiums. |
| >>> underground                     | [MapElement]   | ug       | [1.1] | Underground areas (For example: a metro station footprint). |
| >>> vegetation                      | [MapElement]   | vg       | [1.0] | Forests, grassy areas, etc. |
| >>>> forest                         | [MapElement]   | fr       | [1.0] | Areas of forest land. |
| >>>> golfCourse                     | [MapElement]   | gc       | [1.0] | Areas that encompass golf courses. |
| >>>> park                           | [MapElement]   | pr       | [1.0] | Areas that encompass parks. |
| >>>> playingField                   | [MapElement]   | pf       | [1.0] | Extracted pitches such as a baseball field or tennis court. |
| >>>> reserve                        | [MapElement]   | rsv      | [1.0] | Areas that encompass nature reserves. |
| >> frozenWater                      | [PointStyle]   | fw       | [1.4] | Frozen water, like glacier. |
| >> point                            | [PointStyle]   | pt       | [1.0] | All point features that are drawn with an icon of some sort. |
| >>> address                         | [PointStyle]   | adr      | [1.2] | Address numbers labels. |
| >>> naturalPoint                    | [PointStyle]   | np       | [1.0] | Icons that represent natural features. |
| >>>> peak                           | [PointStyle]   | pk       | [1.0] | Icons that represent mountain peaks. |
| >>>>> volcanicPeak                  | [PointStyle]   | vp       | [1.0] | Icons that represent volcano peaks. |
| >>>> waterPoint                     | [PointStyle]   | wp       | [1.0] | Icons that represent water feature locations such as a waterfall. |
| >>> pointOfInterest                 | [PointStyle]   | poi      | [1.0] | Icons that represent any interesting location. |
| >>>> business                       | [PointStyle]   | bs       | [1.0] | Icons that represent any business location. |
| >>>>> attractionPoint               | [PointStyle]   | atp      | [1.1] | Icons that represent tourist attractions such as museums, zoos, etc. |
| >>>>>> amusementPlacePoint          | [PointStyle]   | app      | [1.4] | Amusement place icon. |
| >>>>>> aquariumPoint                | [PointStyle]   | aqp      | [1.4] | Aquarium icon. |
| >>>>>> artGalleryPoint              | [PointStyle]   | agp      | [1.4] | Art gallery icon. |
| >>>>>> campPoint                    | [PointStyle]   | cpp      | [1.4] | Camp icon. |
| >>>>>> fishingPoint                 | [PointStyle]   | fsp      | [1.4] | Fishing icon. |
| >>>>>> gardenPoint                  | [PointStyle]   | gdp      | [1.4] | Garden icon. |
| >>>>>> hikingPoint                  | [PointStyle]   | hkp      | [1.4] | Hiking icon. |
| >>>>>> libraryPoint                 | [PointStyle]   | lbp      | [1.4] | Library icon. |
| >>>>>> museumPoint                  | [PointStyle]   | mp       | [1.4] | Museum icon. |
| >>>>>> naturalPlacePoint            | [PointStyle]   | npp      | [1.4] | Natural place icon. |
| >>>>>> parkPoint                    | [PointStyle]   | pkp      | [1.4] | Park icon. |
| >>>>>> restAreaPoint                | [PointStyle]   | rap      | [1.4] | Rest area icon. |
| >>>>>> touristAttractionPoint       | [PointStyle]   | tap      | [1.4] | Tourist attraction icon. |
| >>>>>> zooPoint                     | [PointStyle]   | zp       | [1.4] | Zoo icon. |
| >>>>> communityPoint                | [PointStyle]   | cop      | [1.1] | Icons that represent locations of general use to the community. |
| >>>>>> conventionCenterPoint        | [PointStyle]   | ccp      | [1.4] | Convention center icon. |
| >>>>>> financialPoint               | [PointStyle]   | fnp      | [1.4] | Financial icon. |
| >>>>>> governmentPoint              | [PointStyle]   | gvp      | [1.4] | Government icon. |
| >>>>>> informationTechnologyPoint   | [PointStyle]   | iftp     | [1.4] | Information technology icon. |
| >>>>>> palacePoint                  | [PointStyle]   | plp      | [1.4] | Palace icon. |
| >>>>>> pollingStationPoint          | [PointStyle]   | rsp      | [1.4] | Polling station icon. |
| >>>>>> researchPoint                | [PointStyle]   | rp       | [1.4] | Research icon. |
| >>>>> educationPoint                | [PointStyle]   | edp      | [1.1] | Icons that represent schools and other education related locations. |
| >>>>> entertainmentPoint            | [PointStyle]   | etp      | [1.1] | Icons that represent entertainment venues such as theaters, cinemas, etc. |
| >>>>>> artsPoint                    | [PointStyle]   | artp     | [1.4] | Arts icon. |
| >>>>>> bowlingPoint                 | [PointStyle]   | bwp      | [1.4] | Bowling icon. |
| >>>>>> casinoPoint                  | [PointStyle]   | csp      | [1.4] | Casino icon. |
| >>>>>> golfCoursePoint              | [PointStyle]   | gfcp     | [1.4] | Golf course icon. |
| >>>>>> gymPoint                     | [PointStyle]   | gp       | [1.4] | Gym icon. |
| >>>>>> marinaPoint                  | [PointStyle]   | mrp      | [1.4] | Marina icon. |
| >>>>>> movieTheaterPoint            | [PointStyle]   | mtp      | [1.4] | Movie theater icon. |
| >>>>>> nightClubPoint               | [PointStyle]   | ncp      | [1.4] | Night club icon. |
| >>>>>> recreationPoint              | [PointStyle]   | rcp      | [1.4] | Recreation icon. |
| >>>>>> skatingPoint                 | [PointStyle]   | sktp     | [1.4] | Skating icon. |
| >>>>>> skiAreaPoint                 | [PointStyle]   | skap     | [1.4] | Ski area icon. |
| >>>>>> stadiumPoint                 | [PointStyle]   | stmp     | [1.4] | Stadium icon. |
| >>>>>> swimmingPoolPoint            | [PointStyle]   | swpp     | [1.4] | Swimming pool icon. |
| >>>>>> theaterPoint                 | [PointStyle]   | tp       | [1.4] | Theater icon. |
| >>>>>> wineryPoint                  | [PointStyle]   | wnp      | [1.4] | Winery icon. |
| >>>>> essentialServicePoint         | [PointStyle]   | esp      | [1.1] | Icons that represent essential services such as parking, banks, gas, etc. |
| >>>>>> atmPoint                     | [PointStyle]   | atmp     | [1.4] | ATM icon. |
| >>>>>> automobileRentalPoint        | [PointStyle]   | atmrt    | [1.4] | Automobile rental icon. |
| >>>>>> automobileRepairPoint        | [PointStyle]   | atmrp    | [1.4] | Automobile repair icon. |
| >>>>>> bankPoint                    | [PointStyle]   | bkp      | [1.4] | Bank icon. |
| >>>>>> clinicPoint                  | [PointStyle]   | clcp     | [1.4] | Clinic icon. |
| >>>>>> electricChargingStationPoint | [PointStyle]   | ecsp     | [1.4] | Electric charging station icon. |
| >>>>>> fireStationPoint             | [PointStyle]   | essp     | [1.4] | FireStation icon. |
| >>>>>> gasStationPoint              | [PointStyle]   | gsp      | [1.4] | GasStation icon. |
| >>>>>> groceryPoint                 | [PointStyle]   | grcp     | [1.4] | Grocery icon. |
| >>>>>> hospitalPoint                | [PointStyle]   | hp       | [1.4] | Hospital icon. |
| >>>>>> laundryPoint                 | [PointStyle]   | lp       | [1.4] | Laundry icon. |
| >>>>>> liquorAndWineStorePoint      | [PointStyle]   | lwsp     | [1.4] | Liquor and wine store icon. |
| >>>>>> mailPoint                    | [PointStyle]   | mlp      | [1.4] | Mail icon. |
| >>>>>> marketPoint                  | [PointStyle]   | mktp     | [1.4] | Market icon. |
| >>>>>> parkingPoint                 | [PointStyle]   | prkp     | [1.4] | Parking icon. |
| >>>>>> PetServicePoint              | [PointStyle]   | ptp      | [1.4] | Pet service icon. |
| >>>>>> pharmacyPoint                | [PointStyle]   | phmp     | [1.4] | Pharmacy icon. |
| >>>>>> policePoint                  | [PointStyle]   | plcp     | [1.4] | Police icon. |
| >>>>>> postalServicePoint           | [PointStyle]   | psts     | [1.4] | Postal service icon. |
| >>>>>> professionalPoint            | [PointStyle]   | pfp      | [1.4] | Professional service icon. |
| >>>>>> toiletPoint                  | [PointStyle]   | tltp     | [1.4] | Toilet icon. |
| >>>>>> veterinarianPoint            | [PointStyle]   | vtp      | [1.4] | Veterinarian icon. |
| >>>>> foodPoint                     | [PointStyle]   | fp       | [1.0] | Icons that represent restaurants, cafés, etc. |
| >>>>>> barAndGrillPoint             | [PointStyle]   | bgp      | [1.4] | Bar and grill icon. |
| >>>>>> barPoint                     | [PointStyle]   | brp      | [1.4] | Bar icon. |
| >>>>>> breweryPoint                 | [PointStyle]   | brwp     | [1.4] | Brewery icon. |
| >>>>>> cafePoint                    | [PointStyle]   | cfp      | [1.4] | Cafe icon. |
| >>>>>> iceCreamShopPoint            | [PointStyle]   | icsp     | [1.4] | Ice cream shop icon. |
| >>>>>> restaurantPoint              | [PointStyle]   | rstp     | [1.4] | Restaurant icon. |
| >>>>>> teaShopPoint                 | [PointStyle]   | tsp      | [1.4] | TeaShop icon. |
| >>>>> lodgingPoint                  | [PointStyle]   | lop      | [1.1] | Icons that represent hotels and other lodging businesses. |
| >>>>>> hotelPoint                   | [PointStyle]   | htp      | [1.4] | Hotel icon. |
| >>>>> realEstatePoint               | [PointStyle]   | rep      | [1.1] | Icons that represent real estate businesses. |
| >>>>> shoppingPoint                 | [PointStyle]   | shp      | [1.1] | Icons that represent hotels and other lodging businesses. |
| >>>>>> automobileDealerPoint        | [PointStyle]   | atmdp    | [1.4] | Automobile dealer icon. |
| >>>>>> beautyAndSpaPoint            | [PointStyle]   | bsp      | [1.4] | Beauty and spa icon. |
| >>>>>> bookstorePoint               | [PointStyle]   | bksp     | [1.4] | Bookstore icon. |
| >>>>>> departmentStorePoint         | [PointStyle]   | dsp      | [1.4] | Department store icon. |
| >>>>>> electronicsShopPoint         | [PointStyle]   | elsp     | [1.4] | Electronics shop icon. |
| >>>>>> golfShopPoint                | [PointStyle]   | glfsp    | [1.4] | Golf shop icon. |
| >>>>>> homeApplianceShopPoint       | [PointStyle]   | hasp     | [1.4] | Home appliance shop icon. |
| >>>>>> mallPoint                    | [PointStyle]   | mllp     | [1.4] | Mall icon. |
| >>>>>> phoneShopPoint               | [PointStyle]   | psp      | [1.4] | Phone shop icon. |
| >>>> venuePoint                     | [PointStyle]   | vpt      | [1.4] | Encapsulates points that are used primarily in venues. |
| >>>>> babyChangingPoint             | [PointStyle]   | bcp      | [1.4] | Baby changing station icon. |
| >>>>> elevatorPoint                 | [PointStyle]   | ep       | [1.4] | Elevator icon. |
| >>>>> entrancePoint                 | [PointStyle]   | enp      | [1.4] | Entrance icon. |
| >>>>> escalatorPoint                | [PointStyle]   | escp     | [1.4] | Escalator icon. |
| >>>>> femaleRestroomPoint           | [PointStyle]   | frp      | [1.4] | Female restroom icon. |
| >>>>> mailServicePoint              | [PointStyle]   | msp      | [1.4] | Mail service icon. |
| >>>>> maleRestroomPoint             | [PointStyle]   | mrrp     | [1.4] | Male restroom icon. |
| >>>>> meetingPoint                  | [PointStyle]   | mep      | [1.4] | Meeting area icon. |
| >>>>> printerPoint                  | [PointStyle]   | prp      | [1.4] | Printer icon. |
| >>>>> restroomPoint                 | [PointStyle]   | rrp      | [1.4] | Restroom icon. |
| >>>>> stairsPoint                   | [PointStyle]   | sp       | [1.4] | Stairs icon. |
| >>>>> teamPoint                     | [PointStyle]   | tep      | [1.4] | Team area icon. |
| >>>>> telephonePoint                | [PointStyle]   | tlp      | [1.4] | Telephone icon. |
| >>> populatedPlace                  | [PointStyle]   | pp       | [1.0] | Icons that represent the size of populated place (For example: a city or town). |
| >>>> capital                        | [PointStyle]   | cp       | [1.0] | Icons that represent the capital of a populated place. |
| >>>>> adminDistrictCapital          | [PointStyle]   | adc      | [1.0] | Icons that represent the capital of a state or province. |
| >>>>>> majorAdminDistrictCapital    | [PointStyle]   |          | [1.4] | Icons that represent the major capital of a state or province. |
| >>>>>> minorAdminDistrictCapital    | [PointStyle]   |          | [1.4] | Icons that represent the minor capital of a state or province. |
| >>>>> countryRegionCapital          | [PointStyle]   | crc      | [1.0] | Icons that represent the capital of a country or region. |
| >>>> majorPopulatedPlace            | [PointStyle]   |          | [1.4] | Icons that represent the size of major populated place. |
| >>>> minorPopulatedPlace            | [PointStyle]   |          | [1.4] | Icons that represent the size of minor populated place. |
| >>> roadShield                      | [PointStyle]   | rs       | [1.0] | Signs that represent the compact name for a road. (For example: I-5). Use only palette values if you set the ImageFamily property of the settings entry to a value of Palette |
| >>> roadExit                        | [PointStyle]   | re       | [1.0] | Icons that represent exits, typically from a controlled access highway. |
| >>> transit                         | [PointStyle]   | trn      | [1.0] | Icons that represent bus stops, train stops, airports, etc. |
| >> political                        | [BorderedMapElement] | pl | [1.0] | Political regions such as countries, regions and states. |
| >>> adminDistrict                   | [BorderedMapElement] | ad | [1.0] | Admin1, states, provinces, etc., borders and labels. |
| >>> countryRegion                   | [BorderedMapElement] | cr | [1.0] | Country region borders and labels. |
| >>> district                        | [BorderedMapElement] | ds | [1.0] | Admin2, counties, etc., borders and labels. |
| >> structure                        | [MapElement]   | str      | [1.0] | Buildings and other building-like structures. |
| >>> building                        | [MapElement]   | bld      | [1.0] | Buildings. |
| >>>> educationBuilding              | [MapElement]   | eb       | [1.0] | Buildings used for education. |
| >>>> medicalBuilding                | [MapElement]   | mb       | [1.0] | Buildings used for medical purposes such as hospitals. |
| >>>> transitBuilding                | [MapElement]   | tb       | [1.0] | Buildings used for transit such as airports. |
| >>> object                          | [MapElement]   | ob       | [1.4] | Object such as a desk or statue. |
| >>> venueFootprint                  | [BorderedMapElement] | vf | [1.4] | Encapsulates fundamental structural parts of a venue. |
| >>>> floor                          | [BorderedMapElement] | fl | [1.4] | Area of an individual floor in a venue. |
| >>>> footprint                      | [BorderedMapElement] | ft | [1.4] | Shadow that all above-ground floors cast on the ground. |
| >>> wall                            | [MapElement]   | wl       | [1.4] | A wall. |
| >>>> activityWall                   | [MapElement]   | awa      | [1.4] | Wall around activity rooms. |
| >>>> foodWall                       | [MapElement]   | fwa      | [1.4] | Wall around food rooms. |
| >>>> secureWall                     | [MapElement]   | swa      | [1.4] | Boundary between secure and regular areas. |
| >>>> shopWall                       | [MapElement]   | shwa     | [1.4] | Wall around shop rooms. |
| >>>> utilityWall                    | [MapElement]   | uwa      | [1.4] | Wall around utility rooms. |
| >>> zone                            | [MapElement]   | zn       | [1.4] | Areas and rooms. |
| >>>> activityZone                   | [MapElement]   | az       | [1.4] | Zone for activities. |
| >>>>> activityRoom                  | [MapElement]   | azr      | [1.4] | Room for activities. |
| >>>> foodZone                       | [MapElement]   | fz       | [1.4] | Zone for food services. |
| >>>>> foodRoom                      | [MapElement]   | fzr      | [1.4] | Room for food services. |
| >>>>> foodShelves                   | [MapElement]   | fzs      | [1.4] | Shelves containing food. |
| >>>> medicalZone                    | [MapElement]   | mz       | [1.4] | Zone for medical purposes. |
| >>>>> medicalShelves                | [MapElement]   | mzs      | [1.4] | Shelves containing medical items. |
| >>>> room                           | [MapElement]   | r        | [1.4] | Unclassified room. |
| >>>> secureZone                     | [MapElement]   | scz      | [1.4] | Zone reached through a security checkpoint. |
| >>>>> secureRoom                    | [MapElement]   | sczr     | [1.4] | Area reached through a security checkpoint. |
| >>>> serviceZone                    | [MapElement]   | sz       | [1.4] | Zone for providing services. |
| >>>>> counter                       | [MapElement]   | szc      | [1.4] | Counter used for information, checkout, etc. |
| >>>>> serviceRoom                   | [MapElement]   | szr      | [1.4] | Room for providing services. |
| >>>> shelves                        | [MapElement]   | sh       | [1.4] | Unclassified shelves. |
| >>>> shopZone                       | [MapElement]   | shz      | [1.4] | Zone for shopping. |
| >>>>> shopRoom                      | [MapElement]   | shzr     | [1.4] | Room for shopping. |
| >>>>> shopShelves                   | [MapElement]   | shzs     | [1.4] | Shelves for shopping. |
| >>>> utilityZone                    | [MapElement]   | uz       | [1.4] | Zone of utilitarian value. |
| >>>>> utilityRoom                   | [MapElement]   | uzr      | [1.4] | Room of utilitarian value like stair wells and elevators. |
| >> transportation                   | [MapElement]   | trs      | [1.0] | Lines that are part of the transportation network (For example: roads, trains, and ferries). |
| >>> road                            | [MapElement]   | rd       | [1.0] | Lines that represent all roads. |
| >>>> controlledAccessHighway        | [MapElement]   | cah      | [1.0] | Lines that represent large, controlled access highways. |
| >>>>> highSpeedRamp                 | [MapElement]   | hsrp     | [1.0] | Lines that represent high speed ramps that typically connect to controlled access highways. |
| >>>> highway                        | [MapElement]   | hg       | [1.0] | Lines that represent highways. |
| >>>> majorRoad                      | [MapElement]   | mr       | [1.0] | Lines that represent major roads. |
| >>>> arterialRoad                   | [MapElement]   | ard      | [1.0] | Lines that represent arterial roads. |
| >>>> street                         | [MapElement]   | st       | [1.0] | Lines that represent streets. |
| >>>>> ramp                          | [MapElement]   | rm       | [1.0] | Lines that represent ramps that typically connect to highways. |
| >>>>> unpavedStreet                 | [MapElement]   | us       | [1.0] | Lines that represent unpaved streets. |
| >>>> tollRoad                       | [MapElement]   | tr       | [1.0] | Lines that represent roads that cost money to use. |
| >>> railway                         | [MapElement]   | rl       | [1.0] | Railway lines. |
| >>> trail                           | [MapElement]   | trl      | [1.0] | Walking trails through parks or hiking trails. |
| >>> walkway                         | [MapElement]   | wlk      | [1.1] | Elevated walkway. |
| >>> waterRoute                      | [MapElement]   | wr       | [1.0] | Ferry route lines. |
| >> water                            | [MapElement]   | wt       | [1.0] | Anything that looks like water. This includes oceans and streams. |
| >>> river                           | [MapElement]   | rv       | [1.0] | Rivers, streams, or other water passages. Note that this may be a line or polygon and might connect to non-river water bodies. |
| > routeMapElement                   | [MapElement]   |          | [1.0] | All routing related entries. |
| >> routeLine                        | [MapElement]   |          | [1.0] | Route line related entries. |
| >>> drivingRoute                    | [MapElement]   |          | [1.0] | Lines that represent driving routes. |
| >>> scenicRoute                     | [MapElement]   |          | [1.1] | Lines that represent scenic driving routes. |
| >>> walkingRoute                    | [MapElement]   |          | [1.0] | Lines that represent walking routes. |
| > userMapElement                    | [MapElement]   |          | [1.0] | All user entries. |
| >> userArea                         | [MapElement]   |          | [1.0] | The default styling for user polygons such as [MapPolygon] instances. |
| >> userBillboard                    | [PointStyle]   |          | [1.1] | The default styling for user billboards such as [MapBillboard] instances. |
| >> userLine                         | [MapElement]   |          | [1.0] | The default styling for user lines such as [MapPolyline] instances. |
| >> userModel3D                      | [MapElement3D] |          | [1.1] | The default styling for user 3D models such as [MapModel3D] instances (primarily for setting renderAsSurface). |
| >> userPoint                        | [PointStyle]   |          | [1.0] | The default styling for user points such as [MapIcon] instances. |

[Version]: map-style-sheet-entry-properties.md#version-properties
[Settings]: map-style-sheet-entry-properties.md#settings-properties
[BaseMapStyle]: map-style-sheet-entry-properties.md#basemapstyle
[MapElement]: map-style-sheet-entry-properties.md#mapelement-properties
[BorderedMapElement]: map-style-sheet-entry-properties.md#borderedmapelement-properties
[MapElement3D]: map-style-sheet-entry-properties.md#mapelement3d-properties
[PointStyle]: map-style-sheet-entry-properties.md#pointstyle-properties
[MapBillboard]: https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapBillboard
[MapPolygon]: https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapPolygon
[MapPolyline]: https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapPolyline
[MapModel3D]: https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapModel3D
[MapIcon]: https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.Maps.MapIcon
[1.0]: map-style-sheet-support.md
[1.1]: map-style-sheet-support.md
[1.2]: map-style-sheet-support.md
[1.3]: map-style-sheet-support.md
[1.4]: map-style-sheet-support.md
[1.5]: map-style-sheet-support.md
