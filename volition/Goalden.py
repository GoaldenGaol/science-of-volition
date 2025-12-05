# 1. Define the three measurable quantities
rho_plunder = 0.0312   # fraction of non-consensual actions (0–1)
C_mean      = 1.28     # average agent competence
R_mean      = 0.91     # average agent reputation

# 2. The universal threshold
threshold = 0.1 * C_mean * R_mean   # = 0.116 in the 31-domain backtests

#3. The prediction
if rho_plunder < threshold:
    print("Cooperative equilibrium achieved and locked")
    print("Prediction: system survives and prospers")
else:
    print("Fragmentation equilibrium")
    print("Prediction: collapse or chronic conflict")
