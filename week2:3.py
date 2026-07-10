import pandas as pd

sold = pd.read_csv("CRMLSSoldCombined.csv", low_memory=False)
listings = pd.read_csv("CRMLSListingCombined.csv", low_memory=False)

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

soldFiltered.to_csv("CRMLSSoldFiltered.csv", index=False)
listingsFiltered.to_csv("CRMLSListingFiltered.csv", index=False)

#Sold rows/cols: 455658, 80
#Listing rows/cols: 504466, 82

#Unique Sold Property Types: Residential !!!!!
#Unique Listings Property Types: Residential  !!!!!!

# Flagged cols: ['WaterfrontYN', 'BasementYN', 'FireplacesTotal',
#        'AboveGradeFinishedArea', 'TaxAnnualAmount', 'BuilderName', 'TaxYear',
#        'BuildingAreaTotal', 'ElementarySchoolDistrict',
#        'CoBuyerAgentFirstName', 'BelowGradeFinishedArea', 'BusinessType',
#        'CoveredSpaces', 'LotSizeDimensions', 'MiddleOrJuniorSchoolDistrict']

# ClosePrice: 
# count    455656.0
# mean     1124047
# std      1264029
# min      525
# 25%      571745.80
# 50%      815000
# 75%      1280000
# max      110000000

# LivingArea: 
# count    455388
# mean     1900.14
# std      25240.96
# min      0.00
# 25%      1248
# 50%      1643
# 75%      2220
# max      1702132

# DaysOnMarket: 
# count    455658.000000
# mean         37.629472
# std          53.789324
# min        -288
# 25%           8
# 50%          19
# 75%          49
# max       12430

#mortgage rates from FRED
fred_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage_rates = pd.read_csv(fred_url, parse_dates=["observation_date"])
mortgage_rates.columns = ["date", "rate_30yr_fixed"]

#monthly avg rates
mortgage_rates["year_month"] = mortgage_rates["date"].dt.to_period("M")
monthly_rates = (mortgage_rates.groupby("year_month")["rate_30yr_fixed"].mean().reset_index())

#load files
sold = pd.read_csv("CRMLSSoldCombined.csv", low_memory=False)
listings = pd.read_csv("CRMLSListingCombined.csv", low_memory=False)

# year/month keys
sold["year_month"] = pd.to_datetime(sold["CloseDate"], format="mixed").dt.to_period("M")
listings["year_month"] = pd.to_datetime(listings["ListingContractDate"],format="mixed").dt.to_period("M")

#merge mortgage rates
sold_enriched = sold.merge(monthly_rates, on="year_month", how="left")
listings_enriched = listings.merge(monthly_rates, on="year_month", how="left")

#validation
print("Missing sold mortgage rates:",sold_enriched["rate_30yr_fixed"].isna().sum())
print("Missing listing mortgage rates:", listings_enriched["rate_30yr_fixed"].isna().sum())
assert sold_enriched["rate_30yr_fixed"].isna().sum() == 0
assert listings_enriched["rate_30yr_fixed"].isna().sum() == 0
print("Validation passed!")

sold_enriched.to_csv("CRMLSSold_MortgageRates.csv", index=False)
listings_enriched.to_csv("CRMLSListing_MortgageRates.csv", index=False)

#Missing sold mortgage rates: 0
#Missing listing mortgage rates: 0