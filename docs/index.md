# MechMocha Game Engine Using AI (M-GEUAI)

## Project Summary
M-GEUAI is a facilitating application which will provide the much necessary online platform for various different Organizations, Executives and Individuals to submit, digitally sign and comment the different documents to be exchanged between diverse stakeholders of distinguishable organization.

## Project Details
This vast platform will consist three types of users which include Organizations, Officials and Individuals. All of the them will have different tasks as specified below:


### 1.	Organizations
Organizations will be capable of publishing documents online, through our website, which will carry all the necessary information of the required digital signatures by officials for approval of application. They will also have the required info of the last stakeholder who will collect that document and process it.


### 2.	Individuals
Individuals can fill those forms online and send them to officials for approval, they will be notified at each step of processing the document like when it will proceed to the next official, what comments did last executive make etc.


### 3.	Officials or Executives
They will be required to digitally sign the documents and approve them through their .pfx files provided to them on behalf of M-GEUAI.


## Technology
We will develop the application with combining three web apps which will serve 3 diff sectors that is, one will be serving organizations, other to officials or executives and third will serve to normal individuals and all will be joint together by a common database. This means that at the very core level, M-GEUAI will serve the purpose of 3 different applications in one.


## Working
I.	Organizations will be able to see the form builder page, executive hierarchy setter, and other top jobs. They will build forms and save on the site with names of executives who need to approve those applications.

II.	Now, all those applications created by that organization will be saved to  individual’s app database. 

III. Individual will be shown options with no. of organizations. As soon as he chooses his organization, he will see all the forms he can fill. 

IV.	Individual will open the html form,  fill it and send it. 

V.	After clicking send button, application will be converted into pdf form and will be sent to executives’ database. Now, as specified by the organization, all executives mentioned on application will receive it one by one.

VI.	They can approve it by applying digital signature certificate (.pfx file) to pdf or can reject it with adding comments to it which will be sent to the user directly without further processing.

VII. If approved, it will reach to the last officer who will process it.

## Software Used
### • Kivy • PyOpneGL •	PyGame • TensorFLow • SkLearn •	ImageProcessing • VideoProcssing • OpenCV •	Python3 • Matlab

## Process
### 1. 


## Collaboration Required
M-GEUAI requires a time of 6 to 8 months for completion. We want you to support us during the development by sponsorship or salary. Incase of salary, I can work remotely from Patiala or I can work from your office in Banglore.


## In Return
In return M-GEUAI will become a Product of MechMocha with complete copyrights, and Reserch Papers Published under this idea by me and also if possible any Patent under Computer Related Invention(Guidelines by Indian Patent Act) will also be owned by MechMocha.


## Terms and Conditions
Section to be created later by memorandum of Understanding in case of sponsorship, and your terms will be carried forward in case you provide me a salary and job.


## Humble Request
This idea is not copyrighted or registered anywhere in India or anywhere else in the world. So, I hope that MechMocha will not cheat me and copy my idea.

### Ripudaman Singh,
### Thapar University, Patiala
### Founder M-GEUAI
### (+91) 9780-510-630
### rsingh_bemba16@thapar.edu


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
