
# MapCameraChangeCause enumeration (iOS only)

Specifies the reason the position of the map's camera has changed.

>```objectivec 
> typedef NS_ENUM(NSInteger, MSMapCameraChangeCause)
> {
>      MSMapCameraChangeCauseDeveloper = 0,
>      MSMapCameraChangeCauseUserInteraction,
>      MSMapCameraChangeCauseSceneMaintenance,
> }
> ```

### Developer
The position of the map's camera changed programmatically.

### UserInteraction
The user manually changed the position of the map's camera.

### Maintenance
The system changed the position of the map's camera.
