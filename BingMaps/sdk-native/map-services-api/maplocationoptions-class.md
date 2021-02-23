---
title: "MapLocationOptions Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapLocationOptions Class

Forms optional parameters for a geocoding request.

## Constructors

Constructor takes no arguments, initializing all fields by default to empty optional value (parameter will not be included in the request), except for:

* `IncludeNeighborhood` to `true`
* `IncludeCountryCode` to `true`

**Android**

>```java
>MapLocationOptions()
>```

**iOS**

>```objectivec
>- (instancetype)init
>```

## Methods

### SetReferenceIpAddress

When you specify this parameter, the location associated with the IP address is taken into account in computing the results of a location query.  
The default address is the IPv4 address of the request.

**Android**

>```java
>MapLocationOptions setReferenceIpAddress(String value)
>```

**iOS**

>```objectivec
>- (void)setReferenceIpAddress:(NSString*)referenceIpAddress
>```

### SetCulture

Use the culture parameter to specify a culture for your request. The culture parameter provides the following strings in the language of the culture for:
* Geographic entities and place names returned by the Bing Maps REST Services
* Map labels on map images
* Route instructions

*If not specified, devices's system locale language is used by default.*

**Android**

>```java
>MapLocationOptions setCulture(String value)
>```

**iOS**

>```objectivec
>- (void)setCulture:(NSString*)culture
>```

### SetRegion

A string that represents an ISO 3166-1 Alpha-2 region/country code.  
This will alter Geopolitical disputed borders and labels to align with the specified user region.

*If not specified, device's system locale region is used by default.*

**Android**

>```java
>MapLocationOptions setRegion(String value)
>```

**iOS**

>```objectivec
>- (void)setRegion:(NSString*)region
>```

### SetIncludeNeighborhood

Specifies to include the neighborhood with the address information in the response when it is available.

**Android**

>```java
>MapLocationOptions setIncludeNeighborhood(boolean value)
>```

**iOS**

>```objectivec
>- (void)setIncludeNeighborhood:(BOOL)includeNeighborhood
>```

### SetIncludeCountryCode

Specifies to include the [two-letter ISO country code](https://www.iso.org/iso-3166-country-codes.html).

**Android**

>```java
>MapLocationOptions setIncludeCountryCode(boolean value)
>```

**iOS**

>```objectivec
>- (void)setIncludeCountryCode:(BOOL)includeCountryCode
>```

### SetMaxResults

Specifies the maximum number of locations to return in the response.  
Must be an integer between 1 and 20. The default value is 5.

**Android**

>```java
>MapLocationOptions setMaxResults(int value)
>```

**iOS**

>```objectivec
>- (void)setMaxResults:(NSUInteger)maxResults
>```

### SetIncludeEntityTypes

***Only available for geocoding by location.***

Specifies the entity types that you want to return in the response. Only the types you specify will be returned. If the point cannot be mapped to the entity types you specify, no location information is returned in the response.

These entity types are ordered from the most specific entity to the least specific entity. When entities of more than one entity type are found, only the most specific entity is returned. For example, if you specify `Address` and `AdminDistrict` as entity types and entities were found for both types, only the `Address` entity information is returned in the response. One exception to this rule is when both `PopulatedPlace` and `Neighborhood` entity types are specified and information is found for both. In this case, the information for both entity types is returned. Also, more than one `Neighborhood` may be returned because the area covered by two different neighborhoods can overlap.

**Android**

>```java
>MapLocationOptions setIncludeEntityTypes(int value)
>```

**iOS**

>```objectivec
>- (void)setIncludeEntityTypes:(MSMapLocationEntityTypes)IncludeEntityTypes
>```


## See Also

* [MapLocationFinder](MapLocationFinder-class.md)
