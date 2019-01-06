#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Henrique da Silva Santos (rique_dev@hotmail.com)
# GitHub: https://github.com/riquedev

"""

    Exemplo de uso:

    ig_search = IGSearch()
    ig_search.query = 'development'
    ig_search.results

    {
        clear_client_cache: false
        has_more: true
        hashtags: [{position: 92,…}]
        places: [{place: {,…}, position: 99}]
        rank_token: "0.27592643194066424"
        status: "ok"
        users: [{position: 0,…}, {position: 1,…}, {position: 2,…}, {position: 3,…}, {position: 4,…}, {position: 5,…},…]
    }

"""


class IGSearch:
    """ Classe utilizada para realizar buscas no Instagram (funciona como se estivesse buscando na Search Bar do site)"""

    __query = 'instagram'
    __rank_token = 0.1276177921153525
    __include_reel = True

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def rank_token(self) -> float:
        return self.__rank_token

    @rank_token.setter
    def rank_token(self, rank: float):
        self.__rank_token = rank

    @property
    def include_reel(self) -> str:
        return 'true' if self.__include_reel else 'false'

    @include_reel.setter
    def include_reel(self, include_reel: bool):
        self.__include_reel = include_reel

    @property
    def url(self) -> str:
        return "https://www.instagram.com/web/search/topsearch/?context=blended&query={0}&rank_token={1}&include_reel={2}".format(
            self.query, self.rank_token, self.include_reel)

    @property
    def results(self) -> dict:
        import json
        from urllib.request import urlopen
        web_url = urlopen(self.url)
        data = web_url.read()
        return json.loads(data.decode('utf-8'))
