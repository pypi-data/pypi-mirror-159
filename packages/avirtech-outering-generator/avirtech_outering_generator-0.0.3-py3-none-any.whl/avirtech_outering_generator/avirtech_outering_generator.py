from numpy import outer
import arcpy
import os
import Tkinter as tk
from tkinter import messagebox
import tkFileDialog as filedialog
from tkFileDialog import askopenfilename
from simpledbf import Dbf5
import pandas as pd
from os.path import exists
import random, shutil,configparser

class initiation_process:
    @staticmethod
    def initiate_process():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("","Please input your crown plot")
        global folder_plot
        folder_plot = filedialog.askdirectory()
        messagebox.showinfo("","Please input your area location")
        global area_location
        area_location = filedialog.askdirectory()
        messagebox.showinfo("","Please input folder to store result")
        global gdb_location
        gdb_location = filedialog.askdirectory()
        root.destroy

class starting_first:
    @staticmethod
    def starting_process():
        global mxd
        mxd = arcpy.mapping.MapDocument("Current")
        mxd.author = "Dwieka"
        arcpy.env.workspace = "CURRENT"
        global df
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        global plotting_data
        plotting_data = []
        global plotting_data_tif
        plotting_data_tif = []
        global plotting_area
        plotting_area = []

        substring_plot = ".shp"
        substring_plot_2 = ".xml"
        substring_plot_3 = "DESKTOP"

        for file in os.listdir(folder_plot):
            if file.find(substring_plot) != -1 and file.find(substring_plot_2) == -1 and file.find(substring_plot_3) == -1:
                base = os.path.splitext(file)[0]

                location_plot = os.path.join(folder_plot,file)
                new_layer = arcpy.mapping.Layer(location_plot)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")

                plotting_data.append(base)
            elif file.endswith('.tif') or file.endswith('.ecw'):
                data_process = os.path.join(folder_plot,file)
                data_show = file
                arcpy.MakeRasterLayer_management(data_process,data_show,"","")
                plotting_data_tif.append(file)

        for area in os.listdir(area_location):
            if area.find(substring_plot) != -1 and area.find(substring_plot_2) == -1 and area.find(substring_plot_3) == -1:
                base = os.path.splitext(area)[0]
                area_plot = os.path.join(area_location,area)
                new_layer = arcpy.mapping.Layer(area_plot)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")
                plotting_area.append(base)

class create_folder:
    def __init__(self,main_location):
        self.main_location = main_location
    
    def create_folder(self):
        outputgdb = "crowndetection.gdb"
        folder_making = ["clip_ileaf","iso_result","leaf","point_process","outer_ring"]

        for folder in folder_making:
            location = os.path.join(self.main_location,folder)
            os.mkdir(location)

        global location_masking
        location_masking = os.path.join(self.main_location,folder_making[0])
        global iso_location
        iso_location = os.path.join(self.main_location,folder_making[1])
        global leaf_location
        leaf_location = os.path.join(self.main_location,folder_making[2])
        global point_process
        point_process = os.path.join(self.main_location,folder_making[3])
        global buffer_last_location
        buffer_last_location = os.path.join(self.main_location,folder_making[4])
        
        arcpy.CreateFileGDB_management(self.main_location,outputgdb)

        global loc_gdb
        loc_gdb = os.path.join(self.main_location,outputgdb)

class process_first:
    def __init__(self,loc_gdb,name):
        self.loc_gdb = loc_gdb
        self.name = name
        select_data = arcpy.SelectLayerByAttribute_management(plotting_area[0], "NEW_SELECTION", "\"ket\" = '{}'".format(str(areatype)))

        arcpy.SelectLayerByLocation_management(plotting_data[0], "INTERSECT", plotting_area[0], "", "NEW_SELECTION", "NOT_INVERT")

        arcpy.CopyFeatures_management(plotting_data[0],os.path.join(point_process,"{}_point".format(areatype)),"0","0","0")

        arcpy.gp.ExtractByMask_sa(plotting_data_tif[0],plotting_area[0],os.path.join(self.loc_gdb,self.name))

        arcpy.RasterToOtherFormat_conversion(os.path.join(self.loc_gdb,self.name),location_masking,"TIFF")

        arcpy.MakeRasterLayer_management(os.path.join(location_masking,"{}.tif".format(self.name)),"{}_exp".format(self.name),"","")

class processing_raster_medium_grass:   
    def __init__(self,data,main_location,data_process):
        self.data = data
        self.main_location = main_location
        self.data_process = data_process

        arcpy.CopyRaster_management(self.data, os.path.join(self.main_location,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        b3 = "f_b3"

        location_raster_calc = os.path.join(self.main_location,"vari_f")

        location_raster_calc_2 = os.path.join(self.main_location,"egi_f")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b2,"","","2")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b3,"","","3")

        arcpy.gp.RasterCalculator_sa("(\"{}\" - \"{}\") / (\"{}\" + \"{}\" - \"{}\")".format(b2,b1,b2,b1,b3),location_raster_calc)

        arcpy.gp.RasterCalculator_sa("2 * (\"{}\"-\"{}\"-\"{}\")".format(b2,b1,b3),location_raster_calc_2)

        arcpy.CompositeBands_management("f_b1;f_b2;f_b3;vari_f1.tif", os.path.join(self.main_location,"composite"))

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("composite","4",os.path.join(iso_location,"iso_weed"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_weed",os.path.join(iso_location,"rtpisoweed"))

        selection = arcpy.SelectLayerByAttribute_management("rtpisoweed", "NEW_SELECTION", "gridcode = 1")

        arcpy.CopyFeatures_management(selection,os.path.join(self.main_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != self.data and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != "crown_nwd" and str(layer) != self.data_process and str(layer) != "wd_point" and str(layer) != "fwd_point" and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)
        
        arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")
        try:
            arcpy.AddField_management(self.data_process,"ket","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "buffer", "DOUBLE", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "fidcopy", "SHORT", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")
            
        except Exception:
            pass

        #Processing Shapefile
        arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

        arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

        arcpy.CalculateField_management(self.data_process, "fidcopy", "[FID]", "VB", "")

        arcpy.AddField_management("ileaf","l","TEXT","","","50","","NULLABLE","NON_REQUIRED","")

        arcpy.CalculateField_management("ileaf", "l", "\"1\"", "VB", "")

        arcpy.Buffer_analysis("wd_point", os.path.join(self.main_location,"wd_buff"),"1.5 Meters","FULL","ROUND","NONE","","PLANAR")

        arcpy.Merge_management("wd_buff;ileaf",os.path.join(self.main_location,"wdleaf_merge"))

        try:
            arcpy.AddField_management("wdleaf_merge","diss","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
        except Exception:
            pass

        arcpy.CalculateField_management("wdleaf_merge","diss","\"1\"", "VB", "")
        
        arcpy.Dissolve_management("wdleaf_merge",os.path.join(self.main_location,"dileaf"),"diss","","MULTI_PART","DISSOLVE_LINES")

        arcpy.MultipartToSinglepart_management("dileaf",os.path.join(self.main_location,"expld"))

        arcpy.AggregatePolygons_cartography("expld", os.path.join(loc_gdb,"expld_aggregatepolygons2"), "0.3 Meters", "0 SquareMeters", "0 SquareMeters", "NON_ORTHOGONAL", "", os.path.join(loc_gdb,"expld_aggregatepolygons_tbl"))

        arcpy.AddField_management("expld_aggregatepolygons2","fid_new","SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        arcpy.CalculateField_management("expld_aggregatepolygons2", "fid_new", "autoIncrement()", "PYTHON_9.3", "rec=0 \\ndef autoIncrement(): \\n    global rec \\n    pStart = 1  \\n    pInterval = 1 \\n    if (rec == 0):  \\n        rec = pStart  \\n    else:  \\n        rec += pInterval  \\n    return rec ")

        gsd_int = float(format(arcpy.Describe("wd_exp").children[0].meanCellHeight, ".2f"))

        arcpy.env.extent = plotting_area[0]

        arcpy.gp.EucDistance_sa("wd_point",os.path.join(loc_gdb,"euc_wd"),"","{}".format(gsd_int),"","PLANAR","","")
        arcpy.env.extent

        arcpy.gp.ZonalStatistics_sa("expld_aggregatepolygons2","fid_new","euc_wd",os.path.join(loc_gdb,"zon_wd"),"MAXIMUM","DATA")

        arcpy.gp.ExtractValuesToPoints_sa("wd_point","zon_wd",os.path.join(loc_gdb,"wd_out"),"NONE","VALUE_ONLY")

        arcpy.Buffer_analysis("wd_out",os.path.join(buffer_last_location,"crown_wd"),"RASTERVALU","FULL","ROUND","NONE","","PLANAR")

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != "crown_nwd" and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != plotting_area[0] and str(layer) != plotting_data[0] and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)

class processing_raster_non_grassy:
    def __init__(self, data, main_location,data_process):
        self.data = data
        self.main_location = main_location
        self.data_process = data_process

        arcpy.CopyRaster_management(self.data, os.path.join(self.main_location,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        location_raster_calc = os.path.join(self.main_location,"rasc_f")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b2,"","","2")

        arcpy.gp.RasterCalculator_sa("(\"{}\") / (\"{}\")".format(b2,b1),location_raster_calc)

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("rasc_f","3",os.path.join(iso_location,"iso_f"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_f",os.path.join(iso_location,"rtpiso_f"))

        selection = arcpy.SelectLayerByAttribute_management("rtpiso_f", "NEW_SELECTION", "gridcode = 2 or gridcode = 3")

        arcpy.CopyFeatures_management(selection,os.path.join(self.main_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != self.data and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != "crown_nwd" and str(layer) != "nwd_point" and str(layer) != "wd_point" and str(layer) != "fwd_point" and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)

        arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")
        try:
            arcpy.AddField_management(self.data_process,"ket","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "buffer", "DOUBLE", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "fidcopy", "SHORT", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")
            
        except Exception:
            pass

        #Processing Shapefile
        arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

        arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

        arcpy.CalculateField_management(self.data_process, "fidcopy", "[FID]", "VB", "")

        arcpy.AddField_management("ileaf","l","TEXT","","","50","","NULLABLE","NON_REQUIRED","")

        arcpy.CalculateField_management("ileaf", "l", "\"1\"", "VB", "")

        arcpy.Dissolve_management("ileaf",os.path.join(self.main_location,"dileaf"),"l","","MULTI_PART","DISSOLVE_LINES")

        gsd_int = float(format(arcpy.Describe("nwd_exp").children[0].meanCellHeight, ".2f"))

        arcpy.gp.EucDistance_sa(self.data_process, os.path.join(self.main_location,"euc_nwd"),"8","{}".format(gsd_int),"","PLANAR","","")

        arcpy.gp.ExtractByMask_sa("euc_nwd","dileaf", os.path.join(self.main_location,"eucnwdcl"))

        arcpy.MultipartToSinglepart_management("dileaf",os.path.join(self.main_location,"expld"))

        arcpy.AddField_management("expld","fid_new","SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        arcpy.CalculateField_management("expld", "fid_new", "autoIncrement()", "PYTHON_9.3", "rec=0 \\ndef autoIncrement(): \\n    global rec \\n    pStart = 1  \\n    pInterval = 1 \\n    if (rec == 0):  \\n        rec = pStart  \\n    else:  \\n        rec += pInterval  \\n    return rec ")

        arcpy.gp.ZonalStatistics_sa("expld","fid_new","euc_nwd",os.path.join(self.main_location,"zon_nwd"),"MAXIMUM","DATA")

        arcpy.gp.ExtractValuesToPoints_sa(self.data_process,"zon_nwd",os.path.join(self.main_location,"nwd_buff"),"NONE","VALUE_ONLY")

        arcpy.Buffer_analysis("nwd_buff",os.path.join(self.main_location,"crown_nwd"),"RASTERVALU","FULL","ROUND","NONE","","PLANAR")

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != "crown_nwd" and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != plotting_area[0] and str(layer) != plotting_data[0] and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)

class processing_raster_full_grassy:
    def __init__(self,loc_gdb):
        self.loc_gdb = loc_gdb
    
    def processing_raster_full_grassy(self):
        arcpy.CopyRaster_management("fwd_exp", os.path.join(self.loc_gdb,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        b3 = "f_b3"

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b2,"","","2")

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b3,"","","3")

        arcpy.gp.RasterCalculator_sa("\"{}\" / ((1.4 * (\"{}\" - \"{}\")) * \"{}\")".format(b2,b1,b2,b2), os.path.join(self.loc_gdb,"ind"))

        arcpy.CompositeBands_management("fwd_exp;ind",os.path.join(self.loc_gdb,"composite"))

        arcpy.gp.PrincipalComponents_sa("composite", os.path.join(self.loc_gdb,"pca"), "5", "")

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("pca","10",os.path.join(iso_location,"iso_flwd"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_flwd",os.path.join(iso_location,"rtpisoweed"))

        selection = arcpy.SelectLayerByAttribute_management("rtpisoweed", "NEW_SELECTION", "gridcode = 6 OR gridcode = 10")

        arcpy.CopyFeatures_management(selection,os.path.join(leaf_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != "fwd_exp" and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != "crown_nwd" and str(layer) != "nwd_point" and str(layer) != "wd_point" and str(layer) != "fwd_point" and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)

        arcpy.Buffer_analysis("fwd_point", os.path.join(self.loc_gdb,"fwd_buff"),"1.5 Meters","FULL","ROUND","NONE","","PLANAR")

        arcpy.Merge_management("fwd_buff;ileaf",os.path.join(self.loc_gdb,"fwdleaf_merge"))

        try:
            arcpy.AddField_management("fwdleaf_merge","diss","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")
        except Exception:
            pass

        arcpy.CalculateField_management("fwdleaf_merge","diss","\"1\"", "VB", "")

        arcpy.Dissolve_management("fwdleaf_merge",os.path.join(self.loc_gdb,"fwdileaf"),"diss","","MULTI_PART","DISSOLVE_LINES")

        arcpy.MultipartToSinglepart_management("fwdileaf",os.path.join(self.loc_gdb,"expld"))

        arcpy.AddField_management("expld","fid_new","SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        arcpy.CalculateField_management("expld", "fid_new", "autoIncrement()", "PYTHON_9.3", "rec=0 \\ndef autoIncrement(): \\n    global rec \\n    pStart = 1  \\n    pInterval = 1 \\n    if (rec == 0):  \\n        rec = pStart  \\n    else:  \\n        rec += pInterval  \\n    return rec ")

        gsd_int = float(format(arcpy.Describe("fwd_exp").children[0].meanCellHeight, ".2f"))
        arcpy.env.extent = plotting_area[0]

        arcpy.gp.EucDistance_sa("fwd_point",os.path.join(self.loc_gdb,"euc_fwd"),"","{}".format(gsd_int),"","PLANAR","","")
        arcpy.env.extent

        arcpy.gp.ZonalStatistics_sa("expld","fid_new","euc_fwd",os.path.join(self.loc_gdb,"zon_fwd"),"MAXIMUM","DATA")

        arcpy.gp.ExtractValuesToPoints_sa("fwd_point","zon_fwd",os.path.join(self.loc_gdb,"fwd_out"),"NONE","VALUE_ONLY")

        arcpy.Buffer_analysis("fwd_out",os.path.join(self.loc_gdb,"crown_fwd"),"RASTERVALU","FULL","ROUND","NONE","","PLANAR")

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != "crown_nwd" and str(layer) != "crown_fwd" and str(layer) != "crown_wd" and str(layer) != plotting_area[0] and str(layer) != plotting_data[0] and str(layer) != plotting_data_tif[0]:
                arcpy.mapping.RemoveLayer(df,layer)

class process_shape:
    def __init__(self,data_process):
        self.data_process = data_process
        arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")
        try:
            arcpy.AddField_management(self.data_process,"ket","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "buffer", "DOUBLE", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "fidcopy", "SHORT", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")
        except Exception:
            pass

        #Processing Shapefile
        arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

        arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

        arcpy.CalculateField_management(self.data_process, "fidcopy", "autoIncrement()", "PYTHON_9.3", "rec=0 \\ndef autoIncrement(): \\n    global rec \\n    pStart = 1  \\n    pInterval = 1 \\n    if (rec == 0):  \\n        rec = pStart  \\n    else:  \\n        rec += pInterval  \\n    return rec ")

        mylist_dist = list(([float(row.getValue("NEAR_DIST")) for row in arcpy.SearchCursor(self.data_process, fields="NEAR_DIST")]))

        mylist_fid = list(([int(row.getValue("fidcopy")) for row in arcpy.SearchCursor(self.data_process, fields="fidcopy")]))

        ziped = dict(zip(mylist_dist,list(mylist_fid)))

        fids_to_delete = []
        for key, value in ziped.items():
            if float(key) <= 1.0:
                fids_to_delete.append(value)

        if len(fids_to_delete) > 0:
            for fid_to_delete in fids_to_delete:
                arcpy.SelectLayerByAttribute_management(self.data_process,"NEW_SELECTION","\"fidcopy\" = {}".format(fid_to_delete))

                arcpy.DeleteFeatures_management(self.data_process)

            arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")

            arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

            arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

            arcpy.CalculateField_management(self.data_process, "fidcopy", "[FID]", "VB", "")  

class all_process:
    @staticmethod
    def all_process():
        location = os.path.expanduser('~/Documents/Avirtech/Avirkey/Avirkey.ini')
        if exists(location):
            initiation_process.initiate_process()
            starting_first.starting_process()
            process_shape(data_process=plotting_data[0])

            mylist_areatype = list(set([str(row.getValue("ket")) for row in arcpy.SearchCursor(plotting_area[0], fields="ket")]))

            outputgdb = "crowndetection.gdb"

            global areatype
            for areatype in mylist_areatype:
                if str(areatype) == "fwd":
                    name = "fwd"
                    os.mkdir(os.path.join(gdb_location,"fwd"))
                    fwd_location = os.path.join(gdb_location,"fwd")
                    fwd_loc_gdb = os.path.join(fwd_location,outputgdb)

                    create_folder(fwd_location).create_folder()
                    process_first(fwd_location,name)
                    processing_raster_full_grassy(fwd_loc_gdb).processing_raster_full_grassy()
                
                elif str(areatype) == "wd":
                    name = "wd"
                    data = "wd_exp"
                    data_process = "wd_point"
                    export_name = "crown_ring_wd"
                    os.mkdir(os.path.join(gdb_location,"wd"))
                    wd_location = os.path.join(gdb_location,"wd")
                    wd_loc_gdb = os.path.join(wd_location,outputgdb)

                    create_folder(wd_location).create_folder()
                    process_first(wd_location,name)
                    processing_raster_medium_grass(data,wd_location,data_process)
                
                elif str(areatype) == "nwd":
                    name = "nwd"
                    data = "nwd_exp"
                    data_process = "nwd_point"
                    export_name = "crown_ring_nwd"
                    os.mkdir(os.path.join(gdb_location,"nwd"))
                    nwd_location = os.path.join(gdb_location,"nwd")
                    arcpy.CreateFileGDB_management(nwd_location,outputgdb)

                    nwd_loc_gdb = os.path.join(nwd_location,outputgdb)

                    create_folder(nwd_location).create_folder()
                    process_first(nwd_location,name)
                    processing_raster_non_grassy(data,nwd_location,data_process)
            
            substring_merge = "crown"
            outer = []

            arcpy.CreateFileGDB_management(gdb_location,outputgdb)

            gdb_all = os.path.join(gdb_location,outputgdb)

            os.mkdir(os.path.join(gdb_location,"buffer"))

            buffer_location_all = os.path.join(gdb_location,"buffer")

            for merge in arcpy.mapping.ListLayers(mxd):
                if str(merge).find(substring_merge) != -1:
                    outer.append(str(merge))

            s = ";".join(outer)

            arcpy.Merge_management(s,os.path.join(gdb_all,"outer_ring"))

            arcpy.FeatureClassToFeatureClass_conversion("outer_ring",buffer_location_all,"crown_ring_all")

            for layer in arcpy.mapping.ListLayers(mxd):
                if str(layer) == "crown_fwd" and str(layer) == "crown_nwd" and str(layer) == "crown_wd":
                    arcpy.mapping.RemoveLayer(df,layer)
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("showinfo","You don't have Avirkey or maybe your Avirkey is not properly installed, please generate your serial number first!")
            root.destroy

# all_process.all_process()