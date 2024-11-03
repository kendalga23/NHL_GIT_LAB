0: v1/player-spotlight
method

++++++++++++++++++

1: v1/schedule
resource
	now
	Example: v1/schedule/now

	{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: v1/schedule/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}


++++++++++++++++++

2: v1/standings-season
method

++++++++++++++++++

3: /v1/schedule/playoff-series
resource

++++++++++++++++++

4: /v1/score
resource
	now
	Example: /v1/score/now

	{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: /v1/score/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}


++++++++++++++++++

5: v1/location
method

++++++++++++++++++

6: v1/season
method

++++++++++++++++++

7: v1/skater-stats-leaders
resource
	current
	Example: v1/skater-stats-leaders/current

	{season: [0-9]{8}}/{game-type: [0-9]}
	Example: v1/skater-stats-leaders/{season: [0-9]{8}}/{game-type: [0-9]}


++++++++++++++++++

8: v1/where-to-watch
method

++++++++++++++++++

9: v1/club-stats
resource
	{team: \w{3}}/now
	Example: v1/club-stats/{team: \w{3}}/now

	{team: \w{3}}/{season: [0-9]{8}}/{game-type: [0-9]}
	Example: v1/club-stats/{team: \w{3}}/{season: [0-9]{8}}/{game-type: [0-9]}


++++++++++++++++++

10: v1/prospects
resource

++++++++++++++++++

11: /v1/postal-lookup
resource

++++++++++++++++++

12: v1/club-schedule-season
resource
	{team: \w{3}}/now
	Example: v1/club-schedule-season/{team: \w{3}}/now

	{team: \w{3}}/{season: [0-9]{8}}
	Example: v1/club-schedule-season/{team: \w{3}}/{season: [0-9]{8}}


++++++++++++++++++

13: v1/playoff-series
resource

++++++++++++++++++

14: v1/draft-tracker
resource

++++++++++++++++++

15: /v1/draft/picks
resource
	{year: [0-9]{4}}/{round: [0-9]{1,2}}
	Example: /v1/draft/picks/{year: [0-9]{4}}/{round: [0-9]{1,2}}

	now
	Example: /v1/draft/picks/now

	{year: [0-9]{4}}/all
	Example: /v1/draft/picks/{year: [0-9]{4}}/all


++++++++++++++++++

16: v1/scoreboard
resource
	{team: \w{3}}/now
	Example: v1/scoreboard/{team: \w{3}}/now

	now
	Example: v1/scoreboard/now


++++++++++++++++++

17: v1/roster
resource
	{team: \w{3}}/current
	Example: v1/roster/{team: \w{3}}/current

	{team: \w{3}}/{season: [0-9]{8}}
	Example: v1/roster/{team: \w{3}}/{season: [0-9]{8}}


++++++++++++++++++

18: v1/club-schedule
resource
	{team: \w{3}}/month/now
	Example: v1/club-schedule/{team: \w{3}}/month/now

	{team: \w{3}}/month/{month: [0-9]{4}-[0-9]{2}}
	Example: v1/club-schedule/{team: \w{3}}/month/{month: [0-9]{4}-[0-9]{2}}

	{team: \w{3}}/week/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: v1/club-schedule/{team: \w{3}}/week/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}

	{team: \w{3}}/week/now
	Example: v1/club-schedule/{team: \w{3}}/week/now


++++++++++++++++++

19: /v1/ppt-replay
resource
	/goal/{game-id}/{event-number}
	Example: /v1/ppt-replay//goal/{game-id}/{event-number}

	{game-id}/{event-number}
	Example: /v1/ppt-replay/{game-id}/{event-number}


++++++++++++++++++

20: v1/standings
resource
	now
	Example: v1/standings/now

	{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: v1/standings/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}


++++++++++++++++++

21: v1/player
resource
	{player}/game-log/{season: [0-9]{8}}/{game-type: [0-9]}
	Example: v1/player/{player}/game-log/{season: [0-9]{8}}/{game-type: [0-9]}

	{player}/landing
	Example: v1/player/{player}/landing

	{player}/game-log/now
	Example: v1/player/{player}/game-log/now


++++++++++++++++++

22: v1/roster-season
resource

++++++++++++++++++

23: v1/gamecenter
resource
	{game-id: \d+}/play-by-play
	Example: v1/gamecenter/{game-id: \d+}/play-by-play

	{game-id: \d+}/right-rail
	Example: v1/gamecenter/{game-id: \d+}/right-rail

	{game-id: \d+}/landing
	Example: v1/gamecenter/{game-id: \d+}/landing

	{game-id: \d+}/boxscore
	Example: v1/gamecenter/{game-id: \d+}/boxscore


++++++++++++++++++

24: v1/meta
method
resource
	playoff-series/{year}/{series_letter}
	Example: v1/meta/playoff-series/{year}/{series_letter}

	game/{game-id: \d+}
	Example: v1/meta/game/{game-id: \d+}


++++++++++++++++++

25: v1/wsc/game-story
resource

++++++++++++++++++

26: v1/goalie-stats-leaders
resource
	current
	Example: v1/goalie-stats-leaders/current

	{season: [0-9]{8}}/{game-type: [0-9]}
	Example: v1/goalie-stats-leaders/{season: [0-9]{8}}/{game-type: [0-9]}


++++++++++++++++++

27: /v1/draft/rankings
resource
	{year}/{category}
	Example: /v1/draft/rankings/{year}/{category}

	now
	Example: /v1/draft/rankings/now


++++++++++++++++++

28: v1/playoff-bracket
resource

++++++++++++++++++

29: /v1/partner-game/{country-code}/now
param
method

++++++++++++++++++

30: v1/network
resource
	tv-schedule/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: v1/network/tv-schedule/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}

	tv-schedule/now
	Example: v1/network/tv-schedule/now


++++++++++++++++++

31: model/v1/openapi.json
method

++++++++++++++++++

32: v1/schedule-calendar
resource
	now
	Example: v1/schedule-calendar/now

	{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}
	Example: v1/schedule-calendar/{date: [0-9]{4}-[0-9]{2}-[0-9]{2}}


++++++++++++++++++

33: v1/club-stats-season
resource

++++++++++++++++++

34: application.wadl
method
resource
jersey:extended

++++++++++++++++++
