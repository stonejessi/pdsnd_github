import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# get user input for month (all, january, february, ... , june)
# get user input for day of week (all, monday, tuesday, ... sunday)
def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    city_options = ['chicago', 'new york city','washington']
    month_options = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Which city do you want to analyze: Chicago, New York City, or Washington?: ").lower()
        if city in city_options:
            break
        else:
            city = input("Please choose either: Chicago, New York City, or Washington: ").lower()

    while True:
        month = input("Would you like information for a particular month? or type \'all\' for all months: ").lower()
        if month in month_options:
            break
        else:
            month = input("Please choose either: January, February, March, April, May, June or all: ").lower()

    while True:
        day = input("Would you like inofrmation for a particular day or type \'all\' for all days: ").lower()
        if day in day_options:
            break
        else:
            day = input("Please choose either: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ").lower()

    return city, month, day
    print('-'*40)

def load_data(city, month, day):
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
# display the most common month
# display the most common day of week
# display the most common start hour
# load data and filter data
# load data file into a dataframe
# convert the Start time column to datetime
# extract month from Start Time into a new column
# filter by month if applicable
# use the index of the months list to get the corresponding int
# filter by month, day to create the new dataframe
def load_data(city,month,day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    common_month = df['month'].mode()[0]
    print('Most Common Travel Month:', common_month)

    df['day'] = df['Start Time'].dt.day
    if day != 'all':
        day = DAYS.index(day) +1
        df = df[ df['day'] == day]
    common_day = df['day'].mode()[0]
    print('Most Common Travel DAY:', common_day)

    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", common_start_hour)
    start_time = time.time()

    return df
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# display most commonly used start station
# display most commonly used end station
# display most frequent combination of start station and end station trip
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", common_end_station)

    print("The most common combination of start and end station trip is: ",common_start_station, common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# display total travel time
# display mean travel time
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is:", total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time is:", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display counts of user types
# Display counts of gender
# Display earliest, most recent, and most common year of birth
# the most earliest birth year
# the most recent birth year
# the most common birth year
def user_stats(df):
    print('\nCalculating User Stats...\n')

    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('no gender data for this city')

    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        earliest_year = birth_year.min()
        print("The earliest birth year:", earliest_year)
    else:
        print('no birth year data for this city')

    if 'Birth Year' in df.columns:
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
    else:
        print('no birth year data for this city')

    if 'Birth Year' in df.columns:
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    else:
        print('no birth year data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        see_data = input("\nYou like to see five rows of the raw data? type 'yes' or 'no' \n").lower()
        row_index = 0
        while True:
            if see_data != 'yes':
                break
            else:
                print(df[row_index: row_index + 5])
                row_index = row_index + 5
                see_data = input("\n Would you like to see five more rows of raw data? type 'yes' or 'no' \n").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while True:
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
	main()
