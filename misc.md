# Miscellaneous

This area documents things not directly part of the NHL API but related to it, utilized by it or otherwise related to it somehow.

## Player Name Suggestion 

This service appears to be a search of players based on name

`GET https://suggest.svc.nhl.com/svc/suggest/v1/minplayers/NAME/NUMBER`

Takes the NAME value which can be any part of a player's name and a NUMBER of results to return, this endpoint searches for all players with this name fragment

`GET https://suggest.svc.nhl.com/svc/suggest/v1/minactiveplayers/NAME/NUMBER`

Same as the minplayers endpoint however this only looks at active players.
