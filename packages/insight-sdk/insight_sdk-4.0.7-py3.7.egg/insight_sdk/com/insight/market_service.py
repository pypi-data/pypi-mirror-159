from ..interface.mdc_gateway_base_define import EMarketDataType


class market_service(object):
    def __init__(self):
        pass
    # ************************************�������ݶ���************************************
    # �����ĵĹ�ƱTick���ݣ�mdStock��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.StockType
    def onSubscribe_StockType_MD_TICK(self, mdStock):
        pass

    # �����ĵ�ָ��Tick���ݣ�mdIndex��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.IndexType
    def onSubscribe_IndexType_MD_TICK(self, mdIndex):
        pass
        # print(mdIndex)

    # �����ĵ�ծȯTick���ݣ�mdBond��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.BondType
    def onSubscribe_BondType_MD_TICK(self, mdBond):
        pass
        # print(mdBond)

    # �����ĵĻ���Tick���ݣ�mdFund��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.FundType
    def onSubscribe_FundType_MD_TICK(self, mdFund):
        pass
        # print(mdFund)

    # �����ĵ���ȨTick���ݣ�mdOption��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.OptionType
    def onSubscribe_OptionType_MD_TICK(self, mdOption):
        pass
        # print(mdOption)

    # �����ĵ��ڻ�Tick���ݣ�mdFuture��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.OptionType
    def onSubscribe_FuturesType_MD_TICK(self, mdFuture):
        pass
        # print(mdFuture)

    # �����ĵ���ʳɽ���marketdatajson��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.MD_TRANSACTION
    # �����ĵ����ί�У���ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.MD_ORDER
    def onSubscribe_MD_TRANSACTION_and_MD_ORDER(self, marketdatajson):
        if marketdatajson["marketDataType"] == EMarketDataType.MD_TRANSACTION:  # ��ʳɽ�
            mdtransaction = marketdatajson["mdTransaction"]
            pass
            # print(mdtransaction)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_ORDER:  # ���ί��
            mdorder = marketdatajson["mdOrder"]
            pass
            # print(mdorder)
        # print(marketdatajsons)

    # �����ĵ�K��ָ��ģ�ͣ�marketdatajson��ʽΪjson��ʽ
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_15S ����#15����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_1MIN ����#1����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_5MIN ����#5����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_15MIN ����#15����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_30MIN ����#30����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_60MIN ����#60����K��
    # ���ĵ���������ΪEMarketDataType.MD_KLINE_1D ����#��K��
    def onSubscribe_MD_KLINE(self, marketdatajson):
        if marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_15S:  # 15����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_1MIN:  # 1����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_5MIN:  # 5����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_15MIN:  # 15����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_30MIN:  # 30����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_60MIN:  # 60����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_1D:  # ��K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)

        # print(marketdatajson)

    # �����ĵ��ʽ��������ݣ�mdFundFlowAnalysis��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.AD_FUND_FLOW_ANALYSIS
    def onSubscribe_AD_FUND_FLOW_ANALYSIS(self, mdFundFlowAnalysis):
        pass
        # print(mdFundFlowAnalysis)

    # �����ĵ���ȯͨ���ݣ�mdSecurityLending��ʽΪjson��ʽ
    # ���ĵ�֤ȯ����ΪESecurityType.MD_SECURITY_LENDING
    def onSubscribe_MD_SECURITY_LENDING(self, mdSecurityLending):
        pass
        # print(mdSecurityLending)

    # ************************************����ط�����************************************
    # ����طŵĹ�ƱTick���ݣ�mdStock��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.StockType
    def onPlayback_StockType_MD_TICK(self, mdStock):
        pass
        # print(mdStock)

    # ����طŵ�ָ��Tick���ݣ�mdIndex��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.IndexType
    def onPlayback_IndexType_MD_TICK(self, mdIndex):
        pass
        # print(mdIndex)

    # ����طŵ�ծȯTick���ݣ�mdBond��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.BondType
    def onPlayback_BondType_MD_TICK(self, mdBond):
        pass
        # print(mdBond)

    # ����طŵĻ���Tick���ݣ�mdFund��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.FundType
    def onPlayback_FundType_MD_TICK(self, mdFund):
        pass
        # print(mdFund)

    # ����طŵ���ȨTick���ݣ�mdOption��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.OptionType
    def onPlayback_OptionType_MD_TICK(self, mdOption):
        pass
        # print(mdOption)

    # ����طŵ��ڻ�Tick���ݣ�mdFuture��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.OptionType
    def onPlayback_FuturesType_MD_TICK(self, mdFuture):
        pass
        # print(mdFuture)

    # ����طŵ���ʳɽ���marketdatajson��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.MD_TRANSACTION
    # ����طŵ����ί�У���ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.MD_ORDER
    def onPlayback_MD_TRANSACTION_and_MD_ORDER(self, marketdatajson):
        if marketdatajson["marketDataType"] == EMarketDataType.MD_TRANSACTION:  # ��ʳɽ�
            mdtransaction = marketdatajson["mdTransaction"]
            pass
            # print(mdtransaction)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_ORDER:  # ���ί��
            mdorder = marketdatajson["mdOrder"]
            pass
            # print(mdorder)
        # print(marketdatajsons)

    # ����طŵ�K��ָ��ģ�ͣ�marketdatajson��ʽΪjson��ʽ
    # �طŵ���������ΪEMarketDataType.MD_KLINE_15S ����#15����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_1MIN ����#1����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_5MIN ����#5����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_15MIN ����#15����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_30MIN ����#30����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_60MIN ����#60����K��
    # �طŵ���������ΪEMarketDataType.MD_KLINE_1D ����#��K��
    def onPlayback_MD_KLINE(self, marketdatajson):
        if marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_15S:  # 15����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_1MIN:  # 1����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_5MIN:  # 5����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_15MIN:  # 15����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_30MIN:  # 30����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_60MIN:  # 60����K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)
        elif marketdatajson["marketDataType"] == EMarketDataType.MD_KLINE_1D:  # ��K��
            mdKLine = marketdatajson["mdKLine"]
            pass
            # print(mdKLine)

        # print(marketdatajson)

    # ����طŵ��ʽ��������ݣ�mdFundFlowAnalysis��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.AD_FUND_FLOW_ANALYSIS
    def onPlayback_AD_FUND_FLOW_ANALYSIS(self, mdFundFlowAnalysis):
        pass
        # print(mdFundFlowAnalysis)

    # ����طŵ���ȯͨ���ݣ�mdSecurityLending��ʽΪjson��ʽ
    # �طŵ�֤ȯ����ΪESecurityType.MD_SECURITY_LENDING
    def onPlayback_MD_SECURITY_LENDING(self, mdSecurityLending):
        pass
        # print(mdSecurityLending)

    # ����طŵ�״̬��status��ʽΪstring��ʽ
    def onPlaybackStatus(self, status):
        pass
        # print(status)

    # ����ط����󷵻ؽ����response��ʽΪstring��ʽ
    def onPlaybackResponse(self, response):
        pass
        # print(response)

    # ����طſ������󷵻ؽ����response��ʽΪstring��ʽ
    def onPlaybackControlResponse(self, response):
        pass
        # print(response)

    # ************************************�����ѯ���󷵻ؽ��************************************
    # �����ѯ��ʷ�����е�ָ��֤ȯ�Ļ�����Ϣ query_mdcontant_by_type()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ�������µ�ָ��֤ȯ�Ļ�����Ϣ query_last_mdcontant_by_type()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ��ʷ�����е�ָ��֤ȯ�Ļ�����Ϣ query_mdcontant_by_id()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ�������µ�ָ��֤ȯ�Ļ�����Ϣ query_last_mdcontant_by_id()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯָ��֤ȯ��ETF�Ļ�����Ϣ query_ETFinfo()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯָ��֤ȯ������һ��Tick���� query_last_mdtick()�ķ��ؽ����queryresponse��ʽΪlist[json]
    def onQueryResponse(self, queryresponse):
        pass
        # for resonse in iter(queryresponse):
        #     # response��ʽΪjson��ʽ
        #     print(resonse)

