# plama
![This is an image](https://github.com/Sosuke1019/plama/blob/main/static/images/plama_indexpage.png)

## Overview
A flea market service that makes it easy to take over things (furniture, food, clothes...) at the dormitory. 

## Description
-  Persona　<br>
An international student living in a dormitory who wants to take over furniture and clothes from another student when it is time to move out for a year of study. There is no one to take over because there are one to three friends and furthermore, friends are moving out at the same time. It would be a shame to throw them away, but I don't want to go out of my way to ask other dorm residents.
- What can be solved <br>
By consolidating the information into one web service, it will be easier for the students to recruit recipients and for the recipients to search for information. In addition, since the moving period is only about 3 weeks, it can be used as a web application without the need to install it.
- How it works in a nutshell<br>
Anyone can freely sell their items by registering as a user.

## Getting Started

## Features
Video Demo: [Youtube](https://github.com/Sosuke1019) <br>

### Requirement Definition  
- New Registration
- Login Function
	- Name/Room number/Password
- Logout function
- Listing of items on the index screen
- Listing items on the "listings" screen
	- Photo/Product name/Product description
- Delete an item from the edit screen

### Technologies used
- Front-end: HTML, CSS, Bootstrap
- Framework：Flask
- DB：SQLite3
- Web Server：Nginx
- Application Server：gunicorn
- Development Environment：Github

### Features to be implemented in the future
- We have contracted a VPS and obtained a domain, but have not been able to deploy it because it took time to implement Nginx and gunicorn. Therefore, we will deploy after submission.
- Add an account deletion function.
- Add the ability to delete an account. Currently, only a list of products is displayed, but the transaction can be completed within the application by selecting a product.
- When an item is purchased, an email notification will be sent to the user.
- Favorite function

## Reference
- https://bootstrap-guide.com/layout/columns
- https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
- https://qiita.com/Kotabrog/items/fb328b72ac94137897af

## Author
[GitHub](https://github.com/Sosuke1019)
