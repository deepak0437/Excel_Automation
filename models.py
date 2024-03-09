import pandas as pd

read_excel_file = "/Users/deepak.kumar/Downloads/TGY New dealer for Shopify (1).xlsx"
write_csv_file = "/Users/deepak.kumar/Downloads/deale3r.csv"

dataframe = pd.read_excel(read_excel_file).values.tolist()

num = 1
for data in dataframe:
    handle_column = data[5]
    title_column = data[5]
    html_text = f"""<p>Address: {data[6]} - {str(data[3]).replace(",","")}</p>
        <div class=""contact-details"">
        <p><span>Email: </span><span> <a href="mailto:{data[10]}" data-mce-fragment="1" data-mce-href="mailto:{data[10]}">{data[10]}</a></span></p>
        <p><span>Phone: </span><span></span>{str(data[9]).replace(",","")}</p>
        </div>
        <div class=""contact-details"">
        <p><span>Person In-charge : </span><span></span>Sujit Kumar</p>
        <p><span>Phone1: {str(data[11]).replace(",","")}</span></p>
        <p>Is Available: {str(data[14]).upper()}</p>
        </div>"""
    
    csv_frame = pd.read_csv(write_csv_file)
    csv_frame.loc[num, 'Handle'] = handle_column
    csv_frame.loc[num,'Title']=title_column
    csv_frame.loc[num,'Body (HTML)']=html_text
    csv_frame.to_csv(write_csv_file, index=False)  # append=True doesn't work with to_csv method</s
    num += 1
    print("completed......")
    

# print(dataframe)
