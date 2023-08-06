from pfit.NTGSTemperatureMetadataHandler import NTGSTemperatureMetadataHandler
from pfit.TabularMetadataHandler import TabularMetadataHandler
from pfit.NTGS_to_NetCDF import NtgsThermalDataset
from pfit.CSVColMelter import CSVMelter

# ncfile = r"C:\Users\Nick\Downloads\201709\TST_HE_2_DC.nc"
# melted_csv = r"C:\Users\Nick\Downloads\201709\melted_TST HE 2 DC.csv"

# nc_from_melted(ncfile, melted_csv, None, metadata_id=None)

# M = NTGSTemperatureMetadataHandler(r"C:\Users\Nick\Carleton University\NSERC PermafrostNet - Operations - Operations\900_Data\904_DataSciencePlatform\90405_ntgsData\NTGSrefno_2017-009_2020August18\2017-009_2017-009\2017-009_Metadata\NWT_Open_Report_2017-009_Metadata.xlsx")

# M.write_attributes(ncfile, "TST HE2 DC")
# M.write_variables(ncfile, "TST HE2 DC")


##

metadata = r"C:/Users/Nick/Downloads/ESJ_Metadata.xlsx"
data_file = r"C:\Users\Nick\Desktop\clean\pink_west_merged_clean1.csv"
D = NtgsThermalDataset(data_file=data_file, metadata=None, timezoneOffset=-8)


q = D.to_netcdf("C:/Users/Nick/ESJ2.nc")
T = TabularMetadataHandler.from_xlsx(metadata, 0, "index")
T.write_attributes(q, "", loc_lookup="site_name")


# from pathlib import Path
# folder = Path(r"C:\Users\Nick\Desktop\clean")
# for file in folder.glob("*.csv"):
#     print(file)
#     D = NtgsThermalDataset(data_file=data_file, metadata=None, timezoneOffset=-8)