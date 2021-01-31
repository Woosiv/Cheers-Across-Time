import requests
import config

def getCat():
        response=(requests.get("https://api.thecatapi.com/v1/images/search",config.Config.APIKEY)).json()
        return response[0]['url']