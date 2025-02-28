# Data-Science-Projects
# Solar Power Generation Prediction

## Objective
This is a regression project where the goal is to model energy production as a function of environmental variables.

## Dataset Description
The dataset is provided in `solarpowergeneration.csv`, consisting of **10 variables** and **2920 instances**. The variables are:

- **distance_to_solar_noon**: Distance to solar noon (in radians).
- **temperature**: Daily average temperature (in °C).
- **wind_direction**: Daily average wind direction (in degrees, 0-360).
- **wind_speed**: Daily average wind speed (in m/s).
- **sky_cover**: Cloud coverage on a scale from 0 (clear) to 4 (fully covered).
- **visibility**: Visibility in kilometers.
- **humidity**: Humidity percentage.
- **average_wind_speed**: Wind speed average over 3 hours (in m/s).
- **average_pressure**: Barometric pressure over 3 hours (in mercury inches).
- **power_generated (Target)**: Energy production in Joules for every 3 hours.

## Project Overview
This project aims to build a regression model to predict **power_generated** based on environmental factors.

## Repository Structure
- `data/` - Contains the dataset (`solarpowergeneration.csv`).
- `notebooks/` - Jupyter notebooks for data exploration and model training.
- `README.md` - Project documentation.

