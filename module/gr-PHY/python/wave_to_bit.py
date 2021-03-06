#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr



class wave_to_bit(gr.decim_block):
    """
    docstring for block wave_to_bit
    """
    def __init__(self, decim):
        gr.decim_block.__init__(self,
            name="recv_bit",
            in_sig=[numpy.float32],
            out_sig=[numpy.byte], decim=decim)
        self.valuemax = 0
        self.valuemin = 0
        self.len = 0
        self.lenMax = 10000
        self.decim = decim
        #self.file=open('/home/huangxf/test/temp3.txt','w')
        
        self.interval = self.decim/10
        self.cache = numpy.zeros(0)
        self.cachelen = 0
        self.last = numpy.zeros(self.decim/2)
        self.state = False
        self.maxsplitdis = 0
        self.maxsplitpos = -1

    def bit_sync(self,arr):
        if self.cachelen > 0:
            maxdis = abs(self.cache/self.cachelen - sum(arr)/10)
        #maxdis = abs(sum(self.cache)/len(self.cache) - sum(arr[0:self.interval])/self.interval)
        else:
            maxdis = 0
        pos = -1

        for x in range(9):
            #dis = abs(sum(arr[x*self.interval:(x+1)*self.interval])-sum(arr[(x+1)*self.interval:(x+2)*self.interval]))
            #self.file.write(str(sum(arr[x*self.interval:(x+1)*self.interval]))+' ')
            dis = abs((sum(arr[0:(x+1)*self.interval])+self.cache)/(x+1+self.cachelen)-sum(arr[(x+1)*self.interval:])/(9-x))
            if maxdis < dis:
                maxdis = dis
                pos = x


        if pos < 0:
            self.cache = sum(arr[self.interval*9:])
            self.cachelen = 1
            #self.file.write('\n %d %f\n'%(pos,sum(arr)/self.decim))
            return sum(arr)/self.decim
        else:
            ans = (self.cache+sum(arr[0:(pos+1)*self.interval]))/((self.cachelen+pos+1)*self.interval)
            self.cache = sum(arr[self.interval*(pos+1):])
            self.cachelen = 9-pos
            #self.file.write('\n %d %f\n'%(pos,ans))
            return ans

    def corr(self,arr):

        tmp = numpy.append(self.last,arr)
        maxdis = 0
        maxpos = 0
        mindis = 10000000
        maxpos = 0
        for x in range(len(tmp)/self.interval-9):
            dis = sum(tmp[x*self.interval:(x+10)*self.interval])
            if maxdis < dis:
                maxdis = dis
                maxpos = x
            if mindis > dis:
                mindis = dis
                minpos =x
        #for x in range(10):
        #    self.file.write(str(sum(arr[x*self.interval:(x+1)*self.interval]))+' ')
        if self.state:
            if (mindis - self.valuemin) > (self.valuemax -maxdis):
                self.last = tmp[max(maxpos+9,len(self.last)/self.interval+1)*self.interval:].copy()
                #self.file.write('\n %d'%(maxpos-len(self.last)/self.interval,))
            else:
                self.last = tmp[max(minpos+9,len(self.last)/self.interval+1)*self.interval:].copy()
                #self.file.write('\n %d'%(minpos-len(self.last)/self.interval,))
        else:
            self.last = arr[self.interval:].copy()

        #self.file.write(' %f %f\n'%(mindis,maxdis))

        return mindis,maxdis

    def maxsplit(self,arr):
        maxdis = 0
        maxpos = 0
        for x in range(9):
            dis = abs(sum(arr[x*self.interval:(x+1)*self.interval])-sum(arr[(x+1)*self.interval:(x+2)*self.interval]))
            if dis > maxdis:
                maxdis = dis
                maxpos = x + 1
        if self.state:
            if (maxdis > self.maxsplitdis) or (maxdis * 10 > (self.valuemax - self.valuemin)*0.5):
                self.maxsplitdis = maxdis*0.1 + self.maxsplitdis * 0.9
                self.maxsplitpos = maxpos
        else:
            if maxdis > self.maxsplitdis:
                self.maxsplitdis = maxdis
                self.maxsplitpos = maxpos

        #for x in range(10):
        #    self.file.write(str(sum(arr[x*self.interval:(x+1)*self.interval]))+' ')
        #self.file.write('\n %f %f\n'%(self.maxsplitpos,self.maxsplitdis))
        if len(self.cache) == 0:
            self.cache = arr.copy()
            return sum(arr)
        ans = sum(self.cache[int(round(self.maxsplitpos))*self.interval:]) + sum(arr[:int(round(self.maxsplitpos))*self.interval])
        self.cache = arr.copy()
        return ans





    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>

        for i in range(0,len(in0)/self.decim):
            if self.decim < 10:
                tot = sum(in0[i*self.decim:(i+1)*self.decim])
                #tot2 = tot1
            else:
                #tot = self.bit_sync(in0[i*self.decim:(i+1)*self.decim])
                #tot1,tot2 = self.corr(in0[i*self.decim:(i+1)*self.decim])
                tot = self.maxsplit(in0[i*self.decim:(i+1)*self.decim])
                
            #tot = maxsum(in0[i*self.decim:(i+1)*self.decim])
            #tot = segsum(in0[i*self.decim:(i+1)*self.decim])
            if self.len < self.lenMax:
                if self.len == 0:
                    self.valuemin = tot
                    self.valuemax = tot
                    #self.valuemin = tot1
                    #self.valuemax = tot2
                    self.len += 1
                    continue 
                self.len += 1
                #print('len: %d'%self.len)
                
                if tot > self.valuemax:
                    self.valuemax = self.valuemax * 0.2 + tot * 0.8
                if tot < self.valuemin:
                    self.valuemin = self.valuemin * 0.5 + tot * 0.5
                continue
                '''
                if tot2 > self.valuemax:
                    self.valuemax = self.valuemax*0.2 + tot2*0.8
                if tot1 < self.valuemin:
                    self.valuemin = self.valuemin * 0.5 + tot1 * 0.5
                continue
            '''
            self.state = True
                        
            if tot > (self.valuemax * 0.3 + self.valuemin * 0.7):
                self.valuemax = self.valuemax * 0.9 + tot * 0.1
                out[i]=1
            else:
                self.valuemin = self.valuemin * 0.9 + tot * 0.1
                out[i]=0
            '''
            if (tot1 - self.valuemin) > (self.valuemax - tot2):
                self.valuemax = self.valuemax * 0.9 + tot2 * 0.1
                out[i]=1
            else:
                self.valuemin = self.valuemin * 0.9 + tot1 * 0.1
                out[i]=0
                '''
        #self.file.write(str(in0[-1])+' '+str(out[-1])+' '+str(self.valuemin)+' '+str(self.valuemax)+'\n')
        #self.file.write('----------------------\n'+str(self.valuemin)+' '+str(self.valuemax)+'\n---------------------------\n')
        #print('recv_bit: %f %f %f %f'%(in0[0],out[0],minout[0],maxout[0]))
        #print(len(out))
        return len(output_items[0])
