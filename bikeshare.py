import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    list_cities=['chicago', 'new york city', 'washington']
    list_months =['january', 'february', 'march', 'april', 'may', 'june','all']
    list_days =['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    city=''
    """city= input('Enter a city name. Ex. chicago, new york city, washington : ').lower()"""
    while True:
        try:
            city= input('Enter a city name. Ex. chicago, new york city, washington : ').lower()
            if city in list_cities:
                break
            print('That is not a valid city!')
        except Exception as f:
            print(f)
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Enter a month, or all the months with the word ''all'' : ').lower()
            if month in list_months:
                break
            print('That is not a valid month!')
        except Exception as r:
            print(r)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Enter a day of the week, or all the days of the week with the word ''all'' : ').lower()
            if day in list_days:
                break
            print('That is not a valid day!')
        except Exception as e:
            print(e)



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    import calendar
    month_inp=''
    move_month=0
    day_inp=''
    month_num=0
    month_str=''
    day_num=[]
    first_digit_day=[]
    second_digit_day=[]
    format_day = 0
    count_day=0
    count=0
    dict_month={'january':1, 'february':2,'march':3, 'april':4, 'may':5, 'june':6}
    dict_days={'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
    month_names=['january', 'february','march', 'april', 'may', 'june']
    month_inp = str(month)
    day_inp = str(day)
    city_inp=str(city)
    print('running...')

    """Determine the month in number format as a variable month_num"""
    if month != 'all':
        for monthsp, number in dict_month.items():
            if monthsp == month:

                month_num = number
                month_str=str(month_num)
                if month_num<10:
                    month_str='0' + str(month_num)
                break


    """Find the day in format number"""
    if day != 'all':
        for daysp, number in dict_days.items():
            if daysp is day:
                format_day = number
                break

    """Create a list with the days in number format in all of the month"""
    if day != 'all':
        if month != 'all':

            for i in range(1, calendar.monthrange(2017,month_num)[1]):
                count=i
                if calendar.weekday(2017,month_num,i)==format_day:
                    day_num.append(count)
        """Filter day and not filter month"""
        if month == 'all':
            print('This will took around 5 minutes...')
            format_day=0
            move_month=0
            month_num=0
            month_str =''
            df=pd.DataFrame()

            """Find the day in format number"""
            if day != 'all':
                for daysp, number in dict_days.items():
                    if daysp is day:
                        format_day = number
                        break
                for j in range(1,6):
                    move_month=j
                    day_num=[]
                    for i in range(1, calendar.monthrange(2017, move_month)[1]):
                        count=i
                        if calendar.weekday(2017,move_month,i)==format_day:
                            day_num.append(count)
                            month_num = move_month
                            month_str=str(month_num)
                        if month_num<10:
                            month_str='0' + str(month_num)

                        if city == 'chicago':
                            info= pd.read_csv('./chicago.csv')
                            info2=info[info['Start Time'].str[6] == str(month_str[1])]
                            info3=info2[info2['Start Time'].str[5] == str(month_str[0])]

                        if city == 'washington':
                            info= pd.read_csv('./washington.csv')
                            info2=info[info['Start Time'].str[6] == str(month_str[1])]
                            info3=info2[info2['Start Time'].str[5] == str(month_str[0])]


                        if city == 'new york city':
                            info= pd.read_csv('./new_york_city.csv')
                            info2=info[info['Start Time'].str[6] == str(month_str[1])]
                            info3=info2[info2['Start Time'].str[5] == str(month_str[0])]

                        day_mod=''
                        num_char=''
                        if day != 'all':
                            for index in range(len(day_num)):
                                num_char=str(day_num[index])
                                if len(num_char)==1:
                                    day_mod='0'+ num_char
                                    day_num.remove(int(num_char))
                                    day_num.insert(0,day_mod)

                        num_string=''
                        first_digit=['','','','','']
                        second_digit=['','','','','']
                        contador=-1
                        if day != 'all':
                            for i in range (len(day_num)):
                                num_string = str(day_num[i])
                                first_digit[i]=num_string[0]
                                second_digit[i]=num_string[1]

                        if len(first_digit) > 1:
                            df_day1_digit1=info3[info3['Start Time'].str[8] == str(first_digit[0])]
                            df_day1=df_day1_digit1[df_day1_digit1['Start Time'].str[9] == str(second_digit[0])]
                            df_parcial = df_day1

                        if len(first_digit) > 2:
                            df_day2_digit1=info3[info3['Start Time'].str[8] == str(first_digit[1])]
                            df_day2=df_day2_digit1[df_day2_digit1['Start Time'].str[9] == str(second_digit[1])]
                            df_parcial = pd.concat([df_day1, df_day2])

                        if len(first_digit) > 3:
                            df_day3_digit1=info3[info3['Start Time'].str[8] == str(first_digit[2])]
                            df_day3=df_day3_digit1[df_day3_digit1['Start Time'].str[9] == str(second_digit[2])]
                            df_parcial = pd.concat([df_day1, df_day2, df_day3])
                        if len(first_digit) > 4:
                            df_day4_digit1=info3[info3['Start Time'].str[8] == str(first_digit[3])]
                            df_day4=df_day4_digit1[df_day4_digit1['Start Time'].str[9] == str(second_digit[3])]
                            df_parcial = pd.concat([df_day1, df_day2, df_day3,df_day4])
                        if len(first_digit) > 5:
                            df_day5_digit1=info3[info3['Start Time'].str[8] == str(first_digit[4])]
                            df_day5=df_day5_digit1[df_day5_digit1['Start Time'].str[9] == str(second_digit[4])]
                            df_parcial = pd.concat([df_day1, df_day2, df_day3,df_day4,df_day5])
                        if move_month == 1:
                            df1=df_parcial
                        if move_month == 2:
                            df2=pd.concat([df_parcial])
                        if move_month == 3:
                            df3=pd.concat([df_parcial])

                        if move_month ==4:
                            df4=pd.concat([df_parcial])
                        if move_month ==5:
                            df5=pd.concat([df_parcial])
                        if move_month ==6:
                            df6=pd.concat([df_parcial])


            df=pd.concat([df1,df2,df3,df4,df5,df6])
            return df


    """Add a 0 to the number day that is less than 10"""
    day_mod=''
    num_char=''
    if day != 'all':
        for index in range(len(day_num)):
            num_char=str(day_num[index])
            if len(num_char)==1:
                day_mod='0'+ num_char
                day_num.remove(int(num_char))
                day_num.insert(0,day_mod)

    """Create 2 list, the first with the first digit of each day_num and the second with the second digit"""
    num_string=''
    first_digit=['','','','','']
    second_digit=['','','','','']
    contador=-1
    if day != 'all':
        for i in range (len(day_num)):
            num_string = str(day_num[i])
            first_digit[i]=num_string[0]
            second_digit[i]=num_string[1]


    if city == 'chicago':
       info= pd.read_csv('./chicago.csv')

    if city == 'washington':
       info= pd.read_csv('./washington.csv')


    if city == 'new york city':
       info= pd.read_csv('./new_york_city.csv')


    """Filter of month and not filter in day"""
    if month != 'all' and day == 'all':

        df2= info[info['Start Time'].str[6] == str(month_str[1])]
        df=df2[df2['Start Time'].str[5] == str(month_str[0])]
        return df


    """No filter"""

    if month == 'all'and day == 'all':
        if city == 'chicago':
            df= pd.read_csv('./chicago.csv')

        if city == 'washington':
            df= pd.read_csv('./washington.csv')


        if city == 'new york city':
            df= pd.read_csv('./new_york_city.csv')
        return df


    """Filter day and month"""

    if month != 'all' and day != 'all':


        if len(first_digit) > 1:
            df_day1_digit1=info[info['Start Time'].str[8] == str(first_digit[0])]
            df_day1=df_day1_digit1[df_day1_digit1['Start Time'].str[9] == str(first_digit[0])]
            df_day = df_day1

        if len(first_digit) > 2:
            df_day2_digit1=info[info['Start Time'].str[8] == str(first_digit[1])]
            df_day2=df_day2_digit1[df_day2_digit1['Start Time'].str[9] == str(second_digit[1])]
            df_day = pd.concat([df_day1, df_day2])

        if len(first_digit) > 3:
            df_day3_digit1=info[info['Start Time'].str[8] == str(first_digit[2])]
            df_day3=df_day3_digit1[df_day3_digit1['Start Time'].str[9] == str(second_digit[2])]
            df_day = pd.concat([df_day1, df_day2, df_day3])
        if len(first_digit) > 4:
            df_day4_digit1=info[info['Start Time'].str[8] == str(first_digit[3])]
            df_day4=df_day4_digit1[df_day4_digit1['Start Time'].str[9] == str(second_digit[3])]
            df_day = pd.concat([df_day1, df_day2, df_day3,df_day4])
        if len(first_digit) > 5:
            df_day5_digit1=info[info['Start Time'].str[8] == str(first_digit[4])]
            df_day5=df_day5_digit1[df_day5_digit1['Start Time'].str[9] == str(second_digit[4])]
            df_day = pd.concat([df_day1, df_day2, df_day3,df_day4,df_day5])



        df2=df_day[df_day['Start Time'].str[6] == str(month_str[1])]
        df=df2[df2['Start Time'].str[5] == str(month_str[0])]

        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['common month']=df['Start Time'].str[5] + df['Start Time'].str[6]
    print('The most common month is:', df.groupby('common month')['common month'].count().nlargest(1))

    # TO DO: display the most common day of week
    df['common day']=df['Start Time'].str[8] + df['Start Time'].str[9]
    print('The most day of week:', df.groupby('common day')['common day'].count().nlargest(1))
    # TO DO: display the most common start hour
    df['Start Hour']=df['Start Time'].str[11] + df['Start Time'].str[12]
    print('The most start hour was:', df.groupby('Start Hour')['Start Hour'].count().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used Start Station:', df.groupby('Start Station')['Start Station'].count().nlargest(1))

    # TO DO: display most commonly used end station
    print('The most commonly used end Station:', df.groupby('End Station')['End Station'].count().nlargest(1))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination']= df['Start Station'] + ' - ' + df['End Station']
    print('The most frequent combination of start station and end station tip was:', df.groupby('Combination')['Combination'].count().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user tipes: ', df.groupby('User Type')['User Type'].count())

    # TO DO: Display counts of gender

    if city != 'washington':
        print('Counts per gender: ', df.groupby('Gender')['Gender'].count())
    if city == 'washington':
        print('there is not information about gender in this city')

    # TO DO: Display earliest, most recent, and most common year of birth

    if city != 'washington':
        print('The most common year of birth is: ', df.groupby('Birth Year')['Birth Year'].count().nlargest(1))
        print('The most recent year of birth is: ', df.groupby('Birth Year')['Birth Year'].max().nlargest(1))
        print('The earlist year of birth is: ', df.groupby('Birth Year')['Birth Year'].min().nsmallest(1))
    if city == 'washington':
        print('there is not information about birth dates in this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

'''prompt the user whether they would like to see the raw data. If the user answers 'yes,' then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data. The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no,' '''
def raw_data_user_stats(df):
    counter=5
    answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ').lower()
    while True:

        if answer == 'yes':
            print(df.tail(counter))
            answer = input('Would you like to see 5 more lines of raw data? Enter yes or no: ').lower()
            counter+=5
        if answer == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data_user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
