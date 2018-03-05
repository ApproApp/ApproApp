# MechMocha Game Engine Using AI (M-GEUAI)


## Project Summary
M-GEUAI is a game development engine for common people. They can make there own games using simple videos and a bit training to the game on online platform. M-GEUAI will be able to create different types of games such as shooting games in which developer will upload the video and select some target in the video and Engine will automatically select all other targets in the video after converting it to game  player will need to shoot those targets. We can also make run and chase games using this Engine like developer will select a path in the video after converting it to game the player will need to follow the same path. so there are so many games which can be developed by using our game engine and also because it will be a video so it will give a desi culture feel of anywhere in the world.


## Project Details

### Deliverables to MechMocha
We will create a game called Total BlackOut In which we will have a scenario from india train and player will be sitting in the last coach of train and it will be night scene so it will be all black outside the window and lights inside the train. the player will need to shoot the lights around the path from running train to create a total blackout and if player shoots when train is not running or very slow police will catch him and take to the prison.
We will Provide the Game Engine to make such games simply using videos and Images. 
We will provide the web platform for the game engine which will be accessible from all kind of mobile and computer devices.

### Benefits To MechMocha
This kind of platform will give freedom to create games in real world situations and will not require to convert everything to animation.
Player will feel like its a realworld in his or her phone.
This type of platform will provide developers to create games like pokemonGo very easily.


## Technology
We will create the models of for video processing and image processing then we will add same models in the game engine to perform on different videos of users after that we will optimize the models by different ML techniques using the same models we will create total blackout game and create M-GEUAI at last we will develop web platform using Django for game engine and create different versions of total blackout for different platforms like android, ios, Windows etc using Kivy


## Working
Proccess For Developers
Game Developers will be asked to upload a video to convert it to a game.
Now they will be asked to type of game they want to convert to like shooting or Run & Chase.
If they Selects shooting they will be asked to select a few targets in the video and points which cant be shot by the player.
If they Selects the Run & Chase they will be asked to select some path in the video which players need to follow.
similar paths and targets will be selected by our engine and it will be converted to a game.
They will be asked to select which platform they want to convert game to.
They will find the link to download their own game in form of apk or other file according to platform.

Process For Gamers
Gamers will download the game and play it in real world.


## Software Used

### • Kivy • PyOpenGL •	PyGame • TensorFLow • SkLearn •	ImageProcessing • VideoProcssing • OpenCV •	Python3 • Matlab • Django


## Process

### 1. Total Black Out Game Development
In first four months the work will be done on image and video proccessing to develop this game called total black out in which I will take a video from window of a train at night of around 4 to 5 hours. Then by Video Processing using Machine Learning Algorithms of SkLearn, TensorFlow, OpenCV and Matlab we will make the system to capture targets which are having bright lights and at last using PyOpenGL and PyGame we will make shooting game in which player will need to target on the lights on the way. which will create blackout around the track of train. This will give us desi feeling of Indian trains and a lot of Indian culture around the train. but if player shoots the lights when train is not running he will be caught by police and game will be over. also atlast in last 3 weeks game will be converted for different platforms like Android, IOS, windows etc using Kivy.

### 2. M-GEUAI Development
In next three months the work will be done on Game engine using same models of Artificial Intelligence which we developed for our total blackout game development. Using pure Python3 and its packages we will be able to create the game engine.

### 3. Web Platform
In last 2 months we will use django to create a web platform for uploading this game engine and publishing it to the world.


## Collaboration Required
M-GEUAI requires a time of 7 to 9 months for completion. We want you to support us during the development by sponsorship or salary. Incase of salary, I can work remotely from Patiala or I can work from your office in Banglore.


## In Return
In return M-GEUAI will become a Product of MechMocha with complete copyrights, and Reserch Papers Published under this idea by me and also if possible any Patent under Computer Related Invention(Guidelines by Indian Patent Act) will also be owned by MechMocha.


## Terms and Conditions
Section to be created later by memorandum of Understanding in case of sponsorship, and your terms will be carried forward in case you provide me a salary and job.


## Humble Request
This idea is not copyrighted or registered anywhere in India or anywhere else in the world. So, I hope that MechMocha will not cheat me and copy my idea.


## For More INFO Contact
### Ripudaman Singh,
### Thapar University, Patiala
### Founder M-GEUAI
### (+91) 9780-510-630
### rsingh_bemba16@thapar.edu

=======

#### I will be looking forward to your Reply.

=======





# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.


## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).


## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
>>>>>>> bd90123510bc5894ca7541d6577fcc23e9bc150d

test
