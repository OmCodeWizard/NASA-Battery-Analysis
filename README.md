# NASA-Battery-Analysis
This repository contains code for analyzing battery data from NASA's battery testing dataset. The analysis involves processing battery impedance, electrolyte resistance, and charge transfer resistance across charge/discharge cycles to track the aging and performance of various batteries.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Results](#results)
- [License](#license)

## Overview

The code processes raw battery data and metadata to:
1. Clean and handle missing values in battery test data.
2. Calculate relevant metrics (Battery Impedance, Electrolyte Resistance `Re`, Charge Transfer Resistance `Rct`).
3. Visualize the trends of battery performance over time using interactive plots (Battery Impedance vs. Aging, Electrolyte Resistance vs. Aging, Charge Transfer Resistance vs. Aging).

The visualizations are created using Plotly to provide interactive insights into the battery aging process across multiple test cycles.

## Requirements

The following Python libraries are required for this project:
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **plotly**: For interactive visualizations.

You can install the required libraries using the following command:

```bash
pip install pandas numpy plotly
