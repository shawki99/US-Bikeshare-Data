import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nPlease enter the name of the city (chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
            #We were able to get the name of the city to analyze data.
            city = CITY_DATA[city_name.lower()]
        else:
            #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nPlease enter the name of the month ('all' to apply no month filter or january, february, ... , june)\n")
        if month_name.lower() in MONTH_DATA:
            #We were able to get the name of the month to analyze data.
            month = month_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nPlease enter the day ('all' to apply no day filter or monday, tuesday, ... sunday)\n")
        if day_name.lower() in DAY_DATA:
            #We were able to get the name of the month to analyze data.
            day = day_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n")

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
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print(df['month'])
    print('the most common month is {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day is {}'.format(most_common_day))


    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('the most common hour is {}'.format(str(most_common_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_s = df['Start Station'].mode()[0]
    print('the most common used start station is {}'.format(most_common_s))

    # TO DO: display most commonly used end station
    most_common_e = df['End Station'].mode()[0]
    print('the most common used end station is {}'.format(most_common_e))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_c = (df['Start Station'] + "--" + df['End Station']).mode()[0]
    print('the most common used combination of start station and end station trip is {}'.format(str(most_common_c.split("--"))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print("the total travel time was : {}".format(str(total_tt)))

    # TO DO: display mean travel time
    avg_tt = df['Trip Duration'].mean()
    print("the average travel time was : {}".format(str(avg_tt)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you want to view next five row of the data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr_typs = df['User Type'].value_counts()
    print("the user types count is : {}".format(str(usr_typs)))

    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gndr = df['Gender'].value_counts()
        print("the count of gender is : {}".format(str(gndr)))
        # TO DO: Display earliest, most recent, and most common year of birth
        e_birth = df['Birth Year'].min()
        print("the earliest birth year is : {}".format(str(e_birth)))
        
        mr_birth = df['Birth Year'].max()
        print("the most recent birth year is : {}".format(str(mr_birth)))
        
        mc_birth = df['Birth Year'].mode()[0]
        print("the most common birth year is : {}".format(str(mc_birth)))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#         print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        while True:
            view_raw_data = input('\nWould you want to see the first five row of the data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
