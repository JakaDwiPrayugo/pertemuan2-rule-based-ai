import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

x_age = np.arange(0, 101, 1)
x_blood_pressure = np.arange(0, 221, 1)
x_cholesterol = np.arange(100, 251, 1)
x_blood_sugar = np.arange(0, 121, 1)
x_hdl = np.arange(0, 71, 1)
x_ldl = np.arange(0, 191, 1)
y_risk = np.arange(0, 46, 1)

# print range dan batas metric setiap data
print(f"age from {x_age[0]} to {x_age[-1]}")
print(f"blood pressure from {x_blood_pressure[0]} to {x_blood_pressure[-1]}")
print(f"cholesterol from {x_cholesterol[0]} to {x_cholesterol[-1]}")
print(f"blood sugar from {x_blood_sugar[0]} to {x_blood_sugar[-1]}")
print(f"hdl from {x_hdl[0]} to {x_hdl[-1]}")
print(f"ldl from {x_ldl[0]} to {x_ldl[-1]}")
print(f"risk from {y_risk[0]} to {y_risk[-1]}")

# Input Condition Range
input_age = float(input("Enter age (0-100): "))
input_blood_pressure = float(input("Enter blood pressure (0-220): "))
input_cholesterol = float(input("Enter cholesterol (100-250): "))
input_blood_sugar = float(input("Enter blood sugar (0-120): "))
input_ldl = float(input("Enter LDL cholesterol (0-190): "))
input_hdl = float(input("Enter HDL cholesterol (0-70): "))

# Inisiasi
age_young = mf.trapmf(x_age, [0, 0, 30, 40])
age_mid = mf.trapmf(x_age, [30, 40, 50, 60])
age_old = mf.trapmf(x_age, [50, 60, 100, 100])

blood_pressure_low = mf.trapmf(x_blood_pressure, [-30, -5, 100, 120])
blood_pressure_mid = mf.trapmf(x_blood_pressure, [100, 120, 140, 160])
blood_pressure_high = mf.trapmf(x_blood_pressure, [140, 160, 180, 200])
blood_pressure_very_high = mf.trapmf(x_blood_pressure, [180, 200, 220, 220])

cholesterol_low = mf.trapmf(x_cholesterol, [-30, -5, 180, 200])
cholesterol_mid = mf.trapmf(x_cholesterol, [180, 200, 220, 240])
cholesterol_high = mf.trapmf(x_cholesterol, [220, 240, 250, 270])

blood_sugar_very_high = mf.trimf(x_blood_sugar, [90, 120, 130])

ldl_normal = mf.trimf(x_ldl, [0, 100, 100])
ldl_limit = mf.trimf(x_ldl, [100, 130, 160])
ldl_high = mf.trimf(x_ldl, [130, 160, 190])
ldl_very_high = mf.trapmf(x_ldl, [160, 190, 200, 200])

# Fuzzyfikasi
age_fit_young = fuzz.interp_membership(x_age, age_young, input_age)
age_fit_mid = fuzz.interp_membership(x_age, age_mid, input_age)
age_fit_old = fuzz.interp_membership(x_age, age_old, input_age)

blood_pressure_fit_low = fuzz.interp_membership(x_blood_pressure, blood_pressure_low, input_blood_pressure)
blood_pressure_fit_mid = fuzz.interp_membership(x_blood_pressure, blood_pressure_mid, input_blood_pressure)
blood_pressure_fit_high = fuzz.interp_membership(x_blood_pressure, blood_pressure_high, input_blood_pressure)
blood_pressure_fit_very_high = fuzz.interp_membership(x_blood_pressure, blood_pressure_very_high, input_blood_pressure)

cholesterol_fit_low = fuzz.interp_membership(x_cholesterol, cholesterol_low, input_cholesterol)
cholesterol_fit_mid = fuzz.interp_membership(x_cholesterol, cholesterol_mid, input_cholesterol)
cholesterol_fit_high = fuzz.interp_membership(x_cholesterol, cholesterol_high, input_cholesterol)

blood_sugar_fit_very_high = fuzz.interp_membership(x_blood_sugar, blood_sugar_very_high, input_blood_sugar)

ldl_fit_normal = fuzz.interp_membership(x_ldl, ldl_normal, input_ldl)
ldl_fit_limit = fuzz.interp_membership(x_ldl, ldl_limit, input_ldl)
ldl_fit_high = fuzz.interp_membership(x_ldl, ldl_high, input_ldl)
ldl_fit_very_high = fuzz.interp_membership(x_ldl, ldl_very_high, input_ldl)

# Rule
risk_not = np.arange(0, 46, 1)
risk_little = np.arange(0, 46, 1)
risk_mid = np.arange(0, 46, 1)
risk_high = np.arange(0, 46, 1)
risk_very_high = np.arange(0, 46, 1)

rule1 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_low, cholesterol_fit_low), ldl_fit_normal), ldl_fit_high), risk_not)
rule2 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_low, cholesterol_fit_low), ldl_fit_limit), ldl_fit_high), risk_little)
rule3 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_low, cholesterol_fit_low), ldl_fit_high), ldl_fit_high), risk_mid)
rule4 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_low, cholesterol_fit_low), ldl_fit_very_high), ldl_fit_high), risk_high)
rule5 = np.fmin(np.fmin(np.fmin(blood_pressure_fit_mid, cholesterol_fit_low), ldl_fit_high), risk_not)

rule6 = np.fmin(np.fmin(np.fmin(age_fit_young, blood_pressure_fit_mid), cholesterol_fit_mid), risk_not)
rule7 = np.fmin(np.fmin(np.fmin(age_fit_mid, blood_pressure_fit_mid), cholesterol_fit_mid), risk_not)
rule8 = np.fmin(np.fmin(np.fmin(age_fit_old, blood_pressure_fit_mid), cholesterol_fit_mid), risk_not)
rule9 = np.fmin(np.fmin(np.fmin(age_fit_young, blood_pressure_fit_high), cholesterol_fit_high), risk_mid)
rule10 = np.fmin(np.fmin(np.fmin(age_fit_mid, blood_pressure_fit_high), cholesterol_fit_high), risk_high)
rule11 = np.fmin(np.fmin(np.fmin(age_fit_old, blood_pressure_fit_high), cholesterol_fit_high), risk_very_high)

rule12 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, blood_pressure_fit_mid), cholesterol_fit_low), ldl_fit_normal), ldl_fit_high), risk_not)
rule13 = np.fmin(np.fmin(age_fit_young, blood_sugar_fit_very_high), risk_little)
rule14 = np.fmin(np.fmin(age_fit_mid, blood_sugar_fit_very_high), risk_high)
rule15 = np.fmin(np.fmin(age_fit_old, blood_sugar_fit_very_high), risk_very_high)
rule16 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, blood_pressure_fit_low), cholesterol_fit_low), blood_sugar_fit_very_high), ldl_fit_normal), ldl_fit_high), risk_little)
rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, blood_pressure_fit_low), cholesterol_fit_low), blood_sugar_fit_very_high), ldl_fit_normal), ldl_fit_high), risk_high)
rule18 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_old, blood_pressure_fit_low), cholesterol_fit_low), blood_sugar_fit_very_high), ldl_fit_normal), ldl_fit_high), risk_very_high)
rule19 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, blood_pressure_fit_low), cholesterol_fit_low), blood_sugar_fit_very_high), ldl_fit_very_high), ldl_fit_high), risk_very_high)

rule20 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_very_high, cholesterol_fit_high), ldl_fit_very_high), ldl_fit_high), risk_very_high)
rule21 = np.fmin(np.fmin(np.fmin(np.fmin(blood_pressure_fit_high, cholesterol_fit_high), ldl_fit_high), ldl_fit_limit), risk_very_high)
rule22 = np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, blood_pressure_fit_very_high), cholesterol_fit_high), np.fmin(ldl_fit_very_high, age_fit_mid)), risk_mid)

rule23 = np.fmin(np.fmin(age_fit_mid, blood_pressure_fit_very_high), risk_very_high)
rule24 = np.fmin(np.fmin(age_fit_old, blood_pressure_fit_very_high), risk_very_high)

# Defuzzyfikasi
out_risk = np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule2), rule3), rule4), rule5,
                   np.fmax(np.fmax(np.fmax(np.fmax(rule6, rule7), rule8), rule9), rule10,
                           np.fmax(np.fmax(np.fmax(np.fmax(rule11, rule12), rule13), rule14), rule15,
                                   np.fmax(np.fmax(np.fmax(np.fmax(rule16, rule17), rule18), rule19), rule20,
                                           np.fmax.reduce([rule21, rule22, rule23, rule24])))))


defuzzified = fuzz.defuzz(y_risk, out_risk, 'mom')
result = fuzz.interp_membership(y_risk, out_risk, defuzzified)
print("Coroner Heart Diagnosis:", defuzzified)

def diagnosed_as(output):
    if np.sum(output):
        return fuzz.defuzz(y_risk, output, 'centroid')
    else:
        return 0

if defuzzified >= 0 and defuzzified < 5:
    print("Diagnosed as Not Risk")

if 5 <= defuzzified < 10 and diagnosed_as(rule1) > diagnosed_as(rule2):
    print("Diagnosed as Not Risk")

if 5 <= defuzzified < 10 and diagnosed_as(rule1) < diagnosed_as(rule2):
    print("Diagnosed as Little Risk")

if 10 <= defuzzified < 15:
    print("Diagnosed as Little Risk")

if 15 <= defuzzified < 20 and diagnosed_as(rule2) > diagnosed_as(rule3):
    print("Diagnosed as Little Risk")

if 15 <= defuzzified < 20 and diagnosed_as(rule2) < diagnosed_as(rule3):
    print("Diagnosed as Middle Risk")

if 20 <= defuzzified < 25:
    print("Diagnosed as Middle Risk")

if 25 <= defuzzified < 30 and diagnosed_as(rule3) > diagnosed_as(rule4):
    print("Diagnosed as Middle Risk")

if 25 <= defuzzified < 30 and diagnosed_as(rule3) < diagnosed_as(rule4):
    print("Diagnosed as High Risk")

if 30 <= defuzzified < 35:
    print("Diagnosed as High Risk")

if 35 <= defuzzified < 40 and diagnosed_as(rule4) > diagnosed_as(rule5):
    print("Diagnosed as High Risk")

if 40 <= defuzzified < 50:
    print("Diagnosed as Very High Risk")

if 35 <= defuzzified < 40 and diagnosed_as(rule4) < diagnosed_as(rule5):
    print("Diagnosed as Very High Risk")
