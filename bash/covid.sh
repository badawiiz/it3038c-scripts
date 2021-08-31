#1/bin/bash

#This script downloads covid data and displays detailed information

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalized')
VENT=$(echo $DATA | jq '.[0].onVentilatorCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $HOSPITAL hospitalized, and $VENT currently on ventilators"
