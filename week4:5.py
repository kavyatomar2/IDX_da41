import pandas as pd

#load files
sold = pd.read_csv("w23_CRMLSSoldFiltered.csv")
listing = pd.read_csv("w23_CRMLSListingFiltered.csv")

print(f'BEFORE: num of sold rows, cols{sold.shape}, num of list rows, cols {listing.shape}')

#datetime format conversion
dateCols = ['CloseDate', 'PurchaseContractDate', 'ListingContractDate', 'ContractStatusChangeDate']
for col in dateCols:
    if col in sold.columns:
        sold[col] = pd.to_datetime(sold[col])
    if col in listing.columns:
        listing[col] = pd.to_datetime(listing[col])
    
#extra col removal -idk what cols to remove, how to do this part !!!!

#replace missing with NA
sold.replace('', pd.NA)
listing.replace('', pd.NA)

#ensure numeric cols ahve numeric inputs 
numeric_columns = ['ClosePrice', 'ListPrice', 'OriginalListPrice' , 'LivingArea', 'LotSizeAcres', 'BedroomsTotal', 'BathroomsTotalInteger', 'DaysOnMarket', 'YearBuilt']
for col in numeric_columns:
    if col in sold.columns:
        sold[col] = pd.to_numeric(sold[col])

    if col in listing.columns:
        listing[col] = pd.to_numeric(listing[col])

#invalid numeric data
    #sold
sold['invalid_closeprice_flag'] = sold['ClosePrice'] <= 0
sold['invalid_livingarea_flag'] = sold['LivingArea'] <= 0
sold['invalid_daysonmarket_flag'] = sold['DaysOnMarket'] < 0
sold['invalid_bedrooms_flag'] = sold['BedroomsTotal'] < 0
sold['invalid_bathrooms_flag'] = sold['BathroomsTotalInteger'] < 0
    #listing
listing['invalid_closeprice_flag'] = listing['ClosePrice'] <= 0
listing['invalid_livingarea_flag'] = listing['LivingArea'] <= 0
listing['invalid_daysonmarket_flag'] = listing['DaysOnMarket'] < 0
listing['invalid_bedrooms_flag'] = listing['BedroomsTotal'] < 0
listing['invalid_bathrooms_flag'] = listing['BathroomsTotalInteger'] < 0

    #print summary
        #sold
print('SOLD invalid value summary')
print('Invalid Close Prices:', sold['invalid_closeprice_flag'].sum())
print('Invalid Living Areas:', sold['invalid_livingarea_flag'].sum())
print('Negative Days on Market:', sold['invalid_daysonmarket_flag'].sum())
print('Negative Bedrooms:', sold['invalid_bedrooms_flag'].sum())
print('Negative Bathrooms:', sold['invalid_bathrooms_flag'].sum())
        #listing
print('LISTING invalid value summary')
print('Invalid Close Prices:', listing['invalid_closeprice_flag'].sum())
print('Invalid Living Areas:', listing['invalid_livingarea_flag'].sum())
print('Negative Days on Market:', listing['invalid_daysonmarket_flag'].sum())
print('Negative Bedrooms:', listing['invalid_bedrooms_flag'].sum())
print('Negative Bathrooms:', listing['invalid_bathrooms_flag'].sum())