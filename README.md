# incoming-track


API            |  Tracking
:-------------------------:|:-------------------------:
![](images/api.png)  |  ![](images/tracking.png)

# Run

```bash
flask run
```

# Requirements
Flask            |  BeautifulSoup
:-------------------------:|:-------------------------:
<img src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" alt="drawing" width="200"/>  |  <img src="https://i.pinimg.com/originals/05/db/b3/05dbb33728feb29928f03768b2c61486.png" alt="drawing" width="200"/>


# Why ❓️

For those tracking methods that don't provide API (mosts of them ?!) and people that are anxious enough to verify the status time by time, it comes with the idea of scraping the data out of its page.

# Endpoint 🚩
The endpoint is */status* and shall return a json list with the status.

# Configs ⚙️
The setup is composed of two pieces:
* Create a file with name *page.py* and a variable called *PAGE_LINK* with the tracking link.
* Ajust the the searching method to the choosen page.

# Calibration 🧭
The search method looks for a list of tags "p" with class "titulo". Probably it won't be your case so ajust the search to the logic within your page. Be clever!

# Improvments or Suggestions
* Deploy to a server(firebase gcloud, heroku)
* Implement ready to use most famous tracking methods