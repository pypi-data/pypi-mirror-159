import fastf1
from fastf1.plotting import DRIVER_COLORS, DRIVER_TRANSLATE, setup_mpl
import pandas as pd
import traceback

from f1tel_gui.utils import get_cache_path, get_current_season

class F1tel:

    def __init__(self, season: int=get_current_season(), circuit: str=1, session: str="FP1", disable_cache: bool=False):
        if season is None or circuit is None or session is None:
            raise ValueError("season, circuit and session must be set")
        self.season = season
        self.circuit = circuit
        self.session = session
        self.disable_cache = disable_cache

        if not self.disable_cache:
            fastf1.Cache.enable_cache(get_cache_path())
        else:
            fastf1.Cache.disable()

        

        try:
            print("[-] Loading F1 session")
            print("[-] Season: {}".format(self.season))
            print("[-] Circuit: {}".format(self.circuit))
            print("[-] Session: {}".format(self.session))
            self.f1 = fastf1.get_session(self.season, self.circuit, self.session)
            self.f1.load()
            self.laps = self.f1.laps
        except Exception as e:
            print("[!] Exception: {}".format(traceback.format_exc()))
            raise e

    def get_schedule_by_season(season: int):
        current_timestamp = pd.Timestamp.now()
        events =fastf1.get_event_schedule(season)
        return events.loc[events.Session1Date<=str(current_timestamp), :]
    
    def get_schedule_by_circuit(self):
        return self.f1.event

    def get_drivers_by_session(self):

        drivers_df = pd.DataFrame(fastf1.api.driver_info(self.f1.api_path)).transpose()

        drivers_tla=[]

        for driver in self.f1.drivers:
            drivers_tla.append(drivers_df.loc[str(driver), "Tla"])

        return drivers_tla

    def get_driver_color(self, driver: str):
        return DRIVER_COLORS[DRIVER_TRANSLATE[driver]]

    def get_driver_telemetry(self, driver: str, is_fastestlap: bool=False, lap_number: int=1):
        driver_perf = self.laps.pick_driver(driver)
        if is_fastestlap:
            return driver_perf.pick_fastest().get_telemetry()
        elif lap_number in self.laps["LapNumber"].to_list():
            if lap_number < 1:
                lap_number = 1
            if lap_number > max(driver_perf["LapNumber"].unique()):
                return pd.DataFrame()
            else:
                return driver_perf.loc[driver_perf['LapNumber'] == lap_number].get_telemetry()

    def get_max_laps(self):
        return max(self.laps["LapNumber"].unique())