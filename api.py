import requests


class Http:
    base_url = "https://opendart.fss.or.kr/api/"

    def __init__(self, api_key):
        self.params = {
            'crtfc_key': api_key
        }

    def get(self, url, params=None):
        if params is None:
            params = self.params
        res = requests.get(url, params)

        if str(res.status_code)[0] == '2':
            return res.json()

        return res.text

    # 정기 공시
    def get_filings(self, corp_code, bgn_de, pblntf_ty='A'):
        url = self.base_url + 'list.json'

        params = {
            **self.params,
            'corp_code': corp_code,
            'bgn_de': bgn_de,
            'pblntf_ty': pblntf_ty,
            'page_count': '100'
        }

        return self.get(url=url, params=params)['list']
