import pandas as pd

sold = pd.read_csv("w1_CRMLSListingCombined_Unfiltered.csv", low_memory=False)
listings = pd.read_csv("w1_CRMLSSoldCombined_Unfiltered.csv", low_memory=False)

#row/col counts
print('Sold dataset (rows,cols):', sold.shape)
print('Listings dataset (rows, cols):', listings.shape)

#unique property types (isn't working, is only showing residential??
print(f'Unique Sold: {sold["PropertyType"].unique()}')
print(f'Unique Listings: {listings["PropertyType"].unique()}')

#filter by residential
soldFiltered = sold[sold.PropertyType == 'Residential']
listingsFiltered = listings[listings.PropertyType == 'Residential']

#null count table
missingSum = pd.DataFrame({'Null Count': soldFiltered.isnull().sum(), 'Null Percentage': (soldFiltered.isnull().mean() * 100).round(2)})
print(missingSum)

#flagged
missingSum['Flag'] = missingSum['Null Percentage'] > 90
print('Flagged cols: ', missingSum.index[missingSum['Flag']])

#numeric distribution summary
print(f'ClosePrice: {soldFiltered['ClosePrice'].describe()}')
print(f'LivingArea: {soldFiltered['LivingArea'].describe()}')
print(f'DaysOnMarket: {soldFiltered['DaysOnMarket'].describe()}')

soldFiltered.to_csv("w23_CRMLSSoldFiltered.csv", index=False)
listingsFiltered.to_csv("w23_CRMLSListingFiltered.csv", index=False)

# Sold dataset (rows,cols): (766706, 81)
# Listings dataset (rows, cols): (680885, 79)
# Unique Sold: <StringArray>
# [               'Land',         'Residential',    'ResidentialLease',
#       'CommercialSale',  'ManufacturedInPark', 'BusinessOpportunity',
#      'CommercialLease',   'ResidentialIncome']
# Length: 8, dtype: str
# Unique Listings: <StringArray>
# [        'Residential',                'Land',  'ManufacturedInPark',
#    'ResidentialIncome',    'ResidentialLease',      'CommercialSale',
#      'CommercialLease', 'BusinessOpportunity']
# Length: 8, dtype: str
#                               Null Count  Null Percentage
# OriginalListPrice                    931             0.18
# ListingKey                             0             0.00
# CloseDate                          79977            15.85
# ClosePrice                         82895            16.43
# ListAgentFirstName                  3320             0.66
# ...                                  ...              ...
# BuyerOfficeName.1                  86298            17.11
# AssociationFee                    113191            22.44
# LotSizeSquareFeet                  39060             7.74
# MiddleOrJuniorSchoolDistrict      504466           100.00
# UnparsedAddress.1                    645             0.13

# [81 rows x 2 columns]
# Flagged cols:  Index(['FireplacesTotal', 'AboveGradeFinishedArea', 'TaxAnnualAmount',
#        'BuilderName', 'TaxYear', 'BuildingAreaTotal',
#        'ElementarySchoolDistrict', 'CoBuyerAgentFirstName',
#        'BelowGradeFinishedArea', 'BusinessType', 'CoveredSpaces',
#        'LotSizeDimensions', 'MiddleOrJuniorSchoolDistrict'],
#       dtype='str')
# ClosePrice: count    4.215710e+05
# mean     1.127716e+06
# std      1.228588e+06
# min      5.250000e+02
# 25%      5.760000e+05
# 50%      8.200000e+05
# 75%      1.295000e+06
# max      1.100000e+08
# Name: ClosePrice, dtype: float64
# LivingArea: count    5.041170e+05
# mean     1.923460e+03
# std      2.399811e+04
# min      0.000000e+00
# 25%      1.248000e+03
# 50%      1.650000e+03
# 75%      2.245000e+03
# max      1.702132e+07
# Name: LivingArea, dtype: float64
# DaysOnMarket: count    504466.000000
# mean         36.763663
# std          52.999819
# min        -265.000000
# 25%           8.000000
# 50%          18.000000
# 75%          47.000000
# max       12430.000000
# Name: DaysOnMarket, dtype: float64
# 135300
# 101

# Step 1 – Fetch the mortgage rate data from FRED
import pandas as pd
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']

# Step 2 – Resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
 mortgage.groupby('year_month')['rate_30yr_fixed']
 .mean()
 .reset_index()
)

# Step 3 – Create a matching year_month key on the MLS datasets
# Sold dataset — key off CloseDate
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')
# Listings dataset — key off ListingContractDate
listings['year_month'] = pd.to_datetime(
 listings['ListingContractDate']
).dt.to_period('M')

# Step 4 – Merge
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates = listings.merge(mortgage_monthly, on='year_month', how='left')

# Step 5 – Validate the merge
# Check for any unmatched rows (rate should not be null)
print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(listings_with_rates['rate_30yr_fixed'].isnull().sum())
# Preview
print(
 sold_with_rates[
 ['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
 ].head()
)

#     CloseDate year_month  ClosePrice  rate_30yr_fixed
# 0         NaN        NaT         NaN              NaN
# 1         NaN        NaT         NaN              NaN
# 2  2026-05-11    2026-05    320000.0           6.4425
# 3         NaN        NaT         NaN              NaN
# 4  2026-04-01    2026-04      3599.0           6.3320