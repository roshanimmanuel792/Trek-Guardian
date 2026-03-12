# TrekGuardian-v1 Setup & Quick Reference Guide

## 🎯 What You Have

You now have a complete research framework for hypoxia-related datasets with:

### ✅ Completed Setup
- **Project Directory**: `C:\Users\Dell\TrekGuardian-v1`
- **3 Best Hypoxia Datasets**: Researched and curated
- **Documentation**: Comprehensive guides and examples
- **Tools**: Python scripts and Bash utilities
- **Analysis Templates**: Jupyter notebook ready to use

---

## 📂 Folder Structure

```
TrekGuardian-v1/
│
├── README.md                          # Main project documentation
├── requirements.txt                   # Python dependencies
│
└── datasets/
    ├── DATASET_GUIDE.md              # Detailed dataset information (10+ pages)
    ├── dataset_manager.py            # Python CLI tool for dataset management
    ├── download_datasets.sh           # Automated download script
    ├── TrekGuardian_Analysis.ipynb    # Jupyter notebook with examples
    │
    ├── 1_respiratory-oximetry/       # (Download here) 2.5 GB
    ├── 2_vitaldb/                    # (Download here) 95.4 GB
    └── 3_temporal-respiratory/       # (Download here) 18 GB
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd C:\Users\Dell\TrekGuardian-v1
pip install -r requirements.txt
```

### Step 2: Download Datasets
```bash
cd datasets
bash download_datasets.sh
# Then follow the interactive prompts
```

### Step 3: Start Analyzing
```bash
python dataset_manager.py --list
# Or open TrekGuardian_Analysis.ipynb in Jupyter
```

---

## 📊 The 3 Datasets

### Dataset 1: Respiratory and Pulse Oximetry Waveforms
```
Name:        Respiratory and Pulse Oximetry Waveforms from Healthy Adults
Size:        2.5 GB
Subjects:    20 healthy adults
Duration:    10-30 minutes each
Key Data:    SpO2, airway pressure, flow, PPG signals
Hypoxia:     Simulated apnea events
Downloads:   ~10-15 minutes
Focus:       Real-time SpO2 during oxygen desaturation
```

**Best for:** Pulse oximeter validation, apnea detection algorithms

### Dataset 2: VitalDB (Multi-Parameter Vital Signs)
```
Name:        VitalDB, a high-fidelity multi-parameter vital signs database
Size:        95.4 GB (largest, comprehensive)
Subjects:    6,388 surgical patients
Duration:    2-6 hours (intraoperative)
Key Data:    486,451 waveform/numeric tracks, SpO2, BP, HR, ECG, etc.
Hypoxia:     Clinical hypoxemia during anesthesia
Downloads:   Several hours
Focus:       Comprehensive vital signs correlation with SpO2
```

**Best for:** Machine learning, clinical algorithm development, multi-parameter analysis

### Dataset 3: Temporal Respiratory Support in ICU
```
Name:        A Temporal Dataset for Respiratory Support in Critically Ill
Size:        18 GB (structured/efficient)
Subjects:    50,920 ICU patients (largest coverage)
Duration:    90 days per patient (hourly data)
Key Data:    FiO2, SpO2, respiratory support, pulmonary function
Hypoxia:     Natural ICU critical illness
Downloads:   2-4 hours
Focus:       Long-term oxygen therapy and respiratory support
```

**Best for:** Time-series analysis, ICU outcomes, altitude acclimatization studies

---

## 🔧 Command Reference

### View Dataset Information
```bash
python dataset_manager.py --list              # List all datasets
python dataset_manager.py --info vitaldb      # Get info on VitalDB
python dataset_manager.py --status            # Check download status
```

### Get Help
```bash
python dataset_manager.py --download respiratory-oximetry  # Download instructions
python dataset_manager.py --code vitaldb                    # Python code examples
python dataset_manager.py --manifest                        # Generate metadata
```

### Run Download Script
```bash
bash download_datasets.sh                     # Interactive download
```

---

## 🐍 Python Quick Examples

### Load and Analyze SpO2 Data
```python
import vitaldb
import numpy as np

# Load SpO2 from VitalDB case 1
spo2_data = vitaldb.load_case(caseid=1, tnames='Solar8000/SpO2', interval=1)

# Analyze
print(f"Mean SpO2: {np.mean(spo2_data[0]):.2f}%")
print(f"Min SpO2: {np.min(spo2_data[0]):.2f}%")

# Detect hypoxia events (SpO2 < 90%)
hypoxia = spo2_data[0] < 90
print(f"Hypoxia events: {np.sum(hypoxia)}")
```

### Work with Respiratory Oximetry Data
```python
import wfdb

# Load record
record = wfdb.rdrecord('1_respiratory-oximetry/a001')

# Get SpO2 signal
spo2_idx = record.sig_name.index('SpO2')
spo2 = record.p_signal[:, spo2_idx]

# Time axis
time = np.arange(len(spo2)) / record.fs
```

### Analyze Temporal Respiratory Support
```python
import pandas as pd

# Read CSV data
df = pd.read_csv('3_temporal-respiratory/data.csv')

# Filter for patients with hypoxia
hypoxia_cases = df[df['SpO2'] < 90]
print(f"Cases with hypoxia: {hypoxia_cases['caseid'].nunique()}")
```

---

## 📋 File Descriptions

| File | Purpose | Size |
|------|---------|------|
| README.md | Main documentation | 8 KB |
| DATASET_GUIDE.md | Detailed dataset info | 25 KB |
| dataset_manager.py | Python CLI tool | 12 KB |
| download_datasets.sh | Bash download script | 4 KB |
| TrekGuardian_Analysis.ipynb | Jupyter notebook | 18 KB |
| requirements.txt | Python dependencies | 1 KB |

---

## 💾 Storage Requirements

| Dataset | Size | Uncompressed | Total Space Needed |
|---------|------|--------------|-------------------|
| Respiratory Oximetry | 2.5 GB | 2.5 GB | 5 GB |
| VitalDB | 95.4 GB | 95.4 GB | 190 GB |
| Temporal Respiratory | 18 GB | 18 GB | 36 GB |
| **TOTAL** | **116 GB** | **116 GB** | **231 GB** |

**Recommendation**: Start with Dataset 1 (2.5 GB) for testing

---

## ⚙️ System Requirements

- **OS**: Windows, macOS, Linux
- **Python**: 3.7+
- **Disk Space**: 25+ GB minimum (recommend 150+ GB)
- **RAM**: 8 GB minimum (16 GB recommended)
- **Internet**: For downloading datasets (stable connection recommended)

---

## 📚 Documentation Roadmap

1. **README.md** - Start here for overview
2. **DATASET_GUIDE.md** - Detailed dataset specifications
3. **TrekGuardian_Analysis.ipynb** - Run examples interactively
4. **PhysioNet.org** - Official data sources and documentation

---

## 🔑 Key Resources

### Download the Datasets
- **PhysioNet**: https://physionet.org/
- **Respiratory Oximetry**: https://physionet.org/content/respiratory-oximetry-apnoea/1.0.0/
- **VitalDB**: https://physionet.org/content/vitaldb/1.0.0/
- **Temporal Respiratory**: https://physionet.org/content/temporal-respiratory-support/1.1.0/

### Learning Resources
- **WFDB Documentation**: https://wfdb.io/
- **VitalDB Python API**: https://pypi.org/project/vitaldb/
- **Signal Processing**: https://docs.scipy.org/doc/scipy/reference/signal.html

### Related Research
- Sleep Apnea (OSA) detection
- Hypoxemia in critical care
- Altitude acclimatization
- Pulse oximetry algorithms

---

## ⚠️ Important Notes

### Data Privacy
- ✅ All datasets are HIPAA de-identified
- ✅ Free for research and education
- ⚠️ Check individual dataset licenses
- 📋 Citation required for publications

### Download Tips
- Use **wget** for large files (most reliable)
- Consider **AWS S3** for speed (if available)
- Break downloads into sessions
- Verify checksums (SHA256SUMS.txt provided)

### Data Format
- **VitalDB**: Binary `.vital` format (use vitaldb library)
- **Respiratory Oximetry**: WFDB format (use wfdb library)
- **Temporal Respiratory**: CSV format (use pandas)

---

## 🆘 Troubleshooting

### Issue: "Module not found" error
**Solution**: `pip install wfdb vitaldb`

### Issue: Dataset download fails
**Solution**: Use `wget --continue` to resume downloads

### Issue: Can't find records
**Solution**: Verify records are in correct subdirectories

### Issue: Memory issues with large datasets
**Solution**: Use interval parameter to downsample: `load_case(..., interval=10)`

---

## 📞 Support & Contact

- **PhysioNet FAQ**: https://physionet.org/about/faqs/
- **Dataset Authors**: Check individual dataset pages
- **Python Libraries**: See GitHub repositories
- **General Issues**: PhysioNet discussion forum

---

## 🎓 Suggested Learning Path

### Beginner (1-2 weeks)
1. Read README.md
2. Download Dataset 1 (smallest)
3. Run TrekGuardian_Analysis.ipynb
4. Analyze SpO2 trends

### Intermediate (2-4 weeks)
1. Download Dataset 2 (VitalDB)
2. Analyze multi-parameter correlations
3. Develop custom analysis scripts
4. Create visualization dashboards

### Advanced (4+ weeks)
1. Download Dataset 3 (Temporal)
2. Implement machine learning models
3. Time-series forecasting
4. Publish research findings

---

## 📝 Citation Format

When using these datasets, cite as:

```
Lee, H.C., & Jung, C.W. (2022). VitalDB, a high-fidelity multi-parameter vital 
signs database in surgical patients (version 1.0.0). PhysioNet. 
https://doi.org/10.13026/czw8-9p62

Hill, J., Guy, E.F.S., Clifton, E.A.C., et al. (2026). Respiratory and Pulse 
Oximetry Waveforms from Healthy Adults During Simulated Apnoea Events. PhysioNet.
https://doi.org/10.13026/4kmy-gw36

Moukheiber, M., Moukheiber, L., Moukheiber, D., et al. (2025). A Temporal Dataset 
for Respiratory Support in Critically Ill Patients (version 1.1.0). PhysioNet.
https://doi.org/10.13026/3z8t-4r82
```

---

## ✨ Next Steps

1. ✅ **Setup Complete** - You're ready to use TrekGuardian-v1
2. 📥 **Download Datasets** - Run `download_datasets.sh`
3. 📊 **Start Analyzing** - Open `TrekGuardian_Analysis.ipynb`
4. 🔬 **Conduct Research** - Use the tools provided
5. 📄 **Publish Results** - Share your findings!

---

**Project Version**: 1.0  
**Last Updated**: March 11, 2026  
**Location**: `C:\Users\Dell\TrekGuardian-v1`  
**Status**: ✅ Ready to Use
