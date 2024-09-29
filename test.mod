add http://github.com/mikeoliphant/neural-amp-modeler-lv2 0
bypass 0 1
add http://distrho.sf.net/plugins/3BandEQ 1
bypass 1 1
add http://eq10q.sourceforge.net/eq/eq4qm 2
bypass 2 1
add http://lsp-plug.in/plugins/lv2/impulse_responses_stereo 3
bypass 3 1
add urn:dragonfly:room 4
bypass 4 1
connect system:capture_2 effect_0:input
connect effect_0:output effect_1:lv2_audio_in_1
connect effect_1:lv2_audio_out_1 effect_2:input
connect effect_2:output effect_3:in_l
connect effect_2:output effect_3:in_r
connect effect_3:out_l effect_4:lv2_audio_in_1
connect effect_3:out_r effect_4:lv2_audio_in_2
connect effect_4:lv2_audio_out_1 system:playback_1
connect effect_4:lv2_audio_out_2 system:playback_2
preset_load 0 "file:///home/jon/.lv2/Neural_Amp_Modeler_EnglLead1.preset.lv2/EnglLead1.ttl"
param_set 4 dry_level 100
preset_load 4 "file:///home/jon/.lv2/Dragonfly_Room_Reverb_VocalHall.preset.lv2/VocalHall.ttl"
param_set 1 low_mid 120
param_set 1 mid_high 2300
param_set 2 filter4_enable 1
param_set 2 filter4_gain -12
param_set 2 filter4_freq 8000
bypass 0 0
bypass 4 0
bypass 2 0
bypass 1 0
