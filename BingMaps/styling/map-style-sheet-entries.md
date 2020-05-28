---
title: "Map Style Sheet Entries | Microsoft Docs"
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

The entries listed below can be used in a [map style sheet](map-style-sheets.md) to customize the appearance of a Microsoft map.  They can also be used to define how geometry on a map should be represented.

Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

## Settings and Elements

The JSON entries that can be customized are represented in the following list.  They are represented as a tree structure where setting parent entry properties will override child entry properties.  The properties available to each entry can be found in the entry's property group.  This table uses ">" to represent levels in the entry hierarchy.

| Column          | Description |
|-----------------|-------------|
| Web             | Whether the entry is supported by the web map control and what the URI short name is for it. |
| Windows         | The minimum version of Windows that supports the entry. |
| Android and iOS | The minimum version of the iOS or Android control that supports the entry. |

| Name                                | Property Group | Web     | Windows | Android and iOS | Description |
|-------------------------------------|----------------|---------|---------|-----------------|-------------|
| version                             | [Version]      | version | 1703 | 1.0.0 | The style sheet version that you want to use. |
| settings                            | [Settings]     | g       | 1703 | 1.0.0 | The settings that apply to the whole style sheet. |
| mapElement                          | [MapElement]   | me      | 1703 | 1.0.0 | The parent entry to all map entries. |
| > baseMapElement                    | [MapElement]   | bme     | 1703 | 1.0.0 | The parent entry to all non-user entries. |
| >> area                             | [MapElement]   | ar      | 1703 | 1.0.0 | Areas describing land use. These should not to be confused with the physical buildings which are under the structure entry. |
| >>> airport                         | [MapElement]   | ap      | 1703 | 1.0.0 | Areas that encompass airports. |
| >>> areaOfInterest                  | [MapElement]   | ai      | 1709 | 1.0.0 | Areas in which there are a high concentration of businesses or interesting points. |
| >>> cemetery                        | [MapElement]   | cm      | 1703 | 1.0.0 | Areas that encompass cemeteries. |
| >>> continent                       | [MapElement]   | ct      | 1703 | 1.0.0 | Continent area labels. |
| >>> education                       | [MapElement]   | ed      | 1703 | 1.0.0 | Areas that encompass schools and other educational facilities. |
| >>> indigenousPeoplesReserve        | [MapElement]   | ipr     | 1703 | 1.0.0 | Areas that encompass indigenous peoples reserves. |
| >>> industrial                      | [MapElement]   | ind     | 1709 | 1.0.0 | Areas that are used for industrial purposes. |
| >>> island                          | [MapElement]   | is      | 1703 | 1.0.0 | Island area labels. |
| >>> medical                         | [MapElement]   | md      | 1703 | 1.0.0 | Areas that are used for medical purposes (For example: a hospital campus). |
| >>> military                        | [MapElement]   | ima     | 1703 | 1.0.0 | Areas that encompass military bases or have military uses. |
| >>> nautical                        | [MapElement]   | nt      | 1703 | 1.0.0 | Areas that are used for nautical related purposes. |
| >>> neighborhood                    | [MapElement]   | nh      | 1703 | 1.0.0 | Neighborhood area labels. |
| >>> runway                          | [MapElement]   | rw      | 1703 | 1.0.0 | Areas that is used as an airplane runway. |
| >>> sand                            | [MapElement]   | sn      | 1703 | 1.0.0 | Sandy areas like beaches. |
| >>> shoppingCenter                  | [MapElement]   | sct     | 1703 | 1.0.0 | Areas of ground allocated for malls or other shopping centers. |
| >>> stadium                         | [MapElement]   | sta     | 1703 | 1.0.0 | Areas that encompass stadiums. |
| >>> underground                     | [MapElement]   | ug      | 1709 | 1.0.0 | Underground areas (For example: a metro station footprint). |
| >>> vegetation                      | [MapElement]   | vg      | 1703 | 1.0.0 | Forests, grassy areas, etc. |
| >>>> forest                         | [MapElement]   | fr      | 1703 | 1.0.0 | Areas of forest land. |
| >>>> golfCourse                     | [MapElement]   | gc      | 1703 | 1.0.0 | Areas that encompass golf courses. |
| >>>> park                           | [MapElement]   | pr      | 1703 | 1.0.0 | Areas that encompass parks. |
| >>>> playingField                   | [MapElement]   | pf      | 1703 | 1.0.0 | Extracted pitches such as a baseball field or tennis court. |
| >>>> reserve                        | [MapElement]   | rsv     | 1703 | 1.0.0 | Areas that encompass nature reserves. |
| >> frozenWater                      | [PointStyle]   | fw      | 1903 | 1.0.0 | Frozen water, like glacier. |
| >> point                            | [PointStyle]   | pt      | 1703 | 1.0.0 | All point features that are drawn with an icon of some sort. |
| >>> address                         | [PointStyle]   | adr     | 1803 | 1.0.0 | Address numbers labels. |
| >>> naturalPoint                    | [PointStyle]   | np      | 1703 | 1.0.0 | Icons that represent natural features. |
| >>>> peak                           | [PointStyle]   | pk      | 1703 | 1.0.0 | Icons that represent mountain peaks. |
| >>>>> volcanicPeak                  | [PointStyle]   | vp      | 1703 | 1.0.0 | Icons that represent volcano peaks. |
| >>>> waterPoint                     | [PointStyle]   | wp      | 1703 | 1.0.0 | Icons that represent water feature locations such as a waterfall. |
| >>> pointOfInterest                 | [PointStyle]   | poi     | 1703 | 1.0.0 | Icons that represent any interesting location. |
| >>>> business                       | [PointStyle]   | bs      | 1703 | 1.0.0 | Icons that represent any business location. |
| >>>>> attractionPoint               | [PointStyle]   | atp     | 1709 | 1.0.0 | Icons that represent tourist attractions such as museums, zoos, etc. |
| >>>>>> amusementPlacePoint          | [PointStyle]   | app     | 1903 | 1.0.0 | Amusement place icon. |
| >>>>>> aquariumPoint                | [PointStyle]   | aqp     | 1903 | 1.0.0 | Aquarium icon. |
| >>>>>> artGalleryPoint              | [PointStyle]   | agp     | 1903 | 1.0.0 | Art gallery icon. |
| >>>>>> campPoint                    | [PointStyle]   | cpp     | 1903 | 1.0.0 | Camp icon. |
| >>>>>> fishingPoint                 | [PointStyle]   | fsp     | 1903 | 1.0.0 | Fishing icon. |
| >>>>>> gardenPoint                  | [PointStyle]   | gdp     | 1903 | 1.0.0 | Garden icon. |
| >>>>>> hikingPoint                  | [PointStyle]   | hkp     | 1903 | 1.0.0 | Hiking icon. |
| >>>>>> libraryPoint                 | [PointStyle]   | lbp     | 1903 | 1.0.0 | Library icon. |
| >>>>>> museumPoint                  | [PointStyle]   | mp      | 1903 | 1.0.0 | Museum icon. |
| >>>>>> naturalPlacePoint            | [PointStyle]   | npp     | 1903 | 1.0.0 | Natural place icon. |
| >>>>>> parkPoint                    | [PointStyle]   | pkp     | 1903 | 1.0.0 | Park icon. |
| >>>>>> restAreaPoint                | [PointStyle]   | rap     | 1903 | 1.0.0 | Rest area icon. |
| >>>>>> touristAttractionPoint       | [PointStyle]   | tap     | 1903 | 1.0.0 | Tourist attraction icon. |
| >>>>>> zooPoint                     | [PointStyle]   | zp      | 1903 | 1.0.0 | Zoo icon. |
| >>>>> communityPoint                | [PointStyle]   | cop     | 1709 | 1.0.0 | Icons that represent locations of general use to the community. |
| >>>>>> conventionCenterPoint        | [PointStyle]   | ccp     | 1903 | 1.0.0 | Convention center icon. |
| >>>>>> financialPoint               | [PointStyle]   | fnp     | 1903 | 1.0.0 | Financial icon. |
| >>>>>> governmentPoint              | [PointStyle]   | gvp     | 1903 | 1.0.0 | Government icon. |
| >>>>>> informationTechnologyPoint   | [PointStyle]   | iftp    | 1903 | 1.0.0 | Information technology icon. |
| >>>>>> palacePoint                  | [PointStyle]   | plp     | 1903 | 1.0.0 | Palace icon. |
| >>>>>> pollingStationPoint          | [PointStyle]   | rsp     | 1903 | 1.0.0 | Polling station icon. |
| >>>>>> researchPoint                | [PointStyle]   | rp      | 1903 | 1.0.0 | Research icon. |
| >>>>> educationPoint                | [PointStyle]   | edp     | 1709 | 1.0.0 | Icons that represent schools and other education related locations. |
| >>>>> entertainmentPoint            | [PointStyle]   | etp     | 1709 | 1.0.0 | Icons that represent entertainment venues such as theaters, cinemas, etc. |
| >>>>>> artsPoint                    | [PointStyle]   | artp    | 1903 | 1.0.0 | Arts icon. |
| >>>>>> bowlingPoint                 | [PointStyle]   | bwp     | 1903 | 1.0.0 | Bowling icon. |
| >>>>>> casinoPoint                  | [PointStyle]   | csp     | 1903 | 1.0.0 | Casino icon. |
| >>>>>> golfCoursePoint              | [PointStyle]   | gfcp    | 1903 | 1.0.0 | Golf course icon. |
| >>>>>> gymPoint                     | [PointStyle]   | gp      | 1903 | 1.0.0 | Gym icon. |
| >>>>>> marinaPoint                  | [PointStyle]   | mrp     | 1903 | 1.0.0 | Marina icon. |
| >>>>>> movieTheaterPoint            | [PointStyle]   | mtp     | 1903 | 1.0.0 | Movie theater icon. |
| >>>>>> nightClubPoint               | [PointStyle]   | ncp     | 1903 | 1.0.0 | Night club icon. |
| >>>>>> recreationPoint              | [PointStyle]   | rcp     | 1903 | 1.0.0 | Recreation icon. |
| >>>>>> skatingPoint                 | [PointStyle]   | sktp    | 1903 | 1.0.0 | Skating icon. |
| >>>>>> skiAreaPoint                 | [PointStyle]   | skap    | 1903 | 1.0.0 | Ski area icon. |
| >>>>>> stadiumPoint                 | [PointStyle]   | stmp    | 1903 | 1.0.0 | Stadium icon. |
| >>>>>> swimmingPoolPoint            | [PointStyle]   | swpp    | 1903 | 1.0.0 | Swimming pool icon. |
| >>>>>> theaterPoint                 | [PointStyle]   | tp      | 1903 | 1.0.0 | Theater icon. |
| >>>>>> wineryPoint                  | [PointStyle]   | wmp     | 1903 | 1.0.0 | Winery icon. |
| >>>>> essentialServicePoint         | [PointStyle]   | esp     | 1709 | 1.0.0 | Icons that represent essential services such as parking, banks, gas, etc. |
| >>>>>> atmPoint                     | [PointStyle]   | atmp    | 1903 | 1.0.0 | ATM icon. |
| >>>>>> automobileRentalPoint        | [PointStyle]   | atmrt   | 1903 | 1.0.0 | Automobile rental icon. |
| >>>>>> automobileRepairPoint        | [PointStyle]   | atmrp   | 1903 | 1.0.0 | Automobile repair icon. |
| >>>>>> bankPoint                    | [PointStyle]   | bkp     | 1903 | 1.0.0 | Bank icon. |
| >>>>>> clinicPoint                  | [PointStyle]   | clcp    | 1903 | 1.0.0 | Clinic icon. |
| >>>>>> electricChargingStationPoint | [PointStyle]   | ecsp    | 1903 | 1.0.0 | Electric charging station icon. |
| >>>>>> fireStationPoint             | [PointStyle]   | essp    | 1903 | 1.0.0 | FireStation icon. |
| >>>>>> gasStationPoint              | [PointStyle]   | gsp     | 1903 | 1.0.0 | GasStation icon. |
| >>>>>> groceryPoint                 | [PointStyle]   | grcp    | 1903 | 1.0.0 | Grocery icon. |
| >>>>>> hospitalPoint                | [PointStyle]   | hp      | 1903 | 1.0.0 | Hospital icon. |
| >>>>>> laundryPoint                 | [PointStyle]   | lp      | 1903 | 1.0.0 | Laundry icon. |
| >>>>>> liquorAndWineStorePoint      | [PointStyle]   | lwsp    | 1903 | 1.0.0 | Liquor and wine store icon. |
| >>>>>> mailPoint                    | [PointStyle]   | mlp     | 1903 | 1.0.0 | Mail icon. |
| >>>>>> marketPoint                  | [PointStyle]   | mktp    | 1903 | 1.0.0 | Market icon. |
| >>>>>> parkingPoint                 | [PointStyle]   | prkp    | 1903 | 1.0.0 | Parking icon. |
| >>>>>> petsPoint                    | [PointStyle]   | ptp     | 1903 | 1.0.0 | Pets icon. |
| >>>>>> pharmacyPoint                | [PointStyle]   | phmp    | 1903 | 1.0.0 | Pharmacy icon. |
| >>>>>> policePoint                  | [PointStyle]   | plcp    | 1903 | 1.0.0 | Police icon. |
| >>>>>> postalServicePoint           | [PointStyle]   | psts    | 1903 | 1.0.0 | Postal service icon. |
| >>>>>> professionalPoint            | [PointStyle]   | pfp     | 1903 | 1.0.0 | Professional service icon. |
| >>>>>> toiletPoint                  | [PointStyle]   | tltp    | 1903 | 1.0.0 | Toilet icon. |
| >>>>>> veterinarianPoint            | [PointStyle]   | vtp     | 1903 | 1.0.0 | Veterinarian icon. |
| >>>>> foodPoint                     | [PointStyle]   | fp      | 1703 | 1.0.0 | Icons that represent restaurants, cafés, etc. |
| >>>>>> barAndGrillPoint             | [PointStyle]   | bgp     | 1903 | 1.0.0 | Bar and grill icon. |
| >>>>>> barPoint                     | [PointStyle]   | brp     | 1903 | 1.0.0 | Bar icon. |
| >>>>>> breweryPoint                 | [PointStyle]   | brwp    | 1903 | 1.0.0 | Brewery icon. |
| >>>>>> cafePoint                    | [PointStyle]   | cfp     | 1903 | 1.0.0 | Cafe icon. |
| >>>>>> iceCreamShopPoint            | [PointStyle]   | icsp    | 1903 | 1.0.0 | Ice cream shop icon. |
| >>>>>> restaurantPoint              | [PointStyle]   | rstp    | 1903 | 1.0.0 | Restaurant icon. |
| >>>>>> teaShopPoint                 | [PointStyle]   | tsp     | 1903 | 1.0.0 | TeaShop icon. |
| >>>>> lodgingPoint                  | [PointStyle]   | lop     | 1709 | 1.0.0 | Icons that represent hotels and other lodging businesses. |
| >>>>>> hotelPoint                   | [PointStyle]   | htp     | 1903 | 1.0.0 | Hotel icon. |
| >>>>> realEstatePoint               | [PointStyle]   | rep     | 1709 | 1.0.0 | Icons that represent real estate businesses. |
| >>>>> shoppingPoint                 | [PointStyle]   | shp     | 1709 | 1.0.0 | Icons that represent hotels and other lodging businesses. |
| >>>>>> automobileDealerPoint        | [PointStyle]   | atm     | 1903 | 1.0.0 | Automobile dealer icon. |
| >>>>>> beautyAndSpaPoint            | [PointStyle]   | bsp     | 1903 | 1.0.0 | Beauty and spa icon. |
| >>>>>> bookstorePoint               | [PointStyle]   | bksp    | 1903 | 1.0.0 | Bookstore icon. |
| >>>>>> departmentStorePoint         | [PointStyle]   | dsp     | 1903 | 1.0.0 | Department store icon. |
| >>>>>> electronicsShopPoint         | [PointStyle]   | elsp    | 1903 | 1.0.0 | Electronics shop icon. |
| >>>>>> golfShopPoint                | [PointStyle]   | glfsp   | 1903 | 1.0.0 | Golf shop icon. |
| >>>>>> homeApplianceShopPoint       | [PointStyle]   | hasp    | 1903 | 1.0.0 | Home appliance shop icon. |
| >>>>>> mallPoint                    | [PointStyle]   | mllp    | 1903 | 1.0.0 | Mall icon. |
| >>>>>> phoneShopPoint               | [PointStyle]   | psp     | 1903 | 1.0.0 | Phone shop icon. |
| >>>> venuePoint                     | [PointStyle]   | vpt     |      |       | Encapsulates points that are used primarily in venues. |
| >>>>> babyChangingPoint             | [PointStyle]   | bcp     |      |       |   |
| >>>>> elevatorPoint                 | [PointStyle]   | ep      |      |       |   |
| >>>>> entrancePoint                 | [PointStyle]   | enp     |      |       |   |
| >>>>> escalatorPoint                | [PointStyle]   | escp    |      |       |   |
| >>>>> femaleRestroomPoint           | [PointStyle]   | frp     |      |       |   |
| >>>>> mailServicePoint              | [PointStyle]   | msp     |      |       |   |
| >>>>> maleRestroomPoint             | [PointStyle]   | mrrp    |      |       |   |
| >>>>> meetingPoint                  | [PointStyle]   | mep     |      |       |   |
| >>>>> printerPoint                  | [PointStyle]   | prp     |      |       |   |
| >>>>> restroomPoint                 | [PointStyle]   | rrp     |      |       |   |
| >>>>> stairsPoint                   | [PointStyle]   | sp      |      |       |   |
| >>>>> teamPoint                     | [PointStyle]   | tep     |      |       |   |
| >>>>> telephonePoint                | [PointStyle]   | tlp     |      |       |   |
| >>> populatedPlace                  | [PointStyle]   | pp      | 1703 | 1.0.0 | Icons that represent the size of populated place (For example: a city or town). |
| >>>> capital                        | [PointStyle]   | cp      | 1703 | 1.0.0 | Icons that represent the capital of a populated place. |
| >>>>> adminDistrictCapital          | [PointStyle]   | adc     | 1703 | 1.0.0 | Icons that represent the capital of a state or province. |
| >>>>>> majorAdminDistrictCapital    | [PointStyle]   |         | 1903 | 1.0.0 | Icons that represent the major capital of a state or province. |
| >>>>>> minorAdminDistrictCapital    | [PointStyle]   |         | 1903 | 1.0.0 | Icons that represent the minor capital of a state or province. |
| >>>>> countryRegionCapital          | [PointStyle]   | crc     | 1703 | 1.0.0 | Icons that represent the capital of a country or region. |
| >>>> majorPopulatedPlace            | [PointStyle]   |         | 1903 | 1.0.0 | Icons that represent the size of major populated place. |
| >>>> minorPopulatedPlace            | [PointStyle]   |         | 1903 | 1.0.0 | Icons that represent the size of minor populated place. |
| >>> roadShield                      | [PointStyle]   | rs      | 1703 | 1.0.0 | Signs that represent the compact name for a road. (For example: I-5). Use only palette values if you set the ImageFamily property of the settings entry to a value of Palette |
| >>> roadExit                        | [PointStyle]   | re      | 1703 | 1.0.0 | Icons that represent exits, typically from a controlled access highway. |
| >>> transit                         | [PointStyle]   | trn     | 1703 | 1.0.0 | Icons that represent bus stops, train stops, airports, etc. |
| >> political                        | [BorderedMapElement] | pl | 1703 | 1.0.0 | Political regions such as countries, regions and states. |
| >>> adminDistrict                   | [BorderedMapElement] | ad | 1703 | 1.0.0 | Admin1, states, provinces, etc., borders and labels. |
| >>> countryRegion                   | [BorderedMapElement] | cr | 1703 | 1.0.0 | Country region borders and labels. |
| >>> district                        | [BorderedMapElement] | ds | 1703 | 1.0.0 | Admin2, counties, etc., borders and labels. |
| >> structure                        | [MapElement]   | str     | 1703 | 1.0.0 | Buildings and other building-like structures. |
| >>> building                        | [MapElement]   | bld     | 1703 | 1.0.0 | Buildings. |
| >>>> educationBuilding              | [MapElement]   | eb      | 1703 | 1.0.0 | Buildings used for education. |
| >>>> medicalBuilding                | [MapElement]   | mb      | 1703 | 1.0.0 | Buildings used for medical purposes such as hospitals. |
| >>>> transitBuilding                | [MapElement]   | tb      | 1703 | 1.0.0 | Buildings used for transit such as airports. |
| >>> object                          | [MapElement]   | ob      |      |       | Object such as a desk or statue. |
| >>> venueFootprint                  | [BorderedMapElement] | vf |     |       | Encapsulates fundamental structural parts of a venue. |
| >>>> floor                          | [BorderedMapElement] | fl |     |       | Area of an individual floor in a venue. |
| >>>> footprint                      | [BorderedMapElement] | ft |     |       | Shadow that all above-ground floors cast on the ground. |
| >>> wall                            | [MapElement]   | wl      |      |       | A wall. |
| >>>> activityWall                   | [MapElement]   | awa     |      |       | Wall around activity rooms. |
| >>>> foodWall                       | [MapElement]   | fwa     |      |       | Wall around food rooms. |
| >>>> secureWall                     | [MapElement]   | swa     |      |       | Boundary between secure and regular areas. |
| >>>> shopWall                       | [MapElement]   | shwa    |      |       | Wall around shop rooms. |
| >>>> utilityWall                    | [MapElement]   | uwa     |      |       | Wall around utility rooms. |
| >>> zone                            | [MapElement]   | zn      |      |       | Areas and rooms. |
| >>>> activityZone                   | [MapElement]   | az      |      |       | Zone for activities. |
| >>>>> activityRoom                  | [MapElement]   | azr     |      |       | Room for activities. |
| >>>> foodZone                       | [MapElement]   | fz      |      |       | Zone for food services. |
| >>>>> foodRoom                      | [MapElement]   | fzr     |      |       | Room for food services. |
| >>>>> foodShelves                   | [MapElement]   | fzs     |      |       | Shelves containing food. |
| >>>> medicalZone                    | [MapElement]   | mz      |      |       | Zone for medical purposes. |
| >>>>> medicalShelves                | [MapElement]   | mzs     |      |       | Shelves containing medical items. |
| >>>> room                           | [MapElement]   | r       |      |       | Unclassified room. |
| >>>> secureZone                     | [MapElement]   | scz     |      |       | Zone reached through a security checkpoint. |
| >>>>> secureRoom                    | [MapElement]   | sczr    |      |       | Area reached through a security checkpoint. |
| >>>> serviceZone                    | [MapElement]   | sz      |      |       | Zone for providing services. |
| >>>>> counter                       | [MapElement]   | szc     |      |       | Counter used for information, checkout, etc. |
| >>>>> serviceRoom                   | [MapElement]   | szr     |      |       | Room for providing services. |
| >>>> shelves                        | [MapElement]   | sh      |      |       | Unclassified shelves. |
| >>>> shopZone                       | [MapElement]   | shz     |      |       | Zone for shopping. |
| >>>>> shopRoom                      | [MapElement]   | shzr    |      |       | Room for shopping. |
| >>>>> shopShelves                   | [MapElement]   | shzs    |      |       | Shelves for shopping. |
| >>>> utilityZone                    | [MapElement]   | uz      |      |       | Zone of utilitarian value. |
| >>>>> utilityRoom                   | [MapElement]   | uzr     |      |       | Room of utilitarian value like stair wells and elevators. |
| >> transportation                   | [MapElement]   | trs     | 1703 | 1.0.0 | Lines that are part of the transportation network (For example: roads, trains, and ferries). |
| >>> road                            | [MapElement]   | rd      | 1703 | 1.0.0 | Lines that represent all roads. |
| >>>> controlledAccessHighway        | [MapElement]   | cah     | 1703 | 1.0.0 | Lines that represent large, controlled access highways. |
| >>>>> highSpeedRamp                 | [MapElement]   | hsrp    | 1703 | 1.0.0 | Lines that represent high speed ramps that typically connect to controlled access highways. |
| >>>> highway                        | [MapElement]   | hg      | 1703 | 1.0.0 | Lines that represent highways. |
| >>>> majorRoad                      | [MapElement]   | mr      | 1703 | 1.0.0 | Lines that represent major roads. |
| >>>> arterialRoad                   | [MapElement]   | ard     | 1703 | 1.0.0 | Lines that represent arterial roads. |
| >>>> street                         | [MapElement]   | st      | 1703 | 1.0.0 | Lines that represent streets. |
| >>>>> ramp                          | [MapElement]   | rm      | 1703 | 1.0.0 | Lines that represent ramps that typically connect to highways. |
| >>>>> unpavedStreet                 | [MapElement]   | us      | 1703 | 1.0.0 | Lines that represent unpaved streets. |
| >>>> tollRoad                       | [MapElement]   | tr      | 1703 | 1.0.0 | Lines that represent roads that cost money to use. |
| >>> railway                         | [MapElement]   | rl      | 1703 | 1.0.0 | Railway lines. |
| >>> trail                           | [MapElement]   | trl     | 1703 | 1.0.0 | Walking trails through parks or hiking trails. |
| >>> walkway                         | [MapElement]   | wlk     | 1709 | 1.0.0 | Elevated walkway. |
| >>> waterRoute                      | [MapElement]   | wr      | 1703 | 1.0.0 | Ferry route lines. |
| >> water                            | [MapElement]   | wt      | 1703 | 1.0.0 | Anything that looks like water. This includes oceans and streams. |
| >>> river                           | [MapElement]   | rv      | 1703 | 1.0.0 | Rivers, streams, or other water passages. Note that this may be a line or polygon and might connect to non-river water bodies. |
| > routeMapElement                   | [MapElement]   |         | 1703 | 1.0.0 | All routing related entries. |
| >> routeLine                        | [MapElement]   |         | 1703 | 1.0.0 | Route line related entries. |
| >>> drivingRoute                    | [MapElement]   |         | 1703 | 1.0.0 | Lines that represent driving routes. |
| >>> scenicRoute                     | [MapElement]   |         | 1709 | 1.0.0 | Lines that represent scenic driving routes. |
| >>> walkingRoute                    | [MapElement]   |         | 1703 | 1.0.0 | Lines that represent walking routes. |
| > userMapElement                    | [MapElement]   |         | 1703 | 1.0.0 | All user entries. |
| >> userBillboard                    | [MapElement]   |         | 1709 | 1.0.0 | The styling for default MapBillboard instances. |
| >> userLine                         | [MapElement]   |         | 1703 | 1.0.0 | The styling for default MapPolyline instances. |
| >> userModel3D                      | [MapElement3D] |         | 1709 | 1.0.0 | The styling for default MapModel3D instances. This is primarily for setting renderAsSurface. |
| >> userPoint                        | [PointStyle]   |         | 1703 | 1.0.0 | The styling for default MapIcon instances. |

[Version]: map-style-sheet-entry-properties.md#version-properties
[Settings]: map-style-sheet-entry-properties.md#settings-properties
[MapElement]: map-style-sheet-entry-properties.md#mapelement-properties
[BorderedMapElement]: map-style-sheet-entry-properties.md#borderedmapelement-properties
[MapElement3D]: map-style-sheet-entry-properties.md#mapelement3d-properties
[PointStyle]: map-style-sheet-entry-properties.md#pointstyle-properties