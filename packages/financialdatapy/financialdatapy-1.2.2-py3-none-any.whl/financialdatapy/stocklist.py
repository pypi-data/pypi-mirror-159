"""This module retrieves stock lists."""
from abc import ABC, abstractmethod
from functools import cached_property
from io import BytesIO
import json
import pandas as pd
import re
from string import capwords
import xmltodict
from zipfile import ZipFile
from financialdatapy.dartapi import OpenDart
from financialdatapy.exception import DartError
from financialdatapy.exception import EmptyDataFrameError
from financialdatapy.request import Request


class StockList(ABC):
    """Abstract class representing stock list of a stock exchange."""

    @cached_property
    def stock_list(self) -> pd.DataFrame:
        return self.get_stock_list()

    @abstractmethod
    def get_stock_list(self) -> pd.DataFrame:
        pass


class UsStockList(StockList):
    """Class representing stock list in US exchange."""

    def get_stock_list(self) -> pd.DataFrame:
        """Get a list of companies CIK(Central Index Key) from SEC.

        The list also contains ticker of a company.

        :return: Dataframe with CIK, company name, and ticker for its columns.
        :rtype: pandas.DataFrame
        """
        url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        res = Request(url)
        cik_data = res.response_data('json')

        cik_list = pd.DataFrame(cik_data['data'], columns=cik_data['fields'])

        cik_list['exchange'] = cik_list['exchange'].str.upper()
        exchange = cik_list['exchange']
        cik_list = cik_list[(exchange == 'NASDAQ') | (exchange == 'NYSE')]
        cik_list = cik_list.reset_index(drop=True)
        cik_list = cik_list.drop('exchange', axis=1)

        cik_list['cik'] = cik_list['cik'].astype(str)

        # remove all characters after '\' or '/' in a company name
        # ex) Qualcomm inc\de -> Qualcomm inc
        pattern = r'\s?(\/|\\)[a-zA-Z]*'
        regex = re.compile(pattern, flags=re.I)
        cik_list['name'] = [regex.sub('', x) for x in cik_list['name']]

        cik_list['name'] = [capwords(x) for x in cik_list['name']]

        return cik_list

    def search_cik(self, symbol: str) -> str:
        """Search CIK of specific a company.

        :param symbol: Company symbol to search.
        :type symbol: str
        :return: CIK of the company searching for.
        :rtype: str
        """
        symbol_uppercase = symbol.upper()
        cik_list = self.stock_list
        symbol_df = cik_list[cik_list['ticker'] == symbol_uppercase]
        if symbol_df.empty:
            raise EmptyDataFrameError('Cannot search for the symbol.')
        cik = symbol_df['cik'].item()

        # cik number received from source excludes 0s that comes first.
        # Since cik is a 10-digit number, concatenate 0s.
        zeros = 10 - len(str(cik))
        cik = ('0' * zeros) + str(cik)

        return cik


class KorStockList(StockList):
    """This class represents stock list in KOR exchange."""

    def get_stock_list(self) -> pd.DataFrame:
        """Retrieve company code list of stocks listed in Korea Exchange.

        :raises DartError: Failed in getting data from opendart.fss.or.kr.
        :return: List of company codes.
        :rtype: pandas.DataFrame
        """
        open_dart = OpenDart()
        corp_code_file = open_dart.get_corp_code_file()
        try:
            xml_zip_file = ZipFile(BytesIO(corp_code_file))
            extracted_filename = 'CORPCODE.xml'
            xml_file = xml_zip_file.read(extracted_filename).decode('utf-8')
            raw_corp_code = xmltodict.parse(xml_file)
            encoded_corp_code = json.dumps(raw_corp_code)
            corp_code_list = json.loads(encoded_corp_code)
        except Exception:
            raise DartError('Failed in getting data from Dart.')
        else:
            corp_code_list = pd.DataFrame(corp_code_list['result']['list'])
            corp_code_list.dropna(inplace=True)
            return corp_code_list
    
    def search_corp_code(self, symbol: str) -> str:
        """Get corporate code from dart.fss.or.kr.

        :param symbol: Symbol of a company/stock.
        :type symbol: str
        :return: Corporate code.
        :rtype: str
        """
        result = self.stock_list[self.stock_list['stock_code'] == symbol]
        if result.empty:
            raise EmptyDataFrameError('Cannot search for the symbol.')
        corp_code = result.get('corp_code').item()
        return corp_code

    @staticmethod
    def search_stock_code(comp_name: str) -> str:
        """Search stock code with company name in dart.fss.or.kr.

        :param comp_name: Company name.
        :type comp_name: str
        :return: Stock code.
        :rtype: str
        """
        url = 'https://kind.krx.co.kr/common/searchcorpname.do'
        data = {
            'method': 'searchCorpNameJson',
            'searchCodeType': 'char',
            'searchCorpName': comp_name,
        }
        headers = {
            'User-Agent': 'Mozilla',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        res = Request(url, method='post', headers=headers, data=data)
        comp_info_first_result = res.response_data('json')[0]
        company_code = comp_info_first_result['repisusrtcd2']

        return company_code
