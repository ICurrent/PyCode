from countryinfo import CountryInfo

print()
No_of_Country = int(input('Enter the Number Country: '))

for _ in range(No_of_Country):
    print()
    countryCount = input('Enter your country: ')
    country = CountryInfo(countryCount)
    print('Capital is: ',country.capital())
    print('Currencies is: ',country.currencies())
    print('Language is: ',country.languages())
    print('Borders are: ', country.borders())
    print('Others names: ',country.alt_spellings())