# TrekGuardian-v1 🏔️

## Hypoxia-Related Datasets for Oxygen Saturation (SpO2) Research

A comprehensive collection of the 3 best publicly available datasets focusing on hypoxia, oxygen saturation (SpO2), and altitude-related physiological effects.

---

## Quick Start

### View Dataset Summary
```bash
python dataset_manager.py --list
```

### Download a Dataset
```bash
bash download_datasets.sh
```

### Get Download Instructions
```bash
python dataset_manager.py --download vitaldb
```

---

## 📊 The 3 Datasets

### 1. Respiratory and Pulse Oximetry Waveforms (2.5 GB)
- **Focus**: Real-time SpO2 tracking during simulated apnea
- **Subjects**: 20 healthy adults
- **Key Data**: Continuous SpO2, PPG signals, airway pressure
- **Use Cases**: Hypoxia detection, OSA research, pulse oximetry validation
- **Download Time**: ~10-15 minutes

or use similar datasets similar to the one mentioned above having vitals such Spo2 
---

## 📁 Folder Structure

```
TrekGuardian-v1/
├── datasets/
│   ├── DATASET_GUIDE.md                 # Comprehensive dataset guide
│   ├── README.md                        # This file
│   ├── dataset_manager.py               # Python CLI tool
│   ├── download_datasets.sh             # Bash download script
│   ├── datasets_manifest.json           # Auto-generated metadata
│   │
│   ├── 1_respiratory-oximetry/          # (After download)
│   ├── 2_vitaldb/                       # (After download)
│   └── 3_temporal-respiratory/          # (After download)
│
└── README.md
```

---

## 🔧 Installation

### Prerequisites
- Python 3.7+
- 150+ GB free disk space (for all datasets)
- wget or curl for downloads
- Git (optional)

### Setup
```bash
# Clone or navigate to TrekGuardian-v1
cd TrekGuardian-v1/datasets

# Install Python dependencies
pip install wfdb vitaldb pandas scipy matplotlib seaborn

# Make scripts executable (Linux/Mac)
chmod +x download_datasets.sh
chmod +x dataset_manager.py
```

---

## 💾 Download Methods

### Method 1: Automated Download Script
```bash
cd TrekGuardian-v1/datasets
bash download_datasets.sh
```

### Method 2: Using wget directly
```bash
cd TrekGuardian-v1/datasets

# Dataset 1
mkdir -p 1_respiratory-oximetry && cd 1_respiratory-oximetry
wget -r -N -c -np https://physionet.org/files/respiratory-oximetry-apnoea/1.0.0/
cd ..

# Dataset 2
mkdir -p 2_vitaldb && cd 2_vitaldb
wget -r -N -c -np https://physionet.org/files/vitaldb/1.0.0/
cd ..

# Dataset 3 (requires PhysioNet account)
mkdir -p 3_temporal-respiratory && cd 3_temporal-respiratory
wget -r -N -c -np --ask-password https://physionet.org/files/temporal-respiratory-support/1.1.0/
cd ..
```

### Method 3: AWS S3 Command
```bash
# Fastest method (requires AWS CLI)
aws s3 sync --no-sign-request s3://physionet-open/vitaldb/1.0.0/ vitaldb/
```

---

## 🐍 Python Usage Examples

### Load and Analyze SpO2 Data
```python
from dataset_manager import TrekGuardianDatasets

# Initialize manager
tg = TrekGuardianDatasets('.')

# List all datasets
tg.print_dataset_summary()

# Get code examples
print(tg.get_python_code_example('vitaldb'))
```

### Work with VitalDB
```python
import vitaldb
import pandas as pd

# Load SpO2 from multiple cases
cases_data = []
for caseid in range(1, 101):  # First 100 cases
    try:
        data = vitaldb.load_case(caseid, 'Solar8000/SpO2', interval=1)
        cases_data.append({
            'caseid': caseid,
            'spo2_mean': data[0].mean(),
            'spo2_min': data[0].min(),
            'spo2_max': data[0].max()
        })
    except:
        continue

df = pd.DataFrame(cases_data)
print(df.describe())
```

### Analyze Respiratory Oximetry Data
```python
import wfdb
import numpy as np

# Read respiratory oximetry record
record = wfdb.rdrecord('1_respiratory-oximetry/a001')

# Find SpO2 signal
spo2_sig = record.p_signal[:, record.sig_name.index('SpO2')]

# Calculate hypoxia events (SpO2 < 90%)
hypoxia_events = np.sum(spo2_sig < 90)
print(f"Hypoxia events detected: {hypoxia_events}")
```

---

## 📊 Data Characteristics

### Hypoxia-Specific Metrics

| Dataset | SpO2 Range | Resolution | Duration | Hypoxia Events |
|---------|-----------|-----------|----------|----------------|
| Respiratory Oximetry | 70-100% | 1-100 Hz | 10-30 min | Simulated |
| VitalDB | 80-100% | 1-7 sec | 2-6 hours | Clinical |
| Temporal Respiratory | 75-100% | Hourly | 90 days | Natural |

---

## 🎯 Use Cases

### For Researchers
- Algorithm development for hypoxia detection
- SpO2 trend analysis in clinical settings
- Altitude acclimatization studies
- Sleep apnea characterization

### For Engineers
- Pulse oximeter validation
- Wearable device calibration
- Real-time monitoring system design
- Machine learning model training

### For Students
- Physiological signal processing
- Time-series analysis
- Medical data visualization
- Biomedical signal understanding

---

## 📚 Documentation

- **DATASET_GUIDE.md** - Detailed guide for each dataset
- **PhysioNet FAQ** - https://physionet.org/about/faqs/
- **WFDB Documentation** - https://wfdb.io/
- **VitalDB Python API** - https://pypi.org/project/vitaldb/

---

## ⚖️ License & Citation

All datasets are **open access** and free to use for research and education.

### Required Citations

**VitalDB:**
```bibtex
@article{lee2022vitaldb,
  title={VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients},
  author={Lee, HC and Jung, CW},
  journal={Scientific Data},
  volume={9},
  pages={279},
  year={2022}
}
```

**Respiratory Oximetry:**
```bibtex
@misc{hill2026respiratory,
  title={Respiratory and Pulse Oximetry Waveforms from Healthy Adults During Simulated Apnoea Events},
  author={Hill, J and Guy, EFS and others},
  year={2026},
  doi={10.13026/4kmy-gw36}
}
```

**Temporal Respiratory Support:**
```bibtex
@misc{moukheiber2025temporal,
  title={A Temporal Dataset for Respiratory Support in Critically Ill Patients},
  author={Moukheiber, M and others},
  year={2025},
  doi={10.13026/3z8t-4r82}
}
```

---

## 🤝 Contributing

Found an issue? Have a suggestion? Please:
1. Check existing documentation
2. Review PhysioNet guidelines
3. Contact dataset maintainers

---

## ❓ FAQs

**Q: Do I need to register?**
A: Free PhysioNet account recommended for credentialed datasets.

**Q: How much storage do I need?**
A: Minimum 25 GB (just Dataset 1), ideal 150+ GB for all three.

**Q: Can I use this for commercial purposes?**
A: Check individual dataset licenses. Generally allowed with proper attribution.

**Q: How often is data updated?**
A: Datasets are static. New versions released periodically.

**Q: Is the data de-identified?**
A: Yes, all datasets are HIPAA de-identified.

---

## 📞 Support

- **PhysioNet Support**: https://physionet.org/about/
- **WFDB Issues**: https://github.com/MIT-LCP/wfdb
- **Dataset Questions**: Contact dataset authors via PhysioNet

---

**Version**: 1.0  
**Last Updated**: March 11, 2026  
**Maintainer**: TrekGuardian Project  
**License**: CC BY 4.0 (see individual datasets)
