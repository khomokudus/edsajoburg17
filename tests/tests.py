from edsajoburg17 import myModule

def test_dictionary_of_metrics():
    '''
    Test if dictionary_of_metrics functions works correctly
    '''
    assert myModule.dictionary_of_metrics([1,2,3,4,5]) ==  {'mean': 3.0,
        'median': 3.0, 'var': 2.5, 'std': 1.58, 'min': 1, 'max': 5},
        'incorrect'

    assert myModule.dictionary_of_metrics([25,25,8,7,8,9,6,2,5,8,9,6,2,5,2,4])==
    {'mean': 8.19, 'median': 6.5, 'var': 48.7, 'std': 6.98, 'min': 2,
    'max': 25}, 'incorrect'

def test_five_num_summary():
    '''
    Test if the five number summary function works properly.
    '''
    assert myModule.five_num_summary([1,2,3,4,5,6,7,8,9,10,11]) == {'max': 11,
        'median': 6.0, 'min': 1, 'q1': 3.5, 'q3': 8.5}, 'incorrect'

    assert myModule.five_num_summary([11,785,15214,415,8889,12548,1000,1250,35,
                8,7,900,10504]) == {'max': 15214, 'median': 900.0, 'min': 7,
                'q1': 35.0, 'q3': 8889.0}, 'incorrect'
def test_date_parser():
    '''
    Test if the date parser function works properly.
    '''
    assert myModule.date_parser(['2019-11-29 12:50:54','2019-11-29 12:46:53',
    '2019-11-29 12:46:10'])== ['2019-11-29', '2019-11-29', '2019-11-29'],
    'incorrect'

    assert myModule.date_parser(['2015-12-20 11:05:01','2030-11-02 10:05:41'])==
    ['2015-12-20','2030-11-02'], 'incorrect'
