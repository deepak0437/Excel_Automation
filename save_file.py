import csv
def save_file_after_editing():
    x = 0
    head1 = ["Handle",	"Title",	"Body (HTML)",	"Vendor" ,"Product Category", "Type", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description", "Google Shopping / Google Product Category", "Google Shopping / Gender", "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / Condition", "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", "Included / India", "Included / International", "Price / International", "Compare At Price / International", "Status"]
    with open('save_final_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(head1)
        writer.writerow([])

        
read_csv_file = '/Users/deepak.kumar/Desktop/Rohit_project_Automation/web_product_search.csv'  #put always search csv file
write_csv_file = '/Users/deepak.kumar/Desktop/Rohit_project_Automation/products_export_write.csv'  #put always write csv file
live_csv_file = '/Users/deepak.kumar/Desktop/Rohit_project_Automation/Dark Store SKU.csv'  #put always write csv file
print(save_file_after_editing(read_csv_file, write_csv_file,live_csv_file))
