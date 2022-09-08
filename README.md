# M.A.R.S : Music Augmented by Recommendation System

M.A.R.S is a user friendly music recommendation system.

It provides you with music to
suit your taste using its unique algorithm. You can also fine tune your music through different modes.

## Tech Stack
- Web Technologies 
    - Framework
        - Django
    - Hosting
        - Pythonanywhere
    - Others
        - CSS3
        - Bootstrap
        - jquery
        - full page scroll (js library)
- Recommendation Algorithm based on cosine simillarity
- Supporting backend on python
- Spotify API
- Python libraries
    - Scipy
    - Scikit-learn
    - pandas
    - numpy
    - pafy
    - spotipy

## Working
- The song name is passed in the recommendation algorithm
- Apt recommendations for all the different modes (check the website for this feature) are passed by the algorithm from the 132,000+ songs dataset.
- Metadata about the song is taken from the spotify API and saved in the dataset for future recommendations.
- The song is then passed to pafy(see requirements.pip), which generates a playable link for the song. This link is then passed to the webapp, which plays the song along with the next 2 recommendations.

## File structure
```
├── src
│   ├── assets ( contains css, js, fonts and images which are used in website)
│   ├── mars_app
│        ├── templates ( contains html templates used in django)
│        ├── wd ( contains backend code, recommendation engine and dataset)
│        ├── migrations
│        ├── admin.py
│        ├── apps.py
│        ├── models.py
│        ├── tests.py
│        ├── urls.py
│        ├── views.py
│   ├── src
│        ├── etc
│        ├── asgi.py
│        ├── settings.py
│        ├── urls.py
│        ├── wsgi.py
│   ├── manage.py
│   ├── db.sqlite3
│   └── requirements.pip
├── README.md
└── .gitignore
```

## Previous Recommendation engines
- MFCC based model
- Collaborative-filtering based
- Content Based

## Running locally
Install the requirements 
```
pip3 install requirements.pip
```
Move to the src directory and run the following code
```
python3 manage.py runserver
```
This will run the webapp on your localhost [127.0.0.1:8000](http://127.0.0.1:8000)

## To run the app in development mode ( DEBUG=True )
- set DEBUG=True in settings.py file
- copy the assests folder in mars_app folder and rename it as static

## Developed and maintained by:
- [Shivansh Agrawal](https://github.com/coastaldemigod)
- [Sagar Kumar](https://github.com/Sagar-Kumar-007)
- [Danish Gupta](https://github.com/danish1207)

Star the repo and start contributing :)
