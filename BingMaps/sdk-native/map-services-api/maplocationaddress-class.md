---
title: "MapLocationAddress Class | Microsoft Docs"
author: "bmnxplat"
---

# MapLocationAddress Class

Contains address data for a specific location returned from a geocoding request.

## Properties

### FormattedAddress

Specifies the address in a local format. This address may not include the country or region.

*Example: 1 Microsoft Way, Redmond, WA 98052-8300*

**Android**

>```java
>String getFormattedAddress()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* formattedAddress
>```

### AddressLine

Specifies the address line for the address.

*Example: 1 Microsoft Way*

**Android**

>```java
>String getAddressLine()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* addressLine
>```

### Neighborhood

Specifies the neighborhood for the address.

*Example: Ballard*

**Android**

>```java
>String getNeighborhood()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* neighborhood
>```

### Locality

Specifies the locality for the address.

*Example: Seattle*

**Android**

>```java
>String getLocality()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* locality
>```

### AdminDistrict

Specifies the administrative district for the address.

*Example: WA*

**Android**

>```java
>String getAdminDistrict()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* adminDistrict
>```

### AdminDistrict2

Specifies the second level administrative district for the address.

*Example: King Co.*

**Android**

>```java
>String getAdminDistrict2()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* adminDistrict2
>```

### PostalCode

Specifies the postal code for the address.

*Example: 98052*

**Android**

>```java
>String getPostalCode()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* postalCode
>```

### CountryRegion

Specifies the country for the address.

*Example: United States*

**Android**

>```java
>String getCountryRegion()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* countryRegion
>```

### CountryCode

Specifies the [two-letter ISO country code](https://www.iso.org/iso-3166-country-codes.html) for the address.

*Example: US*

**Android**

>```java
>String getCountryCode()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* countryCode
>```

### Landmark

Specifies the landmark name for the address.

*Example: Space Needle*

**Android**

>```java
>String getLandmark()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* landmark
>```

## See also

* [MapLocation](MapLocation-class.md)
