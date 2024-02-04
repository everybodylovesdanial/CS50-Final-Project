# NIMBUS
    #### Video Demo:  <URL HERE>
    #### Description:


    Nimbus is a web-based application that users can use to gain the latest weather report on various cities around the world. Beyond weather updates, Nimbus offers additional features, allowing users to access flood and earthquake reports specific to their current location. Moreover, users can explore real-time weather patterns using the live satellite weather radar feature.

    Users can either choose to input any name of a city, or they can simply use their current location to get weather information on the city that they live in. The displayed information entails current day and date, current temperature in celsius (°C), description of the weather, air quality index, along with a two-day weather forecast. The air quality index is determined using the US-EPA scale, where a rating of 1 means good air quality, while a rating of 6 is hazardous conditions. Other features include information on floods and earthquakes, as well as live satellite weather radar. These features can be accessed by toggling the options located at the upper-right corner of the page on the navigation bar. Both flood and earthquake features can only be used by clicking on the ‘use current location’ button, the manual city input is made unavailable in these two features. Additionally, these two features are exclusive to Malaysia as the dataset is limited to Malaysia only. The flood status report can be categorized into three sections: location, water level, and rainfall. The location section includes information about the nearest flood monitoring station from the current location and the basin where that monitoring station is located. The water level report covers details such as the normal and dangerous water levels at the monitoring station, the current water level, water level trends, and overall conditions. Lastly, the rainfall report provides information on the current rainfall status and the total rainfall for the day. Moreover, the earthquake status report can be divided into two sections: nearest earthquake, and details. Nearest earthquake section covers the epicenter, a term in seismology that describes the point on the Earth's surface where an earthquake originates. Additionally, it also covers the date of the earthquake, as well as direct distance from the current location. The details section covers the magnitude, depth, and status of the earthquake. Another feature that Nimbus offers is the live satellite weather radar. The weather radar showcases the map of Malaysia, but users have the flexibility to navigate and explore other countries by dragging the map. The weather radar is available for access to all countries displayed on the map. There are many map display options that users can choose such as wind animation, satellite, clouds and precipitation, temperature, and many more.

    The front end structure was implemented using HTML, javascript, and CSS. Most of the HTML layout such as the nav-bar was inspired from previous problem sets, and the javascript was used to get the current coordinates of the user when the ‘use current location’ button is clicked. As for the CSS style, it was mainly inspired from a website (https://www.codingnepalweb.com/demos/weather-app-project-html-javascript/). But the main style and theme of Nimbus was based on personal creativity. The background of the website is taken from google image. Furthermore, the back end architecture of the web application was implemented using Python, utilizing the Flask framework. Various API endpoints were utilized to operate the back end system. The main APIs used were Weather API (https://www.weatherapi.com/), the Flood Warning API (https://developer.data.gov.my/realtime-api/flood-warning) and the Earthquake API (https://api.data.gov.my/weather/warning/earthquake). These three API serves as the backbone of the website, providing the real-time data that is presented to the users. Another API used was the OpenCage Geocoding API (https://opencagedata.com/),  primarily utilized to convert the current longitude and latitude fetched through JavaScript into a location name such as country, state, and city. Subsequently, these location names are input into the data APIs to retrieve information about the user's current location. The live weather satellite radar was retrieved from Mateoblue (https://content.meteoblue.com/en) in the form of a widget. The integration process simply required pasting the provided widget code directly into the HTML template.

    In terms of system design, one of the functions that were debated was to either include manual location input for the flood and earthquake features. Initially, allowing users the flexibility to either manually input a location or use their current location appeared to enhance the user interface. However, upon closer examination, it became apparent that this design might not be the most efficient solution, especially considering the presence of multiple flood monitoring stations within a city. To ensure the information provided is truly beneficial to the user, the decision was made to prioritize the use of the current location, presenting data from the nearest flood monitoring station. Additionally, this system design was also debated for the earthquake feature. However it was concluded to be impractical to include input fields as the majority of earthquakes originated from Indonesia and did not significantly impact Malaysia. It is important to note that this feature is only available to users in Malaysia. Therefore, the system was optimized to automatically focus on nearby seismic activity in proximity to the user's current location in Malaysia.

    Designing the system architecture was not the only challenge; various other difficulties arose during the process. For instance, finding the closest monitoring station and seismic activity to the user’s current location posed a great challenge. The flood and earthquake APIs are designed to return data in JSON format, presenting a list of dictionaries that contain coordinates for each location. Consequently, the problem lies in the need to compare the user's current coordinate with the corresponding coordinate in the API's list to get the closest distance. The initial approach to this issue was to use a geolocation API to calculate distances between locations systematically, evaluating each one individually to identify the nearest location. However, using a geolocation API would not be the optimal solution due to its complexity and the requirement for payment to access the API. After some extensive research, along with the help of Chat GPT and CS50.ai chat, the most effective way to approach this problem is by using the Haversine formula. Essentially, the Haversine formula is a mathematical equation used in geography to calculate the distance between two points on a sphere given their longitudes and latitudes. The formula has been defined at the very top of the app.py file, and by calling haversine in the flood and earthquake functions, it would calculate the distance between the user’s fetched coordinate and the extracted coordinates from the flood and earthquake API. Another set of function would be used to update the closest distance and the location as the function iterates through each and every coordinate in the API. Once the closest flood monitoring station or earthquake location is found,  the data will be displayed in the corresponding html template.

    In reflection, CS50X has provided me with an incredible learning journey throughout all the covered topics. This course serves as a solid foundation to the many more programming areas I have yet to explore. Looking back when I first started with Scratch in week 0, I have made significant progress, now equipped with the skills to develop a fully functional website for my final project. Prior to CS50X, I lacked any computer science background, making this experience exceptionally fulfilling. Having completed the Python topic during week 6, I have decided to hop on another CS50 course—CS50P. This choice is driven by my desire to delve deeper and learn more about Python and expand my understanding of the language. Truthfully, my final project for CS50X is an extended and enhanced version of my final project from CS50P, named MyFloodAlert. It operates as a command-line interface for flood reporting status where the user has to enter the locations manually. Nimbus, the enhanced version of MyFloodAlert, allows users to get flood status reports simply by clicking on the current location. As explained earlier, other features include weather report and forecast, earthquake report, as well as live satellite imagery. After four months of constant learning and dedication, my CS50 journey is coming to an end.  My gratitude extends to Dr. Malan and the entire CS50 team for coordinating such an exceptional learning environment. Overall, I take pride in the progress I've made in programming and the journey has been a fulfilling blend of challenges, learning experiences, and rewarding accomplishments. Driven by curiosity, my commitment remains persistent as I explore various aspects of the programming realm. I aspire to delve into languages like Solidity, commonly utilized in the realm of blockchain technology. With the hunger to learn more, I will be constantly pushing the boundaries of my learning journey.

