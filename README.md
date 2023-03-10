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

## Features
Video Demo: [Youtube](https://youtu.be/6x7ziMTXC70) <br>

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

### Points of Ingenuity
- SQLAlcheby was used to allow query operations to be performed in Python coding rather than dynamic SQL. This allowed us to check for syntax errors before execution.
- Nginx was used to reverse proxy requests.
- Since Nginx cannot handle dynamic processing, requests for dynamic pages were processed by flask via gunicorn.
- Since there was a deadline for development, flask was chosen because it is a lightweight framework and the most familiar to use.

### Points of difficulty
- As this was the first time for me to design a DB, I had to check what kind of restrictions I should set for each column.
- It was difficult to understand the configuration of Nginx and gunicorn, and it took a lot of time.
- Nginx and gunicorn worked on local, but security configuration was difficult and we could not deploy.
- We had a hard time implementing an "edit page" that returns different data for each user.
- When displaying data corresponding to a product on the "index page," it was necessary to fetch data from two DBs, so we created a function to handle this.

### Features to be implemented in the future
- I signed up for a VPS and got a domain, but have not been able to deploy it because it took a long time to implement Nginx and gunicorn. Therefore, we will deploy after submission.
- Add an account deletion function.
- Add a function to allow users to select products and purchase them, although currently only a list of products is displayed.
- Add an email notification when an item is purchased.
- Add a "favorite" function.

## Reference
- https://bootstrap-guide.com/layout/columns
- https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
- https://qiita.com/Kotabrog/items/fb328b72ac94137897af
- https://it-dxblog.com/vscode-python-venv/
- https://nansystem.com/sqlite3-enable-foreign-key/
- https://qiita.com/msrks/items/d9c327dd81749ec01d1d

## Author
[GitHub](https://github.com/Sosuke1019)
