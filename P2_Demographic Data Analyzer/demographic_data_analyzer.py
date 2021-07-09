import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # print(df.columns)
    # print('\n\n\n\n')
    # print(df.info())
    print('\n\n\n\n')



    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?

    # print(df['sex'] == 'Male')
    # print(df['sex'].value_counts())
    # male = df['sex'] == 'male'
    # print(df.loc[df['sex'] == 'Male'])
    # print(df.loc[df['sex'] == 'Male', ['age', 'sex']])
    # print(df.loc[df['sex'] == 'Male', ['age']].mean())
    # print(df[['age','sex']])
    average_age_men = float(df.loc[df['sex'] == 'Male', ['age']].mean().round(1))

    # What is the percentage of people who have a Bachelor's degree?

    # print(df['education'].value_counts())
    # print(df['education'] == 'Bachelors')
    # print(df.loc[df['education'] == 'Bachelors', ['education']].count())
    # print(df.shape[0])
    number_of_bachelors_education = int(df.loc[df['education'] == 'Bachelors', ['education']].count())
    total_number_of_people = int(df.shape[0])
    percentage_bachelors = (number_of_bachelors_education / total_number_of_people * 100).__round__(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # print(df['education'].value_counts())
    # print(df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), ['salary']].count())
    # print(df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), ['salary']])

    higher_education_df = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), ['salary']]
    people_having_higher_education_greater_than_50k = int(
        (higher_education_df.loc[higher_education_df['salary'] == '>50K', ['salary']]).count())

    # What percentage of people without advanced education make more than 50K?

    lower_education_df = df.loc[
        ~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')), [
            'salary']]
    people_having_lower_education_greater_than_50k = int(
        (lower_education_df.loc[lower_education_df['salary'] == '>50K', ['salary']]).count())

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = int(higher_education_df.count())
    lower_education = int(lower_education_df.count())

    # percentage with salary >50K
    higher_education_rich = (people_having_higher_education_greater_than_50k / higher_education * 100).__round__(1)
    lower_education_rich = (people_having_lower_education_greater_than_50k / lower_education * 100).__round__(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    workers_working_minimum_hours = df.loc[df['hours-per-week'] == df['hours-per-week'].min(), ['salary']]
    num_min_workers = int(workers_working_minimum_hours.count())

    rich_workers_with_min_hours = int(workers_working_minimum_hours[workers_working_minimum_hours['salary'] == '>50K'].count())

    rich_percentage = rich_workers_with_min_hours/num_min_workers*100

    # What country has the highest percentage of people that earn >50K?
    people_more_than_50K_df = df.loc[df['salary'] == '>50K', ['native-country']].value_counts().sort_index()
    # print(people_more_than_50K_df)

    countries_with_people_more_than_50K_salary = df.loc[df['salary'] == '>50K', ['native-country']]['native-country'].unique()


    people_of_each_country = df.loc[df['native-country'].isin(countries_with_people_more_than_50K_salary)]

    count_of_people_of_each_country = people_of_each_country['native-country'].value_counts().sort_index()
    # print(count_of_people_of_each_country)

    # print(people_more_than_50K_df.div(count_of_people_of_each_country))
    # print(people_more_than_50K_df.divide(count_of_people_of_each_country, fill_value=0))
    percentage_of_people_of_each_country_earing_more_than_50K = people_more_than_50K_df/count_of_people_of_each_country.values*100
    # print(percentage_of_people_of_each_country_earing_more_than_50K)
    # print(percentage_of_people_of_each_country_earing_more_than_50K.loc[percentage_of_people_of_each_country_earing_more_than_50K['native-country'] == percentage_of_people_of_each_country_earing_more_than_50K.max()])

    highest_earning_country = percentage_of_people_of_each_country_earing_more_than_50K[percentage_of_people_of_each_country_earing_more_than_50K ==
                                                                    percentage_of_people_of_each_country_earing_more_than_50K.max()].keys()[0][0]
    highest_earning_country_percentage = (percentage_of_people_of_each_country_earing_more_than_50K.max()).round(1)


    # Identify the most popular occupation for those who earn >50K in India.
    India_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), ['occupation']].value_counts()
    top_IN_occupation = India_occupation[India_occupation == India_occupation.max()].keys()[0][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print('\n')
        print("Number of each race:", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == '__main__':
    calculate_demographic_data()
