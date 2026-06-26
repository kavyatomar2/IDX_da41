import pandas as pd

#listing
    #2024
list_mar24 = pd.read_csv('../CRMLSListing202403.csv')
list_apr24 = pd.read_csv('../CRMLSListing202404.csv')
list_may24 = pd.read_csv('../CRMLSListing202405.csv')
list_june24 = pd.read_csv('../CRMLSListing202406.csv')
list_july24 = pd.read_csv('../CRMLSListing202407.csv')
list_aug24 = pd.read_csv('../CRMLSListing202408.csv')
list_sept24 = pd.read_csv('../CRMLSListing202409.csv')
list_oct24 = pd.read_csv('../CRMLSListing202410.csv')
list_nov24 = pd.read_csv('../CRMLSListing202411.csv')
list_dec24 = pd.read_csv('../CRMLSListing202412.csv')
    #2025
list_jan25 = pd.read_csv('../CRMLSListing202501.csv')
list_feb25 = pd.read_csv('../CRMLSListing202502.csv')
list_mar25 = pd.read_csv('../CRMLSListing202503.csv')
list_apr25 = pd.read_csv('../CRMLSListing202504.csv')
list_may25 = pd.read_csv('../CRMLSListing202505.csv')
list_june25 = pd.read_csv('../CRMLSListing202506.csv')
list_july25 = pd.read_csv('../CRMLSListing202507.csv')
list_aug25 = pd.read_csv('../CRMLSListing202508.csv')
list_sept25 = pd.read_csv('../CRMLSListing202509.csv')
list_oct25 = pd.read_csv('../CRMLSListing202510.csv')
list_nov25 = pd.read_csv('../CRMLSListing202511.csv')
list_dec25 = pd.read_csv('../CRMLSListing202512.csv')
    #2026
list_jan26 = pd.read_csv('../CRMLSListing202601.csv')
list_feb26 = pd.read_csv('../CRMLSListing202602.csv')
list_mar26 = pd.read_csv('../CRMLSListing202603.csv')
list_apr26 = pd.read_csv('../CRMLSListing202604.csv')
list_may26 = pd.read_csv('../CRMLSListing202605.csv') 

allListing = pd.concat([list_mar24, list_apr24, list_may24, list_june24, 
                        list_july24, list_aug24, list_sept24, list_oct24, list_nov24, list_dec24, 
                        list_jan25, list_feb25, list_mar25, list_apr25, list_may25, list_june25, 
                        list_july25, list_aug25, list_sept25, list_oct25, list_nov25, list_dec25, 
                        list_jan26, list_feb26, list_mar26, list_apr26, list_may26]) #ignore_index=True)
print("Num of Listing Rows before 'Residential' filter:", len(allListing))

filteredListing = allListing[allListing['PropertyType'] == 'Residential']
print("Num of Listing Rows after 'Residential' filter:", len(filteredListing))

filteredListing.to_csv('CRMLSListingCombined.csv') #index=False

#sold
    #2024
sold_mar24 = pd.read_csv('../CRMLSSold202403.csv')
sold_apr24 = pd.read_csv('../CRMLSSold202404.csv')
sold_may24 = pd.read_csv('../CRMLSSold202405_filled.csv')
sold_june24 = pd.read_csv('../CRMLSSold202406_filled.csv')
sold_july24 = pd.read_csv('../CRMLSSold202407_filled.csv')
sold_aug24 = pd.read_csv('../CRMLSSold202408.csv')
sold_sept24 = pd.read_csv('../CRMLSSold202409.csv')
sold_oct24 = pd.read_csv('../CRMLSSold202410.csv')
sold_nov24 = pd.read_csv('../CRMLSSold202411.csv')
sold_dec24 = pd.read_csv('../CRMLSSold202412.csv')
    #2025
sold_jan25 = pd.read_csv('../CRMLSSold202501_filled.csv')
sold_feb25 = pd.read_csv('../CRMLSSold202502.csv')
sold_mar25 = pd.read_csv('../CRMLSSold202503.csv')
sold_apr25 = pd.read_csv('../CRMLSSold202504.csv')
sold_may25 = pd.read_csv('../CRMLSSold202505.csv')
sold_june25 = pd.read_csv('../CRMLSSold202506.csv')
sold_july25 = pd.read_csv('../CRMLSSold202507.csv')
sold_aug25 = pd.read_csv('../CRMLSSold202508.csv')
sold_sept25 = pd.read_csv('../CRMLSSold202509.csv')
sold_oct25 = pd.read_csv('../CRMLSSold202510.csv')
sold_nov25 = pd.read_csv('../CRMLSSold202511.csv')
sold_dec25 = pd.read_csv('../CRMLSSold202512.csv')
    #2026
sold_jan26 = pd.read_csv('../CRMLSSold202601.csv')
sold_feb26 = pd.read_csv('../CRMLSSold202602.csv')
sold_mar26 = pd.read_csv('../CRMLSSold202603.csv')
sold_apr26 = pd.read_csv('../CRMLSSold202604.csv')
sold_may26 = pd.read_csv('../CRMLSSold202605.csv')

allSold = pd.concat([sold_mar24, sold_apr24, sold_may24, sold_june24, 
                    sold_july24, sold_aug24, sold_sept24, sold_oct24, sold_nov24, sold_dec24, 
                    sold_jan25, sold_feb25, sold_mar25, sold_apr25, sold_may25, sold_june25, 
                    sold_july25, sold_aug25, sold_sept25, sold_oct25, sold_nov25, sold_dec25, 
                    sold_jan26, sold_feb26, sold_mar26, sold_apr26, sold_may26])
print("Num of Sold Row before 'Residential' filter:", len(allSold)) #ignore_index=True)

filteredSold = allSold[allSold['PropertyType'] == 'Residential']
print("Num of Sold Rows after 'Residential' filter:", len(filteredSold))

filteredSold.to_csv('CRMLSSoldCombined.csv') #index=False

