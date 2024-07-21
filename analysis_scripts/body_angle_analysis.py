import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter
from scipy import stats
import seaborn as sns

# import the configuration script
import PH_config_file

#### SET colors for wax intact and wax removed
colors = sns.color_palette("colorblind", 2)

##################### USER INPUT #########################
### UNCOMMENT color, axes ranges, and trial lists to run analysis

######################################
# PAIRED DATA - WAX INTACT
color_waxstatus = colors[1]

# Define y-ticks for each plot
yticks_ang = np.array([-1, -1 / 2, 0, 1 / 2, 1])
yticks_vel = np.array([-70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80])

trials = [
    'UPLB14-1',
    'UPLB14-3',
    'UPLB14-4',
    'UPLB14-6',
]
######################################

# ###################################
# # PAIRED DATA - WAX REMOVED
# color_waxstatus = colors[0]
#
# # Define y-ticks for each plot
# yticks_ang = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# yticks_vel = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
#
# trials = [
#     'UPLB14-8_nowax',
#     'UPLB14-10_nowax',
#     'UPLB14-11_nowax',
#     'UPLB14-13_nowax',
# ]
# #####################################

# #####################################
# # UNPAIRED DATA - WAX INTACT
# color_waxstatus = colors[1]
#
# # Define y-ticks for each plot
# yticks_ang = np.array([-1, -1 / 2, 0, 1 / 2, 1])
# yticks_vel = np.array([-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
#
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
# color_waxstatus = colors[0]
#
# # Define y-ticks for each plot
# yticks_ang = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
# yticks_vel = np.array([-160, -140,  -120, -100,  -80, -60,-40, -20, 0,  20,  40,  60,  80, 100,  120,  140,  160,  180])
#
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
###############################################################

#### INITIALIZE lists for averaging data
all_interpolated_angles_Y = []
all_interpolated_angular_vel_Y = []
all_interpolated_angles_N = []
all_interpolated_angular_vel_N = []

#### CREATE time linespace for collective data plot
time_common = np.linspace(0, 1, num=500)

#### INITIALIZE plots outside loop
fig1, ax1 = plt.subplots(figsize=(10, 6))
fig2, ax2 = plt.subplots(figsize=(10, 6))

#### SET plot styles
# plot colors
colors_trials = sns.color_palette("husl", 4)
line_styles = ['-', '--', '-.', ':']
num_styles = len(line_styles)

#################### LOOP OVER TRIALS ########################
for trial in trials:
    trial_name = trial
    trial_config = PH_config_file.load_trial_config(trial_name)
    print('\n')
    print(trial_name)

    #### LOAD in data and values from config file
    if trial_config is not None:
        bodypt_filepath = trial_config.get("DLT_data_filepath")
        frame_rate = trial_config.get('frame_rate')
        pixperm = trial_config.get("pixperm")
        wax_status = trial_config.get("wax_status")
        start_frame = trial_config.get('first_move_frame') - 1  # one frame before the first movement frame
        end_frame = trial_config.get('stop_tracking_frame')

        #### LOAD in body point data from DLT tracking
        body_data = pd.read_csv(bodypt_filepath)

        #### SET frame number
        body_data['frame_num'] = body_data.index


        #### CONVERT pix to meters and INVERT Y values
        # Head
        body_data['pt1_cam1_X'] = body_data['pt1_cam1_X'] / pixperm
        body_data['pt1_cam1_Y'] = body_data['pt1_cam1_Y'] / pixperm
        body_data['pt1_cam1_Y'] = -body_data['pt1_cam1_Y']
        # Thorax/Abdomen Junction
        body_data['pt2_cam1_X'] = body_data['pt2_cam1_X'] / pixperm
        body_data['pt2_cam1_Y'] = body_data['pt2_cam1_Y'] / pixperm
        body_data['pt2_cam1_Y'] = -body_data['pt2_cam1_Y']

        #### CROP data to start and end frames and reset index
        body_data = body_data.loc[start_frame:(end_frame + 1)].reset_index(drop=True)

        #### SET index number
        body_data['index_num'] = body_data.index


        #### MIRROR data to depict jump from left to right if needed
        # check direction
        if body_data.loc[body_data.index[-1], 'pt1_cam1_X'] < body_data.loc[body_data.index[0], 'pt1_cam1_X']:
            image_width = 1024 / pixperm # image width for Photron videos is 1024 pixels

            # Flip x-values to mirror the data horizontally
            body_data['pt1_cam1_X'] = image_width - body_data['pt1_cam1_X']
            body_data['pt2_cam1_X'] = image_width - body_data['pt2_cam1_X']
            body_data['pt3_cam1_X'] = image_width - body_data['pt3_cam1_X']
            print('Jump is from right to left --- MIRRORING centroid x-position data')


        #### ADD time column
        body_data['time_s'] = body_data['index_num'] / frame_rate

        #### COPY data to modify
        body_data_modified = body_data.copy()

        # INITIALIZE body x,y values off of manually tracked centroid x,y value at start
        first_value_x = body_data_modified.loc[0, 'pt3_cam1_X']
        first_value_y = body_data_modified.loc[0, 'pt3_cam1_Y']

        # head - use centroid initial x, y as 0,0
        body_data_modified['pt1_cam1_X'] -= first_value_x
        body_data_modified['pt1_cam1_Y'] -= first_value_y
        # distal thorax - use centroid initial x, y as 0,0
        body_data_modified['pt2_cam1_X'] -= first_value_x
        body_data_modified['pt2_cam1_Y'] -= first_value_y


        #### SMOOTH body position data --- Savitzky–Golay filter (window size = 15, polynomial order = 2)
        smooth_window = 15
        poly_order = 2

        body_data_modified['pt1_cam1_X_smooth'] = savgol_filter(body_data_modified['pt1_cam1_X'], smooth_window, poly_order, mode='nearest')
        body_data_modified['pt1_cam1_Y_smooth'] = savgol_filter(body_data_modified['pt1_cam1_Y'], smooth_window, poly_order, mode='nearest')

        body_data_modified['pt2_cam1_X_smooth'] = savgol_filter(body_data_modified['pt2_cam1_X'], smooth_window, poly_order, mode='nearest')
        body_data_modified['pt2_cam1_Y_smooth'] = savgol_filter(body_data_modified['pt2_cam1_Y'], smooth_window, poly_order, mode='nearest')


        #################### CALCULATE BODY ANGLE + CUMULATIVE BODY ANGLE ########################
        #### CALCULATE raw body angle (-pi to pi)
        body_data_modified['body_angle_rad'] = np.arctan2(body_data_modified['pt1_cam1_Y_smooth'] - body_data_modified['pt2_cam1_Y_smooth'], body_data_modified['pt1_cam1_X_smooth'] - body_data_modified['pt2_cam1_X_smooth'])

        #### UNWRAP angle to remove -pi to pi jump
        body_data_modified['unwrapped_angle_rad'] = np.unwrap(body_data_modified['body_angle_rad'])

        #### SMOOTH unwrapped body angle --- Savitzky–Golay filter (window size = 31, polynomial order = 2)
        smooth_window = 31  # Choose an odd number greater than the polynomial order
        poly_order = 2

        body_data_modified['unwrapped_angle_rad_smooth'] = savgol_filter(body_data_modified['unwrapped_angle_rad'], smooth_window, poly_order, mode='nearest')

        #### CALCULATE change in body angle (radians) -- use this to calculate angular velocity later
        body_data_modified['angle_diff_rad'] = body_data_modified['unwrapped_angle_rad_smooth'].diff()

        #### SET intial difference to 0
        body_data_modified.loc[0, 'angle_diff_rad'] = 0

        #### CALCULATE cumulative change in body angle
        body_data_modified['cumulative_angle_rad'] = body_data_modified['angle_diff_rad'].cumsum()

        #### SMOOTH cumulative body angle --- Savitzky–Golay filter (window size = 5, polynomial order = 2)
        smooth_window = 5
        poly_order = 2

        body_data_modified['cumulative_angle_rad_smooth'] = savgol_filter(body_data_modified['cumulative_angle_rad'], smooth_window, poly_order, mode='nearest')

        #### SET the first value of the smoothed data to 0
        first_index = body_data_modified.index[0]  # Get the first index
        body_data_modified.loc[first_index, 'cumulative_angle_rad_smooth'] = 0
        ###############################################################


        ####################### CALCULATE NRR ########################

        #### CALCUALTE range of cumulative body angle changes
        angle_change_range = body_data_modified['cumulative_angle_rad_smooth'].max() - body_data_modified['cumulative_angle_rad_smooth'].min()

        #### PRINT NRR
        print(f"Normalized Rotation Range (rot/jump) = {angle_change_range / (2 * np.pi)}")
        ###############################################################


        ################# CALCULATE T_Stabilize ####################
        # Stabilization threshold values
        threshold = 0.1 # radians
        window_stabilize = 25 # frames

        #### CALCUALTE rolling standard deviation
        rolling_std_body_angle = body_data_modified['cumulative_angle_rad_smooth'].rolling(window=window_stabilize).std()

        #### SELECT for SD when value is below threshold for specified number of frames
        stabilized_body_angle = (rolling_std_body_angle < threshold).rolling(window=window_stabilize).sum() == window_stabilize

        #### APPLY index of first instance to time
        if stabilized_body_angle.any():
            T_stabilize_body_angle = body_data_modified['time_s'][stabilized_body_angle.idxmax()]
        else:
            T_stabilize_body_angle = None

        #### PRINT T_stabilize time
        print('T_stabilize = ', T_stabilize_body_angle, 's')
        ###############################################################


        ################# CALCULATE ANGULAR VELOCITY ####################
        body_data_modified['dt'] = body_data_modified['time_s'].diff()
        body_data_modified.loc[0, 'dt'] = 1 / frame_rate

        body_data_modified['angular_vel_rad_per_s'] = body_data_modified['angle_diff_rad'] / body_data_modified['dt']


        frame_5ms = int(0.005 * frame_rate)

        # At takeoff
        max_abs_vel_index = body_data_modified.loc[:frame_5ms, 'angular_vel_rad_per_s'].abs().idxmax()
        max_angular_velocity = body_data_modified.loc[max_abs_vel_index, 'angular_vel_rad_per_s']

        # At apex:
        apex_index = body_data_modified['pt2_cam1_Y'].idxmax()
        max_abs_vel_index_apex = body_data_modified.loc[apex_index - int(frame_5ms/2):apex_index + int(frame_5ms/2), 'angular_vel_rad_per_s'].abs().idxmax()
        max_angular_velocity_apex = body_data_modified.loc[max_abs_vel_index_apex, 'angular_vel_rad_per_s']

        # At landing
        last_index = body_data_modified.index[-1]
        max_abs_vel_index_landing = body_data_modified.loc[(last_index - frame_5ms)::, 'angular_vel_rad_per_s'].abs().idxmax()
        max_angular_velocity_landing = body_data_modified.loc[max_abs_vel_index_landing, 'angular_vel_rad_per_s']


        #### PRINT angular velcoity values at takeoff, apex, and landing
        print(f"Max absolute angular velocity at takeoff max (within 5ms after start): {max_angular_velocity} rad/s")
        print(f"Max absolute angular velocity at 5ms around apex: {max_angular_velocity_apex} rad/s")
        print(f"Max absolute angular velocity at 5ms from landing to landing: {max_angular_velocity_landing} rad/s")
        ###############################################################
        

        ############## DATA FOR AVERAGING AND PLOTTING ##################

        #### CALCULATE jump duration time
        jump_duration = (end_frame - start_frame + 1) / frame_rate
        
        #### NORMALIZE time
        body_data_modified['time_normalized'] = body_data_modified['time_s'] / jump_duration

        #### INTERPOLATE cumulative body angel values to match common time space
        interpolated_angles = np.interp(time_common, body_data_modified['time_normalized'], body_data_modified['cumulative_angle_rad_smooth'])

        #### INTERPOLATE angular velocity values to match common time space
        interpolated_angular_vel = np.interp(time_common, body_data_modified['time_normalized'], body_data_modified['angular_vel_rad_per_s'])

        #### APPEND to lists
        if wax_status == 'Y':
            all_interpolated_angles_Y.append(interpolated_angles)
            all_interpolated_angular_vel_Y.append(interpolated_angular_vel)
        else:
            all_interpolated_angles_N.append(interpolated_angles)
            all_interpolated_angular_vel_N.append(interpolated_angular_vel)
        ###############################################################
        ###############################################################

# PLOT wax intact cumulative body angle
for idx, interpolated_angles in enumerate(all_interpolated_angles_Y):
    ax1.plot(time_common, interpolated_angles / np.pi, label=f'Trial {trials[idx]}',
             color=colors_trials[idx % len(colors_trials)],
             linestyle=line_styles[idx // len(colors_trials) % num_styles],
             alpha=0.2)

# PLOT wax removed cumulative body angle
for idx, interpolated_angles in enumerate(all_interpolated_angles_N):
    ax1.plot(time_common, interpolated_angles / np.pi, label=f'Trial {trials[idx]}',
             color=colors_trials[idx % len(colors_trials)],
             linestyle=line_styles[idx // len(colors_trials) % num_styles],
             alpha=0.2)

# CALCULATE and PLOT average cumulative body angle and SD for wax intact
if all_interpolated_angles_Y:
    mean_trajectory_angles_Y = np.mean(all_interpolated_angles_Y, axis=0)
    std_deviation_angles_Y = np.std(all_interpolated_angles_Y, axis=0)
    ax1.plot(time_common, mean_trajectory_angles_Y / np.pi, label='Average Trajectory (WAX INTACT)', color=colors[1])
    ax1.fill_between(time_common, (mean_trajectory_angles_Y - std_deviation_angles_Y) / np.pi, (mean_trajectory_angles_Y + std_deviation_angles_Y) / np.pi, alpha=0.4, color=colors[1])

# CALCULATE and PLOT average cumulative body angle and SD for wax removed
if all_interpolated_angles_N:
    mean_trajectory_angles_N = np.mean(all_interpolated_angles_N, axis=0)
    std_deviation_angles_N = np.std(all_interpolated_angles_N, axis=0)
    ax1.plot(time_common, mean_trajectory_angles_N / np.pi, label='Average Trajectory (WAX REMOVED)', color=colors[0])
    ax1.fill_between(time_common, (mean_trajectory_angles_N - std_deviation_angles_N) / np.pi, (mean_trajectory_angles_N + std_deviation_angles_N) / np.pi, alpha=0.4, color=colors[0])

# Set labels and titles for ax1
ax1.set_title('Cumulative Body Angle vs. Time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Cumulative Body Angle (rad)')
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.set_yticks(yticks_ang)
ax1.set_yticklabels([f'{y}π' for y in yticks_ang])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.legend()


# PLOT wax intact angular velocity
for idx, interpolated_angular_vel in enumerate(all_interpolated_angular_vel_Y):
    color = colors_trials[idx % len(colors_trials)]
    linestyle = line_styles[idx // len(colors_trials) % num_styles]
    ax2.plot(time_common, interpolated_angular_vel / np.pi, label=f'Trial {trials[idx]}', color=color, linestyle=linestyle, alpha=0.2)

# PLOT wax removed angular velocity
for idx, interpolated_angular_vel in enumerate(all_interpolated_angular_vel_N):
    color = colors_trials[idx % len(colors_trials)]
    linestyle = line_styles[idx // len(colors_trials) % num_styles]
    ax2.plot(time_common, interpolated_angular_vel / np.pi, label=f'Trial {trials[idx]}', color=color,
             linestyle=linestyle, alpha=0.2)


# CALCULATE and PLOT average angular velocity and SD for wax intact
if all_interpolated_angular_vel_Y:
    mean_trajectory_vel_Y = np.mean(all_interpolated_angular_vel_Y, axis=0)
    std_deviation_vel_Y = np.std(all_interpolated_angular_vel_Y, axis=0)
    ax2.plot(time_common, mean_trajectory_vel_Y / np.pi, label='Average Angular Velocity (WAX INTACT)', color=colors[1])
    ax2.fill_between(time_common, (mean_trajectory_vel_Y - std_deviation_vel_Y) / np.pi,
                         (mean_trajectory_vel_Y + std_deviation_vel_Y) / np.pi, alpha=0.4, color=colors[1])

# CALCULATE and PLOT average angular velocity and SD for wax removed
if all_interpolated_angular_vel_N:
    mean_trajectory_vel_N = np.mean(all_interpolated_angular_vel_N, axis=0)
    std_deviation_vel_N = np.std(all_interpolated_angular_vel_N, axis=0)
    ax2.plot(time_common, mean_trajectory_vel_N / np.pi, label='Average Angular Velocity (WAX REMOVED)', color=colors[0])
    ax2.fill_between(time_common, (mean_trajectory_vel_N - std_deviation_vel_N) / np.pi,
                    (mean_trajectory_vel_N + std_deviation_vel_N) / np.pi, alpha=0.4, color=colors[0])


ax2.axhline(y=0, color='black', linestyle='--', label='y = 0', alpha=0.4)
ax2.set_title('Angular Velocity vs. Time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Angular Velocity (rad/s)')
ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.set_yticks(yticks_vel)
ax2.set_yticklabels([f'{y}π' for y in yticks_vel])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.legend()

plt.show()
###############################################################