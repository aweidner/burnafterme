Post and share links to ephemeral data

# Usage

Add new data (with a TTL of 1w)

    curl -X PUT -H "ContentType: text/plain" --data "Your data goes here" https://burnafter.me

Add new data with a custom timeout
    
    curl -X PUT -H "ContentType: text/plain" --data "Your data goes here" https://burnafter.me/?t=10s

Get existing data (data is deleted after access)

    curl https://burnafter.me/<key>
