#!/bin/bash

FEED_ID="122977"
BASE_DIR=`dirname $0`
TEMP_FILE=$BASE_DIR/'temp.json'
HUMIDITY_FILE=$BASE_DIR/'humidity.json'


VALUE=`$BASE_DIR/sensor`
TEMP_VALUE=`echo $VALUE | awk '{print $2}'`
HUMIDITY_VALUE=`echo $VALUE | awk '{print $1}'`

send_data()
{
    awk 'BEGIN{printf "{\"datastreams\":[ {\"id\":\"'$1'\",\"current_value\":\"%.1f\"} ] } ",'$2'}' > $3
    curl --request PUT --data-binary @$3 --header "X-ApiKey:nCSMZ9wLNhEeL0xIu8_ZNpXFLoCSAKxKRG4xTVM2WDVGbz0g" http://api.cosm.com/v2/feeds/$FEED_ID?timezone=+8
}


send_data temp $TEMP_VALUE $TEMP_FILE
send_data humidity $HUMIDITY_VALUE $HUMIDITY_FILE
