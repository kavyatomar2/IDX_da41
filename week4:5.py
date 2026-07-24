import pandas as pd

#load files
sold = pd.read_csv("w23_CRMLSSoldFiltered.csv")
listing = pd.read_csv("w23_CRMLSListingFiltered.csv")

#before row counts
print("\nBEFORE")
print("Sold:", sold.shape)
print("Listing:", listing.shape)

#datetime format conversion
dateCols = ['CloseDate', 'PurchaseContractDate', 'ListingContractDate', 'ContractStatusChangeDate']
for col in dateCols:
    if col in sold.columns:
        sold[col] = pd.to_datetime(sold[col])
    if col in listing.columns:
        listing[col] = pd.to_datetime(listing[col])

#date consistency check
    #sold
sold["listing_after_close_flag"] = (sold["ListingContractDate"] > sold["CloseDate"])
sold["purchase_after_close_flag"] = (sold["PurchaseContractDate"] > sold["CloseDate"])
sold["negative_timeline_flag"] = (sold["PurchaseContractDate"] < sold["ListingContractDate"])

print("\nSOLD DATA CONSISTENCY CHECK")
print("Listing after Close:", sold["listing_after_close_flag"].sum())
print("Purchase after Close:", sold["purchase_after_close_flag"].sum())
print("Negative Timeline:", sold["negative_timeline_flag"].sum())

    #listing
listing["listing_after_close_flag"] = (listing["ListingContractDate"] > listing["CloseDate"])
listing["purchase_after_close_flag"] = (listing["PurchaseContractDate"] > listing["CloseDate"])
listing["negative_timeline_flag"] = (listing["PurchaseContractDate"] < listing["ListingContractDate"])

print("\nLISTING DATA CONSISTENCY CHECK")
print("Listing after Close:", listing["listing_after_close_flag"].sum())
print("Purchase after Close:", listing["purchase_after_close_flag"].sum())
print("Negative Timeline:", listing["negative_timeline_flag"].sum())

#extra col removal: no redundant cols found

#geographic checks (lat/long)
    #sold
print("\nSOLD GEOGRAPHIC CHECKS")
        #missing
sold["missing_coordinates_flag"] = (sold["Latitude"].isna()|sold["Longitude"].isna())
print("Missing coordinates:", sold["missing_coordinates_flag"].sum())
        #zero
sold["zero_coordinates_flag"] = ((sold["Latitude"] == 0)|(sold["Longitude"] == 0))
print("Zero coordinates:", sold["zero_coordinates_flag"].sum())
        #positive longitude
sold["positive_longitude_flag"] = (sold["Longitude"] > 0)
print("Positive longitude:", sold["positive_longitude_flag"].sum())
        #implausible coordinates (Latitude: 32–42 & Longitude: -125 to -114)
sold["implausible_coordinates_flag"] = ((sold["Latitude"] < 32)|(sold["Latitude"] > 42)|(sold["Longitude"] < -125)|(sold["Longitude"] > -114))
print("Implausible coordinates:", sold["implausible_coordinates_flag"].sum())

    #listing
print("\nLISTING GEOGRAPHIC CHECKS")
        #missing
listing["missing_coordinates_flag"] = (listing["Latitude"].isna()|listing["Longitude"].isna())
print("Missing coordinates:", listing["missing_coordinates_flag"].sum())
        #zero
listing["zero_coordinates_flag"] = ((listing["Latitude"] == 0)|(listing["Longitude"] == 0))
print("Zero coordinates:", listing["zero_coordinates_flag"].sum())
        #pos longitude
listing["positive_longitude_flag"] = (listing["Longitude"] > 0)
print("Positive longitude:", listing["positive_longitude_flag"].sum())
        #implausible coordinates (Latitude: 32–42 & Longitude: -125 to -114)
listing["implausible_coordinates_flag"] = ((listing["Latitude"] < 32)|(listing["Latitude"] > 42)|(listing["Longitude"] < -125)|(listing["Longitude"] > -114))
print("Implausible coordinates:", listing["implausible_coordinates_flag"].sum())

#ensure numeric cols have numeric inputs 
numeric_columns = ['ClosePrice', 'ListPrice', 'OriginalListPrice' , 'LivingArea', 'LotSizeAcres', 'BedroomsTotal', 'BathroomsTotalInteger', 'DaysOnMarket', 'YearBuilt']
for col in numeric_columns:
    if col in sold.columns:
        sold[col] = pd.to_numeric(sold[col])
    if col in listing.columns:
        listing[col] = pd.to_numeric(listing[col])

#replace missing with NA
sold = sold.replace('', pd.NA)
listing = listing.replace('', pd.NA)

#data type conformation
print("\nSOLD DATA TYPES")
print(sold[["CloseDate", "PurchaseContractDate", "ListingContractDate", "ClosePrice", "LivingArea", "DaysOnMarket"]].dtypes)
print("\nLISTING DATA TYPES")
print(listing[["CloseDate", "PurchaseContractDate", "ListingContractDate", "ClosePrice", "LivingArea", "DaysOnMarket"]].dtypes)

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

        #sold
print('\nSOLD INVALID VALUE SUMMARY')
print('Invalid Close Prices:', sold['invalid_closeprice_flag'].sum())
print('Invalid Living Areas:', sold['invalid_livingarea_flag'].sum())
print('Negative Days on Market:', sold['invalid_daysonmarket_flag'].sum())
print('Negative Bedrooms:', sold['invalid_bedrooms_flag'].sum())
print('Negative Bathrooms:', sold['invalid_bathrooms_flag'].sum())
        #listing
print('\nLISTING INVALID VALUE SUMMARY')
print('Invalid Close Prices:', listing['invalid_closeprice_flag'].sum())
print('Invalid Living Areas:', listing['invalid_livingarea_flag'].sum())
print('Negative Days on Market:', listing['invalid_daysonmarket_flag'].sum())
print('Negative Bedrooms:', listing['invalid_bedrooms_flag'].sum())
print('Negative Bathrooms:', listing['invalid_bathrooms_flag'].sum())

#after row counts
print("\nAFTER")
print("Sold:", sold.shape)
print("Listing:", listing.shape)

#csv
sold.to_csv('w45_CRMLSSoldCleaned.csv', index=False)
listing.to_csv('w45_CRMLSListingCleaned.csv', index=False)

# BEFORE
# Sold: (504466, 81)
# Listing: (455658, 79)

# SOLD DATA CONSISTENCY CHECK
# Listing after Close: 82
# Purchase after Close: 94
# Negative Timeline: 312

# LISTING DATA CONSISTENCY CHECK
# Listing after Close: 81
# Purchase after Close: 92
# Negative Timeline: 314

# SOLD GEOGRAPHIC CHECKS
# Missing coordinates: 49467
# Zero coordinates: 62
# Positive longitude: 69
# Implausible coordinates: 207

# LISTING GEOGRAPHIC CHECKS
# Missing coordinates: 53637
# Zero coordinates: 44
# Positive longitude: 34
# Implausible coordinates: 102

# SOLD DATA TYPES
# CloseDate               datetime64[us]
# PurchaseContractDate    datetime64[us]
# ListingContractDate     datetime64[us]
# ClosePrice                     float64
# LivingArea                     float64
# DaysOnMarket                     int64
# dtype: object

# LISTING DATA TYPES
# CloseDate               datetime64[us]
# PurchaseContractDate    datetime64[us]
# ListingContractDate     datetime64[us]
# ClosePrice                     float64
# LivingArea                     float64
# DaysOnMarket                     int64
# dtype: object

# SOLD INVALID VALUE SUMMARY
# Invalid Close Prices: 0
# Invalid Living Areas: 261
# Negative Days on Market: 43
# Negative Bedrooms: 0
# Negative Bathrooms: 0

# LISTING INVALID VALUE SUMMARY
# Invalid Close Prices: 0
# Invalid Living Areas: 161
# Negative Days on Market: 48
# Negative Bedrooms: 0
# Negative Bathrooms: 0

# AFTER
# Sold: (504466, 93)
# Listing: (455658, 91)
