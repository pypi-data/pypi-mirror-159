import numpy as np

'''
This is a hacked confige file, where physical shutter is used to control 568 laser port, and in software it is controlled by laser-enable line of 568 laser.
Valid only for a demo version of denchtop mesoSPIM, to recycle axisting 568nm laser.
'''

ui_options = {'dark_mode' : True, # Dark mode: Renders the UI dark if enabled
              'enable_x_buttons' : True, # Here, specific sets of UI buttons can be disabled
              'enable_y_buttons' : True,
              'enable_z_buttons' : True,
              'enable_f_buttons' : True,
              'enable_rotation_buttons' : True,
              'enable_loading_buttons' : True,
              'window_pos': (100, 100), # position of the main window on the screen, top left corner.
               }

'''
Waveform output for Galvos, ETLs etc.
'''

waveformgeneration = 'NI' # 'DemoWaveFormGeneration' or 'NI'

'''
Card designations need to be the same as in NI MAX, if necessary, use NI MAX
to rename your cards correctly.

A standard mesoSPIM configuration uses two cards:

PXI1Slot5 (old PXI_6229_2) is responsible for the lasers (analog intensity control)
PXI1Slot2 (old PXI_6229_1) is responsible for the shutters, ETL waveforms and galvo waveforms
'''

acquisition_hardware = {'master_trigger_out_line' : 'PXI1Slot2/port0/line1',
                        'camera_trigger_source' : '/PXI1Slot2/PFI0',
                        'camera_trigger_out_line' : '/PXI1Slot2/ctr0',
                        'stage_trigger_source' : '/PXI1Slot2/PFI0',
                        'stage_trigger_out_line' : '/PXI1Slot5/ctr0',
                        'galvo_etl_task_line' : 'PXI1Slot2/ao0:3',
                        'galvo_etl_task_trigger_source' : '/PXI1Slot2/PFI0',
                        'laser_task_line' :  'PXI1Slot5/ao0:3',
                        'laser_task_trigger_source' : '/PXI1Slot2/PFI0'}

'''
Human interface device (Joystick)
'''
sidepanel = 'Demo' #'Demo' or 'FarmSimulator'

'''
Digital laser enable lines
'''

laser = 'NI' # 'Demo' or 'NI'

''' Laser blanking indicates whether the laser enable lines should be set to LOW between
individual images or stacks. This is helpful to avoid laser bleedthrough between images caused by insufficient
modulation depth of the analog input (even at 0V, some laser light is still emitted).
'''
laser_blanking = 'images' # if 'images', laser is off before and after every image; if 'stacks', before and after stacks.

''' The laserdict keys are the laser designation that will be shown
in the user interface '''

laserdict = {'488 nm': 'PXI1Slot5/port0/line2',
             '520 nm': 'PXI1Slot5/port0/line3',
             '568 nm': 'PXI1Slot5/port0/line5', # do not use second BNC block, P0.1 <-> User1 assignment fails in hardware
             '638 nm': 'PXI1Slot5/port0/line4',
             }

'''
Assignment of the analog outputs of the Laser card to the channels
The Empty slots are placeholders.
'''

laser_designation = {'488 nm' : 0,
                     '520 nm' : 1,
                     '568 nm' : 3, # empty terminal, because this 568 is not modulated
                     '638 nm' : 2,
                      }

'''
Assignment of the galvos and ETLs to the 6229 AO channels.
'''

galvo_etl_designation = {'Galvo-L' : 0,
                         'Galvo-R' : 1,
                         'ETL-L' : 2,
                         'ETL-R' : 3,
                         }

'''
Shutter configuration
'''

shutter = 'NI' # 'Demo' or 'NI'
shutterdict = {'shutter_left' : 'PXI1Slot2/port0/line0', # empty terminal, because shutter is used for 568 control
              'shutter_right' : 'PXI1Slot2/port2/line0', # flip mirror control, labeled PFI8 on the BNC connector
              }

''' A bit of a hack: Shutteroptions for the GUI '''
shutteroptions = ('Left','Right')

''' A bit of a hack: Assumes that the shutter_left line is the general shutter
and the shutter_right line is the left/right switch (Right==True)'''

shutterswitch = True # Assumes that the shutter_left line is the general shutter

'''
Camera configuration
'''

'''
For a DemoCamera, only the following options are necessary
(x_pixels and y_pixels can be chosen arbitrarily):

camera_parameters = {'x_pixels' : 1024,
                     'y_pixels' : 1024,
                     'x_pixel_size_in_microns' : 6.5,
                     'y_pixel_size_in_microns' : 6.5,
                     'subsampling' : [1,2,4]}

For a Hamamatsu Orca Flash 4.0 V2 or V3, the following parameters are necessary:

camera_parameters = {'x_pixels' : 2048,
                     'y_pixels' : 2048,
                     'x_pixel_size_in_microns' : 6.5,
                     'y_pixel_size_in_microns' : 6.5,
                     'subsampling' : [1,2,4],
                     'camera_id' : 0,
                     'sensor_mode' : 12,    # 12 for progressive
                     'defect_correct_mode': 2,
                     'binning' : '1x1',
                     'readout_speed' : 1,
                     'trigger_active' : 1,
                     'trigger_mode' : 1, # it is unclear if this is the external lightsheeet mode - how to check this?
                     'trigger_polarity' : 2, # positive pulse
                     'trigger_source' : 2, # external
                    }

For a Photometrics Iris 15, the following parameters are necessary:

camera_parameters = {'x_pixels' : 5056,
                     'y_pixels' : 2960,
                     'x_pixel_size_in_microns' : 4.25,
                     'y_pixel_size_in_microns' : 4.25,
                     'subsampling' : [1,2,4],
                     'speed_table_index': 0,
                     'exp_mode' : 'Edge Trigger', # Lots of options in PyVCAM --> see constants.py
                     'readout_port': 0,
                     'gain_index': 1,
                     'exp_out_mode': 4, # 4: line out
                     'binning' : '1x1',
                     'scan_mode' : 1, # Scan mode options: {'Auto': 0, 'Line Delay': 1, 'Scan Width': 2}
                     'scan_direction' : 0, # Scan direction options: {'Down': 0, 'Up': 1, 'Down/Up Alternate': 2}
                     'scan_line_delay' : 6, # 10.26 us x factor, a factor = 6 equals 71.82 us
                    }

For a Photometrics Prime BSI Express, the following parameters are necessary:

camera_parameters = {'x_pixels' : 2048, #5056
                     'y_pixels' : 2048, # 2960
                     'x_pixel_size_in_microns' : 6.5,
                     'y_pixel_size_in_microns' : 6.5,
                     'subsampling' : [1,2,4],
                     'speed_table_index': 1, # 1 for 100 MHz
                     'exp_mode' : 'Edge Trigger', # Lots of options in PyVCAM --> see constants.py
                     'readout_port': 0,
                     'gain_index': 1, # Enable HDR mode
                     'exp_out_mode': 4, # 4: line out
                     'binning' : '1x1',
                     'scan_mode' : 1, # Scan mode options: {'Auto': 0, 'Line Delay': 1, 'Scan Width': 2}
                     'scan_direction' : 0, # Scan direction options: {'Down': 0, 'Up': 1, 'Down/Up Alternate': 2}
                     'scan_line_delay' : 3, # 11.2 us x factor, a factor = 3 equals 33.6 us
                    }

'''
camera = 'Photometrics' # 'DemoCamera' or 'HamamatsuOrcaFlash' or 'Photometrics'

camera_parameters = {'x_pixels' : 5056,
                     'y_pixels' : 2960,
                     'x_pixel_size_in_microns' : 4.25,
                     'y_pixel_size_in_microns' : 4.25,
                     'subsampling' : [1,2,4],
                     'speed_table_index': 0,
                     'exp_mode' : 'Edge Trigger', # Lots of options in PyVCAM --> see constants.py
                     'readout_port': 0,
                     'gain_index': 1,
                     'exp_out_mode': 4, # 4: line out
                     'binning' : '1x1',
                     'scan_mode' : 1, # Scan mode options: {'Auto': 0, 'Line Delay': 1, 'Scan Width': 2}
                     'scan_direction' : 0, # Scan direction options: {'Down': 0, 'Up': 1, 'Down/Up Alternate': 2}
                     'scan_line_delay' : 6, # 10.26 us x factor, a factor = 6 equals 71.82 us
                    }

binning_dict = {'1x1': (1,1), '2x2':(2,2), '4x4':(4,4)}

'''
Stage configuration
'''

'''
The stage_parameter dictionary defines the general stage configuration, initial positions,
and safety limits. The rotation position defines a XYZ position (in absolute coordinates)
where sample rotation is safe. Additional hardware dictionaries (e.g. pi_parameters)
define the stage configuration details.
'''

stage_parameters = {'stage_type' : 'TigerASI', # 'DemoStage','PI','TigerASI' or other configs found in mesoSPIM_serial.py
                    'startfocus' : -13000,
                    'y_load_position': 10000,
                    'y_unload_position': -23000,
                    'ttl_motion_enabled': True, # Controls whether stage movement is triggered by TTL pulses during acquisitions. Only available for ASI stages.
                    'x_max' : 51000,
                    'x_min' : -46000,
                    'y_max' : 160000,
                    'y_min' : -160000,
                    'z_max' : 99000,
                    'z_min' : -99000,
                    'f_max' : 99000,
                    'f_min' : -99000,
                    'theta_max' : 999,
                    'theta_min' : -999,
                    'x_rot_position': 0,
                    'y_rot_position': 0,
                    'z_rot_position': 0,
                    }
'''
Depending on the stage hardware, further dictionaries define further details of the stage configuration

For a standard mesoSPIM V4 with PI stages, the following pi_parameters are necessary (replace the
serialnumber with the one of your controller):
'''
'''
pi_parameters = {'controllername' : 'C-884',
                 'stages' : ('M-605.2DD','L-406.40DG10','M-112K033','M-116.DG','M-112K033','NOSTAGE'), # M-605.2DD, M-112K033
                 'refmode' : ('FRF',),
                 'serialnum' : ('119046748'),
                 }
'''

'''
For a standard mesoSPIM V5 with PI stages, the following pi_parameters are necessary (replace the
serialnumber with the one of your controller):

pi_parameters = {'controllername' : 'C-884',
                 'stages' : ('L-509.20DG10','L-509.40DG10','L-509.20DG10','M-060.DG','M-406.4PD','NOSTAGE'),
                 'refmode' : ('FRF',),
                 'serialnum' : ('118015799'),
'''

'''
For a benchtop mesoSPIM with an ASI Tiger controller, the following parameters are necessary.
The stage assignment dictionary assigns a mesoSPIM stage (xyzf and theta - dict key) to an ASI stage (XYZ etc)
which are the values of the dict.
'''

asi_parameters = {'COMport' : 'COM23',
                  'baudrate' : 115200,
                  # Important: The stage assignment dict has to be written in the order of installation of ASI cards
                  # This is necessary as the ASI controller always reports the stage position in the same order after a "W XYZVWT" command, no
                  # matter what order of stage designations is sent
                  # V -> (W, not necessary, because linked to V) -> Z -> T -> X -> Y
                  # X -> Y -> Z -> T -> V -> W
                  # {'y':'V', 'z':'Z', 'theta':'F', 'x':'X', 'f':'Y',} is an interim assignment - here, the Z/T card got a new firmware for
                  'stage_assignment': {'y':'V', 'z':'Z', 'theta':'R', 'x':'X', 'f':'Y'},
                  'encoder_conversion': {'V': 10., 'Z': 10., 'R': 100., 'X': 10., 'Y': 10.}, # num of encoder counts per um or degree, depending on stage type.
                  # List of card IDs that have to be triggered in TTL mode (see stage_parameters) These are usually the
                  # cards controlling the sample z-movement and the focus stage (for focus tracking acquisitions).
                  # For an MS-2000 controller, set this parameter to None
                  'ttl_cards':(2,3),
                  }

'''
Filterwheel configuration
'''

'''
For a DemoFilterWheel, no COMport needs to be specified, for a Ludl Filterwheel,
a valid COMport is necessary.
'''
filterwheel_parameters = {'filterwheel_type' : 'DemoFilterWheel', # 'DemoFilterWheel' or 'Ludl' or 'DynamixelFilterWheel'
                          'servo_id' :  1,
                          'COMport' : 'COM15',
                          'baudrate' : 115200}

# Ludl marking 10 = position 0

'''

A Ludl double filter wheel can be
'''

filterdict = {'405-488-561-640-Quadrupleblock' : 0, # Every config should contain this
              '533 540/15' : 1,
              '576 605/65' : 2,
              'Filter 4' : 3,
              'Empty-Alignment' : 4,
              }

filterpositiondict = {  0 : 1515,
                        1 : 2340,
                        2 : 3255,
                        3 : 3975,
                        4 : 4780,
                    }

'''
Zoom configuration
'''

'''
For the DemoZoom, servo_id, COMport and baudrate do not matter. For a Dynamixel zoom,
these values have to be there
'''
zoom_parameters = {'zoom_type' : 'DemoZoom', # 'DemoZoom' or 'Dynamixel'
                   'servo_id' :  1,
                   'COMport' : 'COM9',
                   'baudrate' : 115200} # 57142

'''
The keys in the zoomdict define what zoom positions are displayed in the selection box
(combobox) in the user interface.
'''

zoomdict = {'1x' : 0,
            }
'''
Pixelsize in micron
'''
pixelsize = {'1x' : 4.72,
            }

'''
Initial acquisition parameters

Used as initial values after startup

When setting up a new mesoSPIM, make sure that:
* 'max_laser_voltage' is correct (5 V for Toptica MLEs, 10 V for Omicron SOLE)
* 'galvo_l_amplitude' and 'galvo_r_amplitude' (in V) are correct (not above the max input allowed by your galvos)
* all the filepaths exist
* the initial filter exists in the filter dictionary above
'''

startup = {
'state' : 'init', # 'init', 'idle' , 'live', 'snap', 'running_script'
'samplerate' : 100000,
'sweeptime' : 0.26734,
'position' : {'x_pos':0,'y_pos':0,'z_pos':0,'f_pos':0,'theta_pos':0},
'ETL_cfg_file' : 'config/etl_parameters/ETL-parameters.csv',
'filepath' : '/tmp/file.raw',
'folder' : '/tmp/',
'snap_folder' : '/tmp/',
'file_prefix' : '',
'file_suffix' : '000001',
'zoom' : '1x',
'pixelsize' : 6.55,
'laser' : '488 nm',
'max_laser_voltage':3.3,
'intensity' : 3,
'shutterstate':False, # Is the shutter open or not?
'shutterconfig':'Left', # Can be "Left", "Right","Both","Interleaved"
'laser_interleaving':False,
'filter' : '405-488-561-640-Quadrupleblock',
'etl_l_delay_%' : 7.5,
'etl_l_ramp_rising_%' : 83,
'etl_l_ramp_falling_%' : 2.5,
'etl_l_amplitude' : 0.7,
'etl_l_offset' : 2.3,
'etl_r_delay_%' : 2.5,
'etl_r_ramp_rising_%' : 5,
'etl_r_ramp_falling_%' : 83,
'etl_r_amplitude' : 0.65,
'etl_r_offset' : 2.36,
'galvo_l_frequency' : 199.9,
'galvo_l_amplitude' : 8.0,
'galvo_l_offset' : 0,
'galvo_l_duty_cycle' : 50,
'galvo_l_phase' : np.pi/7,
'galvo_r_frequency' : 199.9,
'galvo_r_amplitude' : 8.0,
'galvo_r_offset' : 0,
'galvo_r_duty_cycle' : 50,
'galvo_r_phase' : np.pi/7,
'laser_l_delay_%' : 10,
'laser_l_pulse_%' : 87,
'laser_l_max_amplitude_%' : 100,
'laser_r_delay_%' : 10,
'laser_r_pulse_%' : 87,
'laser_r_max_amplitude_%' : 100,
'stage_trigger_delay_%' : 92.5, # Set to 92.5 for stage triggering exactly after the ETL sweep
'stage_trigger_pulse_%' : 1,
'camera_delay_%' : 10,
'camera_pulse_%' : 1,
'camera_exposure_time':0.02,
'camera_line_interval':0.000075,
'camera_display_live_subsampling': 2,
'camera_display_snap_subsampling': 1,
'camera_display_acquisition_subsampling': 2,
'camera_binning':'1x1',
'camera_sensor_mode':'ASLM',
'average_frame_rate': 3.44,
}
