from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'WAJJ-aqgc'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Summer16_23Sep2016V4_MC_L1FastJet_AK4PFchs.txt','Summer16_23Sep2016V4_MC_L2Relative_AK4PFchs.txt','Summer16_23Sep2016V4_MC_L3Absolute_AK4PFchs.txt','Summer16_23Sep2016V4_MC_L1FastJet_AK4PFPuppi.txt','Summer16_23Sep2016V4_MC_L2Relative_AK4PFPuppi.txt','Summer16_23Sep2016V4_MC_L3Absolute_AK4PFPuppi.txt']
# Name of the CMSSW configuration file
config.JobType.psetName    = 'analysis.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/group/phys_jetmet/qihuang/'
#config.Data.outLFNDirBase = '/store/user/qihuang/'
config.Data.publication = False
config.Data.outputDatasetTag = 'WAJJ-aqgc'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
