import xlsxwriter

xl_row1=['mod_dt_time_datetime_type','b','c''datetime']
xl_row2=[1,2,3,4]
xl_row0=['x','mod_dt_time_str','mod_dt_time_structure']

workbook = xlsxwriter.Workbook(r'C:\Excel_to_be_written.xlsx')

worksheet = workbook.add_worksheet()
worksheet.write_row(row=0,col=1,data=xl_row0)
worksheet.write_row(row=5,col=0,data=xl_row2)

try:
    workbook.close()
except IOError:
    print("Couldn't open Excel sheet.")
