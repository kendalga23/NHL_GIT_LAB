# NHL API Documentation

## Latest News

### 2024-11-02

The NHL has kindly provided us with a very handy (but ugly) file called application.wadl which documents their entire API. I have taken some time and written a python script (scripts/wadl-map.py) that automatically querries the endpoint that provides the file, converst the XML to JSON and parses it out in a simple but understandable format. The markdown file in the scripts folder provides an example of the output.

**This is a work in progress** - use it at your own discretion, eventually it will be updated to create a much nicer output, possibly even with markdown formatting and will eventually be setup on a website to auto-update every so often and provide browsable documentation that requires less maintenance than the hand-written documentation that exists now.


---
## About this Project

This effort is purely to make it easier for stats nerds and the like to make
use of the wonderful trove of information the NHL provides to us but in a much
more digestible form. 

## Roadmap

Eventually build documentation on features such as cayenneExp which allows for 
retrieval of very complex documentation and perhaps even a more thorough set of 
documentation including examples in multiple common langages (such as using Swagger)

## Files

| file | description |
| --- | --- |
|[made-with.md](made-with.md)|Collection of things made using the NHL API documentation, by no means exhaustive and zero affiliation with these projects.|
|[misc.md](misc.md)|Random things the NHL API uses or is somehow related to|
|[records-api.md](records-api.md)|Documentation on the API for records.nhl.com|
|[stats-api.md](stats-api.md)|The one, the only NHL API (stats) documentation!|
|[new-api.md](new-api.md)|New 2023 NHL API (stats) documentation|


## Contributing

I am only one person so if you see something I have missed please feel free to 
open up a MR/PR and I will get it merged.  Generally speaking I get things done
in a few days as time permits between work and other obligations.

## Contact

Generally I am reached via Twitter [@dw0rd4](https://twitter.com/dw0rd4)

## Acknowledgements

[Kevin Sidwar](https://www.kevinsidwar.com/) - First real source of documentation I found on the API and gave me
a nice starting point for a project that eventually evolved into this repository

[Jon Ursenbach](https://github.com/erunion) - Built out an [OpenAPI 3 spec](https://github.com/erunion/sport-api-specifications) for the NHL API 