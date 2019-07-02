

class CCN:
    instrumentName = 'Cloud Condensation Nuclei Counter'
    instrumentDescription = 'Measures the count and size of the individual aerosol particles that can form into cloud droplets.'
    instrumentFile_Format = '.csv'
    instrumentVariables = ('Current SS', 'Column Temperature Stabilized', 'Delta T', 'T1 Set,', 'T1 Read', 'T2 Set', 'T2 Read', 'T3 Set', 'T3 Read', 'Naftion Set', 'T Naftion', 'Inlet Set', 'T Inlet', 'OCP Set', 'T OCP', 'T Sample', 'Sample Flow', 'Sample Pressure', 'Laser Current', 'Overflow', 'Baseline Mon', '1st Stage Mon', 'Bin #', 'Bin 1', 'Bin 2', 'Bin 3', 'Bin 4', 'Bin 5', 'Bin 6', 'Bin 7', 'Bin 8', 'Bin 9', 'Bin 10', 'Bin 11', 'Bin 12', 'Bin 12', 'Bin 13', 'Bin 14', 'Bin 15', 'Bin 16', 'Bin 17', 'Bin 18', 'Bin 19', 'Bin 20', 'CCN Number Conc', 'Valve Set', 'Alarm Code')
    instrumentVariablesNumber = len(instrumentVariables)

class WIBS_NEO:
    instrumentName = 'Wideband Integrated Bioaerosol Sensor'
    instrumentDescription = 'Provides detailed information on atmospheric bacteria, molds, pollen and other bioaerosols. '
    instrumentFile_Format = '.h5'
    instrumentMonitoringData = ('Board_1',
                                'Bandwidths_0',
                                'Bandwidths_1',
                                'Bandwidths_2',
                                'Bandwidths_3',
                                'Baseline_0',
                                'Baseline_1',
                                'Baseline_2',
                                'Baseline_3',
                                'Clump_Count',
                                'conc_excited_cm3',
                                'conc_total_cm3',
                                'H12310_Temperature',
                                'Max_Transit_Time_counts',
                                'Min_Transit_Time_counts',
                                'Missed_Particle_Count',
                                'Num_Discarded_Particles',
                                'Num_Oversize_Rejects',
                                'RH',
                                'SYS_V',
                                'Sample_MassFlow',
                                'Sample_PSIA',
                                'Sample_SetPoint',
                                'Sample_Temperature',
                                'Sample_VolumetricFlowRate',
                                'Monitored_Seconds',
                                'Sheath_MassFlow',
                                'Sheath_PSIA',
                                'Sheath_SetPoint',
                                'Sheath_Temperature',
                                'Sheath_VolumetricFlowRate',
                                'Sizer_Oversize_Count',
                                'Temperature',
                                'Total_Particle_Count',
                                'Total_Trigger_Count',
                                'Valid_Particle_Count',
                                'XE1_Power',
                                'XE2_Power')
    instrumentParticleData = ('Asphericity',
                              'Density_gcm3',
                              'EP_Overflow_Flag',
                              'Flag_Excited',
                              'Mass_ug',
                              'NF_Shape_0',
                              'NF_Shape_1',
                              'NF_Shape_2',
                              'NF_Shape_3',
                              'NF_Sizer_Relative_Peak',
                              'NF_Sizer_Transit_Time_nsec',
                              'Particle_Seconds',
                              'Size_um',
                              'Xe1_FluorPeak_A',
                              'Xe1_FluorPeak_B',
                              'Xe2_FluorPeak_A',
                              'Xe1_FluorPeak_B')
    instrumentVariables = instrumentMonitoringData + instrumentParticleData


class SP2_XR:
    instrumentName = 'Single Particle Soot Photometer'
    instrumentDescription = 'quantifies the black carbon (soot) in individual aerosol particles.'
    insttrumentFile_Format = 'dummy'

def SEMS(self):
    instrumentName = 'Scanning Electrical Mobility Spectrometer'
    instrumentDescription = ' allows rapid aerosol number size distribution measurements.'
    insttrumentFile_Format = 'dummy'

    # def CLAP (self):
    #     instrumentName =
    #     instrumentDescription =
    #     insttrumentFile_Format =
    # def ACSM (self):
    #     instrumentName = 'Aerosol Chemical Speciation Monitor'
    #     instrumentDescription =
    #     insttrumentFile_Format =
    # def TDHHL (self):
    #     instrumentName =
    #     instrumentDescription =
    #     insttrumentFile_Format =

