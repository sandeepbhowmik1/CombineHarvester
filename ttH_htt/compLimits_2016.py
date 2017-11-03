import os, subprocess, sys

channels = [
  ##"1l_2tau_LLR",
  ##"1l_2tau_ND",
  #"1l_2tau_Tallinn",
  ##"2lss_1tau_Cornell",
  ##"2lss_1tau_LLR",
  #"2lss_1tau_Tallinn",
  ##"3l_1tau_LLR",
  #"3l_1tau_Tallinn",
  "2l_2tau_Tallinn",
  "2los_2tau_Tallinn",
  "2lss_2tau_Tallinn",
]

shapeVariables = {
  "1l_2tau_LLR"       : [ "mTauTauVis" ],
  "1l_2tau_ND"        : [ "mTauTauVis" ],
  "1l_2tau_Tallinn"   : [ "mTauTauVis" ],
  "2lss_1tau_Cornell" : [ "mvaDiscr_2lss" ],
  "2lss_1tau_LLR"     : [ "mvaDiscr_2lss" ],
  "2lss_1tau_Tallinn" : [ "mvaDiscr_2lss" ],
  "3l_1tau_LLR"       : [ "mvaDiscr_3l" ],
  "3l_1tau_Tallinn"   : [ "mvaDiscr_3l" ],
  "2l_2tau_Tallinn"   : [ "mvaDiscr_2l" ],
  "2lss_2tau_Tallinn"   : [ "mvaDiscr_2l" ],
  "2los_2tau_Tallinn"   : [ "mvaDiscr_2l" ],
}

datacardFiles = {
  "1l_2tau_LLR"       : "LLR/datacard_mvis_1l2tau_syst_12.9fb_2017Jan13.root",
  "1l_2tau_ND"        : "ND/sync_workspace.root",
  "1l_2tau_Tallinn"   : "Tallinn/datacard_mvis_1l2tau_12.9fb_2017Jan13.root",
  "2lss_1tau_Cornell" : "Cornell/ttH_2lss_1tau.input.root",
  "2lss_1tau_LLR"     : "LLR/datacard_MVA_2lSS_1tau_nofaketau_syst_12.9fb_2017Jan13.root",
#  "2lss_1tau_Tallinn" : "Tallinn/datacard_MVA_2lSS_1tau_nofaketau_12.9fb_2017Jan13.root",
#  "2lss_1tau_Tallinn" : "Tallinn/ttH_2lss_1tau_35.9fb_mvaDiscr_2lss_2017Feb24.input.root",
  "2lss_1tau_Tallinn" : "prepareDatacards_3l_1tau_mvaDiscr_3l.root",
  "3l_1tau_LLR"       : "LLR/datacard_MVA_3l_1tau_12.9fb_2017Jan13.root",
#  "3l_1tau_Tallinn"   : "Tallinn/datacard_MVA_3l_1tau_nofaketau_12.9fb_2017Jan13.root",
#  "3l_1tau_Tallinn"   : "3l_1tau/prepareDatacards_3l_1tau_mTauTauVis.root",
  "3l_1tau_Tallinn"   : "3l_1tau/addSystDatacards_3l_1tau_mvaDiscr_3l.root",
#  "2l_2tau_Tallinn"   : "2l_2tau/prepareDatacards_2l_2tau_mTauTauVis.root",
#  "2l_2tau_Tallinn"   : "2017Oct31/datacards/2los_2tau/prepareDatacards_2los_2tau_lepOS_mTauTauVis.root",
  "2l_2tau_Tallinn"   : "ttHAnalysis_171018/2016/2017Oct04/datacards/2l_2tau/prepareDatacards_2l_2tau_mTauTauVis.root",
  "2los_2tau_Tallinn"   : "ttHAnalysis/2016/2017Oct31/datacards/2los_2tau/prepareDatacards_2los_2tau_lepOS_mTauTauVis.root",
  "2lss_2tau_Tallinn"   : "ttHAnalysis/2016/2017Oct31/datacards/2lss_2tau/prepareDatacards_2lss_2tau_lepSS_mTauTauVis.root",
}

WriteDatacard_executables = {
  "1l_2tau_LLR"       : 'WriteDatacards_1l_2tau',
  "1l_2tau_ND"        : 'WriteDatacards_1l_2tau',
  "1l_2tau_Tallinn"   : 'WriteDatacards_1l_2tau',
  "2lss_1tau_Cornell" : 'WriteDatacards_2lss_1tau',
  "2lss_1tau_LLR"     : 'WriteDatacards_2lss_1tau',
  "2lss_1tau_Tallinn" : 'WriteDatacards_2lss_1tau',
  "3l_1tau_LLR"       : 'WriteDatacards_3l_1tau',
  "3l_1tau_Tallinn"   : 'WriteDatacards_3l_1tau',
  "2l_2tau_Tallinn"   : 'WriteDatacards_2l_2tau',
  "2los_2tau_Tallinn"   : 'WriteDatacards_2los_2tau',
  "2lss_2tau_Tallinn"   : 'WriteDatacards_2lss_2tau',
}

makePostFitPlots_macros = {
  "1l_2tau_LLR"       : 'makePostFitPlots_1l_2tau.C',
  "1l_2tau_ND"        : 'makePostFitPlots_1l_2tau.C',
  "1l_2tau_Tallinn"   : 'makePostFitPlots_1l_2tau.C',
  "2lss_1tau_Cornell" : 'makePostFitPlots_2lss_1tau.C',
  "2lss_1tau_LLR"     : 'makePostFitPlots_2lss_1tau.C',
  "2lss_1tau_Tallinn" : 'makePostFitPlots_2lss_1tau.C',
  "3l_1tau_LLR"       : 'makePostFitPlots_3l_1tau.C',
  "3l_1tau_Tallinn"   : 'makePostFitPlots_3l_1tau.C',
  "2l_2tau_Tallinn"   : 'makePostFitPlots_2l_2tau.C',
  "2los_2tau_Tallinn"   : 'makePostFitPlots_2los_2tau.C',
  "2lss_2tau_Tallinn"   : 'makePostFitPlots_2lss_2tau.C',
}    

def run_cmd(command):
  print "executing command = '%s'" % command
  p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
  stdout, stderr = p.communicate()
  return stdout

workingDir = os.getcwd()
#datacardDir = "/home/veelken/public/HIG16022_datacards/"
#datacardDir = "/home/sbhowmik/LimitCalculation/CMSSW_7_4_7/src/CombineHarvester/ttH_htt//HIG16022_datacards/"
#datacardDir = "/home/sbhowmik/ttHAnalysis_171018/2016/2017Oct04/datacards/"
datacardDir = "/home/sbhowmik/"

for channel in channels:
  for shapeVariable in shapeVariables[channel]:
    channel_base = None
#    for search_string in [ "1l_2tau", "2lss_1tau", "3l_1tau", "2l_2tau", "2los_2tau", "2lss_2tau" ]:
    for search_string in [ "1l_2tau", "2lss_1tau", "3l_1tau"]:
      if channel.find(search_string) != -1:
        channel_base = search_string
    ##datacardFile_input = os.path.join(datacardDir, channel_base, datacardFiles[channel] % shapeVariable)
    datacardFile_input = os.path.join(datacardDir, datacardFiles[channel])
    datacardFile_output = os.path.join(workingDir, "limits", "ttH_%s.root" % channel)
    run_cmd('rm ttH_%s.txt' % channel)
    run_cmd('rm %s' % datacardFile_output)
    run_cmd('%s --input_file=%s --output_file=%s --add_shape_sys=false' % (WriteDatacard_executables[channel], datacardFile_input, datacardFile_output))
    txtFile = datacardFile_output.replace(".root", ".txt")
    run_cmd('cp %s %s' % (datacardFile_output, datacardFile_output.replace("/limits/", "/")))
    ##run_cmd('combine -M MaxLikelihoodFit -t -1 -m 125 %s' % txtFile)
    run_cmd('combine -M MaxLikelihoodFit -m 125 %s' % txtFile)
    logFile = os.path.join(workingDir, "limits", "ttH_%s_%s_2016.log" % (channel, shapeVariable))
    run_cmd('rm %s' % logFile)
    ##run_cmd('combine -M Asymptotic -t -1 -m 125 %s &> %s' % (txtFile, logFile))
    run_cmd('combine -M Asymptotic -m 125 %s &> %s' % (txtFile, logFile))
    rootFile = os.path.join(workingDir, "limits", "ttH_%s_%s_2016_shapes.root" % (channel_base, shapeVariable))
    run_cmd('rm %s' % rootFile)
    run_cmd('PostFitShapes -d %s -o %s -m 125 -f mlfit.root:fit_s --postfit --sampling --print' % (txtFile, rootFile))
    ##run_cmd('root -b -n -q -l %s++' % os.path.join(workingDir, "macros", makePostFitPlots_macros[channel]))

