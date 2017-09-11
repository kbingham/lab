# lab
SSH based authentication to remote control a board farm

Following the 'gitolite' model of user authentication - provide a system whereby users can connect to a centralised
server acting as a management console for a board farm, with key design goals:

* Multi-user support is a first class citizen in this system to allow automated testing. (CI/Bots are just a user)
* Support 'locking' - to prevent users from interrupting tests or access
* Abstract power management and control
* Handle file upload management (kernel image, dtb...)
