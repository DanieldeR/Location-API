# Location API

This simple location API and frontend provides an endpoint that allows a device to submit its location. The location will then be visualized on the frontend of the application on a map.

**Live Version**: http://location.derepentigny.ca/

## Application Design

The application allows for a device (typically a phone, but could be any IoT device) to submit a location and be displayed on a map. The device can submit API POST requests with its location, and the most recent location will be written to a MongoDB instance. When a frontend user accesses the application from a browser, the last recorded location is displayed.

![image](https://drive.google.com/uc?export=view&id=1B8fm8gBPtFBli2cUVnHVfOR7Y-xnWGw5)

This application is built to run either locally with a MongoDB instance running (locally or in a container) or in Cloud Foundry with an Mlab service bound to the application.

The application is set-up for flexibility and is meant more of starting point than an fully secure and production ready application. For example, there is no API requester validation. Any request that is sent to the server could break the frontend application if it does not contain a `location` parameter.


