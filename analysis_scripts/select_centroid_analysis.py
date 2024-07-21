import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.signal import savgol_filter

# import the configuration script
import PH_config_file

###################### USER INPUT #########################
#### UNCOMMENT trial lists to run analysis

############## SELECT DATA - WAX INTACT ##############
print('Wax Intact Trials')
trials = [
    'UPLB15-4',
    'hopperE-7',
    'UPLB7-2',
    'UPLB7-3',
    'UPLB16-2',
    'UPLB3-4',
]
#####################################

# ############## SELECT DATA - WAX REMOVED ##############
# print('Wax Removed Trials')
# trials = [
#     'UPLB15-9_nowax',
#     'UPLB15-8_nowax',
#     'UPLB11-1_nowax',
#     'UPLB10-5_nowax',
#     'UPLB5-1_nowax',
#     'UPLB5-6_nowax',
# ]
# #####################################
###############################################################

#### SETUP plots
styles = ['-', '--', '-.', ':', '-', '--', '-.', ':']
markers = ['^', 'D', 'o', 's', 'h', 'v', 'p', '*']
color_palette = sns.color_palette("tab10")

plot_color_i = 0
plot_style_i = 0
plot_marker_i = 0

fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

fig2, ax2 = plt.subplots(figsize=(15, 8))
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig3, ax3 = plt.subplots(figsize=(12, 8))
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

fig4, ax4 = plt.subplots(figsize=(12, 8))
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.axhline(y=0, color='black', linestyle='--', alpha=0.1)

fig5, ax5 = plt.subplots(figsize=(12, 8))
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)

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
        D_CD = trial_config.get("drag_constant_constant")
        vel_takeoff_peak = trial_config.get("velocity_takeoff_peak")
        dir_takeoff_peak = trial_config.get("direction_takeoff_peak")

        # Plots
        style = styles[trials.index(trial) % len(styles)]  # Cycle through styles
        plot_color = color_palette[plot_color_i % len(color_palette)]
        plot_style = styles[plot_style_i % len(styles)]
        plot_marker = markers[plot_marker_i % len(markers)]


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
            print(trial_name, ': Jump is from right to left --- MIRRORING centroid x-position data')

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

        #### FIND max length, height, and time
        max_length_smooth = centroid_data_modified['xpos_m_smooth'].max()
        max_height_smooth = centroid_data_modified['ypos_m_smooth'].max()
        max_time = centroid_data_modified['time_s'].max()

        # ################### NORMALIZED VALUES FOR PLOTTING #################
        centroid_data_modified['xpos_m_smooth_NORM'] = centroid_data_modified['xpos_m_smooth'] / max_length_smooth
        centroid_data_modified['ypos_m_smooth_NORM'] = centroid_data_modified['ypos_m_smooth'] / max_height_smooth


        ###############################################################
        #### PLOT normalized trajectories - altogether outside loop
        # SMOOTHED data:
        ax1.plot(centroid_data_modified['xpos_m_smooth_NORM'], centroid_data_modified['ypos_m_smooth_NORM'], linestyle='-', color=plot_color)
        ax1.scatter(centroid_data_modified['xpos_m_smooth_NORM'][::50], centroid_data_modified['ypos_m_smooth_NORM'][::50], label=f'{trial_name}', facecolors=plot_color, edgecolors=plot_color, marker=plot_marker)
        ax1.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.1)
        ax1.axvline(x=0.5, color='black', linestyle='--', linewidth=1, alpha=0.1)

        ax1.set_aspect('equal')
        ax1.tick_params(axis='both', which='major', labelsize=18)  # You can adjust the size as needed
        ax1.set_xlabel('Normalized x-position', fontsize=14)
        ax1.set_ylabel('Normalized y-position', fontsize=14)
        ax1.set_title('Normalized Smooth Centroid Position')
        ax1.legend()


        #### PLOT centroid trajectories

        # SMOOTHED data:
        ax2.plot(centroid_data_modified['xpos_m_smooth'], centroid_data_modified['ypos_m_smooth'], linestyle='-',
                 color=plot_color)
        ax2.scatter(centroid_data_modified['xpos_m_smooth'][::50], centroid_data_modified['ypos_m_smooth'][::50],
                    label=trial_name, facecolors=plot_color, edgecolors=plot_color, marker=plot_marker)
        ax2.axhline(y=0, color='black', linestyle='--', alpha=0.1)

        x_limit = (0, 0.6)
        y_limit = (-0.01, 0.35)
        ax2.set_xlim(x_limit)
        ax2.set_ylim(y_limit)

        ax2.set_aspect('equal')
        ax2.tick_params(axis='both', which='major', labelsize=18)  # You can adjust the size as needed
        ax2.set_xlabel('x-position (m)', fontsize=14)
        ax2.set_ylabel('y-position (m)', fontsize=14)
        ax2.set_title('Smoothed Centroid Position')
        ax2.legend()
        ################################################################

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
        centroid_data_modified_crop1['index_num'] = centroid_data_modified_crop1.index
        centroid_data_modified_crop1['time_s'] = centroid_data_modified_crop1['index_num'] / frame_rate
        centroid_data_modified_crop1['time_normalized'] = centroid_data_modified['time_s'] / \
                                                          centroid_data_modified['time_s'].iloc[-1]

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

        landing_vel_smooth = centroid_data_modified_crop1['velocity_mpers_RAW_smooth'].iloc[-1]
        landing_dir_smooth = centroid_data_modified_crop1['velocity_direction_RAW_smooth'].iloc[-1]

        print('TAKEOFF Experimental Values:')
        print('smooth takeoff velocity (m/s) = ', vel_smooth)
        print('smooth takeoff direction (rad) = ', dir_smooth)
        print('smooth takeoff velocity (BL/s) = ', vel_smooth / BL_m)
        print('smooth takeoff direction (deg) = ', dir_smooth * (180 / np.pi))

        print('\nLANDING Experimental Values:')
        print('smooth landing velocity (m/s) = ', landing_vel_smooth)
        print('landing smooth direction (rad)= ', landing_dir_smooth)
        print('smooth takeoff velocity (BL/s) = ', landing_vel_smooth / BL_m)
        print('landing smooth direction (deg)= ', landing_dir_smooth * (180 / np.pi))
        ################################################################

        #################### CALCUALTE ACCELERATION ####################
        #### CALCULATE derivative of the smoothed velocity
        centroid_data_modified_crop1['acceleration_smooth'] = np.gradient(
            centroid_data_modified_crop1['velocity_mpers_RAW_smooth'], centroid_data_modified_crop1['time_s'])

        #### SMOOTH acceleration --- Savitzky–Golay filter (window size = 31, polynomial order = 1)
        smooth_window = 31
        poly_order = 1
        centroid_data_modified_crop1['acceleration_smooth_smooth'] = savgol_filter(centroid_data_modified_crop1['acceleration_smooth'], smooth_window, poly_order, mode='interp')
        ################################################################

        ################################################################
        #### PLOT acceleration
        ax3.scatter(centroid_data_modified_crop1['time_s'][::5], centroid_data_modified_crop1['acceleration_smooth_smooth'][::5], facecolors='none', edgecolors=plot_color, label = f"{trial_name}, Experimental Data")
        ax3.axhline(y=0, color='black', linestyle='--', alpha=0.1)

        ax3.tick_params(axis='both', which='major', labelsize=18)  # You can adjust the size as needed
        ax3.set_xlabel('Time (s)', fontsize = 14)
        ax3.set_ylabel('Acceleration (m/s^2)', fontsize = 14)
        ax3.set_title('Centroid Acceleration')
        ax3.legend()
        ################################################################

 
        ########################### DRAG MODEL ########################
        #### SET constants
        g = 9.81  # m/s^2
        U_0 = vel_takeoff_peak  # m/s, peak takeoff velocity
        theta_0 = dir_takeoff_peak  # radians, peak takeoff direction
        dt = (1 / frame_rate)

        # Constant Drag
        time_CD_list = []
        x_CD_list = []
        y_CD_list = []
        Ux_CD_list = []
        Uy_CD_list = []
        Umag_CD_list = []

        Ux_CD = U_0 * np.cos(theta_0)
        Uy_CD = U_0 * np.sin(theta_0)

        t_CD = 0
        x_CD = 0
        y_CD = 0

        time_CD_list.append(t_CD)
        x_CD_list.append(x_CD)
        y_CD_list.append(y_CD)
        Ux_CD_list.append(Ux_CD)
        Uy_CD_list.append(Uy_CD)
        Umag_CD_list.append(np.sqrt(Ux_CD ** 2 + Uy_CD ** 2))

        ########## LOOP for Drag CONSTANT ################
        while y_CD >= 0:  # stop computing at end of trajecotry

            Umag_CD = np.sqrt(Ux_CD ** 2 + Uy_CD ** 2)

            dUx_dt_CD = -D_CD * Ux_CD * Umag_CD
            dUy_dt_CD = -g - (D_CD * Umag_CD * Uy_CD)

            Ux_CD += dUx_dt_CD * dt
            Uy_CD += dUy_dt_CD * dt
            x_CD += Ux_CD * dt
            y_CD += Uy_CD * dt

            t_CD += dt

            time_CD_list.append(t_CD)
            x_CD_list.append(x_CD)
            y_CD_list.append(y_CD)
            Ux_CD_list.append(Ux_CD)
            Uy_CD_list.append(Uy_CD)
            Umag_CD_list.append(np.sqrt(Ux_CD ** 2 + Uy_CD ** 2))

        # FOR DRAG CONSTANT
        time_CD_array = np.array(time_CD_list, dtype=np.float64)

        ################################################################
        #### PLOT constant drag model with experimental data
        # Trajectory
        ax4.scatter(centroid_data_modified_crop1['xpos_m_smooth'][::20], centroid_data_modified_crop1['ypos_m_smooth'][::20], label = f"{trial_name}, Experimental Data", facecolors='none', edgecolors=plot_color)
        ax4.plot(x_CD_list, y_CD_list, label=f'Model: Constant Drag, D={D_CD}', linestyle='-', color=plot_color)

        ax4.tick_params(axis='both', which='major', labelsize=18)  # You can adjust the size as needed
        ax4.set_xlabel('x-position (m)', fontsize=14)
        ax4.set_ylabel('y-position (m)', fontsize=14)
        ax4.set_title('Centroid Trajectory Comparison w/ Model')
        ax4.axis('equal')
        ax4.legend()


        # Velocity
        ax5.scatter(centroid_data_modified_crop1['time_s'][::20], centroid_data_modified_crop1['velocity_mpers_RAW_smooth'][::20], label = f"{trial_name}, Experimental Data", facecolors='none', edgecolors=plot_color)
        ax5.plot(time_CD_array, Umag_CD_list, label=f'Model: Constant Drag, D= {D_CD}', linestyle='-', color=plot_color)

        ax5.tick_params(axis='both', which='major', labelsize=18)  # You can adjust the size as needed
        ax5.set_xlabel('Time (s)',fontsize=14)
        ax5.set_ylabel('Centroid Velocity (m/s)', fontsize=14)
        ax5.set_title('Centroid Velocity vs Time Comparison w/ Model', fontsize=14)
        ax5.legend()
        ################################################################

        #### UPDATE plot setting for next trial
        plot_color_i += 1
        plot_style_i += 1
        plot_marker_i += 1
        ################################################################

plt.show()
################################################################