ACCOUNT_INFO = {
'CIS': {
        'ifrs_Revenue': '매출액',
        'ifrs_CostOfSales': '매출원가',
        'ifrs_GrossProfit': '매출총이익',
        'dart_TotalSellingGeneralAdministrativeExpenses': '판매비와관리비',
        'dart_OperatingIncomeLoss': '영업이익',
        'ifrs_ProfitLoss': '당기순이익',
    },
    # 현금흐름표는 누적
    'CF': {
        'ifrs_CashFlowsFromUsedInOperatingActivities': '영업활동현금흐름',
        'ifrs_PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities': '유형자산의 취득',
        'ifrs_PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities': '무형자산의 취득',
        'ifrs_ProceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities': '유형자산의 처분',
        'ifrs_ProceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities': '무형자산의 처분',
        'ifrs_ProceedsFromBorrowingsClassifiedAsFinancingActivities': '차입금의 증가',
        'ifrs_RepaymentsOfBorrowingsClassifiedAsFinancingActivities': '차입금의 상환',
    },
    # 재무상태표
    'BS': {

        'ifrs_CashAndCashEquivalents': '현금및현금성자산',
        'dart_ShortTermTradeReceivable': '매출채권',
        'dart_ShortTermOtherReceivables': '기타수취채권',
        'ifrs_OtherCurrentFinancialAssets': '기타유동금융자산',
        'ifrs_Inventories': '재고자산',
        'dart_OtherCurrentAssets': '기타유동자산',
        # 'ifrs_NoncurrentAssets': '비유동자산',
        'dart_LongTermLeaseholdDeposits': '기타수취채권(비유동)',
        'ifrs_OtherNoncurrentFinancialAssets': '기타비유동금융자산',
        'dart_LongTermTradeReceivablesGross': '매출채권(비유동)',
        'ifrs_PropertyPlantAndEquipment': '유형자산',

        'dart_ShortTermTradePayables': '매입채무',
        'dart_ShortTermOtherPayables': '기타지급채무',
        'ifrs_ShorttermBorrowings': '단기차입금',
        'ifrs_CurrentPortionOfLongtermBorrowings': '유동성장기부채',
        'dart_OtherCurrentLiabilities': '기타유동부채',
        'dart_LongTermBorrowingsGross': '차입금(비유동)',
        'ifrs_RetainedEarnings': '이익잉여금',

        'ifrs_CurrentAssets': '유동자산',
        'ifrs_CurrentLiabilities': '유동부채',
        'ifrs_Liabilities': '부채총계',
        'ifrs_Assets': '자산총계',
        'ifrs_Equity': '자본총계',
    },

}

REPORT_CODES = [
    {'code': '11013', 'name': '1분기보고서'},
    {'code': '11012', 'name': '반기보고서'},
    {'code': '11014', 'name': '3분기보고서'},
    {'code': '11011', 'name': '사업보고서'}
]