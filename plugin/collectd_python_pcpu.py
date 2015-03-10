"""
  collectd_python_pcpu


"""

import collectd

def log_verbose(msg):
  if not PLUGIN_VERBOSE:
    return
  collectd.info('collectd_python_pcpu [verbose]: %s' % msg )

def configure_callback(conf):
  global IOSTAT_INTERVAL, IOSTAT_VERBOSE, IOSTAT_HOST, IOSTAT_UNIT
  for node in conf.children:
    if node.key == 'Verbose':
      PLUGIN_VERBOSE = node.values[0]
    elif node.key == 'Host':
      PLUGIN_HOST = node.values[0]
    elif node.key == 'Interval':
      PLUGIN_INTERVAL = node.values[0]
    elif node.key == 'SampleInt':
      PLUGIN_SAMPLEINT == node.values[0]
    else:
      collectd.warning('collectd_python_pcpu plugin: Unknown config key: %s.' % node.key )

def read_callback(stats=None)
  log_verbose('Read callback called')

  stats = get_cpustats()

  if not stats:
    collectd.error('collectd_python_iostat plugin: No statistics received')
    return

  for metric,value in stats:
    print metric value

def get_cpustats()
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

  time.sleep(PLUGIN_SAMPLEINT)

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


def dispatch_item(metric,value):
  if not type_instance:
    type_instance = key
  
  vl = collectd.Values()
  vl.type = type
  vl.type_instance = type_instance
  vl.plugin = 'pcpu'
  vl.plugin_instance = metric 
  vl.values = [value]
  vl.dispatch()

collectd.register_config(configure_callback)
collectd.register_read(read_callback, PLUGIN_INTERVAL)
