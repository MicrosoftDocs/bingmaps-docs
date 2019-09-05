
# MapCameraChangeReason enumeration

Specifies the reason the position of the map's camera has changed.

**Android**

>```java 
> public enum MapCameraChangeReason 
> {
>     SYSTEM,
>     USER_INTERACTION,
>     PROGRAMMATIC,
> }
> ```

**iOS**

>```objectivec 
> typedef NS_ENUM(NSInteger, MSMapCameraChangeReason)
> {
>      MSMapCameraChangeReasonSystem = 0,
>      MSMapCameraChangeReasonUserInteraction,
>      MSMapCameraChangeReasonProgrammatic
> }
> ```

### System
The position of the map's camera changed programmatically.

### UserInteraction
The user manually changed the position of the map's camera.

### Programmatic
The system changed the position of the map's camera.
