######################## USER INPUT ###########################
#### REPLACE folder with name of directory containing jump_trial_data
folder = "C:/jump_trial_data"
###############################################################

################################# VALUES FOR DATA ANALYSIS ###########################################
trials_config = {
    ####################################################################################################################
    ############################################ WAX INTACT ###########################################################
    ####################################################################################################################
    "UPLB14-1": {
        "wax_status": "Y",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 2573,

        "peak_frame": 10,

        "first_move_frame": 7,
        "stop_tracking_frame": 699,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.8365831429928754,
        "direction_takeoff_peak": 0.9991965104113364,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-1_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-1_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-3": {
        "wax_status": "Y",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1924,

        "peak_frame": 36,

        "first_move_frame": 28,
        "stop_tracking_frame": 742,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.2162325140095147,
        "direction_takeoff_peak": 0.9474987469209671,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-3_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-3_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-4": {
        "wax_status": "Y",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1675,

        "peak_frame": 26,

        "first_move_frame": 22,
        "stop_tracking_frame": 635,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.9467324090437894,
        "direction_takeoff_peak": 0.9696494459161104,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-4_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-6": {
        "wax_status": "Y",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1846,

        "peak_frame": 32,

        "first_move_frame": 29,
        "stop_tracking_frame": 621,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.8398593293971586,
        "direction_takeoff_peak": 0.7470320947517333,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-6_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-6_centroid_data.csv",
    },
    ######################################

    ######################################
    "hopperE-7": {
        "wax_status": "Y",
        "body_length_m": 0.0054,
        "frame_rate": 2000,
        "pixperm": 1676,

        "first_move_frame": 29,
        "stop_tracking_frame": 783,

        "peak_frame": 34,

        "drag_constant_constant": 1.15,

        "velocity_takeoff_peak": 3.1829068287888016,
        "direction_takeoff_peak": 0.9987128659654708,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_E-7_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/hopperE-7_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB17-3": {
        "wax_status": "Y",
        "body_length_m": 0.0035,
        "frame_rate": 2000,
        "pixperm": 3088,

        "first_move_frame": 3,
        "stop_tracking_frame": 663,

        "peak_frame": 4,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.077864052472444,
        "direction_takeoff_peak": 1.118303113813752,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_17-3_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB17-3_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB17-4": {
        "wax_status": "Y",
        "body_length_m": 0.0035,
        "frame_rate": 2000,
        "first_move_frame": 9,
        "stop_tracking_frame": 619,
        "pixperm": 1994,

        "peak_frame": 10,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.8906107475330107,
        "direction_takeoff_peak": 1.1229400922489186,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_17-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB17-4_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB16-2": {
        "wax_status": "Y",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "first_move_frame": 7,
        "stop_tracking_frame": 478,
        "pixperm": 3877,

        "peak_frame": 8,

        "drag_constant_constant": 3.2,

        "velocity_takeoff_peak": 1.2872827323372251,
        "direction_takeoff_peak": 1.3527319987056745,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_16-2_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB16-2_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB16-3": {
        "wax_status": "Y",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "first_move_frame": 6,
        "stop_tracking_frame": 566,
        "pixperm": 4426,

        "peak_frame": 7,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.6238874588486913,
        "direction_takeoff_peak": 1.1863943889994168,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_16-3_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB16-3_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB16-4": {
        "wax_status": "Y",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "first_move_frame": 5,
        "stop_tracking_frame": 560,
        "pixperm": 2956,

        "peak_frame": 6,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.4026893387323371,
        "direction_takeoff_peak": 1.2060120788231834,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_16-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB16-4_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB7-1": {
        "wax_status": "Y",
        "body_length_m": 0.0026,
        "frame_rate": 2500,
        "pixperm": 3056,
        "first_move_frame": 7,
        "stop_tracking_frame": 732,

        "peak_frame": 8,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.6596830563829346,
        "direction_takeoff_peak": 1.0071970301344078,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_7-1_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB7-1_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB7-2": {
        "wax_status": "Y",
        "body_length_m": 0.0026,
        "frame_rate": 2000,
        "pixperm": 3116,
        "first_move_frame": 9,
        "stop_tracking_frame": 959,

        "peak_frame": 9,

        "drag_constant_constant": 1.8,

        "velocity_takeoff_peak": 2.5564729740481864,
        "direction_takeoff_peak": 1.1215133837866815,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_7-2_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB7-2_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB7-3": {
        "wax_status": "Y",
        "body_length_m": 0.0026,
        "frame_rate": 2000,
        "pixperm": 3039,
        "first_move_frame": 7,
        "stop_tracking_frame": 628,

        "peak_frame": 7,

        "drag_constant_constant": 1.3,
        "drag_constant_leg_add": 0.5,

        "velocity_takeoff_peak": 1.782130477764825,
        "direction_takeoff_peak": 1.0403233606171536,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_7-3_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB7-3_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB7-4": {
        "wax_status": "Y",
        "body_length_m": 0.0026,
        "frame_rate": 2000,
        "pixperm": 3218,
        "first_move_frame": 8,
        "stop_tracking_frame": 581,

        "peak_frame": 9,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.5405180005613794,
        "direction_takeoff_peak": 0.9892755330406161,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_7-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB7-4_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB7-5": {
        "wax_status": "Y",
        "body_length_m": 0.0026,
        "frame_rate": 2000,
        "pixperm": 2951,

        "first_move_frame": 21,
        "stop_tracking_frame": 663,

        "peak_frame": 22,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.219545366481464,
        "direction_takeoff_peak": 0.919160287986191,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_7-5_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB7-5_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB2-6": {
        "wax_status": "Y",
        "body_length_m": 0.0046,
        "frame_rate": 2000,
        "first_move_frame": 6,
        "stop_tracking_frame": 533,
        "pixperm": 2679,

        "peak_frame": 9,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.9110815569833182,
        "direction_takeoff_peak": 0.8460211918767914,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_2-6_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB2-6_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB2-7": {
        "wax_status": "Y",
        "body_length_m": 0.0046,
        "frame_rate": 2000,
        "first_move_frame": 7,
        "stop_tracking_frame": 374,
        "pixperm": 2346,

        "peak_frame": 8,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 0.8659999383519922,
        "direction_takeoff_peak": 1.0895473123698165,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_2-7_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB2-7_centroid_data.csv",
    },
    ####################################################################################################################

    ####################################################################################################################
    "UPLB15-4": {
        "wax_status": "Y",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1486,
        "first_move_frame": 15,
        "stop_tracking_frame": 1065,

        "peak_frame": 16,

        "drag_constant_constant": 0.98,

        "velocity_takeoff_peak": 3.6221746292700954,
        "direction_takeoff_peak": 1.1266253390519216,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_15-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB15-4_centroid_data.csv",
    },
    ####################################################################################################################

    ####################################################################################################################
    "UPLB3-4": {
        "wax_status": "Y",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "pixperm": 3376,
        "first_move_frame": 8,
        "stop_tracking_frame": 397,

        "peak_frame": 9,

        "drag_constant_constant": 1.35,

        "velocity_takeoff_peak": 1.095478566205164,
        "direction_takeoff_peak": 1.0886943043139252,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_3-4_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB3-4_centroid_data.csv",
    },
    ####################################################################################################################



    ####################################################################################################################
    ############################################ WAX REMOVED ###########################################################
    ####################################################################################################################
    "UPLB14-8_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1597,
        "first_move_frame": 14,
        "stop_tracking_frame": 496,

        "peak_frame": 17,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.9933197274083965,
        "direction_takeoff_peak": 0.6467208131601471,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-8_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-8_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-10_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 2375,
        "first_move_frame": 15,
        "stop_tracking_frame": 563,

        "peak_frame": 17,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.2776031326825263,
        "direction_takeoff_peak": 0.9134814681633585,

        # Filepath
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-10_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-10_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-11_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1578,

        "peak_frame": 10,

        "first_move_frame": 9,
        "stop_tracking_frame": 486,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.271258437423388,
        "direction_takeoff_peak": 1.0652674674769176,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-11_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-11_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB14-13_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1609,
        "first_move_frame": 9,  # OR 8
        "stop_tracking_frame": 616,

        "peak_frame": 14,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.632493619603305,
        "direction_takeoff_peak": 1.1620334840867468,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_14-13_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB14-13_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB5-1_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0033,
        "frame_rate": 2500,
        "first_move_frame": 10,
        "stop_tracking_frame": 520,
        "pixperm": 1808,

        "peak_frame": 13,

        "drag_constant_constant": 0.4,

        "velocity_takeoff_peak": 1.6550813365910795,
        "direction_takeoff_peak": 0.6708380811597477,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_5-1_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB5-1_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB5-3_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0033,
        "frame_rate": 2500,
        "first_move_frame": 11,
        "stop_tracking_frame": 577,
        "pixperm": 3017,

        "peak_frame": 12,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.6937755580689726,
        "direction_takeoff_peak": 0.7134893291744864,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_5-3_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB5-3_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB5-5_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0033,
        "frame_rate": 2500,
        "first_move_frame": 7,
        "stop_tracking_frame": 580,
        "pixperm": 3175,

        "peak_frame": 14,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.4736797765920457,
        "direction_takeoff_peak": 0.8824642008688028,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_5-5_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB5-5_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "hopperF-2_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0047,
        "frame_rate": 2000,
        "first_move_frame": 4,
        "stop_tracking_frame": 832,
        "pixperm": 1934,

        "peak_frame": 6,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.4736797765920457,
        "direction_takeoff_peak": 0.8824642008688028,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_F-2_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/hopperF-2_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB3-9_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "pixperm": 3758,

        "first_move_frame": 16,
        "stop_tracking_frame": 394,

        "peak_frame": 17,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 0.9039289630663534,
        "direction_takeoff_peak": 1.0662186618617675,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_3-9_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB3-9_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB3-10_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0031,
        "frame_rate": 2000,
        "pixperm": 5062,
        "first_move_frame": 13,
        "stop_tracking_frame": 422,

        "peak_frame": 15,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 1.097239477506539,
        "direction_takeoff_peak": 1.1144360599585394,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_3-10_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB3-10_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB11-1_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0035,
        "frame_rate": 2000,
        "first_move_frame": 7,
        "stop_tracking_frame": 656,
        "pixperm": 1713,

        "peak_frame": 8,

        "drag_constant_constant": 0.15,

        "velocity_takeoff_peak": 2.172241033265116,
        "direction_takeoff_peak": 0.7655109032747541,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_11-1_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB11-1_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB11-4_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0035,
        "frame_rate": 2000,
        "first_move_frame": 7,
        "stop_tracking_frame": 818,
        "pixperm": 1910,

        "peak_frame": 8,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.948340532174629,
        "direction_takeoff_peak": 0.94287038855911,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_11-4_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB11-4_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB11-5_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0035,
        "frame_rate": 2000,
        "first_move_frame": 7,
        "stop_tracking_frame": 715,
        "pixperm": 2039,

        "peak_frame": 8,

        "drag_constant_constant": 0, # not used in select centroid analysis

        "velocity_takeoff_peak": 2.5569503421038604,
        "direction_takeoff_peak": 0.8414208732575205,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_11-5_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB11-5_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB15-8_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1947,
        "first_move_frame": 9,
        "stop_tracking_frame": 1029,

        "peak_frame": 12,

        "drag_constant_constant": 0.0,

        "velocity_takeoff_peak": 2.344950677401368,
        "direction_takeoff_peak": 1.3659522333590766,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_15-8_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB15-8_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB15-9_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0048,
        "frame_rate": 2000,
        "pixperm": 1567,
        "first_move_frame": 8,
        "stop_tracking_frame": 873,

        "peak_frame": 10,

        "drag_constant_constant": 0.15,

        "velocity_takeoff_peak": 2.64441440102831,
        "direction_takeoff_peak": 1.0109969506560008,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_15-9_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB15-9_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB10-5_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0029,
        "frame_rate": 2000,
        "first_move_frame": 11,
        "stop_tracking_frame": 627,
        "pixperm": 1605,  # NEW - 2024-6-17

        "peak_frame": 12,

        "drag_constant_constant": 0,

        "velocity_takeoff_peak": 1.5993977213204342,
        "direction_takeoff_peak": 0.8935278856622011,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_10-5_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB10-5_nowax_centroid_data.csv",
    },
    ######################################

    ######################################
    "UPLB5-6_nowax": {
        "wax_status": "N",
        "body_length_m": 0.0033,
        "frame_rate": 2500,
        "first_move_frame": 11,
        "stop_tracking_frame": 481,
        "pixperm": 5248,

        "peak_frame": 14,

        "drag_constant_constant": 0.4,

        "velocity_takeoff_peak": 1.221636395526575,
        "direction_takeoff_peak": 0.8150513895609591,

        # Filepaths
        "DLT_data_filepath": folder + "/DLT_body-pt-data/DLT_data_5-6_nowax_xypts.csv",
        "centroid_data_filepath": folder + "/centroid-pt-data/all_data/UPLB5-6_nowax_centroid_data.csv",
    },
    ######################################
}
####################################################################################################################

#### FUNCTION to DECREMENT frame number by 1 (avi files start numbering at 1 instead of 0)
def decrement_frame_values(trials):
    for trial_name, config in trials.items():
        for frame_key in ["first_move_frame", "stop_tracking_frame"]:
            if frame_key in config:
                config[frame_key] -= 1

decrement_frame_values(trials_config)



#### FUNCTION to LOAD configuration for a specific trial
def load_trial_config(trial_name):
    trial_config = trials_config.get(trial_name, None)

    if trial_config:
        return trial_config
    else:
        raise ValueError(f"No configuration found for trial {trial_name}")