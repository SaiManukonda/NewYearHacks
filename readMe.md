## How to try this project
1. clone the project and make sure your have python and pip installed

2. Go to the 'Server' folder and create a new python file called ' keys.py '

3. In the 'keys.py' file, create a new variable called 'GOOGLE_API_KEY' and put your google places api key there(you can get the key by going to https://developers.google.com/places/web-service/get-api-key)

4.next thing open your command line and cd your way into the server folder

5.then run this command in your commandline 'pip install -r requirements.txt' (this downloads all the libraries required from the project, whose names are stored in the requirements.txt'

6.then run the 'app.py' python file (run this like you would run any of your python files)

7. your output will be something like this
  * Serving Flask app "app" (lazy loading)
  * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
  * Debug mode: on
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 291-778-880
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  
8.Go to whatever link is present after 'Running on', which in this case is 'ttp://127.0.0.1:5000/'

9.Voila! now you can try this web app and if you would like to understand more about this project keep reading

## Inspiration
Inspired by the new year, we wanted to create a website to tackle some of 2020s biggest problems head on! The problem being visiting places without the risk of catching covid!

## What it does
Our team developed a website that will take the user input of a location and category as well as a desired location. With the information, we will return the optimal times to visit this location in correspondence with CoronaVirus levels.

## How we built it
For the front end we used a program known as bootstrap, which allowed us to create a useful and dynamic website. For the logic we used python to perform our algorithms which determines when a place is safe to visit by getting data from various sources. For the backend of the application we used flask and google places api to get information about the place such as name, image links,etc.

## Challenges we ran into
We originally had a plan of 4 group members, 1 front end, 1 back end, 2 data science people to perform the logic of the product. Due to unexpected emergencies, the front end dev decided to not show up. So we had to learn the front end which we didn’t know as well. But we stuck through and figured it all out.

## Accomplishments that we're proud of
The website is interactive, aesthetically pleasing and simple to use. This allows for the user to get the results back efficiently and visit a place when it is safe.

## What we learned
Bootstrap, frontend dev

## What's next for Safe Search
We want to implement more features to this website, such as crowd sourcing data, where people can input places that are really busy at specific times and we can use that make our results more effective!


