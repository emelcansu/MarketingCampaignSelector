# Marketing Campaign Selector

## Overview

This project implements a dynamic programming-based solution to select marketing campaigns based on a given budget. The goal is to choose the set of campaigns that provides the highest return on investment (ROI) without exceeding the specified budget.

The problem is modeled as a variation of the 0/1 knapsack problem, where:
- The cost of each campaign corresponds to the "weight."
- The return on investment (ROI) corresponds to the "value."
- The budget acts as the "capacity" constraint.

## Features

- Maximizes ROI while staying within a budget limit.
- Uses dynamic programming to efficiently solve the problem.
- Supports flexible inputs for campaign costs and ROIs.
- Easily customizable to handle different numbers of campaigns and budget values.

## Usage

To use the algorithm, simply call the `select_marketing_campaigns` function, passing the following parameters:
- `budget`: The total budget available for selecting campaigns.
- `costs`: A list of costs for each campaign.
- `rois`: A list of ROIs corresponding to each campaign.

### Example Output
![image](https://github.com/user-attachments/assets/b4511425-5738-4ca9-b5e8-68d4a30b18d6)

### Example:

```python
budget = 10
costs = [3, 4, 5]
rois = [5, 6, 10]

marketing_campaign_result, selected_campaigns = select_marketing_campaigns(budget, costs, rois)

print("Max ROI:", marketing_campaign_result)
print("Selected Campaigns (Cost, ROI):", selected_campaigns)
