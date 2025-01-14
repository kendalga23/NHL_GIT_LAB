# NHL Stats API Documentation

[OpenAPI 3.0 specification file for the NHL API](https://github.com/erunion/sport-api-specifications/tree/master/nhl).

Thanks to [erunion](https://github.com/erunion)

`https://statsapi.web.nhl.com`

# Endpoint Tables

| [LEAGUE ENDPOINTS](#league-endpoints) |                                                                            |
| ------------------------------------- | -------------------------------------------------------------------------- |
| [Awards](#awards)                     | Get all awards; get individual award                                       |
| [Conferences](#conferences)           | Get all conferences; get individual conferences                            |
| [Divisions](#divisions)               | Get all divisions; get individual divisions (historical options available) |
| [Franchises](#franchises)             | Get all franchises; Get individual franchise                               |
| [Tournaments](#tournaments)           | Get types; Get playoffs                                                    |
| [Venues](#venues)                     | Get all venues; Get individual venue                                       |

| [GAME ENDPOINTS](#game-endpoints) |                                                      |
| --------------------------------- | ---------------------------------------------------- |
| [Game IDs](#game-ids)             | A note about  how Game IDs are constructed           |
| [Games](#games)                   | Get live data, boxscore, linescore, content, updates |
| [Game Status](#game-status)       | Get list of Game Status                              |
| [Game Types](#game-types)         | Get list of game types and post-season status        |
| [Play Types](#play-types)         | Get types of play for live data                      |

| [PLAYER ENDPOINTS](#player-endpoints) |                                                                   |
| ------------------------------------- | ----------------------------------------------------------------- |
| [Draft](#draft)                       | Get most recent draft; get past draft (by year)whatever           |
| [Players](#players) (called "People") | Get Players (see [player stat modifiers](#player-stat-modifiers)) |
| [Prospects](#prospects)               | Get Players not in the league yet                                 |

| [SCHEDULE/SEASON ENDPOINTS](#schedule-endpoints) |                                                                   |
| ------------------------------------------------ | ----------------------------------------------------------------- |
| [Schedule](#schedule)                            | Get Schedules; see [modifiers](#schedule-modifiers) for varietals |
| [Seasons](#seasons)                              | Get season details                                                |

| [STANDINGS ENDPOINTS](#standings-endpoints) |                                |
| ------------------------------------------- | ------------------------------ |
| [Standings](#standings)                     | Get an aggregate of standings  |
| [Standings Types](#standings-types)         | Get Variety of standings types |

| [TEAMS ENDPOINTS](#teams-endpoints) |                                                               |
| ----------------------------------- | ------------------------------------------------------------- |
| [Team Stats](#team-stats)           | Get current team stats; Get rank of team for categories       |
| [Teams](#teams)                     | Get Team specific info; see [Team modifiers](#team-modifiers) |

| [MISCELLANEOUS ENDPOINTS](#miscellaneous-endpoints) |                                               |
| --------------------------------------------------- | --------------------------------------------- |
| [Configurations](#configurations)                   | List of other endpoints                       |
| [Event Types](#event-types)                         | non-hockey related to venues                  |
| [Expands](#expands)                                 | Shows all possible input for the expand field |
| [Languages](#languages)                             | fairly obvious                                |
| [Performer Types](#performer-types)                 | non-hockey performers for venue               |
| [Platforms](#platforms)                             | Tailor API to specific platform               |
| [Stat Types](#stat-types)                           | List of stat types used for players           |

<br />
<br />
<br />

# League endpoints

## Awards
`GET https://statsapi.web.nhl.com/api/v1/awards` | Get all NHL Awards.

`GET https://statsapi.web.nhl.com/api/v1/awards/ID` | Get an NHL Award.

<details>
   <summary>click for example</summary>

```json
// GET https://statsapi.web.nhl.com/api/v1/awards/1

{
  "copyright": "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "awards": [
    {
      "name": "Stanley Cup",
      "shortName": "The Cup",
      "description": "History: The Stanley Cup, the oldest trophy competed for by professional athletes in North America, was donated by Frederick Arthur, Lord Stanley of Preston and son of the Earl of Derby, in 1893. Lord Stanley purchased the trophy for 10 guineas ($50 at that time) for presentation to the amateur hockey champions of Canada. Since 1906, when Canadian teams began to pay their players openly, the Stanley Cup has been the symbol of professional hockey supremacy. It has been contested only by NHL teams since 1926-27 and has been under the exclusive control of the NHL since 1947.",
      "recipientType": "Team",
      "history": "It all started on March 18, 1892, at a dinner of the Ottawa Amateur Athletic Association. Lord Kilcoursie, a player on the Ottawa Rebels hockey club from Government House, delivered the following message on behalf of Lord Stanley, the Earl of Preston and Governor General of Canada  -- &quot;I have for some time been thinking that it would be a good thing if there were a challenge cup which should be held from year to year by the champion hockey team in the Dominion (of Canada).  There does not appear to be any such outward sign of a championship at present, and considering the general interest which matches now elicit, and the importance of having the game played fairly and under rules generally recognized, I am willing to give a cup which shall be held from year to year by the winning team.&quot; --  Shortly thereafter, Lord Stanley purchased a silver cup measuring 7.5 inches high by 11.5 inches across for the sum of 10 guineas (approximately $50); appointed two Ottawa gentlemen, Sheriff John Sweetland and Philip D. Ross, as trustees of that cup.  The first winner of the Stanley Cup was the Montreal Amateur Athletic Association (AAA) hockey club, champions of the Amateur Hockey Association of Canada for 1893. Ironically, Lord Stanley never witnessed a championship game nor attended a presentation of his trophy, having returned to his native England in the midst of the 1893 season. Nevertheless, the quest for his trophy has become one of the worlds most prestigious sporting competitions.",
      "imageUrl": "http://3.cdn.nhle.com/nhl/images/upload/2017/09/Stanley-Cup.jpg",
      "homePageUrl": "http://www.nhl.com/cup/index.html",
      "link": "/api/v1/awards/1"
    }
  ]
}
```

</details>

<br />

[back to top](#endpoint-tables)

## Conferences

`GET https://statsapi.web.nhl.com/api/v1/conferences` | Returns conference details
for all current NHL conferences.

`GET https://statsapi.web.nhl.com/api/v1/conferences/ID` | Same as above but for
specific conference, also can look up id 7 for World Cup of Hockey.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "conferences" : [ {
    "id" : 6,
    "name" : "Eastern",
    "link" : "/api/v1/conferences/6",
    "abbreviation" : "E",
    "shortName" : "East",
    "active" : true
  }, {
    "id" : 5,
    "name" : "Western",
    "link" : "/api/v1/conferences/5",
    "abbreviation" : "W",
    "shortName" : "West",
    "active" : true
  } ]
}
```

<br /></details>

[back to top](#endpoint-tables)

## Divisions
`GET https://statsapi.web.nhl.com/api/v1/divisions` | Returns full list of divisions
and associated data like which conference they belong to, id values and API links.
Does not show inactive divisions

`GET https://statsapi.web.nhl.com/api/v1/divisions/ID` | Same as above but only for a
single division. This can show old inactive divisions such as 13 Patrick.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "divisions" : [ {
    "id" : 17,
    "name" : "Atlantic",
    "link" : "/api/v1/divisions/17",
    "abbreviation" : "A",
    "conference" : {
      "id" : 6,
      "name" : "Eastern",
      "link" : "/api/v1/conferences/6"
      },
    "active" : true
    },
  ]
}
```

<br /></details>

[back to top](#endpoint-tables)

## Franchises

`GET https://statsapi.web.nhl.com/api/v1/franchises` | Returns a list of franchises

`GET https://statsapi.web.nhl.com/api/v1/franchises/ID` | Gets information on a specific franchise

[back to top](#endpoint-tables)

## Tournaments

`GET https://statsapi.web.nhl.com/api/v1/tournamentTypes` | Gets the possible different tournament types.

`GET https://statsapi.web.nhl.com/api/v1/tournaments/playoffs` | This is used for tracking nested tournaments, specifically the Playoffs due to the nature of their structure.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2019. All Rights Reserved.",
  "id" : 1,
  "name" : "Playoffs",
  "season" : "20182019",
  "defaultRound" : 1,
  "rounds" : [ {
    "number" : 1,
    "code" : 1,
    "names" : {
      "name" : "First Round",
      "shortName" : "R1"
    },
    "format" : {
      "name" : "BO7",
      "description" : "Best of 7",
      "numberOfGames" : 7,
      "numberOfWins" : 4
    }
  }, {
    "number" : 2,
    "code" : 2,
    "names" : {
      "name" : "Second Round",
      "shortName" : "R2"
    },
    "format" : {
      "name" : "BO7",
      "description" : "Best of 7",
      "numberOfGames" : 7,
      "numberOfWins" : 4
    }
  }, {
    "number" : 3,
    "code" : 3,
    "names" : {
      "name" : "Conference Finals",
      "shortName" : "CF"
    },
    "format" : {
      "name" : "BO7",
      "description" : "Best of 7",
      "numberOfGames" : 7,
      "numberOfWins" : 4
    }
  }, {
    "number" : 4,
    "code" : 4,
    "names" : {
      "name" : "Stanley Cup Final",
      "shortName" : "SCF"
    },
    "format" : {
      "name" : "BO7",
      "description" : "Best of 7",
      "numberOfGames" : 7,
      "numberOfWins" : 4
    }
  } ]
}
```
<br /></details>

In order to get additional information the expand modifier can be used such as this example

`?expand=round.series,schedule.game.seriesSummary&season=20182019` | This will add in details like the game summary and the season

[back to top](#endpoint-tables)

## Venues

`GET https://statsapi.web.nhl.com/api/v1/venues` | Get all NHL Venues in API database.

`GET https://statsapi.web.nhl.com/api/v1/venues/ID` | Get an NHL Venue.

<details>
  <summary>click for example</summary>

```json
{
  "copyright": "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2019. All Rights Reserved.",
  "venues": [
    {
      "id": 5064,
      "name": "Pepsi Center",
      "link": "/api/v1/venues/5064",
      "appEnabled": true
    }
  ]
}
```
<br /></details>

[back to top](#endpoint-tables)


# Game endpoints

### Game IDs
>will look like this: 2023020001
>
> The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). Always refer to a season with the starting year. A game played in March 2018 would still have a game ID that starts with 2017
>
> The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star
>
>  The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played. (1353 for seasons with 32 teams (2022 - Present), 1271 for seasons with 31 teams (2017 - 2020) and 1230 for seasons with 30 teams). For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).

[back to top](#endpoint-tables)

## Games
`GET https://statsapi.web.nhl.com/api/v1/game/ID/feed/live` | Returns all data about a specified game id including play data with on-ice coordinates and post-game details like first, second and third stars and any details about shootouts. The data returned is simply too large at often over 30k lines and is best explored with a JSON viewer.

`GET https://statsapi.web.nhl.com/api/v1/game/ID/boxscore` | Returns far less detail
than `feed/live` | and is much more suitable for post-game details including goals,
shots, PIMs, blocked, takeaways, giveaways and hits.

`GET https://statsapi.web.nhl.com/api/v1/game/ID/linescore` | Even fewer details than
boxscore. Has goals, shots on goal, powerplay and goalie pulled status, number of
skaters and shootout information if applicable

`GET http://statsapi.web.nhl.com/api/v1/game/ID/content` | Complex endpoint returning
multiple types of media relating to the game including videos of shots, goals and saves.

`GET https://statsapi.web.nhl.com/api/v1/game/ID/feed/live/diffPatch?startTimecode=yyyymmdd_hhmmss` | Returns updates (like new play events, updated stats for boxscore, etc.) for the specified game ID
since the given startTimecode. If the startTimecode param is missing, returns an empty array.

[back to top](#endpoint-tables)

## Game Status

`GET https://statsapi.web.nhl.com/api/v1/gameStatus` | Returns a list of game status values

[back to top](#endpoint-tables)

## Game Types

`GET https://statsapi.web.nhl.com/api/v1/gameTypes` | Returns list of game types with description and post-season status

[back to top](#endpoint-tables)

## Play Types

`GET https://statsapi.web.nhl.com/api/v1/playTypes` | This shows all the possible play types found within the liveData/plays portion of the game feed

[Back to top](#endpoint-tables)
<br />
<br />
<br />

# Player endpoints

## Draft

`GET https://statsapi.web.nhl.com/api/v1/draft` | Get round-by-round data for current year's NHL Entry Draft.

`GET https://statsapi.web.nhl.com/api/v1/draft/YEAR` | Takes a YYYY format year and returns draft data

<details>
  <summary>click for example</summary>

```json
{
  "copyright": "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "drafts": [{
    "draftYear": 2017,
    "rounds": [{
      "roundNumber": 1,
      "round": "1",
      "picks": [{
        "year": 2017,
        "round": "1",
        "pickOverall": 1,
        "pickInRound": 1,
        "team": {
          "id": 1,
          "name": "New Jersey Devils",
          "link": "/api/v1/teams/1"
        },
        "prospect": {
          "id": 65242,
          "fullName": "Nico Hischier",
          "link": "/api/v1/draft/prospects/65242"
        }
      },
```
<br /></details>

[back to top](#endpoint-tables)

## Players

`GET https://statsapi.web.nhl.com/api/v1/people/ID` | Gets details for a player, must
specify the id value in order to return data.
<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "people" : [ {
    "id" : 8477474,
    "fullName" : "Madison Bowey",
    "link" : "/api/v1/people/8477474",
    "firstName" : "Madison",
    "lastName" : "Bowey",
    "primaryNumber" : "22",
    "birthDate" : "1995-04-22",
    "currentAge" : 22,
    "birthCity" : "Winnipeg",
    "birthStateProvince" : "MB",
    "birthCountry" : "CAN",
    "nationality" : "CAN",
    "height" : "6' 2\"",
    "weight" : 198,
    "active" : true,
    "alternateCaptain" : false,
    "captain" : false,
    "rookie" : true,
    "shootsCatches" : "R",
    "rosterStatus" : "Y",
    "currentTeam" : {
      "id" : 15,
      "name" : "Washington Capitals",
      "link" : "/api/v1/teams/15"
    },
    "primaryPosition" : {
      "code" : "D",
      "name" : "Defenseman",
      "type" : "Defenseman",
      "abbreviation" : "D"
    }
  } ]
}
```
<br /></details>
<br />


`GET https://statsapi.web.nhl.com/api/v1/people/ID/stats` | Complex endpoint with
lots of append options to change what kind of stats you wish to obtain

`GET https://statsapi.web.nhl.com/api/v1/positions` | Simple endpoint that
obtains an array of eligible positions in the NHL

#### Player Stat Modifiers

`?stats=statsSingleSeason&season=19801981` | Obtains single season statistics
for a player

>note - stats have changed over the years, the below sample is for Wayne Gretzky
and does not include things like evenTimeOnIce and other time related stats
<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "statsSingleSeason"
    },
    "splits" : [ {
      "season" : "19801981",
      "stat" : {
        "assists" : 109,
        "goals" : 55,
        "pim" : 28,
        "shots" : 261,
        "games" : 80,
        "powerPlayGoals" : 15,
        "powerPlayPoints" : 53,
        "penaltyMinutes" : "28",
        "shotPct" : 21.07,
        "gameWinningGoals" : 3,
        "overTimeGoals" : 0,
        "shortHandedGoals" : 4,
        "shortHandedPoints" : 7,
        "plusMinus" : 41,
        "points" : 164
      }
    } ]
  } ]
}
```
<br /></details>

> however here is Alex Ovechkin's 20162017 season stats which include time information

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "statsSingleSeason"
    },
    "splits" : [ {
      "season" : "20162017",
      "stat" : {
        "timeOnIce" : "1506:01",
        "assists" : 36,
        "goals" : 33,
        "pim" : 50,
        "shots" : 313,
        "games" : 82,
        "hits" : 216,
        "powerPlayGoals" : 17,
        "powerPlayPoints" : 26,
        "powerPlayTimeOnIce" : "305:21",
        "evenTimeOnIce" : "1198:26",
        "penaltyMinutes" : "50",
        "faceOffPct" : 0.0,
        "shotPct" : 10.5,
        "gameWinningGoals" : 7,
        "overTimeGoals" : 2,
        "shortHandedGoals" : 0,
        "shortHandedPoints" : 0,
        "shortHandedTimeOnIce" : "02:14",
        "blocked" : 29,
        "plusMinus" : 6,
        "points" : 69,
        "shifts" : 1737,
        "timeOnIcePerGame" : "18:21",
        "evenTimeOnIcePerGame" : "14:36",
        "shortHandedTimeOnIcePerGame" : "00:01",
        "powerPlayTimeOnIcePerGame" : "03:43"
      }
    } ]
  } ]
}

```
<br /></details>

`?stats=yearByYear` | Provides a list of every season for a player's career

<details>
  <summary>click for example</summary>

```json
// https://statsapi.web.nhl.com/api/v1/people/8474141/stats?stats=yearByYear
// Patrick Kane

{
    "copyright": "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2023. All Rights Reserved.",
    "stats": [
        {
            "type": {
                "displayName": "yearByYear",
                "gameType": null
            },
            "splits": [
                {
                    "season": "20032004",
                    "stat": {
                        "assists": 77,
                        "goals": 83,
                        "games": 70,
                        "points": 160
                    },
                    "team": {
                        "name": "Det. Honeybaked",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "MWEHL",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20042005",
                    "stat": {
                        "assists": 17,
                        "goals": 16,
                        "pim": 8,
                        "games": 23,
                        "penaltyMinutes": "8",
                        "points": 33
                    },
                    "team": {
                        "name": "USNTDP",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "U-17",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20042005",
                    "stat": {
                        "assists": 21,
                        "goals": 16,
                        "pim": 8,
                        "games": 40,
                        "powerPlayGoals": 5,
                        "penaltyMinutes": "8",
                        "gameWinningGoals": 1,
                        "shortHandedGoals": 0,
                        "plusMinus": 0,
                        "points": 37
                    },
                    "team": {
                        "name": "USNTDP",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "id": 211,
                        "name": "NAHL",
                        "link": "/api/v1/league/211"
                    },
                    "sequenceNumber": 2
                },
                {
                    "season": "20052006",
                    "stat": {
                        "assists": 33,
                        "goals": 35,
                        "pim": 10,
                        "games": 43,
                        "penaltyMinutes": "10",
                        "points": 68
                    },
                    "team": {
                        "name": "USNTDP",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "U-18",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20052006",
                    "stat": {
                        "assists": 17,
                        "goals": 17,
                        "pim": 12,
                        "games": 15,
                        "powerPlayGoals": 7,
                        "penaltyMinutes": "12",
                        "gameWinningGoals": 2,
                        "shortHandedGoals": 1,
                        "points": 34
                    },
                    "team": {
                        "name": "USNTDP",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "id": 211,
                        "name": "NAHL",
                        "link": "/api/v1/league/211"
                    },
                    "sequenceNumber": 2
                },
                {
                    "season": "20052006",
                    "stat": {
                        "assists": 5,
                        "goals": 7,
                        "pim": 2,
                        "games": 6,
                        "penaltyMinutes": "2",
                        "faceOffPct": 0.0,
                        "points": 12
                    },
                    "team": {
                        "id": 67,
                        "name": "United States",
                        "link": "/api/v1/teams/67"
                    },
                    "league": {
                        "id": 147,
                        "name": "WJ18-A",
                        "link": "/api/v1/league/147"
                    },
                    "sequenceNumber": 3
                },
                {
                    "season": "20062007",
                    "stat": {
                        "assists": 83,
                        "goals": 62,
                        "pim": 52,
                        "games": 58,
                        "powerPlayGoals": 22,
                        "penaltyMinutes": "52",
                        "shortHandedGoals": 4,
                        "plusMinus": 42,
                        "points": 145
                    },
                    "team": {
                        "id": 1876,
                        "name": "London",
                        "link": "/api/v1/teams/1876"
                    },
                    "league": {
                        "id": 141,
                        "name": "OHL",
                        "link": "/api/v1/league/141"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20062007",
                    "stat": {
                        "assists": 4,
                        "goals": 5,
                        "pim": 42,
                        "games": 7,
                        "powerPlayGoals": 0,
                        "penaltyMinutes": "42",
                        "shortHandedGoals": 0,
                        "plusMinus": 2,
                        "points": 9
                    },
                    "team": {
                        "id": 67,
                        "name": "United States",
                        "link": "/api/v1/teams/67"
                    },
                    "league": {
                        "id": 147,
                        "name": "WJC-A",
                        "link": "/api/v1/league/147"
                    },
                    "sequenceNumber": 2
                },
                {
                    "season": "20072008",
                    "stat": {
                        "timeOnIce": "1505:59",
                        "assists": 51,
                        "goals": 21,
                        "pim": 52,
                        "shots": 191,
                        "games": 82,
                        "hits": 16,
                        "powerPlayGoals": 7,
                        "powerPlayPoints": 28,
                        "powerPlayTimeOnIce": "323:30",
                        "evenTimeOnIce": "1174:10",
                        "penaltyMinutes": "52",
                        "faceOffPct": 61.54,
                        "shotPct": 10.99,
                        "gameWinningGoals": 4,
                        "overTimeGoals": 1,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "08:19",
                        "blocked": 7,
                        "plusMinus": -5,
                        "points": 72,
                        "shifts": 1838
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20072008",
                    "stat": {
                        "timeOnIce": "00:00",
                        "assists": 7,
                        "goals": 3,
                        "pim": 0,
                        "games": 7,
                        "powerPlayTimeOnIce": "00:00",
                        "evenTimeOnIce": "00:00",
                        "penaltyMinutes": "0",
                        "faceOffPct": 0.0,
                        "shortHandedTimeOnIce": "00:00",
                        "points": 10,
                        "shifts": 0
                    },
                    "team": {
                        "id": 67,
                        "name": "United States",
                        "link": "/api/v1/teams/67"
                    },
                    "league": {
                        "id": 147,
                        "name": "WC-A",
                        "link": "/api/v1/league/147"
                    },
                    "sequenceNumber": 3
                },
                {
                    "season": "20082009",
                    "stat": {
                        "timeOnIce": "1492:40",
                        "assists": 45,
                        "goals": 25,
                        "pim": 42,
                        "shots": 254,
                        "games": 80,
                        "hits": 19,
                        "powerPlayGoals": 13,
                        "powerPlayPoints": 35,
                        "powerPlayTimeOnIce": "334:23",
                        "evenTimeOnIce": "1154:03",
                        "penaltyMinutes": "42",
                        "faceOffPct": 41.94,
                        "shotPct": 9.84,
                        "gameWinningGoals": 4,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "04:14",
                        "blocked": 9,
                        "plusMinus": -2,
                        "points": 70,
                        "shifts": 1867
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20092010",
                    "stat": {
                        "timeOnIce": "1574:06",
                        "assists": 58,
                        "goals": 30,
                        "pim": 20,
                        "shots": 261,
                        "games": 82,
                        "hits": 17,
                        "powerPlayGoals": 9,
                        "powerPlayPoints": 29,
                        "powerPlayTimeOnIce": "265:32",
                        "evenTimeOnIce": "1297:58",
                        "penaltyMinutes": "20",
                        "faceOffPct": 40.91,
                        "shotPct": 11.49,
                        "gameWinningGoals": 6,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 1,
                        "shortHandedTimeOnIce": "10:36",
                        "blocked": 17,
                        "plusMinus": 16,
                        "points": 88,
                        "shifts": 1908
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20092010",
                    "stat": {
                        "assists": 2,
                        "goals": 3,
                        "pim": 2,
                        "games": 6,
                        "penaltyMinutes": "2",
                        "faceOffPct": 0.0,
                        "points": 5
                    },
                    "team": {
                        "id": 67,
                        "name": "U.S.A.",
                        "link": "/api/v1/teams/67"
                    },
                    "league": {
                        "id": 147,
                        "name": "Olympics",
                        "link": "/api/v1/league/147"
                    },
                    "sequenceNumber": 3
                },
                {
                    "season": "20102011",
                    "stat": {
                        "timeOnIce": "1407:47",
                        "assists": 46,
                        "goals": 27,
                        "pim": 28,
                        "shots": 216,
                        "games": 73,
                        "hits": 17,
                        "powerPlayGoals": 5,
                        "powerPlayPoints": 24,
                        "powerPlayTimeOnIce": "236:48",
                        "evenTimeOnIce": "1167:10",
                        "penaltyMinutes": "28",
                        "faceOffPct": 14.29,
                        "shotPct": 12.5,
                        "gameWinningGoals": 2,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "03:49",
                        "blocked": 17,
                        "plusMinus": 7,
                        "points": 73,
                        "shifts": 1749
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20112012",
                    "stat": {
                        "timeOnIce": "1656:12",
                        "assists": 43,
                        "goals": 23,
                        "pim": 40,
                        "shots": 253,
                        "games": 82,
                        "hits": 19,
                        "powerPlayGoals": 4,
                        "powerPlayPoints": 12,
                        "powerPlayTimeOnIce": "284:06",
                        "evenTimeOnIce": "1366:03",
                        "penaltyMinutes": "40",
                        "faceOffPct": 42.18,
                        "shotPct": 9.09,
                        "gameWinningGoals": 5,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "06:03",
                        "blocked": 27,
                        "plusMinus": 7,
                        "points": 66,
                        "shifts": 2001
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20122013",
                    "stat": {
                        "timeOnIce": "942:38",
                        "assists": 32,
                        "goals": 23,
                        "pim": 8,
                        "shots": 138,
                        "games": 47,
                        "hits": 11,
                        "powerPlayGoals": 8,
                        "powerPlayPoints": 17,
                        "powerPlayTimeOnIce": "139:05",
                        "evenTimeOnIce": "803:09",
                        "penaltyMinutes": "8",
                        "faceOffPct": 20.0,
                        "shotPct": 16.67,
                        "gameWinningGoals": 3,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "00:24",
                        "blocked": 9,
                        "plusMinus": 11,
                        "points": 55,
                        "shifts": 1088
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20122013",
                    "stat": {
                        "assists": 10,
                        "goals": 13,
                        "pim": 6,
                        "games": 20,
                        "penaltyMinutes": "6",
                        "points": 23
                    },
                    "team": {
                        "id": 5816,
                        "name": "Biel",
                        "link": "/api/v1/teams/5816"
                    },
                    "league": {
                        "id": 293,
                        "name": "Swiss",
                        "link": "/api/v1/league/293"
                    },
                    "sequenceNumber": 2
                },
                {
                    "season": "20132014",
                    "stat": {
                        "timeOnIce": "1353:06",
                        "assists": 40,
                        "goals": 29,
                        "pim": 22,
                        "shots": 227,
                        "games": 69,
                        "hits": 16,
                        "powerPlayGoals": 10,
                        "powerPlayPoints": 25,
                        "powerPlayTimeOnIce": "228:07",
                        "evenTimeOnIce": "1124:01",
                        "penaltyMinutes": "22",
                        "faceOffPct": 50.0,
                        "shotPct": 12.78,
                        "gameWinningGoals": 6,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "00:58",
                        "blocked": 15,
                        "plusMinus": 7,
                        "points": 69,
                        "shifts": 1578
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20132014",
                    "stat": {
                        "assists": 4,
                        "goals": 0,
                        "pim": 6,
                        "shots": 19,
                        "games": 6,
                        "powerPlayGoals": 0,
                        "penaltyMinutes": "6",
                        "gameWinningGoals": 0,
                        "shortHandedGoals": 0,
                        "plusMinus": 2,
                        "points": 4
                    },
                    "team": {
                        "id": 67,
                        "name": "U.S.A.",
                        "link": "/api/v1/teams/67"
                    },
                    "league": {
                        "id": 147,
                        "name": "Olympics",
                        "link": "/api/v1/league/147"
                    },
                    "sequenceNumber": 2
                },
                {
                    "season": "20142015",
                    "stat": {
                        "timeOnIce": "1210:54",
                        "assists": 37,
                        "goals": 27,
                        "pim": 10,
                        "shots": 186,
                        "games": 61,
                        "hits": 22,
                        "powerPlayGoals": 6,
                        "powerPlayPoints": 22,
                        "powerPlayTimeOnIce": "224:20",
                        "evenTimeOnIce": "984:07",
                        "penaltyMinutes": "10",
                        "faceOffPct": 42.86,
                        "shotPct": 14.52,
                        "gameWinningGoals": 5,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "02:27",
                        "blocked": 14,
                        "plusMinus": 10,
                        "points": 64,
                        "shifts": 1398
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20152016",
                    "stat": {
                        "timeOnIce": "1673:39",
                        "assists": 60,
                        "goals": 46,
                        "pim": 30,
                        "shots": 287,
                        "games": 82,
                        "hits": 37,
                        "powerPlayGoals": 17,
                        "powerPlayPoints": 37,
                        "powerPlayTimeOnIce": "256:30",
                        "evenTimeOnIce": "1413:30",
                        "penaltyMinutes": "30",
                        "faceOffPct": 21.57,
                        "shotPct": 16.03,
                        "gameWinningGoals": 9,
                        "overTimeGoals": 1,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "03:39",
                        "blocked": 21,
                        "plusMinus": 17,
                        "points": 106,
                        "shifts": 1967
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20162017",
                    "stat": {
                        "timeOnIce": "1754:23",
                        "assists": 55,
                        "goals": 34,
                        "pim": 32,
                        "shots": 292,
                        "games": 82,
                        "hits": 28,
                        "powerPlayGoals": 7,
                        "powerPlayPoints": 23,
                        "powerPlayTimeOnIce": "279:02",
                        "evenTimeOnIce": "1469:07",
                        "penaltyMinutes": "32",
                        "faceOffPct": 13.73,
                        "shotPct": 11.64,
                        "gameWinningGoals": 5,
                        "overTimeGoals": 1,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "06:14",
                        "blocked": 15,
                        "plusMinus": 11,
                        "points": 89,
                        "shifts": 1910
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20162017",
                    "stat": {
                        "assists": 2,
                        "goals": 0,
                        "pim": 0,
                        "games": 3,
                        "penaltyMinutes": "0",
                        "plusMinus": -4,
                        "points": 2
                    },
                    "team": {
                        "name": "USA",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "WCup",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 17286
                },
                {
                    "season": "20172018",
                    "stat": {
                        "timeOnIce": "1655:18",
                        "assists": 49,
                        "goals": 27,
                        "pim": 32,
                        "shots": 285,
                        "games": 82,
                        "hits": 18,
                        "powerPlayGoals": 5,
                        "powerPlayPoints": 22,
                        "powerPlayTimeOnIce": "279:27",
                        "evenTimeOnIce": "1369:52",
                        "penaltyMinutes": "32",
                        "faceOffPct": 38.89,
                        "shotPct": 9.47,
                        "gameWinningGoals": 4,
                        "overTimeGoals": 2,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "05:59",
                        "blocked": 14,
                        "plusMinus": -20,
                        "points": 76,
                        "shifts": 1872
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20172018",
                    "stat": {
                        "assists": 12,
                        "goals": 8,
                        "pim": 0,
                        "games": 10,
                        "penaltyMinutes": "0",
                        "plusMinus": -2,
                        "points": 20
                    },
                    "team": {
                        "name": "USA",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "WC",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 17215
                },
                {
                    "season": "20182019",
                    "stat": {
                        "timeOnIce": "1821:37",
                        "assists": 66,
                        "goals": 44,
                        "pim": 22,
                        "shots": 341,
                        "games": 81,
                        "hits": 21,
                        "powerPlayGoals": 9,
                        "powerPlayPoints": 30,
                        "powerPlayTimeOnIce": "300:43",
                        "evenTimeOnIce": "1516:46",
                        "penaltyMinutes": "22",
                        "faceOffPct": 20.0,
                        "shotPct": 12.9,
                        "gameWinningGoals": 7,
                        "overTimeGoals": 3,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "04:08",
                        "blocked": 18,
                        "plusMinus": 2,
                        "points": 110,
                        "shifts": 1912
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20182019",
                    "stat": {
                        "assists": 10,
                        "goals": 2,
                        "pim": 4,
                        "games": 8,
                        "penaltyMinutes": "4",
                        "plusMinus": 0,
                        "points": 12
                    },
                    "team": {
                        "name": "USA",
                        "link": "/api/v1/teams/null"
                    },
                    "league": {
                        "name": "WC",
                        "link": "/api/v1/league/null"
                    },
                    "sequenceNumber": 17215
                },
                {
                    "season": "20192020",
                    "stat": {
                        "timeOnIce": "1493:51",
                        "assists": 51,
                        "goals": 33,
                        "pim": 40,
                        "shots": 275,
                        "games": 70,
                        "hits": 24,
                        "powerPlayGoals": 8,
                        "powerPlayPoints": 23,
                        "powerPlayTimeOnIce": "259:35",
                        "evenTimeOnIce": "1232:01",
                        "penaltyMinutes": "40",
                        "faceOffPct": 25.0,
                        "shotPct": 12.0,
                        "gameWinningGoals": 2,
                        "overTimeGoals": 1,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "02:15",
                        "blocked": 19,
                        "plusMinus": 8,
                        "points": 84,
                        "shifts": 1558
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20202021",
                    "stat": {
                        "timeOnIce": "1244:52",
                        "assists": 51,
                        "goals": 15,
                        "pim": 14,
                        "shots": 191,
                        "games": 56,
                        "hits": 13,
                        "powerPlayGoals": 3,
                        "powerPlayPoints": 22,
                        "powerPlayTimeOnIce": "219:37",
                        "evenTimeOnIce": "1022:40",
                        "penaltyMinutes": "14",
                        "faceOffPct": 28.57,
                        "shotPct": 7.9,
                        "gameWinningGoals": 3,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "02:35",
                        "blocked": 15,
                        "plusMinus": -7,
                        "points": 66,
                        "shifts": 1246
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20212022",
                    "stat": {
                        "timeOnIce": "1702:13",
                        "assists": 66,
                        "goals": 26,
                        "pim": 18,
                        "shots": 287,
                        "games": 78,
                        "hits": 11,
                        "powerPlayGoals": 9,
                        "powerPlayPoints": 31,
                        "powerPlayTimeOnIce": "295:26",
                        "evenTimeOnIce": "1404:41",
                        "penaltyMinutes": "18",
                        "faceOffPct": 50.0,
                        "shotPct": 9.1,
                        "gameWinningGoals": 2,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "02:06",
                        "blocked": 26,
                        "plusMinus": -19,
                        "points": 92,
                        "shifts": 1798
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20222023",
                    "stat": {
                        "timeOnIce": "1077:15",
                        "assists": 29,
                        "goals": 16,
                        "pim": 10,
                        "shots": 182,
                        "games": 54,
                        "hits": 10,
                        "powerPlayGoals": 2,
                        "powerPlayPoints": 18,
                        "powerPlayTimeOnIce": "194:58",
                        "evenTimeOnIce": "881:45",
                        "penaltyMinutes": "10",
                        "faceOffPct": 100.0,
                        "shotPct": 8.79,
                        "gameWinningGoals": 0,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "00:32",
                        "blocked": 10,
                        "plusMinus": -23,
                        "points": 45,
                        "shifts": 1115
                    },
                    "team": {
                        "id": 16,
                        "name": "Chicago Blackhawks",
                        "link": "/api/v1/teams/16"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 1
                },
                {
                    "season": "20222023",
                    "stat": {
                        "timeOnIce": "332:17",
                        "assists": 7,
                        "goals": 5,
                        "pim": 6,
                        "shots": 45,
                        "games": 19,
                        "hits": 3,
                        "powerPlayGoals": 2,
                        "powerPlayPoints": 4,
                        "powerPlayTimeOnIce": "54:40",
                        "evenTimeOnIce": "277:22",
                        "penaltyMinutes": "6",
                        "faceOffPct": 0.0,
                        "shotPct": 11.11,
                        "gameWinningGoals": 1,
                        "overTimeGoals": 0,
                        "shortHandedGoals": 0,
                        "shortHandedPoints": 0,
                        "shortHandedTimeOnIce": "00:15",
                        "blocked": 9,
                        "plusMinus": 1,
                        "points": 12,
                        "shifts": 353
                    },
                    "team": {
                        "id": 3,
                        "name": "New York Rangers",
                        "link": "/api/v1/teams/3"
                    },
                    "league": {
                        "id": 133,
                        "name": "National Hockey League",
                        "link": "/api/v1/league/133"
                    },
                    "sequenceNumber": 2
                }
            ]
        }
    ]
}
```
<br /></details>

`?stats=homeAndAway&season=20162017` | Provides a split between home and away games.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "homeAndAway"
    },
    "splits" : [ {
      "season" : "20162017",
      "stat" : {
        "timeOnIce" : "751:09",
        "assists" : 18,
        "goals" : 20,
        "pim" : 26,
        "shots" : 163,
        "games" : 41,
        "hits" : 97,
        "powerPlayGoals" : 10,
        "powerPlayPoints" : 15,
        "powerPlayTimeOnIce" : "160:21",
        "evenTimeOnIce" : "590:34",
        "penaltyMinutes" : "26",
        "shotPct" : 0.0,
        "gameWinningGoals" : 6,
        "overTimeGoals" : 2,
        "shortHandedGoals" : 0,
        "shortHandedPoints" : 0,
        "shortHandedTimeOnIce" : "00:14",
        "blocked" : 12,
        "plusMinus" : 13,
        "points" : 38,
        "shifts" : 848,
        "timeOnIcePerGame" : "18:19",
        "evenTimeOnIcePerGame" : "14:24",
        "shortHandedTimeOnIcePerGame" : "00:00",
        "powerPlayTimeOnIcePerGame" : "03:54"
      },
      "isHome" : true
    }, {
      "season" : "20162017",
      "stat" : {
        "timeOnIce" : "754:52",
        "assists" : 18,
        "goals" : 13,
        "pim" : 24,
        "shots" : 150,
        "games" : 41,
        "hits" : 119,
        "powerPlayGoals" : 7,
        "powerPlayPoints" : 11,
        "powerPlayTimeOnIce" : "145:00",
        "evenTimeOnIce" : "607:52",
        "penaltyMinutes" : "24",
        "shotPct" : 0.0,
        "gameWinningGoals" : 1,
        "overTimeGoals" : 0,
        "shortHandedGoals" : 0,
        "shortHandedPoints" : 0,
        "shortHandedTimeOnIce" : "02:00",
        "blocked" : 17,
        "plusMinus" : -7,
        "points" : 31,
        "shifts" : 889,
        "timeOnIcePerGame" : "18:24",
        "evenTimeOnIcePerGame" : "14:49",
        "shortHandedTimeOnIcePerGame" : "00:02",
        "powerPlayTimeOnIcePerGame" : "03:32"
      },
      "isHome" : false
    } ]
  } ]
}
```
<br /></details>

`?stats=winLoss&season=20162017` | Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away

`?stats=byMonth&season=20162017` | Monthly split of stats

`?stats=byDayOfWeek&season=20162017` | Split done by day of the week

`?stats=vsDivision&season=20162017` | Division stats split

`?stats=vsConference&season=20162017` | Conference stats split

`?stats=vsTeam&season=20162017` | Conference stats split

`?stats=gameLog&season=20162017` | Provides a game log showing stats for each game of a season

`?stats=regularSeasonStatRankings&season=20162017` | Returns where someone stands vs
the rest of the league for a specific regularSeasonStatRankings

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "regularSeasonStatRankings"
    },
    "splits" : [ {
      "season" : "20162017",
      "stat" : {
        "rankPowerPlayGoals" : "1st",
        "rankBlockedShots" : "405th",
        "rankAssists" : "51st",
        "rankShotPct" : "246th",
        "rankGoals" : "13th",
        "rankHits" : "19th",
        "rankPenaltyMinutes" : "111th",
        "rankShortHandedGoals" : "133rd",
        "rankPlusMinus" : "176th",
        "rankShots" : "2nd",
        "rankPoints" : "20th",
        "rankOvertimeGoals" : "9th",
        "rankGamesPlayed" : "1st"
      }
    } ]
  } ]
}
```
<br /></details>

`?stats=goalsByGameSituation&season=20162017` | Shows number on when goals for a
player happened like how many in the shootout, how many in each period, etc.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "goalsByGameSituation"
    },
    "splits" : [ {
      "season" : "20162017",
      "stat" : {
        "goalsInFirstPeriod" : 8,
        "goalsInSecondPeriod" : 12,
        "goalsInThirdPeriod" : 11,
        "goalsInOvertime" : 2,
        "gameWinningGoals" : 7,
        "emptyNetGoals" : 0,
        "shootOutGoals" : 0,
        "shootOutShots" : 3,
        "goalsTrailingByOne" : 3,
        "goalsTrailingByTwo" : 3,
        "goalsTrailingByThreePlus" : 1,
        "goalsWhenTied" : 14,
        "goalsLeadingByOne" : 7,
        "goalsLeadingByTwo" : 4,
        "goalsLeadingByThreePlus" : 1,
        "penaltyGoals" : 0,
        "penaltyShots" : 0
      }
    } ]
  } ]
}
```
<br /></details>

`?stats=onPaceRegularSeason&season=20172018` | This only works with the current
in-progress season and shows **projected** totals based on current onPaceRegularSeason

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "onPaceRegularSeason"
    },
    "splits" : [ {
      "season" : "20172018",
      "stat" : {
        "timeOnIce" : "1598:04",
        "assists" : 34,
        "goals" : 52,
        "pim" : 32,
        "shots" : 362,
        "games" : 82,
        "hits" : 154,
        "powerPlayGoals" : 14,
        "powerPlayPoints" : 28,
        "powerPlayTimeOnIce" : "338:16",
        "evenTimeOnIce" : "1258:48",
        "penaltyMinutes" : "32",
        "faceOffPct" : 40.0,
        "shotPct" : 14.4,
        "gameWinningGoals" : 10,
        "overTimeGoals" : 6,
        "shortHandedGoals" : 0,
        "shortHandedPoints" : 0,
        "shortHandedTimeOnIce" : "01:00",
        "blocked" : 20,
        "plusMinus" : 24,
        "points" : 86,
        "shifts" : 1676,
        "timeOnIcePerGame" : "09:44",
        "evenTimeOnIcePerGame" : "07:40",
        "powerPlayTimeOnIcePerGame" : "02:03"
      }
    } ]
  } ]
}
```

<br /></details>

[back to top](#endpoint-tables)



## Prospects

`GET https://statsapi.web.nhl.com/api/v1/draft/prospects` | Get all NHL Entry Draft prospects.

`GET https://statsapi.web.nhl.com/api/v1/draft/prospects/ID` | Get an NHL Entry Draft prospect.

<br /></details>

<details>
<summary>click for example</summary>

```json
{
  "copyright": "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "prospects": [
    {
      "id": 53727,
      "fullName": "Zbynek Horak",
      "link": "/api/v1/draft/prospects/53727",
      "firstName": "Zbynek",
      "lastName": "Horak",
      "birthDate": "1995-03-08",
      "birthCountry": "CZE",
      "height": "5' 10\"",
      "weight": 168,
      "shootsCatches": "L",
      "primaryPosition": {
        "code": "L",
        "name": "Left Wing",
        "type": "Forward",
        "abbreviation": "LW"
      },
      "draftStatus": "Elig",
      "prospectCategory": {
        "id": 2,
        "shortName": "Euro Skater",
        "name": "European Skater"
      },
      "amateurTeam": {
        "name": "Znojmo Jr.",
        "link": "/api/v1/teams/null"
      },
      "amateurLeague": {
        "name": "AUSTRIA-JR.",
        "link": "/api/v1/league/null"
      },
      "ranks": {}
    }
  ]
}
```
<br />

</details>

[back to top](#endpoint-tables)

# Schedule endpoints

## Schedule

`GET https://statsapi.web.nhl.com/api/v1/schedule` | Returns a list of data about the schedule for a specified date range. If no date range is specified, returns results from the current day.

>Note: Without any flags or modifiers this endpoint will NOT return pre-season games that occur on the current day.
>
>In order for pre-season games to show up the date must be specified as show below in the Modifiers section


#### Schedule Modifiers

`?expand=schedule.broadcasts` | Shows the broadcasts of the game

`?expand=schedule.linescore` | Linescore for completed games

`?expand=schedule.ticket` | Provides the different places to buy tickets for the upcoming games

`?teamId=30,17` | Limit results to a specific team(s). Team ids can be found through the teams endpoint

`?date=2018-01-09` | Single defined date for the search

`?startDate=2018-01-09` | Start date for the search

`?endDate=2018-01-12` | End date for the search

`?season=20172018` | Returns all games from specified season

`?gameType=R` | Restricts results to only regular season games. Can be set to any value from [Game Types](#game-types) endpoint

`GET https://statsapi.web.nhl.com/api/v1/schedule?teamId=30` | Returns Minnesota Wild games for the current day.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "totalItems" : 1,
  "totalEvents" : 0,
  "totalGames" : 1,
  "totalMatches" : 0,
  "wait" : 10,
  "dates" : [ {
    "date" : "2018-01-09",
    "totalItems" : 1,
    "totalEvents" : 0,
    "totalGames" : 1,
    "totalMatches" : 0,
    "games" : [ {
      "gamePk" : 2017020659,
      "link" : "/api/v1/game/2017020659/feed/live",
      "gameType" : "R",
      "season" : "20172018",
      "gameDate" : "2018-01-10T01:00:00Z",
      "status" : {
        "abstractGameState" : "Preview",
        "codedGameState" : "1",
        "detailedState" : "Scheduled",
        "statusCode" : "1",
        "startTimeTBD" : false
      },
      "teams" : {
        "away" : {
          "leagueRecord" : {
            "wins" : 21,
            "losses" : 16,
            "ot" : 4,
            "type" : "league"
          },
          "score" : 0,
          "team" : {
            "id" : 20,
            "name" : "Calgary Flames",
            "link" : "/api/v1/teams/20"
          }
        },
        "home" : {
          "leagueRecord" : {
            "wins" : 22,
            "losses" : 17,
            "ot" : 3,
            "type" : "league"
          },
          "score" : 0,
          "team" : {
            "id" : 30,
            "name" : "Minnesota Wild",
            "link" : "/api/v1/teams/30"
          }
        }
      },
      "venue" : {
        "name" : "Xcel Energy Center",
        "link" : "/api/v1/venues/null"
      },
      "content" : {
        "link" : "/api/v1/game/2017020659/content"
      }
    } ],
    "events" : [ ],
    "matches" : [ ]
  } ]
}
```
<br /></details>
<br />

`GET https://statsapi.web.nhl.com/api/v1/schedule?teamId=30&startDate=2018-01-02&endDate=2018-01-02` | Returns Minnesota Wild games for January 2, 2018 with attached linescores and broadcasts.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "totalItems" : 1,
  "totalEvents" : 0,
  "totalGames" : 1,
  "totalMatches" : 0,
  "wait" : 10,
  "dates" : [ {
    "date" : "2018-01-02",
    "totalItems" : 1,
    "totalEvents" : 0,
    "totalGames" : 1,
    "totalMatches" : 0,
    "games" : [ {
      "gamePk" : 2017020608,
      "link" : "/api/v1/game/2017020608/feed/live",
      "gameType" : "R",
      "season" : "20172018",
      "gameDate" : "2018-01-03T01:00:00Z",
      "status" : {
        "abstractGameState" : "Final",
        "codedGameState" : "7",
        "detailedState" : "Final",
        "statusCode" : "7",
        "startTimeTBD" : false
      },
      "teams" : {
        "away" : {
          "leagueRecord" : {
            "wins" : 17,
            "losses" : 17,
            "ot" : 5,
            "type" : "league"
          },
          "score" : 1,
          "team" : {
            "id" : 13,
            "name" : "Florida Panthers",
            "link" : "/api/v1/teams/13"
          }
        },
        "home" : {
          "leagueRecord" : {
            "wins" : 21,
            "losses" : 16,
            "ot" : 3,
            "type" : "league"
          },
          "score" : 5,
          "team" : {
            "id" : 30,
            "name" : "Minnesota Wild",
            "link" : "/api/v1/teams/30"
          }
        }
      },
      "linescore" : {
        "currentPeriod" : 3,
        "currentPeriodOrdinal" : "3rd",
        "currentPeriodTimeRemaining" : "Final",
        "periods" : [ {
          "periodType" : "REGULAR",
          "startTime" : "2018-01-03T01:08:44Z",
          "endTime" : "2018-01-03T01:44:06Z",
          "num" : 1,
          "ordinalNum" : "1st",
          "home" : {
            "goals" : 1,
            "shotsOnGoal" : 13,
            "rinkSide" : "right"
          },
          "away" : {
            "goals" : 0,
            "shotsOnGoal" : 9,
            "rinkSide" : "left"
          }
        }, {
          "periodType" : "REGULAR",
          "startTime" : "2018-01-03T02:03:03Z",
          "endTime" : "2018-01-03T02:48:52Z",
          "num" : 2,
          "ordinalNum" : "2nd",
          "home" : {
            "goals" : 3,
            "shotsOnGoal" : 19,
            "rinkSide" : "left"
          },
          "away" : {
            "goals" : 0,
            "shotsOnGoal" : 2,
            "rinkSide" : "right"
          }
        }, {
          "periodType" : "REGULAR",
          "startTime" : "2018-01-03T03:07:33Z",
          "endTime" : "2018-01-03T03:43:39Z",
          "num" : 3,
          "ordinalNum" : "3rd",
          "home" : {
            "goals" : 1,
            "shotsOnGoal" : 9,
            "rinkSide" : "right"
          },
          "away" : {
            "goals" : 1,
            "shotsOnGoal" : 15,
            "rinkSide" : "left"
          }
        } ],
        "shootoutInfo" : {
          "away" : {
            "scores" : 0,
            "attempts" : 0
          },
          "home" : {
            "scores" : 0,
            "attempts" : 0
          }
        },
        "teams" : {
          "home" : {
            "team" : {
              "id" : 30,
              "name" : "Minnesota Wild",
              "link" : "/api/v1/teams/30"
            },
            "goals" : 5,
            "shotsOnGoal" : 41,
            "goaliePulled" : false,
            "numSkaters" : 5,
            "powerPlay" : false
          },
          "away" : {
            "team" : {
              "id" : 13,
              "name" : "Florida Panthers",
              "link" : "/api/v1/teams/13"
            },
            "goals" : 1,
            "shotsOnGoal" : 26,
            "goaliePulled" : false,
            "numSkaters" : 5,
            "powerPlay" : false
          }
        },
        "powerPlayStrength" : "Even",
        "hasShootout" : false,
        "intermissionInfo" : {
          "intermissionTimeRemaining" : 0,
          "intermissionTimeElapsed" : 0,
          "inIntermission" : false
        },
        "powerPlayInfo" : {
          "situationTimeRemaining" : 0,
          "situationTimeElapsed" : 0,
          "inSituation" : false
        }
      },
      "venue" : {
        "name" : "Xcel Energy Center",
        "link" : "/api/v1/venues/null"
      },
      "broadcasts" : [ {
        "id" : 14,
        "name" : "FS-N",
        "type" : "home",
        "site" : "nhl",
        "language" : "en"
      }, {
        "id" : 12,
        "name" : "FS-F",
        "type" : "away",
        "site" : "nhl",
        "language" : "en"
      } ],
      "content" : {
        "link" : "/api/v1/game/2017020608/content"
      }
    } ],
    "events" : [ ],
    "matches" : [ ]
  } ]
}
```

<br /></details>

[back to top](#endpoint-tables)

## Seasons

`GET https://statsapi.web.nhl.com/api/v1/seasons` | Returns data on each season such as if ties were used, divisions, wildcards or the Olympics were participated in

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2019. All Rights Reserved.",
  "seasons" : [ {
    "seasonId" : "20172018",
    "regularSeasonStartDate" : "2017-10-04",
    "regularSeasonEndDate" : "2018-04-08",
    "seasonEndDate" : "2018-06-07",
    "numberOfGames" : 82,
    "tiesInUse" : false,
    "olympicsParticipation" : false,
    "conferencesInUse" : true,
    "divisionsInUse" : true,
    "wildCardInUse" : true
  } ]
}
```
<br /></details>

`GET https://statsapi.web.nhl.com/api/v1/seasons/20172018` | Gets just the data for a specific season

`GET https://statsapi.web.nhl.com/api/v1/seasons/current` | Returns the current season, very useful for code that depends upon this information

[back to top](#endpoint-tables)



# Standings Endpoints

## Standings

`GET https://statsapi.web.nhl.com/api/v1/standings` | Returns ordered standings data
for each team broken up by divisions

<details>
  <summary>click for example</summary>

```json
{
  "team" : {
    "id" : 52,
    "name" : "Winnipeg Jets",
    "link" : "/api/v1/teams/52"
  },
  "leagueRecord" : {
    "wins" : 37,
    "losses" : 17,
    "ot" : 9,
    "type" : "league"
  },
  "goalsAgainst" : 170,
  "goalsScored" : 213,
  "points" : 83,
  "divisionRank" : "2",
  "conferenceRank" : "3",
  "leagueRank" : "6",
  "wildCardRank" : "0",
  "row" : 35,
  "gamesPlayed" : 63,
  "streak" : {
    "streakType" : "losses",
    "streakNumber" : 1,
    "streakCode" : "L1"
  },
}
```
<br /></details>

#### Modifiers

`?season=20032004` | Standings for a specified season

`?expand=standings.record` | Detailed information for each team including home and away records, record in shootouts, last ten games, and split head-to-head records against divisions and conferences

<details>
  <summary>click for example</summary>

```json
{
  "records" : {
    "divisionRecords" : [ {
      "wins" : 11,
      "losses" : 7,
      "ot" : 2,
      "type" : "Central"
    }, {
      "wins" : 5,
      "losses" : 3,
      "ot" : 3,
      "type" : "Atlantic"
    }, {
      "wins" : 15,
      "losses" : 4,
      "ot" : 2,
      "type" : "Pacific"
    }, {
      "wins" : 6,
      "losses" : 3,
      "ot" : 2,
      "type" : "Metropolitan"
    } ],
    "overallRecords" : [ {
      "wins" : 23,
      "losses" : 7,
      "ot" : 2,
      "type" : "home"
    }, {
      "wins" : 14,
      "losses" : 10,
      "ot" : 7,
      "type" : "away"
    }, {
      "wins" : 2,
      "losses" : 2,
      "type" : "shootOuts"
    }, {
      "wins" : 6,
      "losses" : 4,
      "ot" : 0,
      "type" : "lastTen"
    } ],
    "conferenceRecords" : [ {
      "wins" : 11,
      "losses" : 6,
      "ot" : 5,
      "type" : "Eastern"
    }, {
      "wins" : 26,
      "losses" : 11,
      "ot" : 4,
      "type" : "Western"
    } ]
  }
}
```
<br /></details>

[back to top](#endpoint-tables)

## Standings types

`GET https://statsapi.web.nhl.com/api/v1/standingsTypes` | Returns all the standings types
to be used in order do get a specific standings

<details>
  <summary>click for example</summary>

```json
{
[ {
  "name" : "regularSeason",
  "description" : "Regular Season Standings"
}, {
  "name" : "wildCard",
  "description" : "Wild card standings"
}, {
  "name" : "divisionLeaders",
  "description" : "Division Leader standings"
}, {
  "name" : "wildCardWithLeaders",
  "description" : "Wild card standings with Division Leaders"
}, {
  "name" : "preseason",
  "description" : "Preseason Standings"
}, {
  "name" : "postseason",
  "description" : "Postseason Standings"
}, {
  "name" : "byDivision",
  "description" : "Standings by Division"
}, {
  "name" : "byConference",
  "description" : "Standings by Conference"
}, {
  "name" : "byLeague",
  "description" : "Standings by League"
} ]
```
<br /></details>

[back to top](#endpoint-tables)

# Teams Endpoints

## Team Stats

`GET https://statsapi.web.nhl.com/api/v1/teams/5/stats` | Returns current season stats and the current season rankings for a specific team

Ex:
<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "stats" : [ {
    "type" : {
      "displayName" : "statsSingleSeason"
    },
    "splits" : [ {
      "stat" : {
        "gamesPlayed" : 46,
        "wins" : 24,
        "losses" : 19,
        "ot" : 3,
        "pts" : 51,
        "ptPctg" : "55.4",
        "goalsPerGame" : 2.891,
        "goalsAgainstPerGame" : 3.043,
        "evGGARatio" : 0.6602,
        "powerPlayPercentage" : "26.5",
        "powerPlayGoals" : 43.0,
        "powerPlayGoalsAgainst" : 28.0,
        "powerPlayOpportunities" : 162.0,
        "penaltyKillPercentage" : "82.6",
        "shotsPerGame" : 34.7174,
        "shotsAllowed" : 30.3043,
        "winScoreFirst" : 0.76,
        "winOppScoreFirst" : 0.238,
        "winLeadFirstPer" : 0.857,
        "winLeadSecondPer" : 1.0,
        "winOutshootOpp" : 0.6,
        "winOutshotByOpp" : 0.375,
        "faceOffsTaken" : 2889.0,
        "faceOffsWon" : 1474.0,
        "faceOffsLost" : 1415.0,
        "faceOffWinPercentage" : "51.0",
        "shootingPctg" : 8.3,
        "savePctg" : 0.9
      },
      "team" : {
        "id" : 5,
        "name" : "Pittsburgh Penguins",
        "link" : "/api/v1/teams/5"
      }
    } ]
  }, {
    "type" : {
      "displayName" : "regularSeasonStatRankings"
    },
    "splits" : [ {
      "stat" : {
        "wins" : "15th",
        "losses" : "25th",
        "ot" : "30th",
        "pts" : "17th",
        "ptPctg" : "21st",
        "goalsPerGame" : "15th",
        "goalsAgainstPerGame" : "22nd",
        "evGGARatio" : "30th",
        "powerPlayPercentage" : "1st",
        "powerPlayGoals" : "1st",
        "powerPlayGoalsAgainst" : "17th",
        "powerPlayOpportunities" : "4th",
        "penaltyKillOpportunities" : "28th",
        "penaltyKillPercentage" : "10th",
        "shotsPerGame" : "1st",
        "shotsAllowed" : "5th",
        "winScoreFirst" : "8th",
        "winOppScoreFirst" : "24th",
        "winLeadFirstPer" : "10th",
        "winLeadSecondPer" : "1st",
        "winOutshootOpp" : "6th",
        "winOutshotByOpp" : "6th",
        "faceOffsTaken" : "1st",
        "faceOffsWon" : "3rd",
        "faceOffsLost" : "24th",
        "faceOffWinPercentage" : "12th",
        "savePctRank" : "25th",
        "shootingPctRank" : "24th"
      },
      "team" : {
        "id" : 5,
        "name" : "Pittsburgh Penguins",
        "link" : "/api/v1/teams/5"
      }
    } ]
  } ]
}
```

<br /></details>

[back to top](#endpoint-tables)

## Teams

`GET https://statsapi.web.nhl.com/api/v1/teams` | Returns a list of data about
all teams including their id, venue details, division, conference and franchise information.

`GET https://statsapi.web.nhl.com/api/v1/teams/ID` | Returns the same information as above just
for a single team instead of the entire league.

#### Team Modifiers

Add these to the end of the url

`?expand=team.roster` | Shows roster of active players for the specified team

`?expand=person.names` | Same as above, but gives less info.

`?expand=team.schedule.next` | Returns details of the upcoming game for a team

`?expand=team.schedule.previous` | Same as above but for the last game played

`?expand=team.stats` | Returns the teams stats for the season

`?expand=team.roster&season=20142015` | Adding the season identifier shows the roster for that season

`?teamId=4,5,29` | Can string team id together to get multiple teams

`?stats=statsSingleSeasonPlayoffs` | Specify which stats to get. Not fully sure all of the values

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "teams" : [ {
    "id" : 1,
    "name" : "New Jersey Devils",
    "link" : "/api/v1/teams/1",
    "venue" : {
      "name" : "Prudential Center",
      "link" : "/api/v1/venues/null",
      "city" : "Newark",
      "timeZone" : {
        "id" : "America/New_York",
        "offset" : -5,
        "tz" : "EST"
      }
    },
    "abbreviation" : "NJD",
    "teamName" : "Devils",
    "locationName" : "New Jersey",
    "firstYearOfPlay" : "1982",
    "division" : {
      "id" : 18,
      "name" : "Metropolitan",
      "link" : "/api/v1/divisions/18"
    },
    "conference" : {
      "id" : 6,
      "name" : "Eastern",
      "link" : "/api/v1/conferences/6"
    },
    "franchise" : {
      "franchiseId" : 23,
      "teamName" : "Devils",
      "link" : "/api/v1/franchises/23"
    },
    "shortName" : "New Jersey",
    "officialSiteUrl" : "http://www.truesince82.com",
    "franchiseId" : 23,
    "active" : true
  }, {
```
<br /></details>

`GET https://statsapi.web.nhl.com/api/v1/teams/ID/roster` | Returns entire roster for a team
including id value, name, jersey number and position details.

<details>
  <summary>click for example</summary>

```json
{
  "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2018. All Rights Reserved.",
  "roster" : [ {
    "person" : {
      "id" : 8477474,
      "fullName" : "Madison Bowey",
      "link" : "/api/v1/people/8477474"
    },
    "jerseyNumber" : "22",
    "position" : {
      "code" : "D",
      "name" : "Defenseman",
      "type" : "Defenseman",
      "abbreviation" : "D"
    }
  },]
  }
```
<br /></details>

[back to top](#endpoint-tables)

# Miscellaneous Endpoints

### Configurations
`GET https://statsapi.web.nhl.com/api/v1/configurations` | Returns a huge list of other endpoints, sort of the rosetta stone discovery tying many parts of the API together

### Event Types
`GET https://statsapi.web.nhl.com/api/v1/eventTypes` | Shows several event types beyond just hockey games, possibly an artifact left over from being reconfigured to be used by the NHL

### Expands

`GET https://statsapi.web.nhl.com/api/v1/expands` | Shows all possible input for the expand field

### Languages
`GET https://statsapi.web.nhl.com/api/v1/languages` | Shows all possible languages for the API

### Performer types
`GET https://statsapi.web.nhl.com/api/v1/performerTypes` | List of performer types likely tied to venue scheduling information

### Platforms
`GET https://statsapi.web.nhl.com/api/v1/platforms` | This seems to allow the API to be tailored to a specific platform, indicating platform specific behavior/apps.

### Stat Types

`GET https://statsapi.web.nhl.com/api/v1/statTypes` | Returns all the stats types
to be used in order do get a specific kind of player stats

[back to top](#endpoint-tables)