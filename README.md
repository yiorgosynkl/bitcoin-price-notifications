# bitcoin-price-notifications

This project follows the tutorial from [this post](https://realpython.com/python-bitcoin-ifttt/).

There was this problem with the API key, but [this post](https://gist.github.com/SrNightmare09/c0492a8852eb172ebea6c93837837998) helped.

There is also [postman native apps](https://www.postman.com/) or the [CURL command line command](https://everything.curl.dev/).

The corresponding curl command is:
```bash
curl -G -X GET \
--header "Accept:application/json" \
--header "X-CMC_PRO_API_KEY:REPLACE_WITH_PRIVATE_API_KEY" \
https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest \
-d "slug=bitcoin" \
-d "convert=USD"

# or
curl -G -X GET \
--header "Accept:application/json" \
--header "X-CMC_PRO_API_KEY:REPLACE_WITH_PRIVATE_API_KEY" \
https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?slug=bitcoin&convert=USD

# -G: to allow the use of -d arguemnts
# -X: to specify the type of request
# --header: to pass different headers
# -d: to set the arguemnts (could also append the url with "?slug=bitcoin&convert=USD")
```

In order to make the whole backend quickly, use swagger JSON example.
It's about the tools and how to use them, not about what we learn. Software engineering is a lie. If I want now, I can build the app. The problem is being smart to find something cool to build. Or something smart. 
