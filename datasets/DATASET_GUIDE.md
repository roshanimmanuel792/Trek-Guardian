# TrekGuardian-v1: Hypoxia-Related Datasets Guide

## Overview
This directory contains the 3 best hypoxia-related datasets focusing on SpO2 (oxygen saturation), oxygen levels, and altitude effects on physiological parameters. All datasets are sourced from PhysioNet, a premier repository for physiological signals and clinical data.

---

## Dataset 1: Respiratory and Pulse Oximetry Waveforms from Healthy Adults During Simulated Apnoea Events

### Dataset Information
- **Source**: PhysioNet (MIT Laboratory for Computational Physiology)
- **DOI**: https://doi.org/10.13026/4kmy-gw36
- **URL**: https://www.physionet.org/content/respiratory-oximetry-apnoea/1.0.0/
- **Published**: March 4, 2026
- **Version**: 1.0.0
- **Access**: Open Access

### Description
This dataset contains high-resolution airway pressure, flow, and pulse oximetry waveforms from 20 healthy adults during simulated apnoea events. It includes:
- Airway pressure waveforms
- Airflow measurements
- Arterial and venous PPG (photoplethysmography) signals
- SpO2 measurements during normal and apneic conditions

### Key Features for Hypoxia Research
- Real-time SpO2 tracking during oxygen desaturation
- Arterial and venous PPG signals for oxygenation analysis
- Simulated apnea events (similar to altitude-induced hypoxia)
- Detailed respiratory parameters
- 20 healthy subjects with multiple trials

### Applications
- Hypoxia detection algorithms
- Sleep apnea analysis
- Oxygenation monitoring models
- Pulse oximetry validation
- OSA (Obstructive Sleep Apnea) research

### Download Instructions
```bash
# Download the dataset
wget -r -N -c -np https://physionet.org/files/respiratory-oximetry-apnoea/1.0.0/

# Or use:
aws s3 sync --no-sign-request s3://physionet-open/respiratory-oximetry-apnoea/1.0.0/ ./respiratory-oximetry-apnoea/

# Or visit the website and download the ZIP file
```

### File Size
Approximately 2-3 GB (contains waveform data in WFDB format)

### Citation
Hill, J., Guy, E.F.S., Clifton, E.A.C., et al. (2026). Respiratory and Pulse Oximetry Waveforms from Healthy Adults During Simulated Apnoea Events. *PhysioNet*. https://doi.org/10.13026/4kmy-gw36

---

## Dataset 2: VitalDB - High-Fidelity Multi-Parameter Vital Signs Database

### Dataset Information
- **Source**: PhysioNet (MIT Laboratory for Computational Physiology)
- **DOI**: https://doi.org/10.13026/czw8-9p62
- **URL**: https://www.physionet.org/content/vitaldb/1.0.0/
- **Published**: September 21, 2022
- **Version**: 1.0.0
- **Access**: Open Access

### Description
VitalDB is a comprehensive multi-parameter vital signs database containing intraoperative monitoring data from 6,388 surgical cases. Includes:
- Percutaneous oxygen saturation (SpO2) readings
- Arterial blood pressure (continuous)
- ECG waveforms
- Cardiac output parameters
- Temperature monitoring
- Multiple other vital signs

### Key Features for Hypoxia Research
- **486,451 waveform and numeric data tracks** across 196 parameters
- **SpO2 monitoring** throughout surgical procedures
- High-resolution data (62.5-500 Hz for waveforms)
- **6,388 patient cases** with diverse demographics
- Longitudinal vital signs tracking
- Laboratory results integration
- Clinical outcomes correlation

### Applications
- SpO2 variability analysis
- Hypoxemia detection in clinical settings
- Physiological response to anesthesia
- Risk stratification for hypoxia
- Machine learning algorithm development

### Download Instructions
```bash
# Download the entire dataset (95.4 GB)
wget -r -N -c -np https://physionet.org/files/vitaldb/1.0.0/

# Or use AWS S3:
aws s3 sync --no-sign-request s3://physionet-open/vitaldb/1.0.0/ ./vitaldb/

# Or download ZIP file
wget https://physionet.org/content/vitaldb/get-zip/1.0.0/
```

### File Size
**95.4 GB total** (includes 6,388 vital sign files + clinical data)

**Note**: For faster testing, consider downloading a subset of the data first using the Python API:
```python
import vitaldb

# Load specific cases with selected parameters
data = vitaldb.load_case(caseid=1, tnames='Solar8000/SpO2,Solar8000/HR', interval=1)
```

### Citation
Lee, H.C., & Jung, C.W. (2022). VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients (version 1.0.0). *PhysioNet*. RRID:SCR_007345. https://doi.org/10.13026/czw8-9p62

---

## Dataset 3: A Temporal Dataset for Respiratory Support in Critically Ill Patients

### Dataset Information
- **Source**: PhysioNet (MIT Laboratory for Computational Physiology)
- **DOI**: https://doi.org/10.13026/3z8t-4r82
- **URL**: https://www.physionet.org/content/temporal-respiratory-support/1.1.0/
- **Published**: April 15, 2025
- **Version**: 1.1.0
- **Access**: Credentialed Access

### Description
A benchmark dataset with hourly records over a 90-day period from 50,920 ICU subjects. Includes:
- Dynamic pulmonary function data
- Respiratory support parameters
- Oxygen requirements and supplementation
- Oxygenation status indicators
- FiO2 (Fraction of Inspired Oxygen) measurements
- Disease-specific covariates

### Key Features for Hypoxia Research
- **50,920 ICU patients** - largest coverage
- **Hourly time-series data** for long-term tracking
- Oxygen supplementation requirements
- **FiO2 and SpO2 relationships**
- Respiratory support modalities
- ICU outcomes and clinical correlations
- Time-series analysis capabilities

### Applications
- Altitude/hypoxia acclimatization studies
- Oxygen therapy optimization
- Respiratory failure prediction
- ICU outcome prediction
- Hypoxemia recovery patterns
- Critical illness adaptation to hypoxia

### Download Instructions
```bash
# Requires credentialed access (free)
# 1. Create a PhysioNet account: https://physionet.org/login/
# 2. Request credentialed access to the dataset
# 3. Once approved, download using:
wget -r -N -c -np --user your_username --ask-password https://physionet.org/files/temporal-respiratory-support/1.1.0/

# Or use AWS S3 (after authentication):
aws s3 sync s3://physionet-open/temporal-respiratory-support/1.1.0/ ./temporal-respiratory-support/
```

### File Size
Approximately 15-20 GB (structured CSV/parquet format)

### Citation
Moukheiber, M., Moukheiber, L., Moukheiber, D., et al. (2025). A Temporal Dataset for Respiratory Support in Critically Ill Patients (version 1.1.0). *PhysioNet*. https://doi.org/10.13026/3z8t-4r82

---

## Why These 3 Datasets?

| Dataset | Hypoxia Focus | SpO2 Data | Altitude Simulation | Use Case |
|---------|---------------|-----------|-------------------|----------|
| **Respiratory Oximetry** | Direct | Yes (continuous) | Simulated apnea | Real-time monitoring |
| **VitalDB** | Comprehensive | Yes (high-res) | Surgical stress | Clinical validation |
| **Temporal Respiratory** | ICU-focused | Yes (with FiO2) | Critical illness | Long-term tracking |

---

## Quick Start Guide

### Prerequisites
- Python 3.7+
- WFDB toolkit for PhysioNet data
- Sufficient storage (120+ GB recommended)

### Installation
```bash
# Install PhysioNet utilities
pip install wfdb vitaldb

# Download WFDB tools
# Windows: https://physionet.org/physiotools/wfdb.shtml
# Linux/Mac: apt-get install wfdb
```

### Python API Usage
```python
# Load VitalDB data
import vitaldb

# Load SpO2 data from case 1
case_data = vitaldb.load_case(caseid=1, tnames='Solar8000/SpO2', interval=1)

# Load respiratory oximetry data
import wfdb
record = wfdb.rdrecord('respiratory-oximetry-apnoea/a001')
signals, fields = record.signals, record.sig_name
```

---

## Data Privacy & Ethics
- All datasets are **de-identified** for patient privacy
- Usage complies with HIPAA standards
- Free for research and educational use
- Some datasets require institutional review approval
- Citation of source is mandatory

---

## Recommended Software Tools
1. **MATLAB**: `readtable()`, signal processing toolbox
2. **Python**: pandas, scipy, wfdb, vitaldb
3. **R**: `wfdb`, `ggplot2`, tidyverse
4. **Visualization**: OpenSignals, PhysioNet LightWAVE

---

## Support & Documentation
- **PhysioNet FAQ**: https://physionet.org/about/faqs/
- **WFDB Documentation**: https://wfdb.io/
- **VitalDB Python Package**: https://pypi.org/project/vitaldb/
- **PhysioNet Forum**: https://groups.google.com/g/physionet-challenges

---

## Additional Resources for Hypoxia Research
- **Altitude Medicine**: Research on high-altitude hypoxia
- **Sleep Apnea Studies**: OSA-related desaturation
- **Critical Care**: ICU hypoxemia management
- **Wearable Monitoring**: SpO2 tracking devices

---

**Last Updated**: March 11, 2026
**Dataset Version**: TrekGuardian-v1
**Total Potential Data Size**: ~120 GB
