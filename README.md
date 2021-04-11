# huehuehue
Just a project to mess around with hue bulbs


You'll have to edit the huerc.py to add 2 things:

   hue_bridge: ip or hostname of your hue bridge

   api_key: you api key to interact with your hue bridge


Like this:

# huerc.py:
# Set up your HUE_BRIDGE variable and API_KEY herer
hue_bridge="IP ADDRESS"
api_key="API_KEY"


If you are unfamiliar with how to get an api key, check out the philips hue api key doc here:
https://developers.meethue.com/philips-hue-api

Special thanks to Ad Dijkhoff, a guy I met at re:invent in 2017 that 
essentially convinced me to make the initial investment in hue bulbs. 

It's been a wild ride
