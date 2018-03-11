#!/bin/bash
source huerc.py
while [ 1 ];
do
    CVAL=$(curl -s -XGET http://${hue_bridge}/api/${api_key}/lights/3|jq .state.hue)
    if [ $CVAL -eq "8418" ]; then
        echo --------Light was turned off/on--------
        curl -XPUT http://${hue_bridge}/api/${api_key}/lights/3/state -d '{"on": true, "bri": 104, "hue": 65526, "sat": 254, "effect": "none", "xy": [ 0.6912, 0.3082 ], "ct": 153 }'
        echo
        echo
    fi
    sleep 300
done

