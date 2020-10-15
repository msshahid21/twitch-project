# Twitch Part 1: Analyze Data with SQL

## Overview

This section of the cumulative project focuses on the analysis of two data-sets, **chat usage** and **stream viewing** data. I used DBeaver and SQLITE to complete the tasks given by Codecademy (tasks will be shown in each part). I imported the chat usage data as **chat** and the stream viewing data as **stream**.

## Tasks

### What columns do the tables have?

#### <u>Chat Usage</u>

```sqlite
SELECT * FROM chat
LIMIT 20;
```

Contains the following columns:

- time
- device_id
- login
- channel
- country
- player
- game

#### <u>Stream Viewing</u>

```sqlite
SELECT * FROM stream
LIMIT 20;
```

Contains the following columns:

- time
- device_id
- login
- channel
- country
- player
- game
- stream_format
- subscriber

### What are the unique <u>games</u> in the stream table?

```sqlite
SELECT DISTINCT game FROM stream;
```

There were 42 unique games within the stream table (shown in **distinct-games(stream).csv**).

### What are the unique <u>channels</u> in the stream table?

```sqlite
SELECT DISTINCT channel FROM stream;
```

There were 10 unique channels within the stream table:

- frank
- george
- estelle
- morty
- kramer
- jerry
- helen
- newman
- elaine
- susan

### What are the most popular games in the <u>stream</u> table?

```sqlite
SELECT game, COUNT(*) FROM stream
GROUP BY 1
ORDER BY 2
LIMIT 5;
```

The top 5 games in the stream table by number of viewers are:

| Game Title                       | Number of Viewers |
| -------------------------------- | ----------------: |
| League of Legends                |           193,533 |
| Dota 2                           |            85,608 |
| Counter-Strike: Global Offensive |            54,438 |
| DayZ                             |            38,004 |
| Heroes of the Storm              |            35,310 |

### Where are League of Legends (LoL) viewers located?

When executing the SQL statement showing the top 5 countries where LoL viewers are located, I noticed that countries with a value of NULL were in the list. Therefore, to exclude NULL values the code was modified slightly.

```sqlite
SELECT country, COUNT(*) FROM stream
WHERE game = "League of Legends" AND country NOTNULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

| Country             | Number of Viewers |
| ------------------- | ----------------: |
| United States (US)  |            85,606 |
| Canada (CA)         |            13,034 |
| Germany (DE)        |            10,835 |
| United Kingdom (GB) |             6,964 |
| Turkey (TR)         |             4,412 |

### Which source (player) is being used the most to view streams?

```sqlite
SELECT player, COUNT(*) FROM stream
GROUP BY 1
ORDER BY 2 DESC;
```

Showing only Top 5 stream sources (players) below, full list can be found in **player-count(stream).csv**.

| Source (Player) | # Users |
| --------------- | ------: |
| site            | 246,115 |
| iphone_t        | 100,689 |
| android         |  93,508 |
| ipad_t          |  53,646 |
| embed           |  19,819 |

### Grouping games by genre

```sqlite
SELECT game,
CASE
	WHEN game = 'League of Legends'
		THEN 'MOBA'
	WHEN game = 'Dota 2'
		THEN 'MOBA'
	WHEN game = 'Heroes of the Storm'
		THEN 'MOBA'
	WHEN game = 'Counter-Strike: Global Offensive'
		THEN 'FPS'
	WHEN game = 'DayZ'
		THEN 'Survival'
	WHEN game = 'Survival Evolved'
    	THEN 'Survival'
    ELSE 'Other'
END AS 'Genre',
COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;
```

Results shown in **games-genres(stream).csv**.

### At what hours during the day are streams being watched the most?

Upon conducting a query to understand the **time** column in the stream table it can be seen that all the data is from the day 2015-01-01. Therefore the following query will allow us to see at what hours during that specific day were streams being watched the most. However, as this data-set is only from one day there is a limitation to the conclusions that can be drawn from this data. Query only considers for the US viewers due to time differences.

```sqlite
SELECT strftime('%H', time), COUNT(*)
FROM stream
WHERE country = 'US'
GROUP BY 1
ORDER BY 1 ASC;
```

The peak hour of viewership is at the 20 hour mark (8 PM) at 19,656 viewers. Rest of the results are shown in **hourly-viewership(stream).csv**.