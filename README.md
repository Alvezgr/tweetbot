# A tweetbot Python: 

Using a Django app, which are deployed into Heroku.

# the bot:
the robot I chose between facts, jokes, lyrics of Paramore songs and curiosities, update your status on twitter using the tweepy library to work with the Twitter API.

using requests and bs4 for extract data from webs


## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

