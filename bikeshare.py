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
    city = input("\nPlease type one of the folowing cities you want to be filtered 1-Chicago, 2-New York City, 3-Washington: ").lower()
    while city not in CITY_DATA.keys():
        city = input("\nOops! You haven't choosen a correct city, please check spelling!: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("\nPlease type a month you want to filter by and choose from January to June or type All: ").lower()
    while month not in MONTH_LIST:
        month = input("\nSorry! Please try again by choosing a month from January to June!: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input("\nWhat day of week would like to filter by?: ").lower()
    while day not in days:
        day = input("\nsorry! incorrect day, please try again: " ).lower()

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('The most common month is:' ,common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print('The most common day of the week is:' ,common_day)


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour

    common_strt_hr = df['start_hour'].mode()[0]

    print('The most common start hour is:' ,common_strt_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start station is:' ,start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most common end station is:' ,end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_stations'] = df['Start Station'] + " - " + df['End Station']
    freq_strt_end_stations = df['start_end_stations'].mode()[0]
    print('The most frequent start and end station combination are:' ,freq_strt_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['travel time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    total_trvl_time = df['travel time'].sum()
    print("The total travel time is:" ,total_trvl_time)


    # TO DO: display mean travel time
    mean_trvl_time = df['travel time'].mean()
    print("The mean travel time is:" ,mean_trvl_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts of user types:\n' ,user_types_count)


    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender types:\n' ,gender_types)
    except:
        print('\nThere is no gender data available for this city')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nThe earliest birth year is:' ,earliest_birth_year)
        recent_birth_year = int(df['Birth Year'].max())
        print('\nThe latest birth year is:' ,recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe most common birth year is:' ,common_birth_year)
    except:
        print('\nThere is no birth year data available for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """
    Raw data is displayed upon request by the user.
    """

    see_data = input("Would you like to see the raw data?: ").lower()


    start_index = 0
    end_index = 5


    while end_index in range(df.shape[0]):
        if see_data == 'yes':
            print(df.iloc[start_index:end_index])
            start_index += 5
            end_index += 5

            no_more = input("Would you like to see more?: ").lower()
            if no_more == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
