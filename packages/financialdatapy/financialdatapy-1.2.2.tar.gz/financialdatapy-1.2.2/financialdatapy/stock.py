"""This module retrieves financial data of a stock."""
from financialdatapy.date import validate_date
import pandas as pd
import re
from typing import Optional
from financialdatapy.stocklist import KorStockList
from financialdatapy.exception import CountryCodeValidationFailed
from financialdatapy.market import Market


class Stock:
    """A class representing a stock or a company.

    :param symbol: Symbol of a company/stock.
    :type symbol: str
    :param country_code: Country where the stock is listed. The format should
        follow alpha-3 code (ISO 3166), defaults to 'USA'.
    :type country_code: str, optional
    """

    def __init__(self, symbol: str, country_code: str = 'USA') -> None:
        """Initialize Stock."""
        self.country_code = country_code
        self.symbol = symbol

    @property
    def symbol(self) -> str:
        """Getter method of property symbol.

        :return: Symbol of a company/stock.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str) -> None:
        """Setter method of property symbol

        :param symbol: Symbol of a company/stock.
        :type symbol: str
        """
        if self.country_code == 'KOR':
            self._symbol = self._convert_symbol_to_code_in_krx(symbol)
        else:
            self._symbol = symbol

    @property
    def country_code(self) -> str:
        """Getter method of property country_code.

        :return: Country code
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str) -> None:
        """Setter method of property country_code.

        :param country_code: Country code
        :type country_code: str
        """
        country_code = self._validate_country_code(country_code)
        self._country_code = country_code.upper()

    @property
    def market(self) -> Market:
        """Property of :class:`market.Market` instance.

        :return: :class:`market.Market` instance.
        :rtype: :class:`market.Market`
        """
        return Market(self.country_code)

    def _convert_symbol_to_code_in_krx(self, symbol: str) -> str:
        """Convert symbol to company code for stocks in Korea Exchange.

        :param symbol: Symbol of a company/stock.
        :type symbol: str
        :return: Company code
        :rtype: str
        """
        try:
            isinstance(int(symbol), int)
        except ValueError:
            return KorStockList.search_stock_code(symbol)
        else:
            return symbol

    def _validate_country_code(self, country_code: str) -> str:
        """Validate if country code is in alpha-3 code (ISO 3166).

        :param country_code: Country where the stock is listed.
        :type country_code: str
        :raises CountryCodeValidationFailed: If country code is not
            in alpha-3 code format.
        :return: Country code in alpha-3 code (ISO-3166).
        :rtype: str
        """
        try:
            country_code = re.search(r'\b[a-zA-Z]{3}\b', country_code).group()
            country_code = country_code.upper()
        except (TypeError, AttributeError):
            raise CountryCodeValidationFailed(
                'Country code should be in alpha-3 code (ISO 3166) e.g. USA'
            )
        else:
            return country_code

    def financials(
        self,
        financial: str = 'income_statement',
        period: str = 'annual',
        is_standard: bool = False,
        web: bool = False,
    ) -> pd.DataFrame | None:
        """Get financial statements as reported.

        :param financial: Which financial statement to retrieve. Input string
                should be either 'income_statement', 'balance_sheet', or
                'cash_flow', defaults to 'income_statement'
        :type financial: str, optional
        :param period: Either 'annual' or 'quarter', defaults to 'annual'.
        :type period: str, optional
        :param is_standard: Option for retrieving standard financial statements,
            defaults to False.
        :type is_standard: bool, optional
        :param web: Option for opening filings in a web browser,
            defaults to False.
        :type web: bool, optional
        :return: Financial statement as reported.
        :rtype: pandas.DataFrame
        """
        financial_statement = self.market.financial_statement(
            self.symbol,
            financial,
            period,
            is_standard,
            web,
        )
        return financial_statement

    def price(self, start: Optional[str] = None,
              end: Optional[str] = None) -> pd.DataFrame:
        """Get historical stock price data.

        :param start: Start date to query. Format should be in ISO 8601,
            defaults to None.
        :type start: str, optional
        :param end: End date to query. Format should be in ISO 8601, defaults to
            None.
        :type end: str, optional
        :return: Historical stock price data.
        :rtype: pandas.DataFrame
        """
        start = validate_date(start, start=True)
        end = validate_date(end)

        price = self.market.historical_price(self.symbol, start, end)
        price_data = price.get_price_data()

        return price_data

    def __repr__(self) -> str:
        """Returns representational string of :class:`Stock`.

        :return: Representational string of :class:`Stock`.
        :rtype: str
        """
        return f"Stock(symbol='{self.symbol}', country_code='{self.country_code}')"
