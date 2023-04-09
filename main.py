from company import Company
from api import Http
from constants import REPORT_CODES, ACCOUNT_INFO
import requests
from pydash import py_
import pandas as pd
from tqdm import tqdm

BASE_URL = "https://opendart.fss.or.kr/api/"

if __name__ == "__main__":
    api_key = input('API Key값을 입력하세요: ')
    comp_name = input('회사이름을 입력하세요: ')

    target = Company.find_by_name(comp_name)
    filename = f'{comp_name}.xlsx'

    if target is None:
        raise ValueError(f'Not found with name {comp_name}')

    start_year = int(input('데이터 수집 시작년도를 입력하세요(ex. 2018) : '))
    end_year = 2023

    http_inst = Http(api_key=api_key)

    default_params = {
        'crtfc_key': api_key,
        'corp_code': target.corp_code,
        # 'CFS': 연결. 'OFS': 별도
        'fs_div': 'CFS',
    }

    annual_data_columns = []
    quarter_data_columns = []

    quarter_data = []
    annual_data = []
    index = []

    pbar = tqdm(enumerate(range(start_year, end_year + 1)))
    for year_idx, year in pbar:
        pbar.set_description(f"{year}년 데이터 처리중...")
        annual_data_columns.append(str(year))
        accumulated_value_dict = {}

        for report_idx, report_code in enumerate(REPORT_CODES):
            params = {
                **default_params,
                'bsns_year': str(year),
                'reprt_code': report_code['code'],
            }

            data_container = []

            res = requests.get(BASE_URL + 'fnlttSinglAcntAll.json', params=params)

            # status 000 = success
            if res.json()['status'] != '000':
                continue

            quarter_name = str(year)[2:] + f'.{report_idx + 1}Q'
            quarter_data_columns.append(quarter_name)
            results = res.json()['list']

            # sj_div -> BS 재무상태표 / CIS 포괄손익계산서 / CF 현금흐름표
            for sj_div in ACCOUNT_INFO:
                accounts = ACCOUNT_INFO[sj_div]

                for account_id in accounts:
                    # account_id_parsed = account_id.split('_')[-1]
                    account_nm = accounts[account_id]

                    if year_idx == 0 and report_idx == 0:
                        index.append(account_nm)

                    full_account_id = account_id.split('_')[0] + '-full_' + account_id.split('_')[1]
                    target_data = py_.find(results, lambda r: r['account_id'] in [account_id, full_account_id])

                    if target_data is None:
                        value = 0
                    else:
                        value = target_data['thstrm_amount']

                        if value == '':
                            value = 0
                        else:
                            value = int(value)

                    if sj_div == 'BS':
                        data_container.append(value)

                    else:
                        if account_id not in accumulated_value_dict:
                            accumulated_value_dict[account_id] = value
                            data_container.append(value)
                        else:
                            if sj_div == 'CIS':
                                # Only accumulated in annual report
                                if report_idx != 3:
                                    data_container.append(value)
                                    accumulated_value_dict[account_id] += value
                                else:
                                    accumulated_ = accumulated_value_dict[account_id]
                                    data_container.append(value - accumulated_)

                            # 'CF' 현금흐름표
                            else:
                                accumulated_ = accumulated_value_dict[account_id]
                                data_container.append(value - accumulated_)
                                accumulated_value_dict[account_id] = value

            quarter_data.append(data_container)

    df = pd.DataFrame(quarter_data).transpose()
    df = df.div(1000000).round()
    df = df.astype(int)
    df.columns = quarter_data_columns
    df.index = index

    df.loc['OPM(%)'] = (df.loc['영업이익'] / df.loc['매출액']).apply(lambda val: round(val, 3))
    df.loc['GPM(%)'] = (df.loc['매출총이익'] / df.loc['매출액']).apply(lambda val: round(val, 3))
    df.loc['판관비율(%)'] = (df.loc['판매비와관리비'] / df.loc['매출액']).apply(lambda val: round(val, 3))

    df.loc['ROE(%)'] = df.loc['당기순이익'] / df.loc['자본총계']
    df.loc['부채비율'] = df.loc['부채총계'] / df.loc['자본총계']
    # 부채비율
    df.loc['CAPEX'] = df.loc['유형자산의 취득'] - df.loc['유형자산의 처분'] + df.loc['무형자산의 취득'] - df.loc['무형자산의 처분']
    df.loc['순차입 증가액'] = df.loc['차입금의 증가'] - df.loc['차입금의 상환']

    df.to_excel(filename)







