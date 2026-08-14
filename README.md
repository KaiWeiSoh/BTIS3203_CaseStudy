# Analysis of Industrial and Domestic Water Consumption in Malaysia

## Project Overview

This project analyzes water consumption patterns across Malaysian states from **2003 to 2022** using data obtained from **data.gov.my**. The study focuses on comparing **domestic** and **non-domestic** water usage, identifying industrial water demand trends, and evaluating industrial water intensity among Malaysian states.

The analysis was developed as part of the **BTIS3203 - Python for Data Science** course for the Bachelor of Software Engineering (Honours) programme.

---

## Research Questions

The project aims to answer the following questions:

1. What is the overall percentage distribution of water consumption between domestic and non-domestic sectors across Malaysia from 2003 to 2022?

2. What was the growth percentage of non-domestic water consumption from 2003 to 2022 in Malaysia's primary manufacturing states?

3. Which Malaysian state recorded the highest industrial water intensity in 2022 based on long-term non-domestic consumption trends?

---

## Dataset Information

### Dataset Source
- **Name:** Water Consumption by State and Sector
- **Provider:** data.gov.my
- **URL:** https://data.gov.my/data-catalogue/water_consumption

### Dataset Features

The dataset contains:

- Annual water consumption records
- Malaysian state-level data
- Domestic and non-domestic sector classifications
- Measurements in **Million Litres per Day (MLD)**
- Historical records from **2003–2022**

### Data Limitations

- Non-domestic consumption includes both industrial and commercial activities.
- Manufacturing-specific water usage is not separated from other commercial sectors.
- Analysis assumes non-domestic consumption as a proxy for industrial demand.

---

## Project Structure

```text
project/
│
├── water_consumption.csv
├── analysis.py
├── output/
│   ├── overall_distribution.png
│   ├── manufacturing_trend.png
│   └── industrial_intensity.png
│
├── README.md
└── report/
    └── CaseStudy_B230282C.docx
```

---

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Data Preparation

The following preprocessing steps were performed:

1. Load dataset using Pandas.
2. Convert date values into datetime format.
3. Extract year information.
4. Remove records where:
   ```python
   state == "Malaysia"
   ```
   to prevent duplication of national aggregate values.
5. Filter data based on sector requirements for each analysis.

---

## Analysis Methodology

### 1. Overall Water Consumption Distribution

A pie chart was generated to compare the cumulative water consumption between:

- Domestic sector
- Non-domestic sector

This provides an overall national perspective on water resource allocation.

---

### 2. Non-Domestic Consumption Growth in Manufacturing States

Three major industrial states were selected:

- Johor
- Selangor
- Pulau Pinang

A trend analysis was conducted using line charts.

Growth percentage was calculated using:

```text
Growth (%) =
((Value in 2022 - Value in 2003) / Value in 2003) × 100
```

---

### 3. Industrial Water Intensity Analysis

For 2022 data:

```text
Industrial Intensity Ratio =
Non-Domestic Consumption /
Domestic Consumption
```

This ratio was used to identify states experiencing relatively higher industrial pressure on water resources.

---

## Key Findings

### Finding 1: Overall Distribution

- Domestic Consumption: **62.8%**
- Non-Domestic Consumption: **37.2%**

Domestic users consume the majority of Malaysia's water resources, but non-domestic consumption remains substantial and represents more than one-third of total usage.

---

### Finding 2: Manufacturing States Growth (2003–2022)

| State | Growth (%) |
|---------|---------:|
| Johor | 117.89% |
| Selangor | 100.59% |
| Pulau Pinang | 42.13% |

Key observation:

- Johor recorded the highest increase in non-domestic water consumption.
- Selangor also experienced substantial industrial expansion.
- Pulau Pinang showed moderate growth compared with the other manufacturing states.

---

### Finding 3: Industrial Water Intensity

The analysis identified:

**W.P. Labuan** as the state with the highest industrial water intensity ratio in 2022.

This suggests a relatively stronger dependence on non-domestic water consumption compared to domestic demand.

---

## Recommendations

### Ministry of Investment, Trade and Industry (MITI)

- Provide incentives for water-efficient industrial technologies.
- Support implementation of greywater reuse systems.
- Encourage sustainable manufacturing practices.

### National Water Services Commission (SPAN)

- Monitor high-consumption industrial regions.
- Introduce water recycling mandates for large manufacturers.
- Strengthen industrial water efficiency regulations.

### State Water Operators (PBAPP and Others)

- Implement tiered tariffs for excessive industrial consumption.
- Promote industrial water conservation programs.
- Enhance monitoring of high-usage facilities.

---

## How to Run

### Install Dependencies

```bash
pip install pandas matplotlib seaborn numpy
```

### Execute Analysis

```bash
python analysis.py
```

### Expected Outputs

The program should generate:

- Pie Chart: Water Consumption Distribution
- Line Chart: Manufacturing State Trends
- Bar Chart: Industrial Water Intensity Ratio

---

## References

1. Government of Malaysia. Water Consumption by State and Sector. https://data.gov.my/data-catalogue/water_consumption

2. Ministry of Investment, Trade and Industry (MITI). https://www.miti.gov.my

3. National Water Services Commission (SPAN). https://www.span.gov.my

4. Perbadanan Bekalan Air Pulau Pinang (PBAPP). https://pba.com.my

---

## Author

**Soh Kai Wei**  
Bachelor of Software Engineering (Honours)  
Subject: BTIS3203 – Python for Data Science  
Student ID: B230282C
