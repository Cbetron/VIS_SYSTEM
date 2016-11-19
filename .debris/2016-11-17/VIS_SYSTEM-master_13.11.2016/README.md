# VIS_SYSTEM
A simple Home Automation System. It should solve some problems for you. It can be used for Home-Automation as well as a System to do Software things.

The Idea
---------

You got a VIS Server installed on a Computer in your Network. You can connect Sensors(temperature, Door-Closed?), Clients to communicate with the Server or Actors(Door Lock, Speaking Mirror, Light) with it. It should be a simple Home Automation and Server to do some special things for you.

Structure
----------

- VIS_SERVER: Includes the Full functionality. Manages the Sensors, Actors and Clients. Awaiting Requests/orders from clients
- VIS_CLIENT: The Interface between Server and User. GUI and Speech for User-Communication. Sending requests to Server
- VIS_Sensors: Can be Connected to server to get some data of the House/World Outside(f.ex. temp, light, door-closed?=
- VIS_Actors: Can be used to expand the functionality of the Server. turn lights on, locking doors...
