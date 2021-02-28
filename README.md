# MZM-Martialarts Website

---

### Contents:

 - [Description](#description)
 - [UX](#ux)
 - [Features](#features)
 - [Technologies Used](#technologies-used)
 - [Testing](#testing)
 - [Deployment](#deployment)
 - [Credits](#credits)
---

## Description

For the final project I have created a website which is based on the idea of online martial arts club where users can subscribe to the club and recieve weekly videos based of varying difficulties based on the level of their subscription. 

This idea was due to sports facilities being closed for almost 1 year now and would have provided an alternative for kids and adults who wanted to stay physically active at home during lockdowns or for students who wanted to keep up their martial arts training despite all the physical centers being closed. I have used [This website](https://www.mzm-semartialarts.com/) as the basis for the fictional service with permission from the owner, no code was copied from the existing website only text and images were taken from it.
---

## UX

---

Due to the functionality of the website being to provide a subscription model for potential clients to join an online martial arts club it doesn't require many pages, once subscribed the users are added to a mailing list for the admin user and he/she will be able to send out weekly videos/zoom class links so none of this will be happening on the website itself.

User stories:
 - I am martial arts studennt who can no longer practiice martial arts in a slub and am looking to keep up my hobby during lockdown and wish to view different price plans available for online sessions.
 - I am martial arts studennt who can no longer practiice martial arts in a slub and am looking to keep up my hobby during lockdown and wish to subscribe to a advanced level course which provide online sessions to help me keep practice for my grading.
 - I am a parent who wishes to find a way to help my child keep occupied during lockdown and wish to browse for sporting activities which the child can do from home with prospects to continue the training in a studio in person when lockdown finishes.
 - I am a parent who wishes to find a way to help my child keep occupied during lockdown who wants to sign my child up for a begginers course in martial but wish to cancel the subscription when lockdown is over as he will not have as much free time.
 - I am someone not looking to subscribe to online sessions for martial arts but am looking to find a dojo near me to join when lockdown is over.
 - I am the owner of the site and wish to view the mailing list for subscriptions.

---

## Features

### Existing Features

 - A list of subscription plans with prices and descriptions are available for users to look at to compare with other subscription plans.
 - The ability to subscribe and be added to the mailing list of the club for weekly sessions.
 - There is a admin login and registration function using django superuser.
 - Django superuser can have access to view all of the purchases made on the website to view the mailing list and which subscription each person has purchased.
 - Users have the ability to sign up to the website and purchase a subscription plan.
 - Subscribers have the ability to change or cancel their subscription plans. 

### Feaatures left to impend

 - Free trial videos could be added to the website so that people get a chance to see the kind of sessions they will recieve from their subscriptions, this was not added as access to any existing videos was not available.
 - Friendlier ux for purchases, the default stripe payment url is used in this website, a unique one could be created and implemented.
 - Access to the email provided in the link was not available so confirmation emails are sent from a fictional address.
 - Better quality photos would help keep the styling cleaner.
---

## Technologies Used

 - Django - The project is built using Django Frameworks and uses it to create apps as it is quicker than most ways of web development.
 - Stripe - The project uses Stripe to take monthly payments from sunscribers and provide product data.
 - homebrew - Homebrew was installed in the terminal so that the cli for stripe could be installed into the application using `brew install`.
 - aulauth - Allauth was used in order to create a superuser using `python3 manage.py createsuperuser`.
 - Javascript - This was used to add functionality of stripe payments and load stripe payment screens and data.
 - Boostrap4 - Used to add icons, buttons, format contact forms, responsive web design and background colours.
 - HTML + CSS - The front end was written with these languages.
 - Python - The backend was written mostly in python which is the language django is based in. 
---

## Testing

Subscription payment: - Go to the "Membership Plans" page.
              - Select a subscription plan.
              - Click subscribe.
              - Try to submit the empty form and verify that an error message about the required fields appears.
              - Try to submit the form with an invalid billing address and verify that a relevant error message appears.
              - Try to submit the form with an invalid card number and verify that a relevant error message appears.
              - Try to submit the form with all inputs valid  using test card 4242 4242 4242 42424 24/24 424 and verify that a success message appears.

Cancel Subscription: - Go to profile page of user
             - Clcik cancel subscription.
             - Go to superuser.
             - Check that the subscription is canceled from the test user.

Register User: - Add register to navbar.
     - Go to sign up under account icon.
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with an invalid password and verify that a relevant error message appears.
     - Type valid username and password.
     - Click 'Add user' - If success you would be taken to the index.html page and session=user would be in session, if not various errors could happen.
     - To fix any errors check run.py and links in the register form from register.html and try again.

Login User: - Add login to navbar.
     - Go to login under account icon.
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with an invalid password or username and verify that a relevant error message appears.
     - Type username and password created from sign up form.
     - Click 'Login' - If success you would be taken to the index.html page and session=user would be in session, if not various errors could happen.
     - To fix any errors check run.py and links in the register form from register.html and try again.

## Deployment

The website was written in gitpod and deployed through github repositories using regular git commits from the command terminal in gitpod. It is run using Flask

There is no differences between the deployed version and deployment version.

---

## Credits

### content:
 - All information in the site is taken from [This website](https://www.mzm-semartialarts.com/)

### media:
 - All media was taken from the wix library of [This website](https://www.mzm-semartialarts.com/) 
