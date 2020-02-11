# edsajoburg17
This library contains a myModule; which has seven functions to work on the
Eskom data.
The functions:
  1. dictionary_of_metrics
    - 'returns a dictionary with the mean, median,variance, standard deviation,
       minimum and maximum value'

  2. five_num_summary
    - 'returns the five no summary dictionary {max,median,min,q1,q3}'

  3. date_parser
    - 'returns the date in the 'yyyy-mm-dd' format'

  4. extract_municipality_hashtags
    - 'adds two columns to the dataframe'

  5. number_of_tweets_per_day
    - 'counts the number of tweets per day'

  6. word_splitter
    - 'splits sentences into a list of words'

  7. stop_words_remover
    - 'removes any 'stop words' from a string if found in the dictionary of
    stop words.'

## building this package locally
'python setup.py sdist'

## installing this package from GitHub
'pip install git+https://github.com/khomokudus/edsajoburg17.git'

## updating this package from GitHub
'pip install --upgrade git+https://github.com/khomokudus/edsajoburg17.git'
