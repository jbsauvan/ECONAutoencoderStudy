from glob import glob
import pickle
import numpy as np

# Flag to test locally
local = False

files_batch = glob('/home/llr/cms/sauvan/DATA_UPG/HGCAL/Ntuples/study_autoencoder/3_22_1/MinBias_TuneCP5_14TeV-pythia8/MinBias_PU200_HLTWinter20_std_ae_sigdriven_xyseed/210430_091906/ntuple*.root')
# if local test, use only one input file
if local:
    files_batch = files_batch[:1]
output_dir = '/home/llr/cms/sauvan/DATA_UPG/HGCAL/Dataframes/study_autoencoder/3_22_1/pu_for_id_signaldriven/'
file_per_batch = 6

# List of ECON algorithms
fes = ['Threshold0', 'Threshold', 'Mixedbcstc',
        'AutoEncoderTelescopeMSE', 'AutoEncoderStride',
        'AutoEncoderQKerasTTbar', 'AutoEncoderQKerasEle',
        ]

ntuple_template = 'Floatingpoint{fe}Dummy{be}Genclustersntuple/HGCalTriggerNtuple'
algo_trees = {}
for fe in fes:
    be = 'Histomaxxydr015'
    algo_trees[fe] = ntuple_template.format(fe=fe, be=be)

# Preselection pT cut, after calibration
pt_cut = 20
# Store all clusters passing the preselection
store_max_only = False

# Load energy calibration/correction data
with open('/home/llr/cms/sauvan/Projects/L1CalorimeterTrigger_Phase2HGCal/Studies/HGCTPGBackendStudies/data/layer_weights_photons_autoencoder_210430.pkl', 'rb') as f:
    calibration_weights = pickle.load(f)
with open('/home/llr/cms/sauvan/Projects/L1CalorimeterTrigger_Phase2HGCal/Studies/HGCTPGBackendStudies/data/lineareta_electrons_autoencoder_210430.pkl', 'rb') as f:
    correction_cluster = pickle.load(f)

additive_correction = True
correction_inputs = ['cl3d_abseta']

# No ID selection is applied in the preprocessing
bdts = None
working_points = {}
for name in algo_trees.keys():
    working_points[name] = -999
