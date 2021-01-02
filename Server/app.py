from flask import Flask, request, render_template, redirect, url_for
import populartimes
from googleplaces import GooglePlaces,types,lang
import json
from keys import GOOGLE_API_KEY

API_KEY = GOOGLE_API_KEY
google_places = GooglePlaces(API_KEY)

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('home.html')

@app.route('/results/')
@app.route('/results/<typeOfPlace>/<location>')
def Results(typeOfPlace = 'None', location = 'None'):
    if(typeOfPlace == 'None' and location == 'None'):
        return redirect(url_for('HomePage'))
    searched = typeOfPlace +" in " + location
    query_result = google_places.text_search(query = searched)
    info = []
    for place in query_result.places:
        curr = []
        curr.append(place.name)
        place.get_details()
        curr.append(place.website)
        info.append(curr)
        curr.append(place.place_id)
        try:
                temp = place.photos[0]
                temp.get(maxheight = 500, maxwidth = 500)
                if(temp.url != None):
                    curr.append(temp.url)
                else:
                    curr.append('https://emilyshane.org/images/no-image.jpg')

        except:
            curr.append('https://emilyshane.org/images/no-image.jpg')
    return render_template('results.html', data = info, searched2 = searched)

@app.route('/view/<id>')
def Results2(id = "None"):
    place = google_places.get_place(id)
    photos2 = []
    for photo in place.photos:
        photo.get(maxheight=50000, maxwidth=50000)
        photos2.append(photo.url)
    return render_template('view.html', photos = photos2, name = place.name)


if __name__ == "__main__":
    app.run(debug=True)