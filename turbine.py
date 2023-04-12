#variables

windSpeed = 12.29

bladeRadius = 3

operatingEfficiency = .10

A = 3.14159265 * pow(bladeRadius, 2) #blade area

p = 1.2 #density of air constant

PMax = 0.5 * p * A * pow(windSpeed, 3) #max power

P = PMax * operatingEfficiency #actual power

print("Maximum Turbine Power:", round(PMax, 2), "W")
print("Actual Turbine Power:", round(P, 2), "W")

#per capita energy consumption per year (J)

perCapEnergy = 2.57*(10**10)

print("Required energy:", perCapEnergy, "J")

#seconds in a year = 31,536,000

secondsPerYear = 31536000

#W = J/S therefore to find the amount of energy produced in a year to compare to energy consumption, we multiply by the number of seconds in a year
 
powerPerYear = P*secondsPerYear

print("Power produced per year:", round(powerPerYear, 2), "J")

#If power produced in a year is greater than energy consumption than you have enough turbines

if powerPerYear > perCapEnergy:
    print("Produced enough energy, 1 Turbine needed")
else:
    print("Need more turbines")
