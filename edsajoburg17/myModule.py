# import the numpy and pandas module from the python library
import numpy as np
import pandas as pd

# import data and convert it to a dataframe
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

# read a csv file to twitter_df as a dataframe
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping municipality twitter handles to the municipality name
mun_dict = {'@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

# dictionary of english stopwords
stop_words_dict = {
        'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep',
        'something', 'nothing', 'thereupon', 'may', 'why', 'â€™s', 'therefore',
        'you', 'with', 'towards', 'make', 'really', 'few', 'former', 'during',
        'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming',
        'through', 'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole',
        'down', 'seem', 'whereas', 'to', 'their', 'various', 'thereafter',
        'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein',
        'become', 'last', 'between', 'still', 'was', 'almost', 'twelve',
        'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see',
        'whose', 'everywhere', 'yourselves', 'across', 'myself', 'further',
        'did', 'then', 'is', 'except', 'up', 'take', 'became', 'however',
        'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein',
        'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither',
        'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 'forty',
        'what', 'less', 'and', 'please', 'toward', 'about', 'below',
        'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top',
        'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything',
        'nowhere', 'ca', 'though', 'least', 'so', 'both', 'otherwise',
        'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its',
        'after', 'bottom', 'call', 'nâ€™t', 'name', 'even', 'eleven', 'by',
        'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 'much', 'another',
        'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full',
        'themselves', 'been', 'in', "'d", 'wherever', 'part', 'someone',
        'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most',
        'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as',
        'nobody', 'also', 'along', 'than', 'anything', 'he', 'there', 'does',
        'we', 'â€™ll', 'latterly', 'are', 'ten', 'hers', 'should', 'they',
        'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely',
        'sixty', 'made', "'m", 'always', 'those', 'have', 'again', 'her',
        'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 'sometimes',
        'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot',
        'â€˜ll', 'too', 'seems', 'â€™m', 'himself', 'latter', 'whither',
        'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say',
        'via', 'but', 'often', 're', 'our', 'because', 'rather', 'using',
        'without', 'throughout', 'on', 'she', 'never', 'eight', 'no',
        'hereupon', 'them', 'whereafter', 'quite', 'which', 'move', 'thru',
        'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t','him', 'could',
        'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several',
        'side', 'whence', 'me', 'same', 'were', 'it', 'every', 'third',
        'together']}

# funtion 1: Metric Dictionary
def dictionary_of_metrics(items):
    ''' Returns a dictionary of the five number summary.

        Keyword argument:
        items (list) -- a list of number values.

        Returns:
        dictionary: maximum value (max), median, minimum value (min),
                    first quartile (q1) and the third quartile (q3).

        Example:
        >>> five_num_summary([11,1,3,5,8,9,4,10,2,6,7])
            {'mean': 3.0, 'median': 3.0, 'var': 2.5, 'std': 1.58, 'min': 1, 'max': 5}
    '''
    # sort the list and create an array
    items.sort()
    items_array = np.array(items)

    # return a dictionary
    return {'mean':round(items_array.mean(),2),
           'median':round(np.percentile(items_array,50),2),
           'var':round(items_array.var(ddof=1),2),
           'std':round((items_array.var(ddof=1))**(1/2),2),
           'min':round(items_array.min(),2),
           'max':round(items_array.max(),2)}

### END FUNCTION

# Function 2: Five Number Summary
def five_num_summary(items):
    ''' Returns a dictionary of the five number summary.

        Keyword argument:
        items (list) -- a list of number values.

        Returns:
        dictionary: maximum value (max), median, minimum value (min),
                    first quartile (q1) and the third quartile (q3).

        Example:
        >>> five_num_summary([11,1,3,5,8,9,4,10,2,6,7])
           {'max': 11, 'median': 6.0, 'min': 1, 'q1': 3.5, 'q3': 8.5}
    '''
    # sort the list and create an array
    items.sort()
    items_array = np.array(items)

    # return a dictionary of the five number summary
    return {'max':round(items_array.max(),2),
            'median':round(np.percentile(items_array,50),2),
            'min':round(items_array.min(),2),
            'q1':round(np.percentile(items_array,25),2),
            'q3':round(np.percentile(items_array,75),2)}

### END FUNCTION
# Function 3: Date Parser
def date_parser(dates):
    ''' Returns a list of the dates

        Keyword argument:
        dates (list) - a list with the date & time string in the format:
                     'yyyy-mm-dd hh:mm:ss'

        Returns:
        list: list of string with the 'yyyy-mm-dd' date format

        Example:
        >>> date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:10'])
        ['2019-11-29', '2019-11-29']
    '''
    return[date.split(' ')[0] for date in dates]
### END FUNCTION

# Function 4: Municipality & Hashtag Detector
def extract_municipality_hashtags(df):
    # your code here
    ''' Returns a modified dataframe with two new columns.

        Keyword argument:
        df (pandas dataframe): pandas dataframe with Eskom dataframe

        Returns:
        dataframe: modified dataframe with 2 new columns 'municipality' and
                   'hastags'. The column data will be determined from the
                   initial 'df' dataframe.
    '''
    # Defines the function that returns municipality names
    def mun(new):
        ''' Returns the municipality if in a tweet from df.

            Keyword argument:
            df (dataframe) -- dataframe of the ESKOM data

            Returns:
            Returns a value (municipality) if the twitter handle
            is in the tweet.
            Else, it returns 'NaN'
        '''

        mun_str = ''
        # iterate individual elements in dict_key
        for i in mun_dict.keys() :
            if i in new:
                mun_str += mun_dict[i]
        if mun_str == '':
            mun_str = np.nan
        return mun_str


    # Defines the function that returns a list of hashtags from a tweet
    def hasht(new):
        ''' Returns a list of hashtag phrases from a tweet.

            Keyword argument:
            df (dataframe) -- dataframe of the ESKOM data

        '''

        hashtags_list = []
        new_split = new.split()
        for j in new_split:
            if j[0] == "#":
                hashtags_list.append(j.lower())
        if hashtags_list == []:
            hashtags_list.append(np.nan)
        return hashtags_list


    # Concatenates the municipality names and hashtag lists in their respective columns
    df['municipality'] = df['Tweets'].apply(lambda x: mun(x))
    df['hashtags'] = df['Tweets'].apply(lambda x: hasht(x),)

    return df
### END FUNCTION

#Function 5: Number of Tweets per Day
def number_of_tweets_per_day(df):
    ''' returns a dataframe with the number of tweets per day

        Keyword argument:
        df (dataframe): Eskom dataframe

        Returns:
        dataframe:  a new dataframe with the date as the index

        Example:
        >>>number_of_tweets_per_day(twitter_df)
                    Tweets
            Date
        2019-11-20     18
        2019-11-21     11
    '''
    # get the date in the 'yyyy-mm-dd' format
    df['Date']=df['Date'].apply(lambda x: x.split(' ')[0])

    # create a new dataframe tt with the no of tweets per day
    tt = pd.DataFrame(pd.to_datetime(df['Date'],format = '%Y/%m/%d').value_counts())

    # rename the index column
    tt.rename_axis('Date',inplace=True)

    # rename the coumn to 'Tweets'
    tt.rename(columns={'Date':'Tweets'},inplace=True)

    # sorts the dataframe by the index
    tt.sort_index(inplace=True)

    return tt
### END OF FUNCTION

# Function 6: Word Splitter
def word_splitter(df) :
    ''' returns a list of words from a string

        Keyword argument:
        df (dataframe): dataframe with ESKOM data

        Return:
        dataframe: return a modified dataframe wiith a new columns

        Example:
        >>> word_splitter(twitter_df)
                        Tweets          Date                Split Tweets
        0  @BongaDlulane Please.. 2019-11-29 12:50:54  [@bongadlulane, please..]
    '''
    # creates a new column named 'Split Tweets'
    df['Split Tweets'] = df['Tweets'].apply(lambda y: y.lower().split(''))

    # returns a dataframe with 3 columns
    last = df[['Tweets', 'Date', 'Split Tweets']]

    return last
### END OF FUNCTION
