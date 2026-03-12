#!/bin/bash
# TrekGuardian-v1 Dataset Download Script
# Downloads the 3 best hypoxia-related datasets from PhysioNet

set -e

DATASET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DATASET_DIR"

echo "============================================"
echo "TrekGuardian-v1 Dataset Download Manager"
echo "============================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for download tools
if command_exists wget; then
    DOWNLOAD_CMD="wget -c"
    echo "Using wget for downloads"
elif command_exists curl; then
    DOWNLOAD_CMD="curl -L -O -C -"
    echo "Using curl for downloads"
else
    echo "ERROR: Neither wget nor curl found. Please install one of them."
    exit 1
fi

echo ""
echo "DATASET 1: Respiratory and Pulse Oximetry Waveforms"
echo "---------------------------------------------------"
echo "Size: ~2-3 GB"
echo "URL: https://physionet.org/files/respiratory-oximetry-apnoea/1.0.0/"
read -p "Download Dataset 1? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    mkdir -p "1_respiratory-oximetry-apnoea"
    cd "1_respiratory-oximetry-apnoea"
    echo "Downloading Dataset 1..."
    wget -r -N -c -np https://physionet.org/files/respiratory-oximetry-apnoea/1.0.0/
    cd ..
    echo "Dataset 1 downloaded successfully!"
fi

echo ""
echo "DATASET 2: VitalDB - High-Fidelity Multi-Parameter Vital Signs"
echo "---------------------------------------------------------------"
echo "Size: ~95.4 GB (Large dataset)"
echo "URL: https://physionet.org/files/vitaldb/1.0.0/"
echo "Note: This is a very large dataset. Consider downloading subsets."
read -p "Download Dataset 2? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    mkdir -p "2_vitaldb"
    cd "2_vitaldb"
    echo "Downloading Dataset 2..."
    echo "Starting VitalDB download (this will take considerable time)..."
    wget -r -N -c -np https://physionet.org/files/vitaldb/1.0.0/
    cd ..
    echo "Dataset 2 downloaded successfully!"
fi

echo ""
echo "DATASET 3: Temporal Respiratory Support in Critically Ill Patients"
echo "-------------------------------------------------------------------"
echo "Size: ~15-20 GB"
echo "URL: https://physionet.org/files/temporal-respiratory-support/1.1.0/"
echo "Note: Requires free PhysioNet credentialed access"
read -p "Download Dataset 3? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    mkdir -p "3_temporal-respiratory-support"
    cd "3_temporal-respiratory-support"
    echo "Downloading Dataset 3..."
    echo "If prompted, enter your PhysioNet credentials"
    wget -r -N -c -np --ask-password https://physionet.org/files/temporal-respiratory-support/1.1.0/
    cd ..
    echo "Dataset 3 downloaded successfully!"
fi

echo ""
echo "============================================"
echo "Download Complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Install Python dependencies: pip install wfdb vitaldb pandas scipy"
echo "2. Review DATASET_GUIDE.md for usage instructions"
echo "3. Check PhysioNet documentation for data format details"
echo ""
