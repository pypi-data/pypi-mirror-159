import requests
import pandas as pd
from typing import List, Dict, Union
from .agsi_mappings import AGSICompany, AGSIStorage, AGSICountry, lookup_company, lookup_storage, lookup_country
from .alsi_mappings import ALSITerminal, ALSILSO, ALSICountry, lookup_terminal, lookup_lso, lookup_country as lookup_country_alsi
from .exceptions import NoMatchingDataError
from enum import Enum

__title__ = "gie-py"
__version__ = "0.2.3"
__author__ = "Frank Boerman"
__license__ = "MIT"


class APIType(str, Enum):
    ASGI = "https://agsi.gie.eu/api/data/"
    ALSI = "https://alsi.gie.eu/api/data/"


class GieRawClient:
    def __init__(self, api_key):
        self.s = requests.Session()
        self.s.headers.update({
            'user-agent': 'gie-py (github.com/fboerman/gie-py)',
            'x-key': api_key
        })

    def _fetch(self, url: str, t: APIType,
               start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]):
        if type(start) != pd.Timestamp:
            start = pd.Timestamp(start)
        if type(end) != pd.Timestamp:
            end = pd.Timestamp(end)

        def _fetch_one(start, end):
            r = self.s.get(t.value + url, params={
                'from': start.strftime('%Y-%m-%d'),
                'till': end.strftime('%Y-%m-%d')
            })
            r.raise_for_status()

            if t == APIType.ASGI:
                return r.json()['data']
            else:
                return r.json()

        if t == APIType.ASGI and (end - start).days > 30:
            data = []
            start_selected = end - pd.Timedelta(days=30)
            while start_selected > start:
                data += _fetch_one(start_selected, start_selected + pd.Timedelta(days=30))
                start_selected -= pd.Timedelta(days=31)
            data += _fetch_one(start, (start_selected + pd.Timedelta(days=30)))
        elif (end - start).days == 0:
            # only one day being queried, the api will return zero data (weird!)
            # so automatically append one day and then remove it from the result
            end += pd.Timedelta(days=1)
            data = _fetch_one(start, end)[:1]
        else:
            data = _fetch_one(start, end)

        if len(data) == 0:
            raise NoMatchingDataError

        return data

    def query_gas_storage(self, storage: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        storage = lookup_storage(storage)
        return self._fetch(storage.get_url(), APIType.ASGI, start=start, end=end)

    def query_gas_company(self, company: Union[AGSICompany, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        company = lookup_company(company)
        return self._fetch(company.get_url(), APIType.ASGI, start=start, end=end)

    def query_gas_country(self, country: Union[AGSICountry, str],
                      start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        country = lookup_country(country)
        return self._fetch(country.get_url(), APIType.ASGI, start=start, end=end)

    def query_lng_terminal(self, terminal: Union[ALSITerminal, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        terminal = lookup_terminal(terminal)
        return self._fetch(terminal.get_url(), APIType.ALSI, start=start, end=end)

    def query_lng_lso(self, lso: Union[ALSILSO, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        lso = lookup_lso(lso)
        return self._fetch(lso.get_url(), APIType.ALSI, start=start, end=end)

    def query_lng_country(self, country: Union[ALSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        country = lookup_country_alsi(country)
        return self._fetch(country.get_url(), APIType.ALSI, start=start, end=end)


class GiePandasClient(GieRawClient):
    def _fix_agsi_dataframe(self, data):
        df = pd.DataFrame(data).drop(columns=['name', 'code', 'url', 'info'])
        df = df.loc[df['status'] != 'N']
        if len(df) == 0:
            raise NoMatchingDataError
        df['gasDayStart'] = pd.to_datetime(df['gasDayStart'])
        df = df.set_index('gasDayStart')
        # status is only str column, save it for now, convert whole dataframe to float, restore status
        status = df['status'].copy()
        df = df.drop(columns=['status']).replace('-', '0').astype(float)
        df['status'] = status
        return df

    def _fix_alsi_dataframe(self, data):
        df = pd.DataFrame(data).drop(columns=['info'])
        df['gasDayStartedOn'] = pd.to_datetime(df['gasDayStartedOn'])
        df = df.set_index('gasDayStartedOn')
        # status is only str column, save it for now, convert whole dataframe to float, restore status
        status = df['status'].copy()
        df = df.drop(columns=['status']).astype(float)
        df['status'] = status
        return df

    def query_gas_storage(self, storage: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_agsi_dataframe(
            super().query_gas_storage(storage=storage, start=start, end=end)
        )

    def query_gas_company(self, company: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_agsi_dataframe(
            super().query_gas_company(company=company, start=start, end=end)
        )

    def query_gas_country(self, country: Union[AGSICountry, str],
                      start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_agsi_dataframe(
            super().query_gas_country(country=country, start=start, end=end)
        )

    def query_lng_terminal(self, terminal: Union[ALSITerminal, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_alsi_dataframe(
            super().query_lng_terminal(terminal=terminal, start=start, end=end)
        )

    def query_lng_lso(self, lso: Union[ALSILSO, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self._fix_alsi_dataframe(
            super().query_lng_lso(lso=lso, start=start, end=end)
        )

    def query_lng_country(self, country: Union[ALSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> List[Dict]:
        return self._fix_alsi_dataframe(
            super().query_lng_country(country=country, start=start, end=end)
        )
