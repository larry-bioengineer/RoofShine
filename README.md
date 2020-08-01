# Project Roofshine :sunny:

## :thought_balloon: Background
[For most people, the road to solar power is paved with questions: about affordability, weather and light patterns, usable roof area, angle and tilt, government incentives.](https://sustainability.google/projects/project-sunroof/) This investigation is usually done by hiring a local solar rooftop installer or an auditor for a solar panel quotation, which can be troublesome and sometimes expensive, creating a much higher barrier to persuade people to install solar panel. 

The goal of this project is to democratize and automize the process by using image recognition software to analyze these factors. 

### Factor to be analyzed 
- Rooftop size
- Annual sunshine on the spot
	- direction of the roof faces (south or southwest is best)
	- angle of the rooftop tilt
- Possible shading on the roof
	- e.g. trees, buildings 

## :books: Prior Work 
- image recognition on bad satelite images
	- [U-net CNN toward data science](https://towardsdatascience.com/using-image-segmentation-to-identify-rooftops-in-low-resolution-satellite-images-c791975d91cc)
	- [Pre-processing github](https://github.com/AKASH2907/project_sunroof_india)
- [Rooftop dataset](https://github.com/loosgagnet/Building-detection-and-roof-type-recognition)
- Tools for Solar Potential 
	- [Hong Kong Baptist University Solar Map](https://digital.lib.hkbu.edu.hk/solarmap/intro.php)
		- a manual measuring tool where users will highlight their rooftop area and the software will measure the area. 
	- [Project sunroof](https://www.google.com/get/sunroof) by Google 
		- Algorithmically calculate rooftop area and solar potential for household buildings 
		- Only available in US 

## :computer: Development 

### :house: Rooftop Size 
I'm thinking about two-step approaches, 1) Simple tool allowing users to measure their rooftop, 2) automated tool for measuring rooftop size with an option for users to self-correct. 3) combine both tools so if the automated is not calculating correctly, users can have the option to manually correct the estimation. 

#### Development Steps (order based on my own pleasure. what can you do about it? :ghost:)
1. A web app for accessing different map using Google Map API 
2. Rooftop automated recognition using AI on particular images 
3. Rooftop automated recognition based on user selected location 
4. manual measurment tool on the web app 

### :sun_with_face: Sunshine Data 
Don't have much idea right now. Probably using data from Hong Kong Observatory, WindGuru. 

#### Development Steps
1. Querying data(preferably)/web crawling data from observatory site 
2. web app allowing users to find out annual sunshine data, e.g. sun rise and sun set data, intensity 