# -*- coding: utf-8 -*-

"""
Read column names from TTL files for 2012-2015. Create hardcoded column names.

   COLNAMES  = ['name', 'okpo', 'okopf', 'okfs', 'okved', 'inn', 'unit', 'report_type', '1110', '1110_lag', '1120', '1120_lag', '1130', '1130_lag', '1140', '1140_lag', '1150', '1150_lag', '1160', '1160_lag', '1170', '1170_lag', '1180', '1180_lag', '1190', '1190_lag', '1100', '1100_lag', '1210', '1210_lag', '1220', '1220_lag', '1230', '1230_lag', '1240', '1240_lag', '1250', '1250_lag', '1260', '1260_lag', '1200', '1200_lag', '1600', '1600_lag', '1310', '1310_lag', '1320', '1320_lag', '1340', '1340_lag', '1350', '1350_lag', '1360', '1360_lag', '1370', '1370_lag', '1300', '1300_lag', '1410', '1410_lag', '1420', '1420_lag', '1430', '1430_lag', '1450', '1450_lag', '1400', '1400_lag', '1510', '1510_lag', '1520', '1520_lag', '1530', '1530_lag', '1540', '1540_lag', '1550', '1550_lag', '1500', '1500_lag', '1700', '1700_lag', '2110', '2110_lag', '2120', '2120_lag', '2100', '2100_lag', '2210', '2210_lag', '2220', '2220_lag', '2200', '2200_lag', '2310', '2310_lag', '2320', '2320_lag', '2330', '2330_lag', '2340', '2340_lag', '2350', '2350_lag', '2300', '2300_lag', '2410', '2410_lag', '2421', '2421_lag', '2430', '2430_lag', '2450', '2450_lag', '2460', '2460_lag', '2400', '2400_lag', '2510', '2510_lag', '2520', '2520_lag', '2500', '2500_lag', '32003', '32004', '32005', '32006', '32007', '32008', '33103', '33104', '33105', '33106', '33107', '33108', '33117', '33118', '33125', '33127', '33128', '33135', '33137', '33138', '33143', '33144', '33145', '33148', '33153', '33154', '33155', '33157', '33163', '33164', '33165', '33166', '33167', '33168', '33203', '33204', '33205', '33206', '33207', '33208', '33217', '33218', '33225', '33227', '33228', '33235', '33237', '33238', '33243', '33244', '33245', '33247', '33248', '33253', '33254', '33255', '33257', '33258', '33263', '33264', '33265', '33266', '33267', '33268', '33277', '33278', '33305', '33306', '33307', '33406', '33407', '33003', '33004', '33005', '33006', '33007', '33008', '36003', '36004', '4110', '4111', '4112', '4113', '4119', '4120', '4121', '4122', '4123', '4124', '4129', '4100', '4210', '4211', '4212', '4213', '4214', '4219', '4220', '4221', '4222', '4223', '4224', '4229', '4200', '4310', '4311', '4312', '4313', '4314', '4319', '4320', '4321', '4322', '4323', '4329', '4300', '4400', '4490', '6100', '6210', '6215', '6220', '6230', '6240', '6250', '6200', '6310', '6311', '6312', '6313', '6320', '6321', '6322', '6323', '6324', '6325', '6326', '6330', '6350', '6300', '6400', 'date']
   TEXT_COLS = ['name', 'okpo', 'okopf', 'okfs', 'okved', 'inn', 'unit', 'report_type']
   DATE_COL  = 'date'
   
   Note: RENAMER in rows.py was changed.
   RENAMER = dict(...)

"""
from collections import OrderedDict
#import urllib.request
#import chardet
import pandas as pd

def get_format(k):
    return dict(skiprows=k, names=['N','line','type','len'],
                sep = ",", encoding='windows-1251')
             
# urls and skip row offset             
TTL_SPEC = {2015:("http://www.gks.ru/opendata/storage/7708234640-bdboo2015/G2015.TTL", 9)
         , 2014:("http://www.gks.ru/opendata/storage/7708234640-bdboo2014/G2014.TTL", 9)
         , 2013:("http://www.gks.ru/opendata/storage/7708234640-bdboo2013/G2013.TTL", 9)
         , 2012:("http://www.gks.ru/opendata/storage/7708234640-bdboo2012/G2012.TTL", 8)}

def get_encoding(url, fmt):
    with urllib.request.urlopen(url) as src:
        rawdata = src.read()       
    return chardet.detect(rawdata)

def request_colnames(url, fmt):
    with urllib.request.urlopen(url) as src:
        cols_df = pd.read_csv(src, **fmt)
    return cols_df.line.apply(lambda s: s.strip()).tolist()

def get_colnames(year, spec=TTL_SPEC):
    url = spec[year][0]
    fmt = get_format(spec[year][1])
    return request_colnames(url, fmt) 

def screen_colnames():
    years = [2012,2013,2014,2015]
    cols = {year:get_colnames(year) for year in [2012,2013,2014,2015]}
    
    for x in years:
        assert cols[x][0]=='Наименование'
        if x<2015:
            print(set(cols[x]).difference(cols[x+1]))

def generate_colnames():
    # hardcoded get_colnames(year) для любого года
    cols = ['Наименование', 'ОКПО', 'ОКОПФ', 'ОКФС', 'ОКВЭД', 'ИНН', 'Код единицы измерения', 'Тип отчета', '11103', '11104', '11203', '11204', '11303', '11304', '11403', '11404', '11503', '11504', '11603', '11604', '11703', '11704', '11803', '11804', '11903', '11904', '11003', '11004', '12103', '12104', '12203', '12204', '12303', '12304', '12403', '12404', '12503', '12504', '12603', '12604', '12003', '12004', '16003', '16004', '13103', '13104', '13203', '13204', '13403', '13404', '13503', '13504', '13603', '13604', '13703', '13704', '13003', '13004', '14103', '14104', '14203', '14204', '14303', '14304', '14503', '14504', '14003', '14004', '15103', '15104', '15203', '15204', '15303', '15304', '15403', '15404', '15503', '15504', '15003', '15004', '17003', '17004', '21103', '21104', '21203', '21204', '21003', '21004', '22103', '22104', '22203', '22204', '22003', '22004', '23103', '23104', '23203', '23204', '23303', '23304', '23403', '23404', '23503', '23504', '23003', '23004', '24103', '24104', '24213', '24214', '24303', '24304', '24503', '24504', '24603', '24604', '24003', '24004', '25103', '25104', '25203', '25204', '25003', '25004', '32003', '32004', '32005', '32006', '32007', '32008', '33103', '33104', '33105', '33106', '33107', '33108', '33117', '33118', '33125', '33127', '33128', '33135', '33137', '33138', '33143', '33144', '33145', '33148', '33153', '33154', '33155', '33157', '33163', '33164', '33165', '33166', '33167', '33168', '33203', '33204', '33205', '33206', '33207', '33208', '33217', '33218', '33225', '33227', '33228', '33235', '33237', '33238', '33243', '33244', '33245', '33247', '33248', '33253', '33254', '33255', '33257', '33258', '33263', '33264', '33265', '33266', '33267', '33268', '33277', '33278', '33305', '33306', '33307', '33406', '33407', '33003', '33004', '33005', '33006', '33007', '33008', '36003', '36004', '41103', '41113', '41123', '41133', '41193', '41203', '41213', '41223', '41233', '41243', '41293', '41003', '42103', '42113', '42123', '42133', '42143', '42193', '42203', '42213', '42223', '42233', '42243', '42293', '42003', '43103', '43113', '43123', '43133', '43143', '43193', '43203', '43213', '43223', '43233', '43293', '43003', '44003', '44903', '61003', '62103', '62153', '62203', '62303', '62403', '62503', '62003', '63103', '63113', '63123', '63133', '63203', '63213', '63223', '63233', '63243', '63253', '63263', '63303', '63503', '63003', '64003', 'Дата актуализации']
    d = {k:k for k in cols}
          
    rename_texts={'Дата актуализации':'date'
    , 'Наименование':'name'
    , 'ОКПО':'okpo' 
    , 'ОКОПФ':'okopf' 
    , 'ОКФС':'okfs' 
    , 'ОКВЭД':'okved' 
    , 'ИНН':'inn' 
    , 'Код единицы измерения':'unit' 
    , 'Тип отчета':'report_type'}
    this_year = {x:x[0:-1] for x in d.keys() if not x.startswith("3") and x.endswith("3")}
    prev_year = {x:x[0:-1]+"_lag" for x in d.keys() if not x.startswith("3") and x.endswith("4")}

    d.update(rename_texts)
    d.update(this_year)
    d.update(prev_year)

    return [d[x] for x in cols]



# used as hardcoded in rows.py

COLNAMES  = ['name', 'okpo', 'okopf', 'okfs', 'okved', 'inn', 'unit', 'report_type', '1110', '1110_lag', '1120', '1120_lag', '1130', '1130_lag', '1140', '1140_lag', '1150', '1150_lag', '1160', '1160_lag', '1170', '1170_lag', '1180', '1180_lag', '1190', '1190_lag', '1100', '1100_lag', '1210', '1210_lag', '1220', '1220_lag', '1230', '1230_lag', '1240', '1240_lag', '1250', '1250_lag', '1260', '1260_lag', '1200', '1200_lag', '1600', '1600_lag', '1310', '1310_lag', '1320', '1320_lag', '1340', '1340_lag', '1350', '1350_lag', '1360', '1360_lag', '1370', '1370_lag', '1300', '1300_lag', '1410', '1410_lag', '1420', '1420_lag', '1430', '1430_lag', '1450', '1450_lag', '1400', '1400_lag', '1510', '1510_lag', '1520', '1520_lag', '1530', '1530_lag', '1540', '1540_lag', '1550', '1550_lag', '1500', '1500_lag', '1700', '1700_lag', '2110', '2110_lag', '2120', '2120_lag', '2100', '2100_lag', '2210', '2210_lag', '2220', '2220_lag', '2200', '2200_lag', '2310', '2310_lag', '2320', '2320_lag', '2330', '2330_lag', '2340', '2340_lag', '2350', '2350_lag', '2300', '2300_lag', '2410', '2410_lag', '2421', '2421_lag', '2430', '2430_lag', '2450', '2450_lag', '2460', '2460_lag', '2400', '2400_lag', '2510', '2510_lag', '2520', '2520_lag', '2500', '2500_lag', '32003', '32004', '32005', '32006', '32007', '32008', '33103', '33104', '33105', '33106', '33107', '33108', '33117', '33118', '33125', '33127', '33128', '33135', '33137', '33138', '33143', '33144', '33145', '33148', '33153', '33154', '33155', '33157', '33163', '33164', '33165', '33166', '33167', '33168', '33203', '33204', '33205', '33206', '33207', '33208', '33217', '33218', '33225', '33227', '33228', '33235', '33237', '33238', '33243', '33244', '33245', '33247', '33248', '33253', '33254', '33255', '33257', '33258', '33263', '33264', '33265', '33266', '33267', '33268', '33277', '33278', '33305', '33306', '33307', '33406', '33407', '33003', '33004', '33005', '33006', '33007', '33008', '36003', '36004', '4110', '4111', '4112', '4113', '4119', '4120', '4121', '4122', '4123', '4124', '4129', '4100', '4210', '4211', '4212', '4213', '4214', '4219', '4220', '4221', '4222', '4223', '4224', '4229', '4200', '4310', '4311', '4312', '4313', '4314', '4319', '4320', '4321', '4322', '4323', '4329', '4300', '4400', '4490', '6100', '6210', '6215', '6220', '6230', '6240', '6250', '6200', '6310', '6311', '6312', '6313', '6320', '6321', '6322', '6323', '6324', '6325', '6326', '6330', '6350', '6300', '6400', 
             'date']
TEXT_COLS = ['name', 'okpo', 'okopf', 'okfs', 'okved', 'inn', 'unit', 'report_type']
DATE_COL  = ['date']

#   Variable names as in  http://info.avtovaz.ru/files/avtovaz_ras_12m_2013.pdf

RENAMER = OrderedDict([
#             ('name', 'name'),
#             ('okpo', 'okpo'),
#             ('okopf', 'okopf'),
#             ('okfs', 'okfs'),
#             ('okved', 'okved'),
#             ('inn', 'inn'),
#             ('unit', 'unit'),
#             ('report_type', 'report_type'),
#             ('1110', '1110'),
#             ('1110_lag', '1110_lag'),
#             ('1120', '1120'),
#             ('1120_lag', '1120_lag'),
#             ('1130', '1130'),
#             ('1130_lag', '1130_lag'),
#             ('1140', '1140'),
#             ('1140_lag', '1140_lag'),
('1150', 'of'), #основные фонды
('1150_lag', 'of_lag'),
#             ('1160', '1160'),
#             ('1160_lag', '1160_lag'),
#             ('1170', '1170'),
#             ('1170_lag', '1170_lag'),
#             ('1180', '1180'),
#             ('1180_lag', '1180_lag'),
#             ('1190', '1190'),
#             ('1190_lag', '1190_lag'),
 ('1100', 'ta_fix'), #внеоборотные активы
 ('1100_lag', 'ta_fix_lag'),
#             ('1210', '1210'),
#             ('1210_lag', '1210_lag'),
#             ('1220', '1220'),
#             ('1220_lag', '1220_lag'),
#             ('1230', '1230'),
#             ('1230_lag', '1230_lag'),
#             ('1240', '1240'),
#             ('1240_lag', '1240_lag'),
#             ('1250', '1250'),
#             ('1250_lag', '1250_lag'),
#             ('1260', '1260'),
#             ('1260_lag', '1260_lag'),
 ('1200', 'ta_nonfix'), #оборотные активы
 ('1200_lag', 'ta_nonfix_lag'),
  
 ('1600', 'ta'), # активы всего
 ('1600_lag', 'ta_lag'),
  
#             ('1310', '1310'),
#             ('1310_lag', '1310_lag'),
#             ('1320', '1320'),
#             ('1320_lag', '1320_lag'),
#             ('1340', '1340'),
#             ('1340_lag', '1340_lag'),
#             ('1350', '1350'),
#             ('1350_lag', '1350_lag'),
#             ('1360', '1360'),
#             ('1360_lag', '1360_lag'),
#             ('1370', '1370'),
#             ('1370_lag', '1370_lag'),
 ('1300', 'tp_cap'), # капитал
 ('1300_lag', 'tp_cap_lag'),

 ('1410', 'debt_long'), # долгосрочные займы
 ('1410_lag', 'debt_long_lag'),

#             ('1420', '1420'),
#             ('1420_lag', '1420_lag'),
#             ('1430', '1430'),
#             ('1430_lag', '1430_lag'),
#             ('1450', '1450'),
#             ('1450_lag', '1450_lag'),
 ('1400', 'tp_long'), #долгосрочные обязательства 
 ('1400_lag', 'tp_long_lag'),
  
 ('1510', 'debt_short'), # кракосрочные займы
 ('1510_lag', 'debt_short_lag'),
  
#             ('1520', '1520'),
#             ('1520_lag', '1520_lag'),
#             ('1530', '1530'),
#             ('1530_lag', '1530_lag'),
#             ('1540', '1540'),
#             ('1540_lag', '1540_lag'),
#             ('1550', '1550'),
#             ('1550_lag', '1550_lag'),

 ('1500', 'tp_short'), #краткосрочные обязательства 
 ('1500_lag', 'tp_short_lag'),

 ('1700', 'tp'),    # пассивы всего 
 ('1700_lag', 'tp_lag'),

 ('2110', 'sales'), # выручка
 ('2110_lag', 'sales_lag'),
#             ('2120', '2120'),
#             ('2120_lag', '2120_lag'),
#             ('2100', '2100'),
#             ('2100_lag', '2100_lag'),
#             ('2210', '2210'),
#             ('2210_lag', '2210_lag'),
#             ('2220', '2220'),
#             ('2220_lag', '2220_lag'),

 ('2200', 'profit_operational'), #прибыль от продаж
 ('2200_lag', 'profit_operational_lag'),
#             ('2310', '2310'),
#             ('2310_lag', '2310_lag'),
#             ('2320', '2320'),
#             ('2320_lag', '2320_lag'),

 ('2330', 'exp_interest'), # процентные платежи 
 ('2330_lag', 'exp_interest_lag'),
#             ('2340', '2340'),
#             ('2340_lag', '2340_lag'),
#             ('2350', '2350'),
#             ('2350_lag', '2350_lag'),
 ('2300', 'profit_before_tax'), #прибыль до налогообложения
 ('2300_lag', 'profit_before_tax_lag'),
#             ('2410', '2410'),
#             ('2410_lag', '2410_lag'),
#             ('2421', '2421'),
#             ('2421_lag', '2421_lag'),
#             ('2430', '2430'),
#             ('2430_lag', '2430_lag'),
#             ('2450', '2450'),
#             ('2450_lag', '2450_lag'),
#             ('2460', '2460'),
#             ('2460_lag', '2460_lag'),
#             ('2400', '2400'),
#             ('2400_lag', '2400_lag'),
#             ('2510', '2510'),
#             ('2510_lag', '2510_lag'),
#             ('2520', '2520'),
#             ('2520_lag', '2520_lag'),
#             ('2500', '2500'),
#             ('2500_lag', '2500_lag'),
#             ('32003', '32003'),
#             ('32004', '32004'),
#             ('32005', '32005'),
#             ('32006', '32006'),
#             ('32007', '32007'),
#             ('32008', '32008'),
#             ('33103', '33103'),
#             ('33104', '33104'),
#             ('33105', '33105'),
#             ('33106', '33106'),
#             ('33107', '33107'),
#             ('33108', '33108'),
#             ('33117', '33117'),
#             ('33118', '33118'),
#             ('33125', '33125'),
#             ('33127', '33127'),
#             ('33128', '33128'),
#             ('33135', '33135'),
#             ('33137', '33137'),
#             ('33138', '33138'),
#             ('33143', '33143'),
#             ('33144', '33144'),
#             ('33145', '33145'),
#             ('33148', '33148'),
#             ('33153', '33153'),
#             ('33154', '33154'),
#             ('33155', '33155'),
#             ('33157', '33157'),
#             ('33163', '33163'),
#             ('33164', '33164'),
#             ('33165', '33165'),
#             ('33166', '33166'),
#             ('33167', '33167'),
#             ('33168', '33168'),
#             ('33203', '33203'),
#             ('33204', '33204'),
#             ('33205', '33205'),
#             ('33206', '33206'),
#             ('33207', '33207'),
#             ('33208', '33208'),
#             ('33217', '33217'),
#             ('33218', '33218'),
#             ('33225', '33225'),
#             ('33227', '33227'),
#             ('33228', '33228'),
#             ('33235', '33235'),
#             ('33237', '33237'),
#             ('33238', '33238'),
#             ('33243', '33243'),
#             ('33244', '33244'),
#             ('33245', '33245'),
#             ('33247', '33247'),
#             ('33248', '33248'),
#             ('33253', '33253'),
#             ('33254', '33254'),
#             ('33255', '33255'),
#             ('33257', '33257'),
#             ('33258', '33258'),
#             ('33263', '33263'),
#             ('33264', '33264'),
#             ('33265', '33265'),
#             ('33266', '33266'),
#             ('33267', '33267'),
#             ('33268', '33268'),
#             ('33277', '33277'),
#             ('33278', '33278'),
#             ('33305', '33305'),
#             ('33306', '33306'),
#             ('33307', '33307'),
#             ('33406', '33406'),
#             ('33407', '33407'),
#             ('33003', '33003'),
#             ('33004', '33004'),
#             ('33005', '33005'),
#             ('33006', '33006'),
#             ('33007', '33007'),
#             ('33008', '33008'),
#             ('36003', '36003'),
#             ('36004', '36004'),
 ('4110', 'cash_oper_inflow'),        # вcего операционные поступления
 ('4111', 'cash_oper_inflow_sales'),  # поступления от продаж
#             ('4111', '4111'),
#             ('4112', '4112'),
#             ('4113', '4113'),
#             ('4119', '4119'),
#             ('4120', '4120'),
 ('4121', 'paid_to_supplier'),  # платежи поставщикам
 ('4122', 'paid_to_worker'),    # платежи работникам
 ('4123', 'cash_interest'),     # процентные платежи  
 ('4124', 'paid_profit_tax'),
 ('4129', 'paid_other_cost'),
#             ('4100', '4100'),
#             ('4210', '4210'),
#             ('4211', '4211'),
#             ('4212', '4212'),
#             ('4213', '4213'),
#             ('4214', '4214'),
#             ('4219', '4219'),
#             ('4220', '4220'),
 ('4221', 'cash_investment_of'), # создание внеоборотных активов
#             ('4222', '4222'),
#             ('4223', '4223'),
#             ('4224', '4224'),
#             ('4229', '4229'),
#             ('4200', '4200'),
#             ('4310', '4310'),
#             ('4311', '4311'),
#             ('4312', '4312'),
#             ('4313', '4313'),
#             ('4314', '4314'),
#             ('4319', '4319'),
#             ('4320', '4320'),
#             ('4321', '4321'),
#             ('4322', '4322'),
#             ('4323', '4323'),
#             ('4329', '4329'),
#             ('4300', '4300'),
#             ('4400', '4400'),
#             ('4490', '4490'),
#             ('6100', '6100'),
#             ('6210', '6210'),
#             ('6215', '6215'),
#             ('6220', '6220'),
#             ('6230', '6230'),
#             ('6240', '6240'),
#             ('6250', '6250'),
#             ('6200', '6200'),
#             ('6310', '6310'),
#             ('6311', '6311'),
#             ('6312', '6312'),
#             ('6313', '6313'),
#             ('6320', '6320'),
#             ('6321', '6321'),
#             ('6322', '6322'),
#             ('6323', '6323'),
#             ('6324', '6324'),
#             ('6325', '6325'),
#             ('6326', '6326'),
#             ('6330', '6330'),
#             ('6350', '6350'),
#             ('6300', '6300'),
#             ('6400', '6400')
             ])   
             
             
class Columns():
    
    COLUMNS=['name', 'okpo', 'okopf', 'okfs', 'okved', 'inn', 'unit', 'report_type', '1110', '1110_lag', '1120', '1120_lag', '1130', '1130_lag', '1140', '1140_lag', '1150', '1150_lag', '1160', '1160_lag', '1170', '1170_lag', '1180', '1180_lag', '1190', '1190_lag', '1100', '1100_lag', '1210', '1210_lag', '1220', '1220_lag', '1230', '1230_lag', '1240', '1240_lag', '1250', '1250_lag', '1260', '1260_lag', '1200', '1200_lag', '1600', '1600_lag', '1310', '1310_lag', '1320', '1320_lag', '1340', '1340_lag', '1350', '1350_lag', '1360', '1360_lag', '1370', '1370_lag', '1300', '1300_lag', '1410', '1410_lag', '1420', '1420_lag', '1430', '1430_lag', '1450', '1450_lag', '1400', '1400_lag', '1510', '1510_lag', '1520', '1520_lag', '1530', '1530_lag', '1540', '1540_lag', '1550', '1550_lag', '1500', '1500_lag', '1700', '1700_lag', '2110', '2110_lag', '2120', '2120_lag', '2100', '2100_lag', '2210', '2210_lag', '2220', '2220_lag', '2200', '2200_lag', '2310', '2310_lag', '2320', '2320_lag', '2330', '2330_lag', '2340', '2340_lag', '2350', '2350_lag', '2300', '2300_lag', '2410', '2410_lag', '2421', '2421_lag', '2430', '2430_lag', '2450', '2450_lag', '2460', '2460_lag', '2400', '2400_lag', '2510', '2510_lag', '2520', '2520_lag', '2500', '2500_lag', '32003', '32004', '32005', '32006', '32007', '32008', '33103', '33104', '33105', '33106', '33107', '33108', '33117', '33118', '33125', '33127', '33128', '33135', '33137', '33138', '33143', '33144', '33145', '33148', '33153', '33154', '33155', '33157', '33163', '33164', '33165', '33166', '33167', '33168', '33203', '33204', '33205', '33206', '33207', '33208', '33217', '33218', '33225', '33227', '33228', '33235', '33237', '33238', '33243', '33244', '33245', '33247', '33248', '33253', '33254', '33255', '33257', '33258', '33263', '33264', '33265', '33266', '33267', '33268', '33277', '33278', '33305', '33306', '33307', '33406', '33407', '33003', '33004', '33005', '33006', '33007', '33008', '36003', '36004', '4110', '4111', '4112', '4113', '4119', '4120', '4121', '4122', '4123', '4124', '4129', '4100', '4210', '4211', '4212', '4213', '4214', '4219', '4220', '4221', '4222', '4223', '4224', '4229', '4200', '4310', '4311', '4312', '4313', '4314', '4319', '4320', '4321', '4322', '4323', '4329', '4300', '4400', '4490', '6100', '6210', '6215', '6220', '6230', '6240', '6250', '6200', '6310', '6311', '6312', '6313', '6320', '6321', '6322', '6323', '6324', '6325', '6326', '6330', '6350', '6300', '6400', 
             'date']         
    VALID_ROW_WIDTH = len(COLUMNS)
    INN_POSITION = COLUMNS.index('inn')
             
    RENAMER = OrderedDict([('1150', 'of'),
                 ('1100',     'ta_fix'),
                 ('1200',     'ta_nonfix'),
                 ('1600',     'ta'),
                 ('1410',     'debt_long'),
                 ('1510',     'debt_short'),
                 ('1300',     'tp_cap'),
                 ('1400',     'tp_long'),
                 ('1500',     'tp_short'),
                 ('1700',     'tp'),
                 ('2110',     'sales'),
                 ('2200',     'profit_operational'),
                 ('2330',     'exp_interest'),
                 ('2300',     'profit_before_tax'),
                 ('1150_lag', 'of_lag'),
                 ('1100_lag', 'ta_fix_lag'),
                 ('1200_lag', 'ta_nonfix_lag'),
                 ('1600_lag', 'ta_lag'),
                 ('1300_lag', 'tp_cap_lag'),
                 ('1410_lag', 'debt_long_lag'),
                 ('1400_lag', 'tp_long_lag'),
                 ('1510_lag', 'debt_short_lag'),
                 ('1500_lag', 'tp_short_lag'),
                 ('1700_lag', 'tp_lag'),
                 ('2110_lag', 'sales_lag'),
                 ('2200_lag', 'profit_operational_lag'),
                 ('2330_lag', 'exp_interest_lag'),
                 ('2300_lag', 'profit_before_tax_lag'),
                 ('4110', 'cash_in_operations_total'),
                 ('4111', 'cash_in_operations_sales'),
                 ('4121', 'paid_to_supplier'),
                 ('4122', 'paid_to_worker'),
                 ('4123', 'paid_interest'),
                 ('4124', 'paid_profit_tax'),
                 ('4129', 'paid_other_costs'),
                 ('4221', 'cash_out_investment_of')])
    
    DATACOLS = list(RENAMER.keys())
    RENAMED_DATACOLS = list(RENAMER.values())             