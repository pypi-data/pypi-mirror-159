from typing import Optional

from sleeper.api.APIClient import APIClient
from sleeper.enum.RosterPosition import RosterPosition
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.enum.Status import Status
from sleeper.model.FromPlayoffMatchup import FromPlayoffMatchup
from sleeper.model.League import League
from sleeper.model.LeagueSettings import LeagueSettings
from sleeper.model.Matchup import Matchup
from sleeper.model.PlayoffMatchup import PlayoffMatchup
from sleeper.model.Roster import Roster
from sleeper.model.RosterSettings import RosterSettings
from sleeper.model.ScoringSettings import ScoringSettings
from sleeper.util.ConfigReader import ConfigReader


class LeagueAPIClient(APIClient):
    __LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
    __LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
    __USER_ROUTE = ConfigReader.get("api", "user_route")
    __ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
    __MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
    __WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")
    __LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
    __SPORT = Sport.NFL  # For now, only NFL is supported in the API, when other sports are added, this can be passed in

    @staticmethod
    def __build_settings_object(settings_dict: dict) -> LeagueSettings:
        return LeagueSettings(waiver_type=settings_dict["waiver_type"],
                              waiver_day_of_week=settings_dict["waiver_day_of_week"],
                              waiver_clear_days=settings_dict["waiver_clear_days"],
                              waiver_budget=settings_dict["waiver_budget"],
                              type=settings_dict["type"],
                              trade_review_days=settings_dict["trade_review_days"],
                              trade_deadline=settings_dict["trade_deadline"],
                              start_week=settings_dict["start_week"],
                              reserve_slots=settings_dict["reserve_slots"],
                              reserve_allow_out=settings_dict["reserve_allow_out"],
                              playoff_week_start=settings_dict["playoff_week_start"],
                              playoff_teams=settings_dict["playoff_teams"],
                              pick_trading=settings_dict["pick_trading"],
                              offseason_adds=settings_dict["offseason_adds"],
                              num_teams=settings_dict["num_teams"],
                              max_keepers=settings_dict["max_keepers"],
                              leg=settings_dict["leg"],
                              last_scored_leg=settings_dict["last_scored_leg"],
                              last_report=settings_dict["last_report"],
                              draft_rounds=settings_dict["draft_rounds"])

    @staticmethod
    def __build_scoring_settings_object(scoring_settings_dict: dict) -> ScoringSettings:
        return ScoringSettings(yds_allow_0_100=scoring_settings_dict["yds_allow_0_100"],
                               yds_allow_100_199=scoring_settings_dict["yds_allow_100_199"],
                               yds_allow_200_299=scoring_settings_dict["yds_allow_200_299"],
                               yds_allow_300_349=scoring_settings_dict["yds_allow_300_349"],
                               yds_allow_350_399=scoring_settings_dict["yds_allow_350_399"],
                               yds_allow_400_449=scoring_settings_dict["yds_allow_400_449"],
                               yds_allow_450_499=scoring_settings_dict["yds_allow_450_499"],
                               yds_allow_500_549=scoring_settings_dict["yds_allow_500_549"],
                               yds_allow_550p=scoring_settings_dict["yds_allow_550p"],
                               fgm=scoring_settings_dict["fgm"],
                               fgm_0_19=scoring_settings_dict["fgm_0_19"],
                               fgm_20_29=scoring_settings_dict["fgm_20_29"],
                               fgm_30_39=scoring_settings_dict["fgm_30_39"],
                               fgm_40_49=scoring_settings_dict["fgm_40_49"],
                               fgm_50p=scoring_settings_dict["fgm_50p"],
                               fgmiss=scoring_settings_dict["fgmiss"],
                               fgmiss_0_19=scoring_settings_dict["fgmiss_0_19"],
                               fgmiss_20_29=scoring_settings_dict["fgmiss_20_29"],
                               fgmiss_30_39=scoring_settings_dict["fgmiss_30_39"],
                               fgmiss_40_49=scoring_settings_dict["fgmiss_40_49"],
                               fgmiss_50p=scoring_settings_dict["fgmiss_50p"],
                               fg_ret_yd=scoring_settings_dict["fg_ret_yd"],
                               pass_2pt=scoring_settings_dict["pass_2pt"],
                               pass_int=scoring_settings_dict["pass_int"],
                               pass_sack=scoring_settings_dict["pass_sack"],
                               pass_cmp=scoring_settings_dict["pass_cmp"],
                               pass_cmp_40p=scoring_settings_dict["pass_cmp_40p"],
                               pass_inc=scoring_settings_dict["pass_inc"],
                               pass_att=scoring_settings_dict["pass_att"],
                               pass_yd=scoring_settings_dict["pass_yd"],
                               pass_td=scoring_settings_dict["pass_td"],
                               def_pass_def=scoring_settings_dict["def_pass_def"],
                               def_td=scoring_settings_dict["def_td"],
                               def_st_fum_rec=scoring_settings_dict["def_st_fum_rec"],
                               def_st_td=scoring_settings_dict["def_st_td"],
                               def_st_ff=scoring_settings_dict["def_st_ff"],
                               def_2pt=scoring_settings_dict["def_2pt"],
                               st_fum_rec=scoring_settings_dict["st_fum_rec"],
                               st_ff=scoring_settings_dict["st_ff"],
                               st_tkl_solo=scoring_settings_dict["st_tkl_solo"],
                               st_td=scoring_settings_dict["st_td"],
                               fum_rec=scoring_settings_dict["fum_rec"],
                               fum_lost=scoring_settings_dict["fum_lost"],
                               fum=scoring_settings_dict["fum"],
                               fum_ret_yd=scoring_settings_dict["fum_ret_yd"],
                               idp_safe=scoring_settings_dict["idp_safe"],
                               idp_ff=scoring_settings_dict["idp_ff"],
                               idp_blk_kick=scoring_settings_dict["idp_blk_kick"],
                               idp_int=scoring_settings_dict["idp_int"],
                               idp_tkl=scoring_settings_dict["idp_tkl"],
                               idp_def_td=scoring_settings_dict["idp_def_td"],
                               idp_pass_def=scoring_settings_dict["idp_pass_def"],
                               idp_fum_rec=scoring_settings_dict["idp_fum_rec"],
                               idp_sack=scoring_settings_dict["idp_sack"],
                               idp_tkl_ast=scoring_settings_dict["idp_tkl_ast"],
                               idp_tkl_solo=scoring_settings_dict["idp_tkl_solo"],
                               rush_att=scoring_settings_dict["rush_att"],
                               pts_allow_0=scoring_settings_dict["pts_allow_0"],
                               pts_allow_1_6=scoring_settings_dict["pts_allow_1_6"],
                               pts_allow_7_13=scoring_settings_dict["pts_allow_7_13"],
                               pts_allow_14_20=scoring_settings_dict["pts_allow_14_20"],
                               pts_allow_21_27=scoring_settings_dict["pts_allow_21_27"],
                               pts_allow_28_34=scoring_settings_dict["pts_allow_28_34"],
                               pts_allow_35p=scoring_settings_dict["pts_allow_35p"],
                               rush_40p=scoring_settings_dict["rush_40p"],
                               rush_2pt=scoring_settings_dict["rush_2pt"],
                               rush_yd=scoring_settings_dict["rush_yd"],
                               rush_td=scoring_settings_dict["rush_td"],
                               bonus_rush_yd_100=scoring_settings_dict["bonus_rush_yd_100"],
                               bonus_rush_yd_200=scoring_settings_dict["bonus_rush_yd_200"],
                               bonus_rec_yd_100=scoring_settings_dict["bonus_rec_yd_100"],
                               bonus_rec_yd_200=scoring_settings_dict["bonus_rec_yd_200"],
                               bonus_pass_yd_300=scoring_settings_dict["bonus_pass_yd_300"],
                               bonus_pass_yd_400=scoring_settings_dict["bonus_pass_yd_400"],
                               rec_yd=scoring_settings_dict["rec_yd"],
                               rec_2pt=scoring_settings_dict["rec_2pt"],
                               rec=scoring_settings_dict["rec"],
                               rec_td=scoring_settings_dict["rec_td"],
                               rec_40p=scoring_settings_dict["rec_40p"],
                               tkl=scoring_settings_dict["tkl"],
                               tkl_loss=scoring_settings_dict["tkl_loss"],
                               tkl_solo=scoring_settings_dict["tkl_solo"],
                               tkl_ast=scoring_settings_dict["tkl_ast"],
                               int_ret_yd=scoring_settings_dict["int_ret_yd"],
                               int=scoring_settings_dict["int"],
                               pr_td=scoring_settings_dict["pr_td"],
                               pr_yd=scoring_settings_dict["pr_yd"],
                               sack_yd=scoring_settings_dict["sack_yd"],
                               sack=scoring_settings_dict["sack"],
                               kr_yd=scoring_settings_dict["kr_yd"],
                               kr_td=scoring_settings_dict["kr_td"],
                               blk_kick=scoring_settings_dict["blk_kick"],
                               blk_kick_ret_yd=scoring_settings_dict["blk_kick_ret_yd"],
                               xpmiss=scoring_settings_dict["xpmiss"],
                               ff=scoring_settings_dict["ff"],
                               qb_hit=scoring_settings_dict["qb_hit"],
                               xpm=scoring_settings_dict["xpm"],
                               safe=scoring_settings_dict["safe"])

    @classmethod
    def __build_league_object(cls, league_dict: dict) -> League:
        return League(total_rosters=league_dict["total_rosters"],
                      status=Status.from_str(league_dict["status"]),
                      sport=Sport.from_str(league_dict["sport"]),
                      settings=cls.__build_settings_object(league_dict["settings"]),
                      season_type=SeasonType.from_str(league_dict["season_type"]),
                      season=league_dict["season"],
                      scoring_settings=cls.__build_scoring_settings_object(league_dict["scoring_settings"]),
                      roster_positions=[RosterPosition.from_str(roster_position) for roster_position in
                                        league_dict["roster_positions"]],
                      previous_league_id=league_dict["previous_league_id"],
                      name=league_dict["name"],
                      league_id=league_dict["league_id"],
                      draft_id=league_dict["draft_id"],
                      avatar=league_dict["avatar"])

    @classmethod
    def __build_leagues_list(cls, league_dict_list: dict) -> list[League]:
        leagues = list()
        for league_dict in league_dict_list:
            leagues.append(cls.__build_league_object(league_dict))
        return leagues

    @classmethod
    def __build_roster_settings_object(cls, roster_settings_dict: dict) -> RosterSettings:
        return RosterSettings(wins=roster_settings_dict["wins"],
                              waiver_position=roster_settings_dict["waiver_position"],
                              waiver_budget_used=roster_settings_dict["waiver_budget_used"],
                              total_moves=roster_settings_dict["total_moves"],
                              ties=roster_settings_dict["ties"],
                              losses=roster_settings_dict["losses"],
                              fpts_decimal=roster_settings_dict["fpts_decimal"],
                              fpts_against_decimal=roster_settings_dict["fpts_against_decimal"],
                              fpts_against=roster_settings_dict["fpts_against"],
                              fpts=roster_settings_dict["fpts"])

    @classmethod
    def __build_roster_object(cls, roster_dict: dict) -> Roster:
        return Roster(starters=roster_dict["starters"],
                      settings=cls.__build_roster_settings_object(roster_dict["settings"]),
                      roster_id=roster_dict["roster_id"],
                      reserve=roster_dict["reserve"],
                      players=roster_dict["players"],
                      owner_id=roster_dict["owner_id"],
                      league_id=roster_dict["league_id"])

    @classmethod
    def __build_rosters_list(cls, roster_dict_list: dict) -> list[Roster]:
        rosters = list()
        for roster_dict in roster_dict_list:
            rosters.append(cls.__build_roster_object(roster_dict))
        return rosters

    @classmethod
    def __build_matchup_object(cls, matchup_object_dict: dict) -> Matchup:
        return Matchup(starters=matchup_object_dict["starters"],
                       roster_id=matchup_object_dict["roster_id"],
                       players=matchup_object_dict["players"],
                       matchup_id=matchup_object_dict["matchup_id"],
                       points=matchup_object_dict["points"],
                       custom_points=matchup_object_dict["custom_points"])

    @classmethod
    def __build_matchups_list(cls, matchup_dict_list: dict) -> list[Matchup]:
        matchups = list()
        for matchup_dict in matchup_dict_list:
            matchups.append(cls.__build_matchup_object(matchup_dict))
        return matchups

    @classmethod
    def __build_from_playoff_matchup_object(cls, from_playoff_matchup_object: Optional[dict]) -> Optional[
        FromPlayoffMatchup]:
        if from_playoff_matchup_object is None:
            return None
        return FromPlayoffMatchup(won_matchup_id=from_playoff_matchup_object.get("w", None),
                                  lost_matchup_id=from_playoff_matchup_object.get("l", None))

    @classmethod
    def __build_playoff_matchup_object(cls, playoff_matchup_object: dict) -> PlayoffMatchup:
        return PlayoffMatchup(round=playoff_matchup_object["r"],
                              matchup_id=playoff_matchup_object["m"],
                              team_1_roster_id=playoff_matchup_object["t1"],
                              team_2_roster_id=playoff_matchup_object["t2"],
                              winning_roster_id=playoff_matchup_object["w"],
                              losing_roster_id=playoff_matchup_object["l"],
                              team_1_from=cls.__build_from_playoff_matchup_object(
                                  playoff_matchup_object.get("t1_from", None)),
                              team_2_from=cls.__build_from_playoff_matchup_object(
                                  playoff_matchup_object.get("t2_from", None)))

    @classmethod
    def __build_playoff_matchups_list(cls, playoff_matchup_dict_list: dict) -> list[PlayoffMatchup]:
        playoff_matchups = list()
        for playoff_matchup_dict in playoff_matchup_dict_list:
            playoff_matchups.append(cls.__build_playoff_matchup_object(playoff_matchup_dict))
        return playoff_matchups

    @classmethod
    def get_league(cls, *, league_id: str) -> League:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id)
        return cls.__build_league_object(cls._get(url))

    @classmethod
    def get_user_leagues_for_year(cls, *, user_id: str, year: str) -> list[League]:
        url = cls._build_route(cls.__USER_ROUTE, user_id, cls.__LEAGUES_ROUTE, cls.__SPORT.value.lower(), year)
        return cls.__build_leagues_list(cls._get(url))

    @classmethod
    def get_rosters(cls, *, league_id: str) -> list[Roster]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__ROSTERS_ROUTE)
        return cls.__build_rosters_list(cls._get(url))

    @classmethod
    def get_matchups_for_week(cls, *, league_id: str, week: int) -> list[Matchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__MATCHUPS_ROUTE, week)
        return cls.__build_matchups_list(cls._get(url))

    @classmethod
    def get_winners_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__WINNERS_BRACKET_ROUTE)
        return cls.__build_playoff_matchups_list(cls._get(url))

    @classmethod
    def get_losers_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__LOSERS_BRACKET_ROUTE)
        return cls.__build_playoff_matchups_list(cls._get(url))
