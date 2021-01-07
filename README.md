## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# 18011020 Alper Reha YAZGAN - Web Data Mining Termpaper - Url Text Content Keyword Finder by Web Scraper  

- Project is avaliable on [THIS HEROKU LINK](https://yazganwebminingproject.herokuapp.com/) you can check this link to see on action.

## About

This project aiming to create an open source standalone web text content scraper and keyword finder from given url.


## Getting Started

Getting up is so easy.

1. Install [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/).
2. Install your dependencies

    ```
    pip install -r requirements.txt
    ```

3. Start your app

    ```
    flask run
    ```

## Routes


    PUBLIC ROUTES:
    GET / (Home Page For All Actions)
    GET /all (You can see all saved website and keywords pair in the table design view)

    /* For Web Scraping and Keyword Finding */
    POST /search (param:searchtext --> Enter URL for fetch and find keywords )

    /* For Normal Search Engine Query */
    POST /search (param:searchtext --> Enter keywords to find the appropriate site )

    /* For API Requests */
    POST /api/text (param:text --> Enter full text content to find the keywords )


## Deployment  
You can deploy this application on [Heroku](https://www.heroku.com/) like web cloud platforms to perform code on action. Procfile is avaliable for Heroku

## Testing

Simply run `flask run` inside project directory and all your tests will be run.


## TODO

 - [ ] Improve Keyword Finder Algorithm
 - [ ] Improve Text Content Finder Utilities
 - [ ] Improve UI

## License

Alper Reha YAZGAN
Copyright (c) 2020
Licensed under the [MIT license](LICENSE).
