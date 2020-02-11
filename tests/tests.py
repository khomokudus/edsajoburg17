from edsajoburg17 import myModule

def test_functions_in_myModule():
    '''
    test if dictionary_of_metrics functions works correctly
    '''
    assert myModule.dictionary_of_metrics([1,2,3,4,5]) ==  {'mean': 3.0,
            'median': 3, 'variance': 2.5, 'standard deviation': 1.58, 'min': 1,
            'max': 5}, 'incorrect'

    assert myModule.dictionary_of_metrics([25,25,8,7,8,9,6,2,5,8,9,6,
                2,5,2,4]) == {'mean': 8.19, 'median': 6.5, 'variance': 48.7,
                'standard deviation': 6.98, 'min': 2, 'max': 25}, 'incorrect'


    # Test if the function five_num_summary is working properly

    assert myModule.five_num_summary([1,2,3,4,5,6,7,8,9,10,11]) == {'max': 11,
                'median': 6, 'min': 1, 'q1': 3, 'q3': 9}, 'incorrect'

    assert myModule.five_num_summary([11,785,15214,415,8889,12548,1000,1250,35,
                8,7,900,10504]) == {'max': 15214, 'median': 900, 'min': 7,
                'q1': 35, 'q3': 10504}, 'incorrect'

    # test the function date_parser:
    assert myModule.date_parser(['2019-11-29 12:50:54','2019-11-29 12:46:53',
            '2019-11-29 12:46:10'])==['2019-11-29', '2019-11-29', '2019-11-29'],
            'incorrect'
