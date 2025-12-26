# Formula 1 Race Analysis

A comprehensive collection of Formula 1 2025 season race results, including qualifying and practice session data for all Grand Prix races.

*Here is the inspiration for the creation of this repository, a Formula 1 car displayed in John Dalton Building, Manchester Met.*
<p align="center">
<img src="https://github.com/ChuinHongYap/formula1_race_analysis/blob/main/images/f1_mmu.jpg" width="600" alt="F1 car in ManMet">
</p>

## Overview
This repository contains structured data for the 2025 F1 season, covering:
- **24 races** from Australia (31st March) to Abu Dhabi (7th December)
- **Race results** with final grid positions
- **Qualifying sessions** with starting grid positions
- **Practice sessions** (practice/1,	practice/2,	practice/3) where applicable
- **Sprint sessions** for sprint weekends (USA, Qatar, Brazil)
  
**Status Codes:**
- **DNF**: Did Not Finish
- **DNS**: Did Not Start
- **DQ**: Disqualified
- **NC**: No Classification / Did not participate
- **DSQ**: Disqualified after race

The repository is organised as below:
```text
.
├── codes/              # Main code
│   ├── analysis/       # Output analysis
│   └── races_all/      # Main data
├── images/             # Project images
├── requirements.txt    # Required packages
└── README.md           # Project overview
```

## Requirements

This project requires **Python 3.8+**. 

### Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Notes
### Sprint Weekends
Three races used the sprint format with only one practice session:
- **Chinese GP** (Shanghai)
- **Miami GP** (Miami)
- **Belgian GP** (Spa-Francorchamps)
- **United States GP** (COTA, Austin)
- **Brazil GP** (Interlagos, São Paulo)
- **Qatar GP** (Lusail)

**Note:** This repository captures the complete 2025 F1 season as of the Abu Dhabi Grand Prix finale. Data accuracy verified against official F1 timing and results sources.
