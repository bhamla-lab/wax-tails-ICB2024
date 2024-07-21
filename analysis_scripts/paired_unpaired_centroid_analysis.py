import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# import the configuration script
import PH_config_file

###################### USER INPUT #########################
#### UNCOMMENT trial lists to run analysis

######################################
# PAIRED DATA - WAX INTACT
trials = [
    'UPLB14-1',
    'UPLB14-3',
    'UPLB14-4',
    'UPLB14-6',
]
######################################

# #####################################
# # PAIRED DATA - WAX REMOVED
# trials = [
#     ### PAIRED GROUP - UPLB14 ####
#     'UPLB14-8_nowax',
#     'UPLB14-10_nowax',
#     'UPLB14-11_nowax',
#     'UPLB14-13_nowax',
# ]
# #####################################

# #####################################
# # UNPAIRED DATA - WAX INTACT
# trials = [
#     'hopperE-7',
#     'UPLB17-3',
#     'UPLB17-4',
#     'UPLB16-2',
#     'UPLB16-3',
#     'UPLB16-4',
#     'UPLB7-1',
#     'UPLB7-2',
#     'UPLB7-3',
#     'UPLB7-4',
#     'UPLB7-5',
#     'UPLB2-6',
#     'UPLB2-7',
# ]
# #####################################

# #####################################
# # UNPAIRED DATA - WAX REMOVED
# trials = [
#     'UPLB5-1_nowax',
#     'UPLB5-3_nowax',
#     'UPLB5-5_nowax',
#     'hopperF-2_nowax',
#     'UPLB3-9_nowax',
#     'UPLB3-10_nowax',
#     'UPLB14-8_nowax',
#     'UPLB14-10_nowax',
#     'UPLB14-11_nowax',
#     'UPLB14-13_nowax',
#     'UPLB11-1_nowax',
#     'UPLB11-4_nowax',
#     'UPLB11-5_nowax',
# ]
# #####################################

#################### LOOP OVER TRIALS ########################
for trial in trials:
    trial_name = trial
    trial_config = PH_config_file.load_trial_config(trial_name)
    print('\n')
    print(trial_name)

    if trial_config is not None:
        #### LOAD in data and values from config file
        centroid_filepath = trial_config.get("centroid_data_filepath")
        frame_rate = trial_config.get('frame_rate')
        pixperm = trial_config.get("pixperm")
        start_frame = trial_config.get('first_move_frame') - 1  # one frame before the first movement frame
        BL_m = trial_config.get('body_length_m')

        peak_frame = trial_config.get("peak_frame")

        ### LOAD in centroid data
        centroid_data = pd.read_csv(centroid_filepath)

        #### CONVERT pix to m
        centroid_data['ypos_m'] = centroid_data['ypos_pix'] / pixperm
        centroid_data['xpos_m'] = centroid_data['xpos_pix'] / pixperm

        #### INVERT y-values
        centroid_data['ypos_m'] = -centroid_data['ypos_m']

        #### MIRROR data to depict jump from left to right if needed
        if centroid_data.loc[centroid_data.index[start_frame + 5], 'xpos_m'] < centroid_data.loc[
            centroid_data.index[start_frame], 'xpos_m']:  # check direction
            image_width = 1024 / pixperm  # image width for Photron videos is 1024 pixels

            # Flip x-values to mirror the data horizontally
            centroid_data['xpos_m'] = image_width - centroid_data['xpos_m']
            print('Jump is from right to left --- MIRRORING centroid x-position data')

        #### COPY data to modify
        centroid_data_modified = centroid_data.copy()

        #### SMOOTH position data --- Savitzky–Golay filter (window size = 21, polynomial order = 1)
        smooth_window = 21
        poly_order = 1

        centroid_data_modified['xpos_m_smooth'] = savgol_filter(centroid_data_modified['xpos_m'], smooth_window,
                                                                poly_order, mode='interp')
        centroid_data_modified['ypos_m_smooth'] = savgol_filter(centroid_data_modified['ypos_m'], smooth_window,
                                                                poly_order, mode='interp')

        #### INITIALIZE centroid points off of start frame x,y
        # RAW data:
        first_value_x = centroid_data_modified.loc[0, 'xpos_m']
        first_value_y = centroid_data_modified.loc[0, 'ypos_m']

        centroid_data_modified['xpos_m'] -= first_value_x
        centroid_data_modified['ypos_m'] -= first_value_y

        # SMOOTHED data:
        first_value_x = centroid_data_modified.loc[0, 'xpos_m_smooth']
        first_value_y = centroid_data_modified.loc[0, 'ypos_m_smooth']

        centroid_data_modified['xpos_m_smooth'] -= first_value_x
        centroid_data_modified['ypos_m_smooth'] -= first_value_y

        #### SET time
        centroid_data_modified['time_s'] = centroid_data_modified['index_num'] / frame_rate


        #################### CALCULATE VELOCITY ########################
        ##### CALCULATE velocity componenets from raw values
        centroid_data_modified['vel_x_RAW'] = np.gradient(centroid_data_modified['xpos_m'],
                                                          centroid_data_modified['time_s'])
        centroid_data_modified['vel_y_RAW'] = np.gradient(centroid_data_modified['ypos_m'],
                                                          centroid_data_modified['time_s'])

        #### CALCULATE velocity from raw values
        centroid_data_modified['velocity_mpers_RAW'] = np.sqrt(
            centroid_data_modified['vel_x_RAW'] ** 2 + centroid_data_modified['vel_y_RAW'] ** 2)

        #### CALCULATE velocity direction from raw values
        centroid_data_modified['velocity_direction_RAW'] = np.arctan2(centroid_data_modified['vel_y_RAW'],
                                                                      centroid_data_modified['vel_x_RAW'])

        #### WRAP direction values across -pi and pi (add 2pi)
        centroid_data_modified['velocity_direction_RAW_unwrap'] = np.unwrap(
            centroid_data_modified['velocity_direction_RAW'])

        #### CROP to peak take-off velocity frame and reset starting time to 0 (important step for smoothing)
        peak_frame_idx = centroid_data_modified.index[centroid_data_modified['frame_num'] == peak_frame].tolist()
        peak_frame_idx = peak_frame_idx[0]

        centroid_data_modified_crop1 = centroid_data_modified[peak_frame_idx::].reset_index(drop=True)


        #### SMOOTH velocity magnitude and direction --- Savitzky–Golay filter (window size = 71, polynomial order = 1)
        smooth_window = 71
        poly_order = 1

        # velocity direction
        centroid_data_modified_crop1['velocity_direction_RAW_smooth'] = savgol_filter(
            centroid_data_modified_crop1['velocity_direction_RAW'], smooth_window, poly_order, mode='interp')
        # velocity magnitude
        centroid_data_modified_crop1['velocity_mpers_RAW_smooth'] = savgol_filter(
            centroid_data_modified_crop1['velocity_mpers_RAW'], smooth_window, poly_order, mode='interp')

        #### PRINT peak takeoff velcoity and landing velocity
        vel_smooth = centroid_data_modified_crop1['velocity_mpers_RAW_smooth'].iloc[0]
        dir_smooth = centroid_data_modified_crop1['velocity_direction_RAW_smooth'].iloc[0]

        print('Takeoff Experimental Values:')
        print('smooth takeoff velocity (m/s) = ', vel_smooth)
        print('smooth takeoff direction (rad) = ', dir_smooth)
        print('smooth takeoff velocity (BL/s) = ', vel_smooth / BL_m)
        print('smooth takeoff direction (deg) = ', dir_smooth * (180 / np.pi))
        ################################################################