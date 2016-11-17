from remote import RemoteDataset
def test_remote():
    assert RemoteDataset(2012).download().unrar()
    assert RemoteDataset(2013).download().unrar()
    assert RemoteDataset(2014).download().unrar()
    assert RemoteDataset(2015).download().unrar()
    
    for f in [RemoteDataset(x).rar_content() for x in [2012,2013,2014,2015]]:
        assert f    
    
    

#------------------------------------------------------------------------------------

from row_parser import dequote, okved3, EMPTY
def test_okved():  
    tests = { "1": [1, EMPTY, EMPTY]
           , "01": [1, EMPTY, EMPTY]
        , "44.20": [44,  20,  EMPTY]
      , "1.10.11": [1,   10,   11]}
    for k, v in tests.items():
        assert okved3(k) == v            
        
def test_dequote():
    assert dequote('Открытое акционерное общество "База отдыха "Энергетик"') == \
           ['Открытое акционерное общество', 'База отдыха "Энергетик"']
    assert dequote('Общество с ограниченной ответственностью "РИОНИ"') == \
           ['Общество с ограниченной ответственностью', 'РИОНИ']
    assert dequote('МУНИЦИПАЛЬНОЕ УНИТАРНОЕ ПРЕДПРИЯТИЕ "ТЕХНО-ТОРГОВЫЙ ЦЕНТР "РЕМБЫТТЕХНИКА" МУНИЦИПАЛЬНОГО ОБРАЗОВАНИЯ "ГОРОД АРХАНГЕЛЬСК"') == ['МУНИЦИПАЛЬНОЕ УНИТАРНОЕ ПРЕДПРИЯТИЕ', 'ТЕХНО-ТОРГОВЫЙ ЦЕНТР "РЕМБЫТТЕХНИКА" МУНИЦИПАЛЬНОГО ОБРАЗОВАНИЯ "ГОРОД АРХАНГЕЛЬСК"']

#------------------------------------------------------------------------------------

# def test_parse_row():    
    # cols = parse_colnames()
    # r = parse_row(vec=next(csv_block(1)))
    # assert len(r) == 271
    # d = dict(zip(cols, r))
    # assert d['year'] > 2000
    # assert isinstance(d['title'],str)       
# def test_lines():
   # a = next(csv_block(1))
   # assert isinstance(a, list)
   # assert isinstance(a[5], str)   

#------------------------------------------------------------------------------------
LINE1_2013_PARSED = [2013, '20140617', 'Общество с ограниченной ответственностью', 'СОК "Эдельвейс"', '24', 93, 4, 0, '67645404', '0', '16', '93.04', '2454021005', '384', '1', 0, 0, 0, 0, 0, 0, 0, 0, 20, 94, 0, 0, 0, 0, 0, 0, 0, 0, 20, 94, 161, 64, 0, 0, 467, 876, 0, 0, 459, 212, 0, 0, 1087, 1152, 1106, 1246, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 889, 746, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 216, 500, 0, 0, 0, 0, 0, 0, 216, 500, 1106, 1246, 13027, 8511, 12736, 7253, 291, 1258, 0, 0, 0, 0, 291, 1258, 0, 0, 0, 0, 0, 0, 0, 0, 71, 61, 220, 1197, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 220, 1196, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[2013, 'Открытое акционерное общество', 'Российское акционерное общество по производству цветных и драгоценных металлов "Норильский никель"', 24, 65, 23, 1, '00002565', '12247', '16', '65.23.1', '2457009983', '384', '2', 150, 150, 0, 0, 0, 0, 0, 0, 21, 56, 0, 0, 3129154, 3129154, 35332, 18558, 0, 0, 3164657, 3147918, 23, 23, 0, 0, 3728, 1951, 2970548, 2900387, 31526, 13763, 0, 0, 3005825, 2916124, 6170482, 6064042, 47250, 47250, 0, 0, 0, 0, 2266991, 2266991, 7087, 7087, 3848006, 3741048, 6169334, 6062376, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 226, 360, 0, 0, 922, 1306, 0, 0, 1148, 1666, 6170482, 6064042, 2245363, 2951506, 2100227, 2770211, 145136, 181295, 0, 0, 31315, 52939, 113821, 128356, 13748, 29792, 5230, 1364, 0, 0, 42, 58, 3508, 12216, 129333, 147354, 40038, 27104, -18723, -18867, 0, 0, 32894, 16500, 15231, 14258, 106958, 122492, 0, 0, 0, 0, 106958, 122492, 47250, 0, 2266991, 7087, 3741048, 6062376, 0, 0, 0, 0, 106958, 106958, 106958, 106958, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47250, 0, 2266991, 7087, 3848006, 6169334, 6169334, 3062376, 2249685, 0, 57, 0, 2249628, 2245685, 8132, 20362, 0, 154, 2217037, 4000, 13748, 0, 0, 0, 13748, 0, 0, 0, 0, 0, 0, 0, 13748, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17748, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

from row_parser import adjust_row   
def test_row_parser():    
    v = ['Открытое акционерное общество "Российское акционерное общество по производству цветных и драгоценных металлов "Норильский никель"', '00002565', '12247', '16', '65.23.1', '2457009983', '384', '2', '150', '150', '0', '0', '0', '0', '0', '0', '21', '56', '0', '0', '3129154', '3129154', '35332', '18558', '0', '0', '3164657', '3147918', '23', '23', '0', '0', '3728', '1951', '2970548', '2900387', '31526', '13763', '0', '0', '3005825', '2916124', '6170482', '6064042', '47250', '47250', '0', '0', '0', '0', '2266991', '2266991', '7087', '7087', '3848006', '3741048', '6169334', '6062376', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '226', '360', '0', '0', '922', '1306', '0', '0', '1148', '1666', '6170482', '6064042', '2245363', '2951506', '2100227', '2770211', '145136', '181295', '0', '0', '31315', '52939', '113821', '128356', '13748', '29792', '5230', '1364', '0', '0', '42', '58', '3508', '12216', '129333', '147354', '40038', '27104', '-18723', '-18867', '0', '0', '32894', '16500', '15231', '14258', '106958', '122492', '0', '0', '0', '0', '106958', '122492', '47250', '0', '2266991', '7087', '3741048', '6062376', '0', '0', '0', '0', '106958', '106958', '106958', '106958', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '47250', '0', '2266991', '7087', '3848006', '6169334', '6169334', '3062376', '2249685', '0', '57', '0', '2249628', '2245685', '8132', '20362', '0', '154', '2217037', '4000', '13748', '0', '0', '0', '13748', '0', '0', '0', '0', '0', '0', '0', '13748', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '17748', '15', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    p = adjust_row(v, 2013)
    assert p == LINE1_2013_PARSED
    
#------------------------------------------------------------------------------------
    
from reader import Dataset
def test_reader():
    assert Dataset(2013).peep(skip=0) == LINE1_2013_PARSED   