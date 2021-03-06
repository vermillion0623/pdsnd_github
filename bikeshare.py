import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Enter City Name[chicago, new york city, washington]: ")
            city = city.lower()
            if CITY_DATA[city]:
                break
        except:
            pass
            print(" Invalid City Name! Try again! ")

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = input("Enter Month: ")
            #print(months.index(month))
            month = month.lower()
            if month == "all" or MONTHS.index(month):
                break
        except:
            pass
            print(" Invalid Month!! Try again!! ")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter day of week: ")
            #print(day.title())
            day = day.lower()
            if day == "all" or (DAYS.index(day)+1):
                break
        except:
            pass
            print(" Invalid Days!!! Try again!!! ")


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
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    #print(df['day_of_week'])

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAYS.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("most common month: ", df['month'].mode()[0])

    # display the most common day of week
    print("most common day of week: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("most common start hour: ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station: ",  df['Start Station'].mode()[0])

    # display most commonly used end station
    print("most commonly used end station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    #print(df.groupby(["Start Station", "End Station"]).count("Trip Duration"))
    #df["Start_End"] = list(zip(df["Start Station"], df["End Station"]))
    #print("most frequent combination of start/end station: ", df["Start_End"].mode()[0])
    print("most frequent combination of start station and end station trip: ", df["Trip Duration"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time: ", df['Trip Duration'].sum())

    # display mean travel time
    print("mean travel time: ", round(df['Trip Duration'].mean(), 1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    print('\n')

    # Display counts of gender
    print(df['Gender'].value_counts())
    print('\n')

    # Display earliest, most recent, and most common year of birth
    print("earliest year of birth: ", int(min(df['Birth Year'].dropna())))
    print("most recent year of birth: ", int(max(df['Birth Year'].dropna())))
    print("most common year of birth: ", int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data."""
    i = 0
    # TO DO: convert the user input to lower case using lower() function
    raw = input("\nDo you want to see raw data? [input Yes or No]\n")
    raw = raw.lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df[i:i+5])
            # TO DO: convert the user input to lower case using lower() function
            raw = input("\nDo you want to see additional raw data? [input Yes or No]\n")
            raw = raw.lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print(df.columns)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == "chicago" or city == "new york city":
            user_stats(df)
        else:
            print("No User Status for ", city)

        display_raw_data(df)

        while True:
            try:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                restart = restart.lower()
                if restart == 'yes' or restart == "no":
                    break
                else :
                    print(" Invalid Input, Try again ")
            except:
                pass
                print(" Invalid Input, Try again ")

        if restart != 'yes':
            break




if __name__ == "__main__":
	main()
