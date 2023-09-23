# New API Documentation

The NHL has surprised us all with a new API, so that means a new file to track all the parts of it people have discovered so far.

`https://api-web.nhle.com/v1/`

# Schedule endpoints

`GET https://api-web.nhle.com/v1/schedule/now` | Gets schedule of games for today

`GET https://api-web.nhle.com/v1/schedule/2023-09-23` | Gets schedule of games for specified date
<details>
    <summary>click for example</summary>
```json
// GET https://api-web.nhle.com/v1/schedule/2018-09-01

{
  "nextStartDate": "2018-09-15",
  "previousStartDate": "2018-06-02",
  "gameWeek": [
    {
      "date": "2018-09-01",
      "dayAbbrev": "SAT",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-02",
      "dayAbbrev": "SUN",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-03",
      "dayAbbrev": "MON",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-04",
      "dayAbbrev": "TUE",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-05",
      "dayAbbrev": "WED",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-06",
      "dayAbbrev": "THU",
      "numberOfGames": 0,
      "games": []
    },
    {
      "date": "2018-09-07",
      "dayAbbrev": "FRI",
      "numberOfGames": 0,
      "games": []
    }
  ],
  "preSeasonStartDate": "2018-09-15",
  "regularSeasonStartDate": "2018-10-03",
  "regularSeasonEndDate": "2019-04-06",
  "playoffEndDate": "2019-06-12",
  "numberOfGames": 0
}
```
</details>

<br />

`GET https://api-web.nhle.com/v1/club-schedule-season/TEAM_ABBR/now` | gets the full season schedule for the specified team

`GET https://api-web.nhle.com/v1/club-schedule/TEAM_ABBR/week/now` | ADD description

`GET https://api-web.nhle.com/v1/club-schedule/TEAM_ABBR/month/now` | ADD description

# Standings

`GET https://api-web.nhle.com/v1/standings/now` | Gets standings as of the current date

`GET https://api-web.nhle.com/v1/standings-season` | ADD description

# Stats

`GET https://api-web.nhle.com/v1/club-stats-season/TEAM_ABBR` | Team stats by season

`GET https://api-web.nhle.com/v1/player/PLAYER_ID/landing` | Player specific stats

# Rosters

`GET https://api-web.nhle.com/v1/roster/TEAM_ABBR/now` | ADD description

`GET https://api-web.nhle.com/v1/roster-season/TEAM_ABBR` | ADD description

# Game details

`GET https://api-web.nhle.com/v1/score/now` | Linescore details

`GET https://api-web.nhle.com/v1/gamecenter/GAME_ID/boxscore` |  Boxscore details

