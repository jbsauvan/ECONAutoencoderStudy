from glob import glob
import itertools

# Flag to test locally
local = False

# DeltaR matching threshold
threshold = 0.05
# Input files
files_photons = glob('/home/llr/cms/sauvan/DATA_UPG/HGCAL/Ntuples/study_autoencoder/3_22_1/SinglePhoton_PT2to200/GammaGun_Pt2_200_PU0_HLTWinter20_std_ae_xyseed/210430_091126/ntuple*.root')
files_electrons = glob('/home/llr/cms/sauvan/DATA_UPG/HGCAL/Ntuples/study_autoencoder/3_22_1/SingleElectron_PT2to200/ElectronGun_Pt2_200_PU200_HLTWinter20_std_ae_xyseed/210430_090451/ntuple*.root')
files_pions = [] 
if local:
    files_photons = files_photons[:1] if len(files_photons)>0 else []
    files_electrons = files_electrons[:1] if len(files_electrons)>0 else []
    files_pions = files_pions[:1] if len(files_pions)>0 else []
# Pick one of the different algos trees to retrieve the gen information
gen_tree = 'FloatingpointThreshold0DummyHistomaxxydr015GenmatchGenclustersntuple/HGCalTriggerNtuple'
# STore only information on the best match
bestmatch_only = True
output_dir = '/home/llr/cms/sauvan/DATA_UPG/HGCAL/Dataframes/study_autoencoder/3_22_1/electron_photon_signaldriven/'
file_per_batch_electrons = 5
file_per_batch_pions = 2
file_per_batch_photons = 2
algo_trees = {}
# List of ECON algorithms
fes = ['Threshold0', 'Threshold', 'Mixedbcstc',
        'AutoEncoderTelescopeMSE', 'AutoEncoderStride',
        'AutoEncoderQKerasTTbar', 'AutoEncoderQKerasEle',
        ]
ntuple_template = 'Floatingpoint{fe}Dummy{be}GenmatchGenclustersntuple/HGCalTriggerNtuple'
algo_trees = {}
for fe in fes:
    be = 'Histomaxxydr015'
    algo_trees[fe] = ntuple_template.format(fe=fe, be=be)
