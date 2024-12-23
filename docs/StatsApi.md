# swagger_client.StatsApi

All URIs are relative to *https://statsapi.mlb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**beast_stats**](StatsApi.md#beast_stats) | **GET** /api/v1/stats/search | View stats from search
[**get_outs_above_average**](StatsApi.md#get_outs_above_average) | **GET** /api/v1/stats/analytics/outsAboveAverage | Get outs above average for the current batter
[**get_spray_chart**](StatsApi.md#get_spray_chart) | **GET** /api/v1/stats/analytics/sprayChart | Get the spray chart info for the current batter
[**get_stolen_base_probability**](StatsApi.md#get_stolen_base_probability) | **GET** /api/v1/stats/analytics/stolenBaseProbability | Get the probability of a hit for the given hit data
[**grouped_stats**](StatsApi.md#grouped_stats) | **GET** /api/v1/stats/grouped | View grouped stats
[**leaders2**](StatsApi.md#leaders2) | **GET** /api/v1/stats/leaders | Get leaders for a statistic
[**metric_stats**](StatsApi.md#metric_stats) | **GET** /api/v1/stats/metrics | View metric stats
[**stats2**](StatsApi.md#stats2) | **GET** /api/v1/stats | View stats

# **beast_stats**
> StatContainerRestObject beast_stats(group, game_pks=game_pks, play_ids=play_ids, seasons=seasons, game_types=game_types, _date=_date, start_date=start_date, end_date=end_date, team_ids=team_ids, pitcher_team_ids=pitcher_team_ids, batter_team_ids=batter_team_ids, sport_ids=sport_ids, pitcher_sport_ids=pitcher_sport_ids, batter_sport_ids=batter_sport_ids, league_ids=league_ids, pitcher_league_ids=pitcher_league_ids, batter_league_ids=batter_league_ids, division_ids=division_ids, pitcher_division_ids=pitcher_division_ids, batter_division_ids=batter_division_ids, pitchers_on_team_ids=pitchers_on_team_ids, batters_on_team_ids=batters_on_team_ids, player_ids=player_ids, player_pool=player_pool, pitcher_ids=pitcher_ids, batter_ids=batter_ids, catcher_ids=catcher_ids, first_baseman_ids=first_baseman_ids, second_baseman_ids=second_baseman_ids, third_baseman_ids=third_baseman_ids, shortstop_ids=shortstop_ids, left_fielder_ids=left_fielder_ids, center_fielder_ids=center_fielder_ids, right_fielder_ids=right_fielder_ids, runner_first_ids=runner_first_ids, runner_second_ids=runner_second_ids, runner_third_ids=runner_third_ids, venue_ids=venue_ids, pitch_hand=pitch_hand, bat_side=bat_side, pitch_types=pitch_types, pitch_codes=pitch_codes, event_types=event_types, positions=positions, primary_positions=primary_positions, min_pitch_speed=min_pitch_speed, max_pitch_speed=max_pitch_speed, min_spin_rate=min_spin_rate, max_spin_rate=max_spin_rate, min_extension=min_extension, max_extension=max_extension, min_exit_velocity_against=min_exit_velocity_against, max_exit_velocity_against=max_exit_velocity_against, min_launch_angle_against=min_launch_angle_against, max_launch_angle_against=max_launch_angle_against, min_exit_velocity=min_exit_velocity, max_exit_velocity=max_exit_velocity, min_launch_angle=min_launch_angle, max_launch_angle=max_launch_angle, min_home_run_distance=min_home_run_distance, max_home_run_distance=max_home_run_distance, min_hit_distance=min_hit_distance, max_hit_distance=max_hit_distance, min_hang_time=min_hang_time, max_hang_time=max_hang_time, min_hit_probability=min_hit_probability, max_hit_probability=max_hit_probability, min_catch_probability=min_catch_probability, max_catch_probability=max_catch_probability, min_attack_angle=min_attack_angle, max_attack_angle=max_attack_angle, min_bat_speed=min_bat_speed, max_bat_speed=max_bat_speed, min_home_run_x_ballparks=min_home_run_x_ballparks, max_home_run_x_ballparks=max_home_run_x_ballparks, is_barrel=is_barrel, hit_trajectories=hit_trajectories, limit=limit, offset=offset, group_by=group_by, compare_over=compare_over, sort_stat=sort_stat, sort_modifier=sort_modifier, sort_order=sort_order, percentile=percentile, min_occurrences=min_occurrences, min_plate_appearances=min_plate_appearances, min_innings=min_innings, qualifier_rate=qualifier_rate, sit_codes=sit_codes, show_totals=show_totals, include_null_metrics=include_null_metrics, stat_fields=stat_fields, at_bat_numbers=at_bat_numbers, pitch_numbers=pitch_numbers, fields=fields, debug=debug, active_status=active_status)

View stats from search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups
game_pks = [56] # list[int] | Comma delimited list of unique primary keys (optional)
play_ids = ['play_ids_example'] # list[str] | Comma delimited list of unique play identifiers (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] | Type of Game. Available types in /api/v1/gameTypes (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
end_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
pitcher_team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
batter_team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
pitcher_sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
batter_sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
pitcher_league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
batter_league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
division_ids = [56] # list[int] | Comma delimited list of Unique League Identifiers (optional)
pitcher_division_ids = [56] # list[int] | Comma delimited list of Unique League Identifiers (optional)
batter_division_ids = [56] # list[int] | Comma delimited list of Unique League Identifiers (optional)
pitchers_on_team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
batters_on_team_ids = [56] # list[int] | Unique Team Identifier. Format: 141, 147, etc (optional)
player_ids = [56] # list[int] | A unique identifier for a player (optional)
player_pool = swagger_client.PlayerPoolEnum() # PlayerPoolEnum | Return \"ALL\" or only \"QUALIFIED\" players based on plate appearances. (optional)
pitcher_ids = [56] # list[int] | A unique identifier for a player (optional)
batter_ids = [56] # list[int] | A unique identifier for a player (optional)
catcher_ids = [56] # list[int] | A unique identifier for a player (optional)
first_baseman_ids = [56] # list[int] | A unique identifier for a player (optional)
second_baseman_ids = [56] # list[int] | A unique identifier for a player (optional)
third_baseman_ids = [56] # list[int] | A unique identifier for a player (optional)
shortstop_ids = [56] # list[int] | A unique identifier for a player (optional)
left_fielder_ids = [56] # list[int] | A unique identifier for a player (optional)
center_fielder_ids = [56] # list[int] | A unique identifier for a player (optional)
right_fielder_ids = [56] # list[int] | A unique identifier for a player (optional)
runner_first_ids = [56] # list[int] | A unique identifier for a player (optional)
runner_second_ids = [56] # list[int] | A unique identifier for a player (optional)
runner_third_ids = [56] # list[int] | A unique identifier for a player (optional)
venue_ids = [56] # list[int] | Unique Venue Identifier (optional)
pitch_hand = 'pitch_hand_example' # str | Handedness of pitcher (optional)
bat_side = 'bat_side_example' # str | Bat side of hitter (optional)
pitch_types = [swagger_client.PitchType()] # list[PitchType] | Classification of pitch (fastball, curveball, etc...) (optional)
pitch_codes = [swagger_client.PitchCode()] # list[PitchCode] | Result of the pitch (ball, called strike, etc...) (optional)
event_types = [swagger_client.EventType()] # list[EventType] | Type of event (optional)
positions = [swagger_client.BaseballPosition()] # list[BaseballPosition] | All of the details of a player's position (optional)
primary_positions = [swagger_client.BaseballPosition()] # list[BaseballPosition] | All of the details of a player's position (optional)
min_pitch_speed = 1.2 # float | Minimum value to filter on (optional)
max_pitch_speed = 1.2 # float | Maximum value to filter on (optional)
min_spin_rate = 1.2 # float | Minimum value to filter on (optional)
max_spin_rate = 1.2 # float | Maximum value to filter on (optional)
min_extension = 1.2 # float | Minimum value to filter on (optional)
max_extension = 1.2 # float | Maximum value to filter on (optional)
min_exit_velocity_against = 1.2 # float | Minimum value to filter on (optional)
max_exit_velocity_against = 1.2 # float | Maximum value to filter on (optional)
min_launch_angle_against = 1.2 # float | Minimum value to filter on (optional)
max_launch_angle_against = 1.2 # float | Maximum value to filter on (optional)
min_exit_velocity = 1.2 # float | Minimum value to filter on (optional)
max_exit_velocity = 1.2 # float | Maximum value to filter on (optional)
min_launch_angle = 1.2 # float | Minimum value to filter on (optional)
max_launch_angle = 1.2 # float | Maximum value to filter on (optional)
min_home_run_distance = 1.2 # float | Minimum value to filter on (optional)
max_home_run_distance = 1.2 # float | Maximum value to filter on (optional)
min_hit_distance = 1.2 # float | Minimum value to filter on (optional)
max_hit_distance = 1.2 # float | Maximum value to filter on (optional)
min_hang_time = 1.2 # float | Minimum value to filter on (optional)
max_hang_time = 1.2 # float | Maximum value to filter on (optional)
min_hit_probability = 1.2 # float | Minimum value to filter on (optional)
max_hit_probability = 1.2 # float | Maximum value to filter on (optional)
min_catch_probability = 1.2 # float | Minimum value to filter on (optional)
max_catch_probability = 1.2 # float | Maximum value to filter on (optional)
min_attack_angle = 1.2 # float | Minimum value to filter on (optional)
max_attack_angle = 1.2 # float | Maximum value to filter on (optional)
min_bat_speed = 1.2 # float | Minimum value to filter on (optional)
max_bat_speed = 1.2 # float | Maximum value to filter on (optional)
min_home_run_x_ballparks = 1.2 # float | Minimum value to filter on (optional)
max_home_run_x_ballparks = 1.2 # float | Maximum value to filter on (optional)
is_barrel = true # bool | Whether or not a play resulted in a barreled ball (optional)
hit_trajectories = [swagger_client.HitTrajectory()] # list[HitTrajectory] | Trajectory of hit (line drive, fly ball, etc...) (optional)
limit = 56 # int | Number of results to return (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
group_by = [swagger_client.GroupByEnum()] # list[GroupByEnum] | Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP (optional)
compare_over = [swagger_client.GroupByEnum()] # list[GroupByEnum] | Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP (optional)
sort_stat = swagger_client.BaseballStatsEnum() # BaseballStatsEnum | Baseball stat to sort splits by. (optional)
sort_modifier = swagger_client.AggregateSortTypeEnum() # AggregateSortTypeEnum | The prefix modifier for the sort stat.  avg, min, max. I.E minExitVelocity, maxLaunchAngle, avgHitDistance (optional)
sort_order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
percentile = 56 # int | Only return averages above this percentile. used for best effort plays (optional)
min_occurrences = 56 # int | Minimum occurrences to filter upon (optional)
min_plate_appearances = 56 # int | Minimum occurrences to filter upon (optional)
min_innings = 56 # int | Minimum occurrences to filter upon (optional)
qualifier_rate = 1.2 # float | Minimum occurrences to filter upon (optional)
sit_codes = ['sit_codes_example'] # list[str] | Situation code for a given stat split. (optional)
show_totals = true # bool | Columns to return totals (optional)
include_null_metrics = true # bool | Show events with null metrics (optional)
stat_fields = [swagger_client.StatField()] # list[StatField] | Baseball stat fields to populate (optional)
at_bat_numbers = [56] # list[int] | The at bat number of a given game. Format: 1, 2, 3, etc (optional)
pitch_numbers = [56] # list[int] | The pitch number of a given game. Format: 1, 2, 3, etc (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
debug = true # bool |  (optional)
active_status = swagger_client.PlayerActiveStatusEnum() # PlayerActiveStatusEnum | Whether or not a player is active (optional)

try:
    # View stats from search
    api_response = api_instance.beast_stats(group, game_pks=game_pks, play_ids=play_ids, seasons=seasons, game_types=game_types, _date=_date, start_date=start_date, end_date=end_date, team_ids=team_ids, pitcher_team_ids=pitcher_team_ids, batter_team_ids=batter_team_ids, sport_ids=sport_ids, pitcher_sport_ids=pitcher_sport_ids, batter_sport_ids=batter_sport_ids, league_ids=league_ids, pitcher_league_ids=pitcher_league_ids, batter_league_ids=batter_league_ids, division_ids=division_ids, pitcher_division_ids=pitcher_division_ids, batter_division_ids=batter_division_ids, pitchers_on_team_ids=pitchers_on_team_ids, batters_on_team_ids=batters_on_team_ids, player_ids=player_ids, player_pool=player_pool, pitcher_ids=pitcher_ids, batter_ids=batter_ids, catcher_ids=catcher_ids, first_baseman_ids=first_baseman_ids, second_baseman_ids=second_baseman_ids, third_baseman_ids=third_baseman_ids, shortstop_ids=shortstop_ids, left_fielder_ids=left_fielder_ids, center_fielder_ids=center_fielder_ids, right_fielder_ids=right_fielder_ids, runner_first_ids=runner_first_ids, runner_second_ids=runner_second_ids, runner_third_ids=runner_third_ids, venue_ids=venue_ids, pitch_hand=pitch_hand, bat_side=bat_side, pitch_types=pitch_types, pitch_codes=pitch_codes, event_types=event_types, positions=positions, primary_positions=primary_positions, min_pitch_speed=min_pitch_speed, max_pitch_speed=max_pitch_speed, min_spin_rate=min_spin_rate, max_spin_rate=max_spin_rate, min_extension=min_extension, max_extension=max_extension, min_exit_velocity_against=min_exit_velocity_against, max_exit_velocity_against=max_exit_velocity_against, min_launch_angle_against=min_launch_angle_against, max_launch_angle_against=max_launch_angle_against, min_exit_velocity=min_exit_velocity, max_exit_velocity=max_exit_velocity, min_launch_angle=min_launch_angle, max_launch_angle=max_launch_angle, min_home_run_distance=min_home_run_distance, max_home_run_distance=max_home_run_distance, min_hit_distance=min_hit_distance, max_hit_distance=max_hit_distance, min_hang_time=min_hang_time, max_hang_time=max_hang_time, min_hit_probability=min_hit_probability, max_hit_probability=max_hit_probability, min_catch_probability=min_catch_probability, max_catch_probability=max_catch_probability, min_attack_angle=min_attack_angle, max_attack_angle=max_attack_angle, min_bat_speed=min_bat_speed, max_bat_speed=max_bat_speed, min_home_run_x_ballparks=min_home_run_x_ballparks, max_home_run_x_ballparks=max_home_run_x_ballparks, is_barrel=is_barrel, hit_trajectories=hit_trajectories, limit=limit, offset=offset, group_by=group_by, compare_over=compare_over, sort_stat=sort_stat, sort_modifier=sort_modifier, sort_order=sort_order, percentile=percentile, min_occurrences=min_occurrences, min_plate_appearances=min_plate_appearances, min_innings=min_innings, qualifier_rate=qualifier_rate, sit_codes=sit_codes, show_totals=show_totals, include_null_metrics=include_null_metrics, stat_fields=stat_fields, at_bat_numbers=at_bat_numbers, pitch_numbers=pitch_numbers, fields=fields, debug=debug, active_status=active_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->beast_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | 
 **game_pks** | [**list[int]**](int.md)| Comma delimited list of unique primary keys | [optional] 
 **play_ids** | [**list[str]**](str.md)| Comma delimited list of unique play identifiers | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **end_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **pitcher_team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **batter_team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **pitcher_sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **batter_sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **pitcher_league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **batter_league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **division_ids** | [**list[int]**](int.md)| Comma delimited list of Unique League Identifiers | [optional] 
 **pitcher_division_ids** | [**list[int]**](int.md)| Comma delimited list of Unique League Identifiers | [optional] 
 **batter_division_ids** | [**list[int]**](int.md)| Comma delimited list of Unique League Identifiers | [optional] 
 **pitchers_on_team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **batters_on_team_ids** | [**list[int]**](int.md)| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **player_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **player_pool** | [**PlayerPoolEnum**](.md)| Return \&quot;ALL\&quot; or only \&quot;QUALIFIED\&quot; players based on plate appearances. | [optional] 
 **pitcher_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **batter_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **catcher_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **first_baseman_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **second_baseman_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **third_baseman_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **shortstop_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **left_fielder_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **center_fielder_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **right_fielder_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **runner_first_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **runner_second_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **runner_third_ids** | [**list[int]**](int.md)| A unique identifier for a player | [optional] 
 **venue_ids** | [**list[int]**](int.md)| Unique Venue Identifier | [optional] 
 **pitch_hand** | **str**| Handedness of pitcher | [optional] 
 **bat_side** | **str**| Bat side of hitter | [optional] 
 **pitch_types** | [**list[PitchType]**](PitchType.md)| Classification of pitch (fastball, curveball, etc...) | [optional] 
 **pitch_codes** | [**list[PitchCode]**](PitchCode.md)| Result of the pitch (ball, called strike, etc...) | [optional] 
 **event_types** | [**list[EventType]**](EventType.md)| Type of event | [optional] 
 **positions** | [**list[BaseballPosition]**](BaseballPosition.md)| All of the details of a player&#x27;s position | [optional] 
 **primary_positions** | [**list[BaseballPosition]**](BaseballPosition.md)| All of the details of a player&#x27;s position | [optional] 
 **min_pitch_speed** | **float**| Minimum value to filter on | [optional] 
 **max_pitch_speed** | **float**| Maximum value to filter on | [optional] 
 **min_spin_rate** | **float**| Minimum value to filter on | [optional] 
 **max_spin_rate** | **float**| Maximum value to filter on | [optional] 
 **min_extension** | **float**| Minimum value to filter on | [optional] 
 **max_extension** | **float**| Maximum value to filter on | [optional] 
 **min_exit_velocity_against** | **float**| Minimum value to filter on | [optional] 
 **max_exit_velocity_against** | **float**| Maximum value to filter on | [optional] 
 **min_launch_angle_against** | **float**| Minimum value to filter on | [optional] 
 **max_launch_angle_against** | **float**| Maximum value to filter on | [optional] 
 **min_exit_velocity** | **float**| Minimum value to filter on | [optional] 
 **max_exit_velocity** | **float**| Maximum value to filter on | [optional] 
 **min_launch_angle** | **float**| Minimum value to filter on | [optional] 
 **max_launch_angle** | **float**| Maximum value to filter on | [optional] 
 **min_home_run_distance** | **float**| Minimum value to filter on | [optional] 
 **max_home_run_distance** | **float**| Maximum value to filter on | [optional] 
 **min_hit_distance** | **float**| Minimum value to filter on | [optional] 
 **max_hit_distance** | **float**| Maximum value to filter on | [optional] 
 **min_hang_time** | **float**| Minimum value to filter on | [optional] 
 **max_hang_time** | **float**| Maximum value to filter on | [optional] 
 **min_hit_probability** | **float**| Minimum value to filter on | [optional] 
 **max_hit_probability** | **float**| Maximum value to filter on | [optional] 
 **min_catch_probability** | **float**| Minimum value to filter on | [optional] 
 **max_catch_probability** | **float**| Maximum value to filter on | [optional] 
 **min_attack_angle** | **float**| Minimum value to filter on | [optional] 
 **max_attack_angle** | **float**| Maximum value to filter on | [optional] 
 **min_bat_speed** | **float**| Minimum value to filter on | [optional] 
 **max_bat_speed** | **float**| Maximum value to filter on | [optional] 
 **min_home_run_x_ballparks** | **float**| Minimum value to filter on | [optional] 
 **max_home_run_x_ballparks** | **float**| Maximum value to filter on | [optional] 
 **is_barrel** | **bool**| Whether or not a play resulted in a barreled ball | [optional] 
 **hit_trajectories** | [**list[HitTrajectory]**](HitTrajectory.md)| Trajectory of hit (line drive, fly ball, etc...) | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **group_by** | [**list[GroupByEnum]**](GroupByEnum.md)| Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP | [optional] 
 **compare_over** | [**list[GroupByEnum]**](GroupByEnum.md)| Group stats by PLAYER, TEAM, SEASON, VENUE, SPORT or STAT_GROUP | [optional] 
 **sort_stat** | [**BaseballStatsEnum**](.md)| Baseball stat to sort splits by. | [optional] 
 **sort_modifier** | [**AggregateSortTypeEnum**](.md)| The prefix modifier for the sort stat.  avg, min, max. I.E minExitVelocity, maxLaunchAngle, avgHitDistance | [optional] 
 **sort_order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **percentile** | **int**| Only return averages above this percentile. used for best effort plays | [optional] 
 **min_occurrences** | **int**| Minimum occurrences to filter upon | [optional] 
 **min_plate_appearances** | **int**| Minimum occurrences to filter upon | [optional] 
 **min_innings** | **int**| Minimum occurrences to filter upon | [optional] 
 **qualifier_rate** | **float**| Minimum occurrences to filter upon | [optional] 
 **sit_codes** | [**list[str]**](str.md)| Situation code for a given stat split. | [optional] 
 **show_totals** | **bool**| Columns to return totals | [optional] 
 **include_null_metrics** | **bool**| Show events with null metrics | [optional] 
 **stat_fields** | [**list[StatField]**](StatField.md)| Baseball stat fields to populate | [optional] 
 **at_bat_numbers** | [**list[int]**](int.md)| The at bat number of a given game. Format: 1, 2, 3, etc | [optional] 
 **pitch_numbers** | [**list[int]**](int.md)| The pitch number of a given game. Format: 1, 2, 3, etc | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **debug** | **bool**|  | [optional] 
 **active_status** | [**PlayerActiveStatusEnum**](.md)| Whether or not a player is active | [optional] 

### Return type

[**StatContainerRestObject**](StatContainerRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outs_above_average**
> StatsRestObject get_outs_above_average(game_pk, timecode=timecode, fields=fields)

Get outs above average for the current batter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | 
timecode = 'timecode_example' # str |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get outs above average for the current batter
    api_response = api_instance.get_outs_above_average(game_pk, timecode=timecode, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_outs_above_average: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**|  | 
 **timecode** | **str**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spray_chart**
> StatsRestObject get_spray_chart(game_pk, timecode=timecode, fields=fields)

Get the spray chart info for the current batter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | 
timecode = 'timecode_example' # str |  (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)

try:
    # Get the spray chart info for the current batter
    api_response = api_instance.get_spray_chart(game_pk, timecode=timecode, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_spray_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**|  | 
 **timecode** | **str**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stolen_base_probability**
> list[int] get_stolen_base_probability(game_pk, timecode=timecode)

Get the probability of a hit for the given hit data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
game_pk = 56 # int | 
timecode = 'timecode_example' # str |  (optional)

try:
    # Get the probability of a hit for the given hit data
    api_response = api_instance.get_stolen_base_probability(game_pk, timecode=timecode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stolen_base_probability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **int**|  | 
 **timecode** | **str**|  | [optional] 

### Return type

**list[int]**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouped_stats**
> StatsRestObject grouped_stats(stats, group, person_id=person_id, team_id=team_id, team_ids=team_ids, game_type=game_type, season=season, seasons=seasons, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, metrics=metrics, game_pk=game_pk, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, batter_id=batter_id, pitcher_id=pitcher_id, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, fields=fields, sort_stat=sort_stat, order=order, player_pool=player_pool, position=position, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, exclude_traded_players=exclude_traded_players, offset=offset, limit=limit, stat_fields=stat_fields, sort_field=sort_field)

View grouped stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
metrics = [swagger_client.MetricType()] # list[MetricType] | Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
batter_team_id = [56] # list[int] | A unique identifier for the batter's team (optional)
pitcher_team_id = [56] # list[int] | A unique identifier for the pitcher's team (optional)
batter_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
pitcher_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
sit_codes = ['sit_codes_example'] # list[str] | Situation code for a given stat split. (optional)
combine_sits = true # bool | If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
sort_stat = swagger_client.BaseballStatsEnum() # BaseballStatsEnum | Baseball stat to sort splits by. (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
player_pool = swagger_client.PlayerPoolEnum() # PlayerPoolEnum | Return \"ALL\" or only \"QUALIFIED\" players based on plate appearances. (optional)
position = [swagger_client.BaseballPosition()] # list[BaseballPosition] | Position number. Format: 1, 2, 3, etc (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
games_back = 56 # int | Returns results from the last 'X' games played. (optional)
exclude_traded_players = true # bool | Excludes players who have since been traded from the input team (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
limit = 56 # int | Number of results to return (optional)
stat_fields = [swagger_client.StatField()] # list[StatField] | Baseball stat fields to populate (optional)
sort_field = swagger_client.StatField() # StatField | Baseball statField to sort on.  If no statField is given, sortField defaults to BASIC.  If 1 statField is given, that is the default sortField. (optional)

try:
    # View grouped stats
    api_response = api_instance.grouped_stats(stats, group, person_id=person_id, team_id=team_id, team_ids=team_ids, game_type=game_type, season=season, seasons=seasons, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, metrics=metrics, game_pk=game_pk, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, batter_id=batter_id, pitcher_id=pitcher_id, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, fields=fields, sort_stat=sort_stat, order=order, player_pool=player_pool, position=position, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, exclude_traded_players=exclude_traded_players, offset=offset, limit=limit, stat_fields=stat_fields, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->grouped_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | 
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **metrics** | [**list[MetricType]**](MetricType.md)| Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **batter_team_id** | [**list[int]**](int.md)| A unique identifier for the batter&#x27;s team | [optional] 
 **pitcher_team_id** | [**list[int]**](int.md)| A unique identifier for the pitcher&#x27;s team | [optional] 
 **batter_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **pitcher_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **sit_codes** | [**list[str]**](str.md)| Situation code for a given stat split. | [optional] 
 **combine_sits** | **bool**| If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **sort_stat** | [**BaseballStatsEnum**](.md)| Baseball stat to sort splits by. | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **player_pool** | [**PlayerPoolEnum**](.md)| Return \&quot;ALL\&quot; or only \&quot;QUALIFIED\&quot; players based on plate appearances. | [optional] 
 **position** | [**list[BaseballPosition]**](BaseballPosition.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **games_back** | **int**| Returns results from the last &#x27;X&#x27; games played. | [optional] 
 **exclude_traded_players** | **bool**| Excludes players who have since been traded from the input team | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **stat_fields** | [**list[StatField]**](StatField.md)| Baseball stat fields to populate | [optional] 
 **sort_field** | [**StatField**](.md)| Baseball statField to sort on.  If no statField is given, sortField defaults to BASIC.  If 1 statField is given, that is the default sortField. | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaders2**
> LeagueLeaderContainerRestObject leaders2(leader_categories=leader_categories, leader_game_types=leader_game_types, stat_group=stat_group, season=season, expand=expand, sport_id=sport_id, sport_ids=sport_ids, stats=stats, limit=limit, offset=offset, team_id=team_id, team_ids=team_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, player_pool=player_pool, stat_type=stat_type, player_active=player_active, position=position, sit_codes=sit_codes, opposing_team_id=opposing_team_id, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, group_by=group_by, fields=fields)

Get leaders for a statistic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
leader_categories = [swagger_client.PersonLeadersEnum()] # list[PersonLeadersEnum] |  (optional)
leader_game_types = [swagger_client.GameTypeEnum()] # list[GameTypeEnum] |  (optional)
stat_group = [swagger_client.StatGroup()] # list[StatGroup] |  (optional)
season = 'season_example' # str |  (optional)
expand = [swagger_client.ExpandEnum()] # list[ExpandEnum] |  (optional)
sport_id = 56 # int |  (optional)
sport_ids = [56] # list[int] |  (optional)
stats = [swagger_client.StatType()] # list[StatType] |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
team_id = 56 # int |  (optional)
team_ids = [56] # list[int] |  (optional)
league_id = 56 # int |  (optional)
league_ids = [56] # list[int] |  (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum |  (optional)
player_pool = swagger_client.PlayerPoolEnum() # PlayerPoolEnum |  (optional)
stat_type = swagger_client.StatType() # StatType |  (optional)
player_active = swagger_client.PlayerActiveStatusEnum() # PlayerActiveStatusEnum |  (optional)
position = [swagger_client.BaseballPosition()] # list[BaseballPosition] |  (optional)
sit_codes = ['sit_codes_example'] # list[str] |  (optional)
opposing_team_id = 56 # int |  (optional)
start_date = '2013-10-20' # date |  (optional)
end_date = '2013-10-20' # date |  (optional)
days_back = 56 # int |  (optional)
games_back = 56 # int |  (optional)
group_by = swagger_client.GroupByEnum() # GroupByEnum |  (optional)
fields = ['fields_example'] # list[str] |  (optional)

try:
    # Get leaders for a statistic
    api_response = api_instance.leaders2(leader_categories=leader_categories, leader_game_types=leader_game_types, stat_group=stat_group, season=season, expand=expand, sport_id=sport_id, sport_ids=sport_ids, stats=stats, limit=limit, offset=offset, team_id=team_id, team_ids=team_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, player_pool=player_pool, stat_type=stat_type, player_active=player_active, position=position, sit_codes=sit_codes, opposing_team_id=opposing_team_id, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, group_by=group_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->leaders2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leader_categories** | [**list[PersonLeadersEnum]**](PersonLeadersEnum.md)|  | [optional] 
 **leader_game_types** | [**list[GameTypeEnum]**](GameTypeEnum.md)|  | [optional] 
 **stat_group** | [**list[StatGroup]**](StatGroup.md)|  | [optional] 
 **season** | **str**|  | [optional] 
 **expand** | [**list[ExpandEnum]**](ExpandEnum.md)|  | [optional] 
 **sport_id** | **int**|  | [optional] 
 **sport_ids** | [**list[int]**](int.md)|  | [optional] 
 **stats** | [**list[StatType]**](StatType.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **team_id** | **int**|  | [optional] 
 **team_ids** | [**list[int]**](int.md)|  | [optional] 
 **league_id** | **int**|  | [optional] 
 **league_ids** | [**list[int]**](int.md)|  | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)|  | [optional] 
 **player_pool** | [**PlayerPoolEnum**](.md)|  | [optional] 
 **stat_type** | [**StatType**](.md)|  | [optional] 
 **player_active** | [**PlayerActiveStatusEnum**](.md)|  | [optional] 
 **position** | [**list[BaseballPosition]**](BaseballPosition.md)|  | [optional] 
 **sit_codes** | [**list[str]**](str.md)|  | [optional] 
 **opposing_team_id** | **int**|  | [optional] 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **days_back** | **int**|  | [optional] 
 **games_back** | **int**|  | [optional] 
 **group_by** | [**GroupByEnum**](.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**LeagueLeaderContainerRestObject**](LeagueLeaderContainerRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_stats**
> StatsRestObject metric_stats(stats, metrics, person_id=person_id, person_ids=person_ids, batter_id=batter_id, pitcher_id=pitcher_id, team_id=team_id, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, position=position, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, pitch_hand=pitch_hand, venue_id=venue_id, game_pk=game_pk, min_value=min_value, max_value=max_value, percentile=percentile, min_occurrences=min_occurrences, offset=offset, limit=limit, order=order, _date=_date, start_date=start_date, end_date=end_date, game_type=game_type, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, fields=fields, debug=debug)

View metric stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatsApi(swagger_client.ApiClient(configuration))
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes
metrics = [swagger_client.MetricType()] # list[MetricType] | Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
person_ids = [56] # list[int] | Unique Player Identifier. Format: 434538, 429665, etc (optional)
batter_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
pitcher_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
opposing_player_id = 56 # int | A unique identifier for the opposing team (optional)
position = [swagger_client.BaseballPosition()] # list[BaseballPosition] | All of the details of a player's position (optional)
event_type = [swagger_client.EventType()] # list[EventType] | Type of event (optional)
pitch_type = ['pitch_type_example'] # list[str] | Classification of pitch (fastball, curveball, etc...) (optional)
hit_trajectory = [swagger_client.HitTrajectory()] # list[HitTrajectory] | Trajectory of hit (line drive, fly ball, etc...) (optional)
bat_side = 'bat_side_example' # str | Bat side of hitter (optional)
pitch_hand = 'pitch_hand_example' # str | Handedness of pitcher (optional)
venue_id = [56] # list[int] | All of the details of a venue (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
min_value = 1.2 # float | Minimum value to filter on (optional)
max_value = 1.2 # float | Maximum value to filter on (optional)
percentile = 56 # int | Only return averages above this percentile. used for best effort plays (optional)
min_occurrences = 56 # int | Minimum occurrences to filter upon (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
limit = 56 # int | Number of results to return (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
_date = '2013-10-20' # date | Date of Game. Format: YYYY-MM-DD (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
batter_team_id = [56] # list[int] | A unique identifier for the batter's team (optional)
pitcher_team_id = [56] # list[int] | A unique identifier for the pitcher's team (optional)
fields = ['fields_example'] # list[str] | Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute (optional)
debug = true # bool |  (optional)

try:
    # View metric stats
    api_response = api_instance.metric_stats(stats, metrics, person_id=person_id, person_ids=person_ids, batter_id=batter_id, pitcher_id=pitcher_id, team_id=team_id, group=group, season=season, seasons=seasons, sport_id=sport_id, opposing_team_id=opposing_team_id, opposing_player_id=opposing_player_id, position=position, event_type=event_type, pitch_type=pitch_type, hit_trajectory=hit_trajectory, bat_side=bat_side, pitch_hand=pitch_hand, venue_id=venue_id, game_pk=game_pk, min_value=min_value, max_value=max_value, percentile=percentile, min_occurrences=min_occurrences, offset=offset, limit=limit, order=order, _date=_date, start_date=start_date, end_date=end_date, game_type=game_type, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, fields=fields, debug=debug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->metric_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | 
 **metrics** | [**list[MetricType]**](MetricType.md)| Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics | 
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **person_ids** | [**list[int]**](int.md)| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **batter_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **pitcher_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **opposing_player_id** | **int**| A unique identifier for the opposing team | [optional] 
 **position** | [**list[BaseballPosition]**](BaseballPosition.md)| All of the details of a player&#x27;s position | [optional] 
 **event_type** | [**list[EventType]**](EventType.md)| Type of event | [optional] 
 **pitch_type** | [**list[str]**](str.md)| Classification of pitch (fastball, curveball, etc...) | [optional] 
 **hit_trajectory** | [**list[HitTrajectory]**](HitTrajectory.md)| Trajectory of hit (line drive, fly ball, etc...) | [optional] 
 **bat_side** | **str**| Bat side of hitter | [optional] 
 **pitch_hand** | **str**| Handedness of pitcher | [optional] 
 **venue_id** | [**list[int]**](int.md)| All of the details of a venue | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **min_value** | **float**| Minimum value to filter on | [optional] 
 **max_value** | **float**| Maximum value to filter on | [optional] 
 **percentile** | **int**| Only return averages above this percentile. used for best effort plays | [optional] 
 **min_occurrences** | **int**| Minimum occurrences to filter upon | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **_date** | **date**| Date of Game. Format: YYYY-MM-DD | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **batter_team_id** | [**list[int]**](int.md)| A unique identifier for the batter&#x27;s team | [optional] 
 **pitcher_team_id** | [**list[int]**](int.md)| A unique identifier for the pitcher&#x27;s team | [optional] 
 **fields** | [**list[str]**](str.md)| Comma delimited list of specific fields to be returned. Format: topLevelNode, childNode, attribute | [optional] 
 **debug** | **bool**|  | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats2**
> StatsRestObject stats2(stats, group, person_id=person_id, team_id=team_id, team_ids=team_ids, game_type=game_type, season=season, seasons=seasons, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, metrics=metrics, game_pk=game_pk, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, batter_id=batter_id, pitcher_id=pitcher_id, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, fields=fields, sort_stat=sort_stat, order=order, player_pool=player_pool, position=position, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, exclude_traded_players=exclude_traded_players, offset=offset, limit=limit)

View stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
stats = [swagger_client.StatType()] # list[StatType] | Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes
group = [swagger_client.StatGroup()] # list[StatGroup] | Category of statistic to return. Available types in /api/v1/statGroups
person_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
team_id = 56 # int | Unique Team Identifier. Format: 141, 147, etc (optional)
team_ids = [56] # list[int] | Comma delimited list of Unique Team identifiers (optional)
game_type = swagger_client.GameTypeEnum() # GameTypeEnum | Type of Game. Available types in /api/v1/gameTypes (optional)
season = 'season_example' # str | Season of play (optional)
seasons = ['seasons_example'] # list[str] | Comma delimited list of Seasons of play (optional)
sport_id = 56 # int | Top level organization of a sport (optional)
sport_ids = [56] # list[int] | Comma delimited list of top level organizations of a sport (optional)
league_id = 56 # int | Unique League Identifier (optional)
league_ids = [56] # list[int] | Comma delimited list of Unique league identifiers (optional)
league_list_id = swagger_client.LeagueListsEnum() # LeagueListsEnum | Unique League List Identifier (optional)
metrics = [swagger_client.MetricType()] # list[MetricType] | Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics (optional)
game_pk = 56 # int | Unique Primary Key Representing a Game (optional)
batter_team_id = [56] # list[int] | A unique identifier for the batter's team (optional)
pitcher_team_id = [56] # list[int] | A unique identifier for the pitcher's team (optional)
batter_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
pitcher_id = 56 # int | Unique Player Identifier. Format: 434538, 429665, etc (optional)
sit_codes = ['sit_codes_example'] # list[str] | Situation code for a given stat split. (optional)
combine_sits = true # bool | If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false (optional)
opposing_team_id = 56 # int | A unique identifier for the opposing team. Must be used with Team ID (optional)
fields = ['fields_example'] # list[str] |  (optional)
sort_stat = swagger_client.BaseballStatsEnum() # BaseballStatsEnum | Baseball stat to sort splits by. (optional)
order = swagger_client.SortOrderEnum() # SortOrderEnum | The order of sorting, ascending or descending (optional)
player_pool = swagger_client.PlayerPoolEnum() # PlayerPoolEnum | Return \"ALL\" or only \"QUALIFIED\" players based on plate appearances. (optional)
position = [swagger_client.BaseballPosition()] # list[BaseballPosition] | Position number. Format: 1, 2, 3, etc (optional)
start_date = '2013-10-20' # date | Start date for range of data (must be used with end date). Format: MM/DD/YYYY (optional)
end_date = '2013-10-20' # date | End date for range of data (must be used with start date). Format: MM/DD/YYYY (optional)
days_back = 56 # int | Returns results from the last 'X' days (Starting from yesterday). (optional)
games_back = 56 # int | Returns results from the last 'X' games played. (optional)
exclude_traded_players = true # bool | Excludes players who have since been traded from the input team (optional)
offset = 56 # int | The pointer to start for a return set; used for pagination (optional)
limit = 56 # int | Number of results to return (optional)

try:
    # View stats
    api_response = api_instance.stats2(stats, group, person_id=person_id, team_id=team_id, team_ids=team_ids, game_type=game_type, season=season, seasons=seasons, sport_id=sport_id, sport_ids=sport_ids, league_id=league_id, league_ids=league_ids, league_list_id=league_list_id, metrics=metrics, game_pk=game_pk, batter_team_id=batter_team_id, pitcher_team_id=pitcher_team_id, batter_id=batter_id, pitcher_id=pitcher_id, sit_codes=sit_codes, combine_sits=combine_sits, opposing_team_id=opposing_team_id, fields=fields, sort_stat=sort_stat, order=order, player_pool=player_pool, position=position, start_date=start_date, end_date=end_date, days_back=days_back, games_back=games_back, exclude_traded_players=exclude_traded_players, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats** | [**list[StatType]**](StatType.md)| Type of statistics. Format: Individual, Team, Career, etc. Available types in /api/v1/statTypes | 
 **group** | [**list[StatGroup]**](StatGroup.md)| Category of statistic to return. Available types in /api/v1/statGroups | 
 **person_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **team_id** | **int**| Unique Team Identifier. Format: 141, 147, etc | [optional] 
 **team_ids** | [**list[int]**](int.md)| Comma delimited list of Unique Team identifiers | [optional] 
 **game_type** | [**GameTypeEnum**](.md)| Type of Game. Available types in /api/v1/gameTypes | [optional] 
 **season** | **str**| Season of play | [optional] 
 **seasons** | [**list[str]**](str.md)| Comma delimited list of Seasons of play | [optional] 
 **sport_id** | **int**| Top level organization of a sport | [optional] 
 **sport_ids** | [**list[int]**](int.md)| Comma delimited list of top level organizations of a sport | [optional] 
 **league_id** | **int**| Unique League Identifier | [optional] 
 **league_ids** | [**list[int]**](int.md)| Comma delimited list of Unique league identifiers | [optional] 
 **league_list_id** | [**LeagueListsEnum**](.md)| Unique League List Identifier | [optional] 
 **metrics** | [**list[MetricType]**](MetricType.md)| Name of metric(s) for metric log stats.  Available metrics in /api/v1/metrics | [optional] 
 **game_pk** | **int**| Unique Primary Key Representing a Game | [optional] 
 **batter_team_id** | [**list[int]**](int.md)| A unique identifier for the batter&#x27;s team | [optional] 
 **pitcher_team_id** | [**list[int]**](int.md)| A unique identifier for the pitcher&#x27;s team | [optional] 
 **batter_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **pitcher_id** | **int**| Unique Player Identifier. Format: 434538, 429665, etc | [optional] 
 **sit_codes** | [**list[str]**](str.md)| Situation code for a given stat split. | [optional] 
 **combine_sits** | **bool**| If true, gathers stats where all of the situational criteria are met. If false, returns stats where any of the situational criteria are met. Default: false | [optional] 
 **opposing_team_id** | **int**| A unique identifier for the opposing team. Must be used with Team ID | [optional] 
 **fields** | [**list[str]**](str.md)|  | [optional] 
 **sort_stat** | [**BaseballStatsEnum**](.md)| Baseball stat to sort splits by. | [optional] 
 **order** | [**SortOrderEnum**](.md)| The order of sorting, ascending or descending | [optional] 
 **player_pool** | [**PlayerPoolEnum**](.md)| Return \&quot;ALL\&quot; or only \&quot;QUALIFIED\&quot; players based on plate appearances. | [optional] 
 **position** | [**list[BaseballPosition]**](BaseballPosition.md)| Position number. Format: 1, 2, 3, etc | [optional] 
 **start_date** | **date**| Start date for range of data (must be used with end date). Format: MM/DD/YYYY | [optional] 
 **end_date** | **date**| End date for range of data (must be used with start date). Format: MM/DD/YYYY | [optional] 
 **days_back** | **int**| Returns results from the last &#x27;X&#x27; days (Starting from yesterday). | [optional] 
 **games_back** | **int**| Returns results from the last &#x27;X&#x27; games played. | [optional] 
 **exclude_traded_players** | **bool**| Excludes players who have since been traded from the input team | [optional] 
 **offset** | **int**| The pointer to start for a return set; used for pagination | [optional] 
 **limit** | **int**| Number of results to return | [optional] 

### Return type

[**StatsRestObject**](StatsRestObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

