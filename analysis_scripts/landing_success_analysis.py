import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

######################## USER INPUT ###########################
#### REPLACE folder with name of directory containing jump_trial_data
folder = "C:/jump_trial_data"
landing_filename = "/landing-success-data/landing_assessment.csv"
landing_filepath = folder + landing_filename
###############################################################

#### LOAD landing data
# Landing is NOT successful if there is rolling / pinwheeling or bouncing with contact lost OR if the planthopper impacts the ground with its body and not its legs first
landing_data = pd.read_csv(landing_filepath)

#### FILTER data
# ONLY assess jumps with YES or NO landing assessment
landing_data_modified = landing_data[landing_data['landing_successful'].isin(['YES', 'NO'])]

#### Seperate out WAX INTACT (wax_status = ON) and WAX REMOVED (wax_status = OFF)
wax_on = landing_data_modified[landing_data_modified['wax_status'] == 'ON']
wax_off = landing_data_modified[landing_data_modified['wax_status'] == 'OFF']

#### Seperate out landing assessment (REMOVE, UNABLE TO DETERMINE, UNKNOWN)
wax_on_remove = (wax_on['landing_successful'] == 'REMOVE').sum()
wax_off_remove = (wax_off['landing_successful'] == 'REMOVE').sum()

wax_on_UTD = (wax_on['landing_successful'] == 'UNABLE TO DETERMINE').sum()
wax_off_UTD = (wax_off['landing_successful'] == 'UNABLE TO DETERMINE').sum()

wax_on_unknown = (wax_on['landing_successful'] == 'UNKNOWN').sum()
wax_off_unknown = (wax_off['landing_successful'] == 'UNKNOWN').sum()


##################### CALCULATE SUCCESS RATE #######################
#### COUNT successful landings in each group
successful_wax_on = (wax_on['landing_successful'] == 'YES').sum()
successful_wax_off = (wax_off['landing_successful'] == 'YES').sum()

print("successful_wax_on = ", successful_wax_on)
print("successful_wax_off = ", successful_wax_off)

#### COUNT number of trials
num_trials_wax_on = len(wax_on)
num_trials_wax_off = len(wax_off)

print("num_trials_wax_on = ", num_trials_wax_on)
print("num_trials_wax_off = ", num_trials_wax_off)

#### CALCULATE success ratio
success_rate_wax_on = successful_wax_on / num_trials_wax_on
success_rate_wax_off = successful_wax_off / num_trials_wax_off

#### CONVERT to percentages
success_per_wax_on = success_rate_wax_on * 100
success_per_wax_off = success_rate_wax_off * 100
###############################################################

##################### CALCULATE STATISTICS ###########################
#### CALCULATE the standard error for each group
error_wax_on = ((success_rate_wax_on * (1 - success_rate_wax_on) / num_trials_wax_on)**0.5)
error_wax_off = ((success_rate_wax_off * (1 - success_rate_wax_off) / num_trials_wax_off)**0.5)

error_per_wax_on = error_wax_on * 100
error_per_wax_off = error_wax_off * 100

#### COMPUTE Chi-squared test

unsuccessful_wax_on = num_trials_wax_on - successful_wax_on
unsuccessful_wax_off = num_trials_wax_off - successful_wax_off
chi_table = [[successful_wax_on, unsuccessful_wax_on], [successful_wax_off, unsuccessful_wax_off]]

stat, p, dof, expected = chi2_contingency(chi_table)

#### PRINT values
print("Success Rate (Wax Intact) %:", success_per_wax_on)
print("Error (Wax Intact) %:", error_per_wax_on)
print("Success Rate (Wax Removed):", success_per_wax_off)
print("Error (Wax Removed):", error_per_wax_off)
print("Chi-squared test statistic:", stat)
print("P-value:", p)
print("Number of trials (Wax Intact):", num_trials_wax_on)
print("Number of trials (Wax Removed):", num_trials_wax_off)
###############################################################

###############################################################
#### PLOT the success rates
# Plot settings
colors = sns.color_palette("colorblind", 6)
colors_new = [colors[1], colors[0]]

# Pie graphs
success_rate_wax_on = [success_per_wax_on, 100 - success_per_wax_on]
success_rate_wax_off = [success_per_wax_off, 100 - success_per_wax_off]

# wax intact
fig1, ax1 = plt.subplots(1, 1, figsize=(14, 7))
ax1.pie(success_rate_wax_on, startangle=90, explode=(0.1, 0), colors=colors_new, labels=['Successful', 'Unsuccessful'], autopct='%1.1f%%')
ax1.axis('equal')
ax1.set_title('WAX INTACT LANDING SUCCESS', color='black')
fig1.tight_layout()

# wax removed
fig2, ax2 = plt.subplots(1, 1, figsize=(14, 7))
ax2.pie(success_rate_wax_off, startangle=90, explode=(0.1, 0), colors=colors_new, labels=['Successful', 'Unsuccessful'], autopct='%1.1f%%')
ax2.axis('equal')
ax2.set_title('WAX REMOVED LANDING SUCCESS', color='black')
fig2.tight_layout()

plt.show()
###############################################################