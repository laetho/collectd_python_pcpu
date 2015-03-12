#!/usr/bin/python

import os
import time

def get_cpustats():

  fd = open('/proc/stat')
  buf = fd.readlines()[0].split()

  user, nice, sys, idle, iowait, irq, sirq, steal, guest, guestn = (
    float(buf[1]), float(buf[2]),
    float(buf[3]), float(buf[4]),
    float(buf[5]), float(buf[6]),
    float(buf[7]), float(buf[8]),
    float(buf[9]), float(buf[10])
  )
  fd.close()

  time.sleep(1)

  fd = open('/proc/stat')
  buf = fd.readlines()[0].split()

  user_n, nice_n, sys_n, idle_n, iowait_n, irq_n, sirq_n, steal_n, guest_n, guestn_n = (
    float(buf[1]), float(buf[2]),
    float(buf[3]), float(buf[4]),
    float(buf[5]), float(buf[6]),
    float(buf[7]), float(buf[8]),
    float(buf[9]), float(buf[10])
  )
  fd.close()

  # Calculate delta jiffies.
  dj = ( (user_n-user)
      +(nice_n-nice)
      +(sys_n-sys)
      +(idle_n-idle)
      +(iowait_n-iowait)
      +(irq_n-irq)
      +(sirq_n-sirq)
      +(steal_n-steal)
      +(guest_n-guest)
      +(guestn_n-guestn) )

  user   = (((user_n - user) / dj) * 100)
  nice   = (((nice_n - nice) / dj) * 100)
  sys    = (((sys_n - sys) / dj ) * 100)
  idle   = (((idle_n - idle) / dj ) * 100)
  iowait = (((iowait_n - iowait) / dj ) * 100)
  irq    = (((irq_n - irq) / dj ) * 100)
  sirq   = (((sirq_n - sirq) / dj ) * 100)
  steal  = (((steal_n - steal) / dj ) * 100)
  guest  = (((guest_n - guest) / dj ) * 100)
  guestn = (((guestn_n - guestn) / dj ) * 100)

  return {'user':user, 
          'nice':nice,
          'sys':sys,
          'idle':idle,
          'iowait':iowait,
          'irq':irq,
          'sirq':sirq,
          'steal':steal,
          'guest':guest,
          'guestn':guestn}

stats = get_cpustats()

for metric,value in stats.items():
  print (str(metric) + ":" + str(value)) 

