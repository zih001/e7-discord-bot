WELCOME! This is going to be THE repo for Darkwatch/DeadlySynz coding practice/yufinebot revival/news broadcaster playground. Don't mind the crazy rigid coding convention, this is mostly for learning and also some practical application, namely getting the latest posts from E7 STOVE and outputting through a discord bot.

To clone this project, we're using GitHub and Git Fork. We're also using VS Code with Python and Typescript add-ons.

The tech we'll be using are the following:
1. PolitePol for webscraping, takes in post links, titles, etc and outputs XML. Provides an URL that we need to websocket-fy.
2. Python app for consuming the XML content, converting to JSON, and making call to databasee to see if latest post is inserted.
3. MongoDB - data persistence, discord bot will talk to this to grab latest posts.
4. Node.js and typescript - used to write discord bot.

more will be added... 