import pandas as pd
from openpyxl import load_workbook 
from xlrd import open_workbook
import os

# def translateToXlsx():
#     path= os.listdir()
#     print(path)
#     for name in path:
#         if name.endswith('.xls'):
#             n= name.replace('.xls','')
#             df= pd.read_excel(name,sheet_name='12月',skiprows=1)
#             print(df.columns)
#             column_names= ['生产日期', '机台号', '产品名称', '生产批号', '厚度um', '宽度mm', 'OK/NG',
#                             '离型力G', '投入面积㎡', '投入重量KG', '产出面积㎡', '产出重量KG', '报废面积㎡',
#                             '报废重量KG', '报废率%', '膜材换算率', '操作失误', '搬运失误', '调机', '送客户', '边料',
#                             '管底', '少膜', '备注', '余料面积㎡', '余数重量Kg', '备注1', '备注2', '备注3']

#             # print(len(column_names))
#             df.columns= column_names
#             df.to_excel(f'{n}.xlsx',index=False)

            
df= pd.read_excel('12月.xlsx' )
# newdf= df.loc[~df['生产日期'].isna()]
df.生产日期= df.生产日期.dt.date
# newdf.投入重量KG= newdf.投入重量KG.round(2)
# newdf.产出重量KG= newdf.产出重量KG.round(2)
# newdf.报废重量KG= newdf.报废重量KG.round(2)
# newdf['报废率%']= newdf['报废率%'].round(2)
# newdf['余数重量Kg']= newdf['余数重量Kg'].round(2)
# newdf.to_excel('12月.xlsx',index=False)
columns_names= df.columns()
for i,row in df.iterrows():
    for i,v in row.items():
        print(v)
    break 

# column_names= ['生产日期', '部门', '机台号', '产品名称', '生产批号', '厚度um', '宽度mm', 'OK/NG',
#        '离型力G', '投入面积㎡', '投入重量KG', '产出面积㎡', '产出重量KG', '报废面积㎡',
#        '报废重量KG', '报废率%', '膜材换算率', '操作失误', '搬运失误', '调机', '送客户', '边料',
#        '管底', '少膜', '备注', '余料面积㎡', '余数重量Kg', '备注1', '备注2',
#        '备注3']

