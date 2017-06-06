<<<<<<< HEAD
# ApproApp

## Project Summary
ApproApp is an app, which will provide the necessary online platform for different Organizations, Executives and Individuals to submit, digitally sign and comment the different documents to be exchanged between different stakeholders of organization.

## Project Details
Platform will consist three types of users that are Organizations, Officials and Individuals all will have different tasks as given below

### 1.	Organizations
Organizations will be capable of publishing documents online through our site which will carry necessary information of required digital signatures by officials for approval of application and required info of last stakeholder who will collect that document and process it.

### 2.	Individuals
Individuals can fill those forms online and send them to officials for approval, they will be notified at each step when document will proceed to next official and he will also get notified what comments did last executive made

### 3.	Officials or Executives
They will be required to digitally sign the documents and approve them through their .pfx files provided to them on behalf of ApproApp.

## Technology
We will develop the web with combining three web apps that is one will be serving organizations, other to officials or executives and third will serve to normal individuals and all will be joint together by common database.

## Working
I.	Organizations will be able to see form builder page, executive hierarchy setter, and other top jobs. They will build forms and save on site with names of executives who need to approve those applications.
II.	Now all those applications created by that organization will be saved to individual’s app database.
III.	Individual will be shown option with no. of organizations when he will choose his organization he will see all forms he can fill.
IV.	Individual will open the html form and fill it and send it.
V.	After clicking send button application will be converted into pdf form and will be sent to executives’ database now as specified by the organization all executives mentioned on application will receive that application one by one.
VI.	They can approve by applying digital signature certificate (.pfx file) to pdf or can reject it with adding comments to it which will be sent to user directly without further processing.
VII.	Now it will reach to last officer who will process it.

## Software Used
### •	Django •	Python 3 •	SQL(anyone) •	HTML5 •	CSS3 •	Bootstrap •	JavaScript •	AngularJS •	Django addons 	Report Lab 	Identity4

## Process
Frontend will be made by using HTML, CSS, angular etc.
At backend, we need three main steps 
A.	Creating form builder is easy with Django using dynamic memory allocation.
B.	In converting html pages to pdf, we can use free open source addon ReportLab.
C.	PDF can be signed using identity4 free opensource software.

## Collaboration Required
ApproApp requires a team of individuals who can collaborate with us to develop the product. We need you for 45 days with work from home or part time conditions.

## In Return
In return ApproApp will be Providing you a place in core team and experience letter.

## Terms and Conditions
After complete development of the product, copyrights will be owned by the company.



### Ripudaman Singh,
### Thapar University, Patiala
### Founder ApproApp
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
