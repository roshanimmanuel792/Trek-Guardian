#!/usr/bin/env python3
"""
TrekGuardian-v1 Dataset Access Module
Provides easy access and management of hypoxia-related datasets
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Optional
import urllib.request
import urllib.error

class TrekGuardianDatasets:
    """Manager for TrekGuardian hypoxia datasets"""
    
    DATASETS = {
        "respiratory-oximetry": {
            "name": "Respiratory and Pulse Oximetry Waveforms",
            "url": "https://physionet.org/files/respiratory-oximetry-apnoea/1.0.0/",
            "doi": "https://doi.org/10.13026/4kmy-gw36",
            "size_gb": 2.5,
            "subjects": 20,
            "access": "open",
            "parameters": ["SpO2", "Airway Pressure", "Flow", "PPG"],
            "description": "Pulse oximetry and respiratory waveforms during simulated apnea"
        },
        "vitaldb": {
            "name": "VitalDB - Multi-Parameter Vital Signs",
            "url": "https://physionet.org/files/vitaldb/1.0.0/",
            "doi": "https://doi.org/10.13026/czw8-9p62",
            "size_gb": 95.4,
            "subjects": 6388,
            "access": "open",
            "parameters": ["SpO2", "BP", "HR", "ECG", "Temperature", "CO", "etc"],
            "description": "High-fidelity intraoperative vital signs from 6,388 surgical cases"
        },
        "temporal-respiratory": {
            "name": "Temporal Respiratory Support Dataset",
            "url": "https://physionet.org/files/temporal-respiratory-support/1.1.0/",
            "doi": "https://doi.org/10.13026/3z8t-4r82",
            "size_gb": 18.0,
            "subjects": 50920,
            "access": "credentialed",
            "parameters": ["FiO2", "SpO2", "Pulmonary Function", "Respiratory Support"],
            "description": "Hourly respiratory data from 50,920 ICU patients over 90 days"
        }
    }
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.datasets_path = self.base_path / "datasets"
        self.metadata_file = self.datasets_path / "datasets_manifest.json"
        
    def list_datasets(self) -> Dict:
        """List all available datasets"""
        return self.DATASETS
    
    def get_dataset_info(self, dataset_key: str) -> Optional[Dict]:
        """Get information about a specific dataset"""
        if dataset_key in self.DATASETS:
            return self.DATASETS[dataset_key]
        return None
    
    def print_dataset_summary(self):
        """Print summary of all datasets"""
        print("\n" + "="*70)
        print("TrekGuardian-v1: Hypoxia-Related Datasets")
        print("="*70 + "\n")
        
        total_size = 0
        total_subjects = 0
        
        for idx, (key, info) in enumerate(self.DATASETS.items(), 1):
            print(f"\n[DATASET {idx}] {info['name']}")
            print("-" * 70)
            print(f"  Description:  {info['description']}")
            print(f"  DOI:          {info['doi']}")
            print(f"  Size:         {info['size_gb']} GB")
            print(f"  Subjects:     {info['subjects']:,}")
            print(f"  Access:       {info['access'].upper()}")
            print(f"  Parameters:   {', '.join(info['parameters'])}")
            print(f"  Download:     {info['url']}")
            
            total_size += info['size_gb']
            total_subjects += info['subjects']
        
        print("\n" + "="*70)
        print(f"TOTAL:")
        print(f"  Combined Size:     {total_size:.1f} GB")
        print(f"  Total Subjects:    {total_subjects:,}")
        print("="*70 + "\n")
    
    def save_manifest(self):
        """Save dataset manifest to JSON"""
        manifest = {
            "version": "1.0",
            "created": str(Path(__file__).stat().st_mtime),
            "datasets": self.DATASETS,
            "total_size_gb": sum(d['size_gb'] for d in self.DATASETS.values()),
            "total_subjects": sum(d['subjects'] for d in self.DATASETS.values())
        }
        
        self.datasets_path.mkdir(parents=True, exist_ok=True)
        with open(self.metadata_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"Manifest saved to: {self.metadata_file}")
    
    def check_downloaded_status(self) -> Dict[str, bool]:
        """Check which datasets have been downloaded"""
        status = {}
        for key in self.DATASETS.keys():
            dataset_dir = self.datasets_path / key
            status[key] = dataset_dir.exists() and len(list(dataset_dir.glob("*"))) > 0
        return status
    
    def get_download_instructions(self, dataset_key: str) -> str:
        """Get download instructions for a dataset"""
        if dataset_key not in self.DATASETS:
            return f"Unknown dataset: {dataset_key}"
        
        dataset = self.DATASETS[dataset_key]
        instructions = f"""
Download Instructions for: {dataset['name']}

1. Using wget:
   wget -r -N -c -np {dataset['url']}

2. Using AWS S3:
   aws s3 sync --no-sign-request s3://physionet-open/{dataset_key}/ ./

3. Web Browser:
   Visit: {dataset['url']}

4. Python API:
   import vitaldb  # For VitalDB
   import wfdb     # For respiratory data
   
Size: {dataset['size_gb']} GB
Subjects: {dataset['subjects']:,}
Access: {dataset['access'].upper()}
DOI: {dataset['doi']}
"""
        return instructions
    
    def get_python_code_example(self, dataset_key: str) -> str:
        """Get Python code example for working with dataset"""
        examples = {
            "respiratory-oximetry": """
# Load respiratory oximetry data using WFDB
import wfdb

# Read a record
record = wfdb.rdrecord('respiratory-oximetry-apnoea/a001')

# Get signal names
print("Available signals:", record.sig_name)

# Extract SpO2 signal
spo2_idx = record.sig_name.index('SpO2') if 'SpO2' in record.sig_name else 0
spo2_data = record.p_signal[:, spo2_idx]

# Plot
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 4))
plt.plot(spo2_data)
plt.title('SpO2 During Apnea Event')
plt.xlabel('Sample')
plt.ylabel('SpO2 (%)')
plt.show()
""",
            "vitaldb": """
# Load VitalDB data
import vitaldb
import pandas as pd

# Load SpO2 data from case 1
case_data = vitaldb.load_case(caseid=1, tnames='Solar8000/SpO2', interval=1)

# Create DataFrame
df = pd.DataFrame(case_data[0], columns=['SpO2'])

# Calculate statistics
print(f"Mean SpO2: {df['SpO2'].mean():.2f}%")
print(f"Min SpO2: {df['SpO2'].min():.2f}%")
print(f"Max SpO2: {df['SpO2'].max():.2f}%")

# Load multiple parameters
data = vitaldb.load_case(
    caseid=1,
    tnames=['Solar8000/SpO2', 'Solar8000/HR', 'Solar8000/BT'],
    interval=1
)
""",
            "temporal-respiratory": """
# Load temporal respiratory data
import pandas as pd

# Read CSV data
df = pd.read_csv('temporal-respiratory-support/data.csv')

# Filter for SpO2 and FiO2
respiratory_data = df[['caseid', 'timestamp', 'SpO2', 'FiO2']]

# Calculate trends
respiratory_data['SpO2_trend'] = respiratory_data.groupby('caseid')['SpO2'].pct_change()

# Analyze by patient
for caseid, group in respiratory_data.groupby('caseid'):
    print(f"Case {caseid}: Mean SpO2 = {group['SpO2'].mean():.2f}%")
"""
        }
        return examples.get(dataset_key, "No example available for this dataset")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="TrekGuardian Dataset Manager")
    parser.add_argument("--list", action="store_true", help="List all datasets")
    parser.add_argument("--info", type=str, help="Get info on specific dataset")
    parser.add_argument("--download", type=str, help="Get download instructions")
    parser.add_argument("--manifest", action="store_true", help="Save manifest file")
    parser.add_argument("--code", type=str, help="Get Python code example")
    parser.add_argument("--status", action="store_true", help="Check download status")
    
    args = parser.parse_args()
    
    tg = TrekGuardianDatasets()
    
    if args.list or (len(sys.argv) == 1):
        tg.print_dataset_summary()
    
    if args.info:
        info = tg.get_dataset_info(args.info)
        if info:
            print(json.dumps(info, indent=2))
        else:
            print(f"Dataset not found: {args.info}")
    
    if args.download:
        print(tg.get_download_instructions(args.download))
    
    if args.manifest:
        tg.save_manifest()
    
    if args.code:
        print(tg.get_python_code_example(args.code))
    
    if args.status:
        status = tg.check_downloaded_status()
        print("\nDownload Status:")
        for key, downloaded in status.items():
            status_str = "✓ Downloaded" if downloaded else "✗ Not Downloaded"
            print(f"  {key}: {status_str}")


if __name__ == "__main__":
    main()
