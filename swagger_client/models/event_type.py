# coding: utf-8

"""
    Stats API Documentation

    Official API for Major League Baseball.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    GAME_START = "game_start"
    GAME_FINISHED = "game_finished"
    BALL = "ball"
    INTENT_BALL = "intent_ball"
    PITCHOUT = "pitchout"
    BLOCKED_BALL = "blocked_ball"
    AUTOMATIC_BALL = "automatic_ball"
    CALLED_STRIKE = "called_strike"
    SWINGING_STRIKE = "swinging_strike"
    FOUL = "foul"
    FOUL_TIP = "foul_tip"
    FOUL_BUNT = "foul_bunt"
    BUNT_FOUL_TIP = "bunt_foul_tip"
    MISSED_BUNT = "missed_bunt"
    SWINGING_PITCHOUT = "swinging_pitchout"
    FOUL_PITCHOUT = "foul_pitchout"
    SWINGING_STRIKE_BLOCKED = "swinging_strike_blocked"
    UNKNOWN_STRIKE = "unknown_strike"
    AUTOMATIC_STRIKE = "automatic_strike"
    HIT_INTO_PLAY = "hit_into_play"
    HIT_INTO_PLAY_NO_OUT = "hit_into_play_no_out"
    HIT_INTO_PLAY_SCORE = "hit_into_play_score"
    PITCHOUT_HIT_INTO_PLAY = "pitchout_hit_into_play"
    PITCHOUT_HIT_INTO_PLAY_NO_OUT = "pitchout_hit_into_play_no_out"
    PITCHOUT_HIT_INTO_PLAY_SCORE = "pitchout_hit_into_play_score"
    PICKOFF_ATTEMPT_1B = "pickoff_attempt_1b"
    PICKOFF_ATTEMPT_2B = "pickoff_attempt_2b"
    PICKOFF_ATTEMPT_3B = "pickoff_attempt_3b"
    PICKOFF_1B = "pickoff_1b"
    PICKOFF_2B = "pickoff_2b"
    PICKOFF_3B = "pickoff_3b"
    PITCHER_STEP_OFF = "pitcher_step_off"
    PICKOFF_ERROR_1B = "pickoff_error_1b"
    PICKOFF_ERROR_2B = "pickoff_error_2b"
    PICKOFF_ERROR_3B = "pickoff_error_3b"
    BATTER_TIMEOUT = "batter_timeout"
    MOUND_VISIT = "mound_visit"
    NO_PITCH = "no_pitch"
    SINGLE = "single"
    DOUBLE = "double"
    TRIPLE = "triple"
    HOME_RUN = "home_run"
    DOUBLE_PLAY = "double_play"
    FIELD_ERROR = "field_error"
    ERROR = "error"
    FIELD_OUT = "field_out"
    FIELDERS_CHOICE = "fielders_choice"
    FIELDERS_CHOICE_OUT = "fielders_choice_out"
    FORCE_OUT = "force_out"
    GROUNDED_INTO_DOUBLE_PLAY = "grounded_into_double_play"
    GROUNDED_INTO_TRIPLE_PLAY = "grounded_into_triple_play"
    STRIKEOUT = "strikeout"
    STRIKE_OUT = "strike_out"
    STRIKEOUT_DOUBLE_PLAY = "strikeout_double_play"
    STRIKEOUT_TRIPLE_PLAY = "strikeout_triple_play"
    TRIPLE_PLAY = "triple_play"
    SAC_FLY = "sac_fly"
    CATCHER_INTERF = "catcher_interf"
    BATTER_INTERFERENCE = "batter_interference"
    FIELDER_INTERFERENCE = "fielder_interference"
    RUNNER_INTERFERENCE = "runner_interference"
    FAN_INTERFERENCE = "fan_interference"
    RUN = "run"
    BATTER_TURN = "batter_turn"
    EJECTION = "ejection"
    CS_DOUBLE_PLAY = "cs_double_play"
    DEFENSIVE_INDIFF = "defensive_indiff"
    SAC_FLY_DOUBLE_PLAY = "sac_fly_double_play"
    SAC_BUNT = "sac_bunt"
    SAC_BUNT_DOUBLE_PLAY = "sac_bunt_double_play"
    WALK = "walk"
    INTENT_WALK = "intent_walk"
    HIT_BY_PITCH = "hit_by_pitch"
    PLAY_BY_PLAY = "play_by_play"
    PLAY_BY_PLAY_EXTRA = "play_by_play_extra"
    INJURY = "injury"
    BETWEEN_INNINGS = "between_innings"
    PLATE_APPEARANCE = "plate_appearance"
    OS_RULING_PENDING_PRIOR = "os_ruling_pending_prior"
    OS_RULING_PENDING_PRIMARY = "os_ruling_pending_primary"
    AT_BAT_START = "at_bat_start"
    RUNNER_MOVEMENT = "runner_movement"
    PASSED_BALL = "passed_ball"
    OTHER_ADVANCE = "other_advance"
    RUNNER_DOUBLE_PLAY = "runner_double_play"
    RUNNER_PLACED = "runner_placed"
    LEFT_ON_BASE = "left_on_base"
    PITCHING_SUBSTITUTION = "pitching_substitution"
    RELIEF_NO_OUT = "relief_no_out"
    OFFENSIVE_SUBSTITUTION = "offensive_substitution"
    DEFENSIVE_SWITCH = "defensive_switch"
    UMPIRE_SUBSTITUTION = "umpire_substitution"
    PITCHER_SWITCH = "pitcher_switch"
    REPLAY_MANAGER = "replay_manager"
    REPLAY_UMPIRE = "replay_umpire"
    PITCH_CHALLENGE = "pitch_challenge"
    GAME_ADVISORY = "game_advisory"
    STOLEN_BASE = "stolen_base"
    STOLEN_BASE_2B = "stolen_base_2b"
    STOLEN_BASE_3B = "stolen_base_3b"
    STOLEN_BASE_HOME = "stolen_base_home"
    CAUGHT_STEALING = "caught_stealing"
    CAUGHT_STEALING_2B = "caught_stealing_2b"
    CAUGHT_STEALING_3B = "caught_stealing_3b"
    CAUGHT_STEALING_HOME = "caught_stealing_home"
    DEFENSIVE_SUBSTITUTION = "defensive_substitution"
    PICKOFF_CAUGHT_STEALING_2B = "pickoff_caught_stealing_2b"
    PICKOFF_CAUGHT_STEALING_3B = "pickoff_caught_stealing_3b"
    PICKOFF_CAUGHT_STEALING_HOME = "pickoff_caught_stealing_home"
    BALK = "balk"
    FORCED_BALK = "forced_balk"
    WILD_PITCH = "wild_pitch"
    OTHER_OUT = "other_out"
    EMPTY = ""
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """EventType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EventType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
