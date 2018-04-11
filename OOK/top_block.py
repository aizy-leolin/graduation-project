#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 10 16:25:04 2018
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
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
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
        	1, samp_rate, samp_rate/decim+samp_rate/(decim *10), samp_rate/(decim *10), firdes.WIN_HAMMING, 6.76))
        self.digital_packet_headerparser_b_default_0 = digital.packet_headerparser_b(header_len, "packet_len")
        self.digital_header_payload_demux_0_2 = digital.header_payload_demux(
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
        self.digital_crc32_bb_0 = digital.crc32_bb(True, "packet_len", True)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/huangxf/graduation-project/OOK/test2.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.PHY_wave_to_float_single_cpp_0 = PHY.wave_to_float_single_cpp(decim)
        self.PHY_float_to_bit_single_cpp_0_0 = PHY.float_to_bit_single_cpp(0.5)
        self.PHY_float_to_bit_single_cpp_0 = PHY.float_to_bit_single_cpp(0.5)
        self.PHY_find_preamble_cpp_0 = PHY.find_preamble_cpp((0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0), 60, 500)
        self.PHY_conv_decode_tag_single_0 = PHY.conv_decode_tag_single("packet_len")

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_default_0, 'header_data'), (self.digital_header_payload_demux_0_2, 'header_data'))    
        self.connect((self.PHY_conv_decode_tag_single_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.PHY_find_preamble_cpp_0, 0), (self.digital_header_payload_demux_0_2, 1))    
        self.connect((self.PHY_float_to_bit_single_cpp_0, 0), (self.PHY_find_preamble_cpp_0, 0))    
        self.connect((self.PHY_float_to_bit_single_cpp_0_0, 0), (self.digital_packet_headerparser_b_default_0, 0))    
        self.connect((self.PHY_wave_to_float_single_cpp_0, 0), (self.PHY_float_to_bit_single_cpp_0, 0))    
        self.connect((self.PHY_wave_to_float_single_cpp_0, 0), (self.digital_header_payload_demux_0_2, 0))    
        self.connect((self.PHY_wave_to_float_single_cpp_0, 0), (self.qtgui_sink_x_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.PHY_wave_to_float_single_cpp_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_crc32_bb_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0_2, 1), (self.PHY_conv_decode_tag_single_0, 0))    
        self.connect((self.digital_header_payload_demux_0_2, 0), (self.PHY_float_to_bit_single_cpp_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.decim+self.samp_rate/(self.decim *10), self.samp_rate/(self.decim *10), firdes.WIN_HAMMING, 6.76))

    def get_header_len(self):
        return self.header_len

    def set_header_len(self, header_len):
        self.header_len = header_len

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.decim+self.samp_rate/(self.decim *10), self.samp_rate/(self.decim *10), firdes.WIN_HAMMING, 6.76))


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
