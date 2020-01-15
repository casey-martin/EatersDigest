CREATE TABLE food_des (
        'NDB_No' TEXT PRIMARY KEY, 
        'FdGrp_Cd' TEXT,
        'Long_Desc' TEXT,
        'Shrt_Desc' TEXT, 
        'ComName' TEXT,
        'ManufacName' TEXT,
        'Survey' TEXT,
        'Ref_desc' TEXT,
        'Refuse' REAL,
        'SciName' TEXT,
        'N_Factor' REAL,
        'Pro_Factor' REAL,
        'Fat_Factor' REAL,
        'CHO_Factor' REAL);


CREATE TABLE fd_group (
        'FdGrp_Cd' TEXT PRIMARY KEY,
        'FdGrp_Desc' TEXT
    );

CREATE TABLE nut_data (
        'NDB_No' TEXT,
        'Nutr_No' ,
        'Nutr_Val' REAL,
        'Num_Data_Pts' INT,
        'Std_Error' REAL,
        'Src_Cd' TEXT,
        'Deriv_Cd' TEXT,
        'Ref_NDB_No' INT,
        'Add_Nutr_Mark' TEXT,
        'Num_Studies' INT,
        'Min' REAL,
        'Max' REAL,
        'DF' REAL,
        'Low_EB' REAL,
        'Up_EB' REAL,
        'Stat_cmt' TEXT,
        'AddMod_Date' TEXT,
        'CC' TEXT
    );


CREATE TABLE nutr_def (
        'Nutr_No' TEXT PRIMARY KEY,
        'Units' TEXT,
        'Tagname' TEXT,
        'NutrDesc' TEXT,
        'Num_Dec' TEXT,
        'SR_Order' INT
    );


CREATE TABLE weight (
        'NDB_No' TEXT,
        'Seq' REAL,
        'Amount' REAL,
        'Msre_Desc' TEXT,
        'Gm_Wgt' REAL,
        'Num_Data_Pts' INT,
        'Std_Dev' REAL
    );

.mode csv
.separator "^"
.import FOOD_DES.txt food_des
.import FD_GROUP.txt fd_group
.import NUT_DATA.txt nut_data
.import NUTR_DEF.txt nutr_def
.import WEIGHT.txt weight
