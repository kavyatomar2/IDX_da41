import pandas as pd

def load_csv(filename):
    return pd.read_csv(f"../{filename}", encoding="cp1252")

#listing
    #2024
list_jan24 = load_csv('CRMLSListing202401.csv')
list_feb24 = load_csv('CRMLSListing202402.csv')
list_mar24 = load_csv('CRMLSListing202403.csv')
list_apr24 = load_csv('CRMLSListing202404.csv')
list_may24 = load_csv('CRMLSListing202405.csv')
list_june24 = load_csv('CRMLSListing202406.csv')
list_july24 = load_csv('CRMLSListing202407.csv')
list_aug24 = load_csv('CRMLSListing202408.csv')
list_sept24 = load_csv('CRMLSListing202409.csv')
list_oct24 = load_csv('CRMLSListing202410.csv')
list_nov24 = load_csv('CRMLSListing202411.csv')
list_dec24 = load_csv('CRMLSListing202412.csv')
    #2025
list_jan25 = load_csv('CRMLSListing202501.csv')
list_feb25 = load_csv('CRMLSListing202502.csv')
list_mar25 = load_csv('CRMLSListing202503.csv')
list_apr25 = load_csv('CRMLSListing202504.csv')
list_may25 = load_csv('CRMLSListing202505.csv')
list_june25 = load_csv('CRMLSListing202506.csv')
list_july25 = load_csv('CRMLSListing202507.csv')
list_aug25 = load_csv('CRMLSListing202508.csv')
list_sept25 = load_csv('CRMLSListing202509.csv')
list_oct25 = load_csv('CRMLSListing202510.csv')
list_nov25 = load_csv('CRMLSListing202511.csv')
list_dec25 = load_csv('CRMLSListing202512.csv')
    #2026
list_jan26 = load_csv('CRMLSListing202601.csv')
list_feb26 = load_csv('CRMLSListing202602.csv')
list_mar26 = load_csv('CRMLSListing202603.csv')
list_apr26 = load_csv('CRMLSListing202604.csv')
list_may26 = load_csv('CRMLSListing202605.csv') 
list_june26 = load_csv('CRMLSListing202606.csv') 

allListing = pd.concat([list_jan24, list_feb24, list_mar24, list_apr24, list_may24, list_june24, 
                        list_july24, list_aug24, list_sept24, list_oct24, list_nov24, list_dec24, 
                        list_jan25, list_feb25, list_mar25, list_apr25, list_may25, list_june25, 
                        list_july25, list_aug25, list_sept25, list_oct25, list_nov25, list_dec25, 
                        list_jan26, list_feb26, list_mar26, list_apr26, list_may26, list_june26]) #ignore_index=True)
print("Num of Listing Rows before 'Residential' filter:", len(allListing))

allListing.to_csv('w1_CRMLSListingCombined_Unfiltered.csv', index=False)

filteredListing = allListing[allListing['PropertyType'] == 'Residential']
print("Num of Listing Rows after 'Residential' filter:", len(filteredListing))

filteredListing.to_csv('w1_CRMLSListingCombined.csv') #index=False

#sold
    #2024
sold_jan24 = load_csv('CRMLSSold202401.csv')
sold_feb24 = load_csv('CRMLSSold202402.csv')
sold_mar24 = load_csv('CRMLSSold202403.csv')
sold_apr24 = load_csv('CRMLSSold202404.csv')
sold_may24 = load_csv('CRMLSSold202405.csv')
sold_june24 = load_csv('CRMLSSold202406.csv')
sold_july24 = load_csv('CRMLSSold202407.csv')
sold_aug24 = load_csv('CRMLSSold202408.csv')
sold_sept24 = load_csv('CRMLSSold202409.csv')
sold_oct24 = load_csv('CRMLSSold202410.csv')
sold_nov24 = load_csv('CRMLSSold202411.csv')
sold_dec24 = load_csv('CRMLSSold202412.csv')
    #2025
sold_jan25 = load_csv('CRMLSSold202501.csv')
sold_feb25 = load_csv('CRMLSSold202502.csv')
sold_mar25 = load_csv('CRMLSSold202503.csv')
sold_apr25 = load_csv('CRMLSSold202504.csv')
sold_may25 = load_csv('CRMLSSold202505.csv')
sold_june25 = load_csv('CRMLSSold202506.csv')
sold_july25 = load_csv('CRMLSSold202507.csv')
sold_aug25 = load_csv('CRMLSSold202508.csv')
sold_sept25 = load_csv('CRMLSSold202509.csv')
sold_oct25 = load_csv('CRMLSSold202510.csv')
sold_nov25 = load_csv('CRMLSSold202511.csv')
sold_dec25 = load_csv('CRMLSSold202512.csv')
    #2026
sold_jan26 = load_csv('CRMLSSold202601.csv')
sold_feb26 = load_csv('CRMLSSold202602.csv')
sold_mar26 = load_csv('CRMLSSold202603.csv')
sold_apr26 = load_csv('CRMLSSold202604.csv')
sold_may26 = load_csv('CRMLSSold202605.csv')
sold_june26 = load_csv('CRMLSSold202606.csv')

allSold = pd.concat([sold_jan24, sold_feb24, sold_mar24, sold_apr24, sold_may24, sold_june24, 
                    sold_july24, sold_aug24, sold_sept24, sold_oct24, sold_nov24, sold_dec24, 
                    sold_jan25, sold_feb25, sold_mar25, sold_apr25, sold_may25, sold_june25, 
                    sold_july25, sold_aug25, sold_sept25, sold_oct25, sold_nov25, sold_dec25, 
                    sold_jan26, sold_feb26, sold_mar26, sold_apr26, sold_may26, sold_june26])
print("Num of Sold Row before 'Residential' filter:", len(allSold)) #ignore_index=True)

allSold.to_csv('w1_CRMLSSoldCombined_Unfiltered.csv', index=False)

filteredSold = allSold[allSold['PropertyType'] == 'Residential']
print("Num of Sold Rows after 'Residential' filter:", len(filteredSold))

filteredSold.to_csv('w1_CRMLSSoldCombined.csv') #index=False

#Num of Listing Rows before 'Residential' filter: 766706
#Num of Listing Rows after 'Residential' filter: 504466

#Num of Sold Row before 'Residential' filter: 680885
#Num of Sold Rows after 'Residential' filter: 455658
