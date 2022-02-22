<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="SSVEP" version="2.0">
	<nodes>
		<node id="0" name="FIR Filter" position="(332.0, 145.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="bandpass filter" uuid="26939834-3a48-40ee-b1c1-be705d0551b2" version="1.0.0" />
		<node id="1" name="Time Series Plot" position="(492.0, 203.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="filtered EEG data" uuid="25d2df7c-de50-423b-9411-cf50d1f32ea2" version="1.0.1" />
		<node id="2" name="LSL Input" position="(53.0, 135.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="975556c0-7056-4bbf-b4c2-7d2ec1dad785" version="1.0.0" />
		<node id="3" name="LSL Output" position="(486.0, 87.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="ea8ad4e6-a294-46fe-a8f7-e4eaf1433061" version="1.0.0" />
		<node id="4" name="Inspect Data" position="(579.0, 357.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="cc9ac9f6-83f4-4479-9e26-be0c904274e0" version="2.1.1" />
		<node id="5" name="Time Series Plot" position="(207.0, 32.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="raw EEG data" uuid="6ef38556-3c1e-42e1-9d57-c9647afe8bc0" version="1.0.1" />
		<node id="6" name="Print To Console" position="(700.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="a9dd9e35-be6b-43ac-afd0-7bbd55cc30d4" version="1.0.0" />
		<node id="7" name="FIR Filter" position="(198.0, 143.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="50Hz bandstop" uuid="0c81aead-a1c4-46bb-888a-654013a46fad" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="2" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsDSwRLO0s8ZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29y
ZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAACvgAAAZkAAAQ1AAACWwAAAsYAAAG4AAAE
LQAAAlMAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3BfYXR0
ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAfcAAACfAAADbgAAAlcAAAH/AAAAvgAAA2YA
AAJPAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkSwNYBQAAAHRpdGxlcSVYEQAAAGZpbHRlcmVkIEVFRyBkYXRhcSZYCgAAAHplcm9fY29s
b3JxJ1gHAAAAIzdGN0Y3RnEoWAgAAAB6ZXJvbWVhbnEpiHUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gSAAAAbmFtZT0nb3BlbkJDSWRhdGEncQxYBwAAAHJlY292ZXJxDYhY
FAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5HP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFy
cmF5cRJDLgHZ0MsAAQAAAAADAwAAAX0AAAR6AAACWQAAAwsAAAGcAAAEcgAAAlEAAAAAAABxE4Vx
FIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAwMAAAEZAAAEegAA
Ar0AAAMLAAABOAAABHIAAAK1AAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETWAsAAABpZFNTVkVQX0NDQXEUWAUA
AABzcmF0ZXEVWA0AAAAodXNlIGRlZmF1bHQpcRZYCwAAAHN0cmVhbV9uYW1lcRdYCQAAAFNTVkVQ
X0NDQXEYWAsAAABzdHJlYW1fdHlwZXEZWAMAAABFRUdxGlgTAAAAdXNlX2RhdGFfdGltZXN0YW1w
c3EbiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEciXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGIWAoAAABhdXRvX2Nsb3NlcQKJWAgAAABjb2xfYXhp
c3EDWAQAAAB0aW1lcQRYCAAAAGRlY2ltYWxzcQVLBlgNAAAAZXZlcnlfbl90aWNrc3EGSwFYDQAA
AGZld2VyX2J1dHRvbnNxB4hYCQAAAGZvbnRfc2l6ZXEISwpYEAAAAGluaXRpYWxfcG9zaXRpb25x
CV1xCihLFEsyTfQBTZABZVgIAAAAcm93X2F4aXNxC1gFAAAAc3BhY2VxDFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAA
AFFCeXRlQXJyYXlxEEMuAdnQywABAAAAAAMDAAABJgAABHwAAAK4AAADDAAAAUwAAARzAAACrwAA
AAAAAHERhXESh3ETUnEUWA4AAABzZXRfYnJlYWtwb2ludHEViVgPAAAAc2hvd19heGVzX3RhYmxl
cRaIWA8AAABzaG93X2RhdGFfdGFibGVxF4hYEgAAAHNob3dfbWFya2Vyc190YWJsZXEYiFgQAAAA
c2hvd19tYXhfY29sdW1uc3EZSxRYDwAAAHNob3dfbWF4X3ZhbHVlc3EaSzJYEgAAAHNob3dfc3Ry
ZWFtc190YWJsZXEbiFgLAAAAc3RyZWFtX25hbWVxHFgNAAAAKHVzZSBkZWZhdWx0KXEdWAwAAAB3
aW5kb3dfdGl0bGVxHlgTAAAASW5zcGVjdCBEYXRhIFBhY2tldHEfdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAfcAAACfAAADbgAAAlcAAAH/AAAAvgAAA2YA
AAJPAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkSwNYBQAAAHRpdGxlcSVYDAAAAHJhdyBFRUcgZGF0YXEmWAoAAAB6ZXJvX2NvbG9ycSdY
BwAAACM3RjdGN0ZxKFgIAAAAemVyb21lYW5xKYh1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABvbmx5X25vbmVtcHR5cQGJWA0AAABwcmludF9jaGFubmVscQKJWA0AAABwcmlu
dF9jb21wYWN0cQOJWAoAAABwcmludF9kYXRhcQSIWA0AAABwcmludF9tYXJrZXJzcQWIWA0AAABw
cmludF9zdHJlYW1zcQZdcQdYCgAAAHByaW50X3RpbWVxCIlYCwAAAHByaW50X3RyaWFscQmJWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cQpjc2lwCl91bnBpY2tsZV90eXBlCnELWAwAAABQeVF0NC5R
dENvcmVxDFgKAAAAUUJ5dGVBcnJheXENQy4B2dDLAAEAAAAAAwMAAAFPAAAEfAAAAo8AAAMMAAAB
dQAABHMAAAKGAAAAAAAAcQ6FcQ+HcRBScRFYDgAAAHNldF9icmVha3BvaW50cRKJdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsxSzNlWA0AAABtaW5pbXVtX3BoYXNlcQmIWAQAAABtb2RlcQpY
CAAAAGJhbmRzdG9wcQtYBQAAAG9yZGVycQxYDQAAACh1c2UgZGVmYXVsdClxDVgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEOY3NpcApfdW5waWNrbGVfdHlwZQpxD1gMAAAAUHlRdDQuUXRDb3JlcRBY
CgAAAFFCeXRlQXJyYXlxEUMuAdnQywABAAAAAAHvAAABAwAAA2YAAAG2AAAB9wAAASIAAANeAAAB
rgAAAAAAAHEShXETh3EUUnEVWA4AAABzZXRfYnJlYWtwb2ludHEWiVgKAAAAc3RvcF9hdHRlbnEX
R0BJAAAAAAAAdS4=
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node1",
            "data",
            "node4",
            "data"
        ],
        [
            "node3",
            "data",
            "node6",
            "data"
        ],
        [
            "node3",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node1",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        3,
                        4,
                        59,
                        60
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "26939834-3a48-40ee-b1c1-be705d0551b2"
        },
        "node2": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 3
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "filtered EEG data"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "25d2df7c-de50-423b-9411-cf50d1f32ea2"
        },
        "node3": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Ch0",
                        "Ch1",
                        "Ch2",
                        "Ch3",
                        "Ch4",
                        "Ch5",
                        "Ch6",
                        "Ch7"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='openBCIdata'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "975556c0-7056-4bbf-b4c2-7d2ec1dad785"
        },
        "node4": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "idSSVEP_CCA"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "SSVEP_CCA"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "ea8ad4e6-a294-46fe-a8f7-e4eaf1433061"
        },
        "node5": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 50
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "cc9ac9f6-83f4-4479-9e26-be0c904274e0"
        },
        "node6": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 3
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "raw EEG data"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "6ef38556-3c1e-42e1-9d57-c9647afe8bc0"
        },
        "node7": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "only_nonempty": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "print_data": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "print_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a9dd9e35-be6b-43ac-afd0-7bbd55cc30d4"
        },
        "node8": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        49,
                        51
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "bandstop"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "0c81aead-a1c4-46bb-888a-654013a46fad"
        }
    },
    "version": 1.1
}</patch>
</scheme>
