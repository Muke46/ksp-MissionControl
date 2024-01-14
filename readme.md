### Kerbal mods requirements:
- kRPC (CKAN): to control the vessel and receive data from the game
- HullcamVDS Continued(CKAN) and OCISLY(https://github.com/jrodrigv/OfCourseIStillLoveYou/releases): to obtain live view for the vessel cameras

### The Plan:
- Vessel control (C++?)
  - 3D rotational control with PID loops (rocket + planes?)
  - Thrust control for hovering
- Missions planning 
  - Orbit calculations
  - Performance calculations
  - PID parameters tuning for the different part of the mission
  - Standarized (ex JSON) mission plan 
- Control monitoring GUI
  - Implement the OCISLY inside to have direct access to the camera's feeds
  - Naveball visualization
  - Orbit visualization(s?)
  - Terrain visualization
  - Mission plan visualization
  - Basic control to modify the mission plan?