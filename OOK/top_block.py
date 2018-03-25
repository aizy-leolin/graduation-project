#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Mar 24 00:25:41 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PHY
import sip
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_0 = samp_rate_0 = 80000
        self.samp_rate = samp_rate = 8000000
        self.header_len = header_len = 12
        self.decim = decim = 10

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(433000000, 0)
        self.uhd_usrp_source_0.set_gain(80, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_1_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	433000000, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/decim, samp_rate/(decim *10), firdes.WIN_HAMMING, 6.76))
        self.digital_packet_headerparser_b_default_0 = digital.packet_headerparser_b(header_len, "packet_len")
        self.digital_header_payload_demux_0_2 = digital.header_payload_demux(
        	  header_len,
        	  1,
        	  0,
        	  "packet_len",
        	  "",
        	  True,
        	  gr.sizeof_char,
        	  "rx_time",
                  samp_rate/decim,
                  (),
            )
        self.digital_header_payload_demux_0_1 = digital.header_payload_demux(
        	  header_len,
        	  1,
        	  0,
        	  "packet_len",
        	  "",
        	  True,
        	  gr.sizeof_float,
        	  "rx_time",
                  samp_rate/decim,
                  (),
            )
        self.digital_header_payload_demux_0_0 = digital.header_payload_demux(
        	  header_len,
        	  1,
        	  0,
        	  "packet_len",
        	  "",
        	  True,
        	  gr.sizeof_float,
        	  "rx_time",
                  samp_rate/decim,
                  (),
            )
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  header_len,
        	  1,
        	  0,
        	  "packet_len",
        	  "",
        	  True,
        	  gr.sizeof_float,
        	  "rx_time",
                  samp_rate/decim,
                  (),
            )
        self.digital_crc32_bb_0 = digital.crc32_bb(True, "packet_len", False)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "", ""); self.blocks_tag_debug_0.set_display(True)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/huangxf/graduation-project/OOK/test2.txt", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/huangxf/graduation-project/OOK/test.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.PHY_wave_to_float_0 = PHY.wave_to_float(10)
        self.PHY_float_to_bit_tag_0_0 = PHY.float_to_bit_tag("packet_len")
        self.PHY_float_to_bit_0 = PHY.float_to_bit()
        self.PHY_find_preamble_0 = PHY.find_preamble((0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0),60)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.blocks_message_debug_0, 'print'))    
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))    
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.digital_header_payload_demux_0_0, 'header_data'))    
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.digital_header_payload_demux_0_1, 'header_data'))    
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.digital_header_payload_demux_0_2, 'header_data'))    
        self.connect((self.PHY_find_preamble_0, 0), (self.blocks_char_to_float_0_1, 0))    
        self.connect((self.PHY_find_preamble_0, 0), (self.digital_header_payload_demux_0, 1))    
        self.connect((self.PHY_find_preamble_0, 0), (self.digital_header_payload_demux_0_0, 1))    
        self.connect((self.PHY_find_preamble_0, 0), (self.digital_header_payload_demux_0_1, 1))    
        self.connect((self.PHY_find_preamble_0, 0), (self.digital_header_payload_demux_0_2, 1))    
        self.connect((self.PHY_float_to_bit_0, 0), (self.PHY_find_preamble_0, 0))    
        self.connect((self.PHY_float_to_bit_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.PHY_float_to_bit_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.PHY_float_to_bit_0, 0), (self.digital_header_payload_demux_0_2, 0))    
        self.connect((self.PHY_float_to_bit_tag_0_0, 0), (self.blocks_tag_debug_0, 0))    
        self.connect((self.PHY_float_to_bit_tag_0_0, 0), (self.digital_crc32_bb_0, 0))    
        self.connect((self.PHY_wave_to_float_0, 2), (self.PHY_float_to_bit_0, 2))    
        self.connect((self.PHY_wave_to_float_0, 1), (self.PHY_float_to_bit_0, 1))    
        self.connect((self.PHY_wave_to_float_0, 0), (self.PHY_float_to_bit_0, 0))    
        self.connect((self.PHY_wave_to_float_0, 0), (self.digital_header_payload_demux_0, 0))    
        self.connect((self.PHY_wave_to_float_0, 1), (self.digital_header_payload_demux_0_0, 0))    
        self.connect((self.PHY_wave_to_float_0, 2), (self.digital_header_payload_demux_0_1, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_1_0, 0))    
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.PHY_wave_to_float_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 1), (self.PHY_float_to_bit_tag_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.digital_header_payload_demux_0_0, 1), (self.PHY_float_to_bit_tag_0_0, 1))    
        self.connect((self.digital_header_payload_demux_0_0, 0), (self.blocks_null_sink_1, 1))    
        self.connect((self.digital_header_payload_demux_0_1, 1), (self.PHY_float_to_bit_tag_0_0, 2))    
        self.connect((self.digital_header_payload_demux_0_1, 0), (self.blocks_null_sink_1, 2))    
        self.connect((self.digital_header_payload_demux_0_2, 1), (self.blocks_null_sink_2, 0))    
        self.connect((self.digital_header_payload_demux_0_2, 0), (self.digital_packet_headerparser_b_default_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.decim, self.samp_rate/(self.decim *10), firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(433000000, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_header_len(self):
        return self.header_len

    def set_header_len(self, header_len):
        self.header_len = header_len

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.decim, self.samp_rate/(self.decim *10), firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
