
# UserLocationTrackingMode enumeration

Controls how tracking of the users location is done for the map.

**Android**

>```java
> enum UserLocationTrackingMode
> {
>     NONE,
>     ALWAYS_CENTERED_ON_USER,
>     INTERRUPTIBLE_CENTERED_ON_USER,
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapUserLocationTrackingMode)
> {
>     MSMapUserLocationTrackingModeNone,
>     MSMapUserLocationTrackingModeAlwaysCenteredOnUser,
>     MSMapUserLocationTrackingModeInterruptibleCenteredOnUser
> };
>```

## Values

### None

Don't track the user.

### Always center on user

The camera will remain centered on the user position.

### Interruptible centered on user

Keeps the camera centered on the user position unless the user interacts with the map to move it away from the center.
