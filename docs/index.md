# ApproApp

## Project Summary
ApproApp is a facilitating application which will provide the much necessary online platform for various different Organizations, Executives and Individuals to submit, digitally sign and comment the different documents to be exchanged between diverse stakeholders of distinguishable organization.

## Project Details
This vast platform will consist three types of users which include Organizations, Officials and Individuals. All of the them will have different tasks as specified below:


### 1.	Organizations
Organizations will be capable of publishing documents online, through our website, which will carry all the necessary information of the required digital signatures by officials for approval of application. They will also have the required info of the last stakeholder who will collect that document and process it.

![alt text](https://raw.githubusercontent.com/ApproApp/ApproApp/master/docs/img/img1.jpg)


### 2.	Individuals
Individuals can fill those forms online and send them to officials for approval, they will be notified at each step of processing the document like when it will proceed to the next official, what comments did last executive make etc.


### 3.	Officials or Executives
They will be required to digitally sign the documents and approve them through their .pfx files provided to them on behalf of ApproApp.


## Technology
We will develop the application with combining three web apps which will serve 3 diff sectors that is, one will be serving organizations, other to officials or executives and third will serve to normal individuals and all will be joint together by a common database. This means that at the very core level, approapp will serve the purpose of 3 different applications in one.


## Working
I.	Organizations will be able to see the form builder page, executive hierarchy setter, and other top jobs. They will build forms and save on the site with names of executives who need to approve those applications.

II.	Now, all those applications created by that organization will be saved to  individual’s app database. 

III. Individual will be shown options with no. of organizations. As soon as he chooses his organization, he will see all the forms he can fill. 

IV.	Individual will open the html form,  fill it and send it. 

V.	After clicking send button, application will be converted into pdf form and will be sent to executives’ database. Now, as specified by the organization, all executives mentioned on application will receive it one by one.

VI.	They can approve it by applying digital signature certificate (.pfx file) to pdf or can reject it with adding comments to it which will be sent to the user directly without further processing.

VII. If approved, it will reach to the last officer who will process it.

## Software Used
### •	Django •	Python 3 •	SQL(anyone) •	HTML5 •	CSS3 •	Bootstrap •	JavaScript •	AngularJS •	Django addons 	Report Lab 	Identity4

## Process
Frontend will be made by using HTML, CSS, angular etc. At backend, we need three main steps : 

A.	Creating form builder is easy with Django using dynamic memory allocation. 

B.	In converting html pages to pdf, we can use free open source addon ReportLab. 

C.	PDF can be signed using identity 4 free opensource software.


## Collaboration Required
ApproApp requires a team of individuals who can collaborate with us to develop the product. We need you for 45 days with work from home or part time conditions.


## In Return
In return ApproApp will be Providing you a place in core team.


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
