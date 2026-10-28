#!/usr/bin/env python3
"""Run one explicitly bounded benchmark and record reproducibility metadata."""
import argparse,hashlib,json,platform,subprocess,time,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--timeout',type=float,default=60);p.add_argument('--n',type=int,required=True);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
if not a.command or a.timeout<=0 or a.n not in (5,6,7,8):p.error('need a command, positive timeout and n=5..8')
t0=time.monotonic()
try:
 r=subprocess.run(a.command,capture_output=True,timeout=a.timeout);status='finished'if r.returncode==0 else'failed';code=r.returncode;output=r.stdout
except subprocess.TimeoutExpired as e:status='timeout';code=None;output=e.stdout or b''
print(json.dumps({'n':a.n,'command':a.command,'timeout_seconds':a.timeout,'elapsed_seconds':time.monotonic()-t0,'status':status,'exit_code':code,'stdout_sha256':hashlib.sha256(output).hexdigest(),'machine':platform.machine(),'platform':platform.platform(),'python':sys.version,'boxes':None,'certified_count':None,'interpretation':'timing only; no scaling extrapolation or proof status inferred'},indent=2))
