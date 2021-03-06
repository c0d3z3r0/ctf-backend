from dynamic_preferences.types import \
    StringPreference, LongStringPreference, IntegerPreference
from dynamic_preferences.registries import global_preferences_registry


@global_preferences_registry.register
class BackendTitle(StringPreference):
    section = 'general'
    name = 'sitename'
    verbose_name = 'Backend Title'
    default = 'CTF-Backend'
    help_text = 'The website title (Default: '+default+')'


@global_preferences_registry.register
class Background(LongStringPreference):
    section = 'general'
    name = 'background'
    verbose_name = 'Background'
    default = """\
0000000: ffd8 ffe0 0010 7466 4855 0001 0101 0048  ......tfHU.....H
0000010: 0048 0000 ffdb 0043 0003 0202 0302 0203  .H.....C........
0000020: 0303 0304 0303 0405 0805 0504 0405 0a07  ................
0000030: 0706 080c 0a0c 0c0b 0a0b 0b0d 0e12 100d  ................
0000040: 0e11 0e0b 0b10 1610 1113 1415 1515 0c0f  ................
0000050: 1718 1614 1812 1415 14ff db00 4301 0304  ............C...
0000060: 0405 0405 0905 0509 140d 0b0d 1414 1414  ................
0000070: 1414 1414 1414 1414 1414 1414 1414 1414  ................
0000080: 1414 1414 1414 1414 1414 1414 1414 1414  ................
0000090: 1414 1414 1414 1414 1414 1414 1414 ffc2  ................
00000a0: 0011 0800 6401 9003 0111 0002 1101 0311  ....d...........
00000b0: 01ff c400 1b00 0100 0301 0101 0100 0000  ................
00000c0: 0000 0000 0000 0004 0506 0708 0302 ffc4  ................
00000d0: 0014 0101 0000 0000 0000 0000 0000 0000  ................
00000e0: 0000 0000 ffda 000c 0301 0002 1003 1000  ................
00000f0: 0001 f548 0000 0000 0000 0000 0000 0000  ...H............
0000100: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000110: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000120: 0000 0000 0000 0000 0000 0000 0004 43cb  ..............C.
0000130: c772 2e4a 137e 64cc c17c 7373 5c68 0cc1  .r.J.~d..|ss\h..
0000140: 765f 19c2 9cfc 9524 735c 4228 cd31 620a  v_.....$s\B(.1b.
0000150: 7354 624c a1d3 0c51 1094 5a9b 439e 1ae2  sTbL...Q..Z.C...
0000160: 69b4 0000 0000 1c00 8c62 8be3 d3e7 0731  i........b.....1
0000170: 2483 2e75 f2a8 8c60 8e80 4321 928d a991  $..u...`..C!....
0000180: 2013 8ad3 5054 9853 a69d 20fc 98e2 a8c6   ...PT.S.. .....
0000190: 9d14 ab33 a6a8 e647 4036 e74e 0000 0000  ...3...G@6.N....
00001a0: 0045 39c1 5275 c258 0011 0960 0000 0000  .E9.Ru.X...`....
00001b0: 0000 0000 0000 0000 000f 3d97 a678 b432  ..........=..x.2
00001c0: a746 290b 839f 9af3 ee60 0da9 fa22 9527  .F)......`...".'
00001d0: 473e e549 d540 0000 0000 0000 0000 0000  G>.I.@..........
00001e0: 03cf e5d9 624b 32c0 a436 45c9 9a3e 0541  ....bK2..6E..>.A
00001f0: b62e 4fb1 cb8d d120 cf1b b34a 0000 0000  ..O.... ...J....
0000200: 0000 0000 0000 0000 0000 0000 0002 214a  ..............!J
0000210: 6940 0000 0000 0000 0000 0000 0000 0a00  i@..............
0000220: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000230: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000240: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000250: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0000260: 0000 0000 007f ffc4 0028 1000 0301 0001  .........(......
0000270: 0204 0505 0000 0000 0000 0004 0506 0302  ................
0000280: 0107 0014 1516 1330 3650 7012 1720 2640  .......06Pp.. &@
0000290: ffda 0008 0101 0001 0502 fc36 5959 022e  ...........6YY..
00002a0: 9766 39dc 5a31 c095 5d42 b9b2 f16f 509b  .f9.Z1..]B...oP.
00002b0: cfc3 8ab5 2836 9ca8 e9a8 0257 ac66 bbad  ....(6.....W.f..
00002c0: abe1 95b5 7ed7 6793 4ffd 754a 4ad2 9bd5  ....~.g.O.uJJ...
00002d0: 30b9 44ac d62e 075e b231 e1af 04eb 6046  0.D....^.1....`F
00002e0: d5ee 9c53 ace3 5ddc 0c97 2c5f 5cc5 9747  ...S..]...,_\..G
00002f0: 144c 51cf 2ea1 703d 0e96 8e75 15bd 397c  .LQ...p=...u..9|
0000300: cb9b a1d5 8e61 dda1 6075 050b 850e 1efa  .....a..`u......
0000310: df84 1604 f919 4b16 2fba c73b 35d8 b958  ......K./..;5..X
0000320: bc31 7d77 70b1 c0a1 ab1d 34c9 b57f 3d12  .1}wp.....4...=.
0000330: a7aa 52ff 0069 4ee1 03cd 1352 297c e49b  ..R..iN....R)|..
0000340: fd28 96fc c5bf 4b35 724a 9940 8635 9ab6  .(....K5rJ.@.5..
0000350: cfd5 3cd7 c14c 8599 ba5a cf75 5233 859b  ..<..L...Z.uR3..
0000360: b556 3e97 c042 5b63 1d64 bd23 7672 6171  .V>..B[c.d.#vraq
0000370: a1e1 dc60 f990 8315 489d f55d 2e3d 1980  ...`....H..].=..
0000380: 181d 1afa 1a5b 65ed 9e58 1181 6152 02a8  .....[e..X..aR..
0000390: 2abe 9ea1 c7b7 f29e 97c2 b477 3c52 486f  *..........w<RHo
00003a0: fd29 d730 8ca5 5249 5c58 afee 1d42 cc4e  .).0..RI\X...B.N
00003b0: 36a4 4f6a c4ab eaa2 6209 a0c9 7b6d dbca  6.Oj....b...{m..
00003c0: 859b 1cfc 64fc 3994 1f55 d482 d063 127b  ....d.9..U...c.{
00003d0: 559a 2882 1590 b4d7 499d 2ec7 b72e b79b  U.(.....I.......
00003e0: f25d bbf3 3d27 be71 78f5 2451 238a e4d3  .]..='.qx.$Q#...
00003f0: 201d ee58 99eb 88bf c4a2 f007 0fb3 73ee   ..X..........s.
0000400: 21a7 72f7 d14e 3856 356b f026 7513 21e0  !.r..N8V5k.&u.!.
0000410: 7366 04dc a569 0d5b 0f70 7e0e 79d0 bc6e  sf...i.[.p~.y..n
0000420: cde7 2136 a696 765f b4d0 dc69 b135 ae9e  ..!6..v_...i.5..
0000430: b586 254e 3616 536a 87a5 4102 8c21 a8a9  ..%N6.Sj..A..!..
0000440: e580 49e2 8280 e1da fa49 742a fb5d f427  ..I......It*.].'
0000450: fbff 006f 8c59 a728 f661 f825 03a3 c642  ...o.Y.(.a.%...B
0000460: 818e 6efd 886f 2855 70a6 e0cc 2edd 31c7  ..n..o(Up.....1.
0000470: 9739 e78a 19b2 169b f49b 01cf da69 e108  .9...........i..
0000480: c1b9 d154 864e 3540 d717 8811 6d3e 8e49  ...T.N5@....m>.I
0000490: 1f29 e44b a6ab 8066 fe7c f21a fc3a 7e0a  .).K...f.|...:~.
00004a0: e400 691e b32a 64fb ebf7 0284 c0ec 3299  ..i..*d.......2.
00004b0: 4f86 bf98 3fff c400 1411 0100 0000 0000  O...?...........
00004c0: 0000 0000 0000 0000 0000 90ff da00 0801  ................
00004d0: 0301 013f 0122 bfff c400 1411 0100 0000  ...?."..........
00004e0: 0000 0000 0000 0000 0000 0000 90ff da00  ................
00004f0: 0801 0201 013f 0122 bfff c400 3d10 0001  .....?."....=...
0000500: 0302 0501 0505 0508 0007 0000 0000 0102  ................
0000510: 0304 0511 0012 1321 3141 0614 2251 6115  .......!1A.."Qa.
0000520: 3271 81a1 2342 6291 b110 1630 3350 5270  2q..#Bb....03PRp
0000530: d120 7483 b2b3 c1c2 ffda 0008 0101 0006  . t.............
0000540: 3f02 ff00 0dbd 25e5 6465 9417 16ab 5ec0  ?.....%.de....^.
0000550: 6e71 545c 2ed0 a60e 8eb2 a2c3 1073 eb36  nqT\.........s.6
0000560: 8415 66cc a1b5 ec71 4da9 5565 25ad 68ed  ..f....qM.Ue%.h.
0000570: 15b8 a1ef 2ca2 fc0f 9e17 362c b6dc 8a8b  ....,.....6,....
0000580: e773 8cb6 f3bf 1842 19a8 a16b 5bc9 6129  .s.....B...k[.a)
0000590: 0855 cad5 c74f af1f b1b6 a7cd 4477 1cdd  .U...O......Dw..
00005a0: 2920 93f4 e315 c9b5 1988 ee91 6a2e b4db  ) ..........j...
00005b0: bb59 2d8c b946 dcf3 89b2 e9ef f7d1 15b2  .Y-..F..........
00005c0: b5b6 8042 b617 e0fc 311e b322 2539 74c7  ...B....1.."%9t.
00005d0: 8a6c cb2e ab5e ca3f 913e 9876 9744 8f15  .l...^.?.>.v.D..
00005e0: c763 b61c 7dd9 64e5 17e1 22dd 71de 5d6f  .c..}.d...".q.]o
00005f0: babc d2d4 d3ed 93ee 2d3c e1c8 5a0d b74e  ........-<..Z..N
0000600: 5c43 2a3b 963a 8b19 f25f e077 3f96 0c49  \C*;.:..._.w?..I
0000610: 3516 db7c 1b14 8055 97e2 40db 066e 6d66  5..|...U..@..nmf
0000620: c81a 61bd f549 f742 7e38 9e67 b4cb 3222  ..a..I.B~8.g..2"
0000630: cc5c 5296 2f6f 081e 7f1c 53e0 4769 a34c  .\R./o....S.Gi.L
0000640: 90a7 9aef 0abe 65ad b4dd 597d 2f61 f9e2  ......e...Y}/a..
0000650: 64d4 41a7 9a74 6cca d353 aad6 5b63 ef79  d.A..tl..S..[c.y
0000660: 0db7 c53d 3164 0893 6725 a76e e345 7a2c  ...=1d..g%.n.Ez,
0000670: ab95 f91b 5b8c 46a7 d11f 8f5a 941b 2ebf  ....[.F....Z....
0000680: 5194 d965 b033 1006 41bd f11a 4488 6cfb  Q..e.3..A...D.l.
0000690: 49e7 847c 8973 ec92 a24d 944f 96df 5c45  I..|.s...M.O..\E
00006a0: a5d5 d884 a329 0a5b 6e41 5a8e 5cbb f881  .....).[nAZ.\...
00006b0: c4aa bc38 115c a1c7 5a93 e359 d771 2936  ...8.\..Z..Y.q)6
00006c0: 2b1d 314f 8344 6597 e5cb 67bc e792 486d  +.1O.De...g...Hm
00006d0: b6bc cdb7 c4e6 6a2d 3712 7405 e490 12af  ......j-7.t.....
00006e0: 05ad 70a1 e981 0d8a 936b 90a3 940b 1009  ..p......k......
00006f0: f436 b620 a131 230a 6c89 8cc4 d65a 8a9c  .6. .1#.l....Z..
0000700: 5e7e 4803 8b6f ce19 f637 b3fa eaf7 ecfe  ^~H..o...7......
0000710: 96b6 5f9e 2af3 2baa 88cc 582f f77d 6888  .._.*.+...X/.}h.
0000720: 5949 55ec 7cc9 dca7 129e 6673 5367 16ca  YIU.|.....fsSg..
0000730: 9146 d1d3 4b43 500c c5de b61d 3d71 50ef  .F..KCP.....=qP.
0000740: e861 b911 6639 1488 f7cb e1b7 9fc7 0f56  .a..f9.........V
0000750: e3c0 8668 8d95 1c8b 70f7 8521 2775 7974  ...h....p..!'uyt
0000760: 3883 0a05 5130 0b9e 3912 951c b9a2 9280  8...Q0..9.......
0000770: a46d 6def 7c3a aa2b 716a 3161 3690 eca9  .mm.|:.+qj1a6...
0000780: 0148 54a5 e5b9 c891 eefc f1d9 da94 477b  .HT...........G{
0000790: ab33 67b2 dbd9 ac6c 839b 3a77 f873 871a  .3g....l..:w.s..
00007a0: 8135 121c 6f75 2402 0fd7 9c53 bdb1 536c  .5..ou$....S..Sl
00007b0: 549f cd9a e9b7 df50 17b0 b0d8 61d1 4d8f  T......P....a.M.
00007c0: 4d4c 445a cecc 7157 736d fdde 30b7 9d60  MLDZ..qWsm..0..`
00007d0: 30f3 4f29 8584 2b32 094f 549f 2fe2 f6f3  0.O)..+2.OT./...
00007e0: fe72 7ffd 98ec a693 a986 c38c 37ab 3951  .r..........7.9Q
00007f0: f5b4 3ec8 5ac9 f5b9 c76d 9869 d726 485a  ..>.Z....m.i.&HZ
0000800: 6338 17dd f44b 9ca8 9c83 8b81 f3c7 6593  c8...K........e.
0000810: 4e8e a4a9 8a8b 0951 d129 0cef fcbb ff00  N......Q.)......
0000820: af2f d953 9355 6d7a 3359 6845 7834 5636  ./.S.Umz3YhEx4V6
0000830: 1652 36f3 38ab bb0e 308e 935b 5254 1c67  .R6.8...0..[RT.g
0000840: 3f75 4787 7cbf 86c3 1527 989a 6a72 1ca4  ?uG.|....'..jr..
0000850: 2d6c 3ea8 8238 7141 6027 c3d7 7ea7 1097  -l>..8qA`'..~...
0000860: 4c6a 5fef 8ea2 0ad2 b42b dfbf 8f30 3e1c  Lj_......+...0>.
0000870: bce2 ad2a a21c 6e1d 45a6 54db e941 50cc  ...*..n.E.T..AP.
0000880: 8197 2edd 7133 ba06 a2b9 53a8 392d 6d4c  ....q3....S.9-mL
0000890: cc9f b157 dddb 7dec 3e47 0c25 f14b 4bc2  ...W..}.>G.%.KK.
00008a0: 9e90 b0ce a641 1f57 7cbf 8fe9 8934 ea8d  .....A.W|....4..
00008b0: 7954 8714 e2f3 b2e5 243e 1eb9 f7b3 fdeb  yT......$>......
00008c0: e288 e52d e892 2243 6d7a 62a8 db8d 28ac  ...-.."Cmzb...(.
00008d0: ad5e 3c83 f0da dbe3 b4ec 4776 030b 726b  .^<.......Gv..rk
00008e0: e92e 02b0 52fd d19a df87 2ded d6f8 ecbc  ....R.....-.....
00008f0: 6c94 76de 692f a622 5ad5 d3b6 98cd 9faf  l.v.i/."Z.......
0000900: 1e58 7691 3259 8149 8cbc b24e 4515 c950  .Xv.2Y.I...NE..P
0000910: 3ee0 ca36 4e3b 28f4 620c 672a b154 d902  >..6N;(.b.g*.T..
0000920: de1b 1b6d 8a9b fda0 ef02 9f35 b694 c96f  ...m.......5...o
0000930: 3e99 5246 520e 5ebf ef04 144b 5d3d 53ed  >.RFR.^....K]=S.
0000940: 6526 ef77 1be2 30ec ba1e f679 6562 715a  e&.w..0....yebqZ
0000950: 5590 7f66 eade f7c4 decb bac3 e6af f6d1  U..f............
0000960: 9a65 2d13 aa16 4d94 0f97 8b14 59f3 42fb  .e-...M.....Y.B.
0000970: 9269 629e ebc8 4950 6d49 20ef 6f3c 76be  .ib...IPmI .o<v.
0000980: a105 a712 2a25 a4c6 0a19 4b89 6c6e 7e7b  ....*%....K.ln~{
0000990: e1a8 0f76 8df2 b6ec 5301 1440 9750 a1d0  ...v....S..@.P..
00009a0: 5b8f cf14 a86b 9369 30aa 6c48 7d19 15e0  [....k.i0.lH}...
00009b0: 4589 bf1b f238 c48a d447 7563 a5a5 29b5  E....8...Guc..).
00009c0: e523 3286 c39f c588 2caf f9ca 46ab 97e7  .#2.....,...F...
00009d0: 32b7 3fae 20cc 98e6 8c66 f3e6 5e52 6d77  2.?. ....f..^Rmw
00009e0: 943a 7c71 5586 8937 9336 a6fc 8611 915e  .:|qU..7.6.....^
00009f0: 3458 1bf1 b707 9c54 69d4 bf69 aea2 f38a  4X.....Ti..i....
0000a00: 6c52 8150 6028 9b6a 5b8b 751b f963 b091  lR.P`(.j[.u..c..
0000a10: 09cc 5866 4357 f832 918a fc49 edba 1c91  ..XfCW.2...I....
0000a20: 2d72 e2e5 6ca8 3f9c 7ba3 f2c7 6562 ca8e  -r..l.?.{...eb..
0000a30: a756 9a8b 4a5c 7b6e acd9 d593 eb6c 5324  .V..J\{n.....lS$
0000a40: d29b 5e8c 265d 129e 2d14 0dc5 928d fc8e  ..^.&]..-.......
0000a50: 154a 5c47 1751 9697 0328 0c93 aca2 a212  .J\G.Q...(......
0000a60: a07d 3ff9 c53e 9bda 643d df61 4742 1272  .}?..>..d=.aGB.r
0000a70: b965 1284 e6ca 53b1 e3e9 8b3e 871b 603c  .e....S....>..`<
0000a80: b114 3c9b 2f47 eedf ebfc 779a 4b8a 654e  ..<./G....w.K.eN
0000a90: 20a4 388f 7937 ea31 1a65 56b2 ed50 4539   .8.y7.1.eV..PE9
0000aa0: 9868 b296 d295 799b 7385 c56f b70c b925  .h....y.s..o...%
0000ab0: 02ea 6530 592b 4fc4 5f0c a1e7 7bc3 c940  ..e0Y+O._...{..@
0000ac0: 0b77 2e5c e7a9 b74f f894 f497 9b8e ca7d  .w.\...O.......}
0000ad0: e71d 5654 8f9f f477 9f80 e515 888d a884  ..VT...w........
0000ae0: b73e 5e57 ddb7 502f b5fd 714c 6689 11b7  .>^W..P/..qLf...
0000af0: 26cc 60c8 5779 57d9 b290 aca6 f6e7 c408  &.`.WyW.........
0000b00: c52e 9b56 cb13 bdbe bd65 534a 95aa da12  ...V.....eSJ....
0000b10: 0d93 d772 6d6f 4c54 a376 6d87 69f5 3010  ...rmoLT.vm.i.0.
0000b20: a30a b19c 246f ef5a e4ee 0fe9 8355 6e35  ....$o.Z.....Un5
0000b30: 2087 10bc 921d 250f 956a d8ea 2f8c bcfe   .....%..j../...
0000b40: 4312 69b3 1501 e7db 6b5d 0fd3 5dce d293  C.i.....k]..]...
0000b50: 7b11 f1c4 28f3 bd94 b665 ba19 d385 273b  {...(....e....';
0000b60: cca8 f19b 1358 a1c5 87dd a139 a2e3 d354  .....X.....9...T
0000b70: af1a c721 3970 e7ef 6b72 1b61 51da ee8d  ...!9p..kr.aQ...
0000b80: 3456 a6c2 ede3 1e0e 4e6c 4f53 565b b0a5  4V......NlOSV[..
0000b90: ae33 46a0 e64b 2011 6cea f40a fa62 a31a  .3F..K .l....b..
0000ba0: a2a8 2f2a 2c63 2f5e 98ee a36a 40e7 e789  ../*,c/^...j@...
0000bb0: 32a5 c18a d536 586c b7a4 b3aa d8ce 920a  2....6Xl........
0000bc0: ba1b fa79 e2ab 16a2 5c72 1d39 a652 db09  ...y....\r.9.R..
0000bd0: 5948 ccb1 9b36 dd71 2699 570a 9ed5 36a0  YH...6.q&.W...6.
0000be0: e308 52d6 a04e 4e0d c7a2 b15e 9701 8d18  ..R..NN....^....
0000bf0: 8d2f b934 3315 71ef ee7d 6d88 7ecb 7648  ./.43.q..}m.~.vH
0000c00: ed13 ef24 30e1 7d4a 5b9b f88a bd2d 7c47  ...$0.}J[....-|G
0000c10: a4d2 6334 fd41 d6cb ea54 8243 6da2 f6b9  ..c4.A...T.Cm...
0000c20: b7ae 3bb5 7929 6168 7ae4 53de 5043 c9b7  ..;.y)ahz.S.PC..
0000c30: e76d cede 98a6 7fd4 ff00 caaf e80e 374f  .m............7O
0000c40: 8f43 9911 4a2a 4fb4 e2dd c6ef d2e3 9f9e  .C..J*O.........
0000c50: 29f3 69d2 6133 548e dad9 5a74 3247 7105  ).i.a3T...Zt2Gq.
0000c60: 4556 b278 b5f1 165b f2e1 a6b5 11e5 3ac1  EV.x...[......:.
0000c70: 6db3 a212 5394 a0f5 f9e1 fac5 5df8 ee4c  m...S.......]..L
0000c80: 5b22 321b 8808 6d08 bdfa efce 2051 cbd1  ["2...m..... Q..
0000c90: fbdc 57b5 b7b9 65cf 1a8e 53d6 de2c 4b92  ..W...e...S..,K.
0000ca0: f2a0 4544 9a72 e214 d3da d30d acab 903a  ..ED.r.........:
0000cb0: edd7 9c52 73fb 25be e329 a773 c768 a5c7  ...Rs.%..).s.h..
0000cc0: 509e 732a dcfa 7189 cfd0 e543 eed3 5cd6  P.s*..q....C..\.
0000cd0: 7199 a957 8167 929c b860 409b 07f9 2943  q..W.g...`@...)C
0000ce0: ca90 d1be a755 a6df a1c3 14c8 d210 e496  .....U..........
0000cf0: e409 4b5c 81e0 7d7d 737a 7fac 4993 3053  ..K\..}}sz..I.0S
0000d00: da8f 2a9e a88e 334f 6f4c 0255 d05b 7dba  ..*...3OoL.U.[}.
0000d10: 9df0 aa22 aa30 550d a090 cab2 a82d 6011  ...".0U......-`.
0000d20: 60bf 2b0f 2f21 876a 9449 115b 7643 61b7  `.+./!.j.I.[vCa.
0000d30: da98 0e53 6e14 2dd7 0e47 43c9 9139 c2b7  ...Sn.-..GC..9..
0000d40: 96ea f64a dd57 feb1 1e1b 8a4b 8f8b add5  ...J.W.....K....
0000d50: a7ef 2c9b 9c49 a897 28b2 e6bf b6b4 82e9  ..,..I..(.......
0000d60: 284f f6a6 c058 6235 5a93 2596 2a0d 3458  (O...Xb5Z.%.*.4X
0000d70: 5264 025b 7117 bd8d b7e7 1e17 696e d494  Rd.[q.......in..
0000d80: f5c8 5a56 194b 76e0 5b72 6ffa e131 aaf2  ..ZV.Kv.[ro..1..
0000d90: 296d d263 a0e5 790b 505e 652e fe22 ab0b  )m.c..y.P^e.."..
0000da0: 6e7e 9843 6dd5 60b8 e2ce 54a1 3210 493e  n~.Cm.`...T.2.I>
0000db0: 5cff 0051 5332 596e 432a f79b 7539 927e  \..QS2YnC*..u9.~
0000dc0: 5843 8dd2 a0b6 e20e 64ad 31d0 083e 7c7f  XC......d.1..>|.
0000dd0: 987f ffc4 0029 1001 0002 0202 0201 0108  .....)..........
0000de0: 0300 0000 0000 0001 1121 0031 4151 6171  .........!.1AQaq
0000df0: 81b1 1030 5070 91a1 d1f0 20c1 e1ff da00  ...0Pp.... .....
0000e00: 0801 0100 013f 21fc 9bb0 9a52 1a48 2da3  .....?!....R.H-.
0000e10: 8cac ff00 6994 ad4a a6ce b467 18a4 5494  ....i..J...g..T.
0000e20: 0edb 4065 9154 a98a 58c1 a5de 5929 5842  ..@e.T..X...Y)XB
0000e30: 31c1 87ea 7d84 b8e8 8b52 c187 96b1 8695  1...}....R......
0000e40: a0aa 49f4 b6b3 ce09 5b2c 5808 06e4 0c64  ..I.....[,X....d
0000e50: 824f 6100 6f91 a5fa b83c e3ff 00c7 d791  .Oa.o....<......
0000e60: 73ac 352c 87a3 20cf 5a7e 7256 0a50 321d  s.5,.. .Z~rV.P2.
0000e70: c144 44c4 b2dc 766c e901 7b71 5f25 3674  .DD...vl..{q_%6t
0000e80: fb4a 40f7 9f2a e0c9 2996 55d7 1589 9520  .J@..*..).U....
0000e90: 2e43 622a 4865 32cd 59a5 05a2 6e14 d9e7  .Cb*He2.Y...n...
0000ea0: 3789 46ab 2112 51cb c66b c8fd f904 70f8  7.F.!.Q..k....p.
0000eb0: 9e58 7019 3c89 91b1 81bd 4070 a6df 6229  .Xp.<.....@p..b)
0000ec0: 6cc3 a1ef bc6c ab00 f4c5 9ba7 ac81 06b5  l....l..........
0000ed0: 8105 64ac 5672 e858 a913 a44e facf 51ac  ..d.Vr.X...N..Q.
0000ee0: b494 27d3 7857 fa43 04a2 0a8e da2a f3fa  ..'.xW.C.....*..
0000ef0: cbff 00ae 9f18 d1af 8384 9b41 0880 e717  ...........A....
0000f00: 522a b0da 6ccd 99f2 c703 3827 85ec adab  R*..l.....8'....
0000f10: ae2b 23a5 ec56 05c7 a1eb 9c1a 9331 e115  .+#..V.......1..
0000f20: 519d 4c73 1917 5c44 cd60 4ceb 49c0 3f09  Q.Ls..\D.`L.I.?.
0000f30: 6568 22a1 d50d 7186 a8e8 8b52 0087 92af  eh"...q....R....
0000f40: 2f1e 3f44 959b 8ef3 7a2e 8d46 0702 a5f5  /.?D....z..F....
0000f50: 3951 ed70 69e4 29fa fdef f55d 703f 77c9  9Q.pi.)....]p?w.
0000f60: 9a63 7027 de42 3c4c 3b01 f59a 8edc 73b2  .cp'.B<L;.....s.
0000f70: 809d 8095 8989 1f64 8fb4 5c5a 8376 47f3  .......d..\Z.vG.
0000f80: 9a3e 3baa a7cd 411d e409 f690 01c0 48e6  .>;...A.......H.
0000f90: b341 9372 3357 5d04 3c16 54f3 9350 113f  .A.r3W].<.T..P.?
0000fa0: aa98 5338 8ead 502d bc51 b1ab 2ef0 d6dc  ..S8..P-.Q......
0000fb0: e22e 12bb 4c4e 997e 8a22 ca41 4797 ae31  ....LN.~.".AG..1
0000fc0: 45b2 3849 6750 4f45 6093 1c55 50ac d70c  E.8IgPOE`..UP...
0000fd0: 6ea3 4616 294e 2365 f076 99c6 7afa 4c4c  n.F.)N#e.v..z.LL
0000fe0: c585 bce2 164f 254b 0509 5158 38d9 b47e  .....O%K..QX8..~
0000ff0: c71a 41ab 62d5 d017 c90d cffa f18d 7294  ..A.b.........r.
0001000: 640d 2973 8547 ce1f 6668 c869 1496 f8cd  d.)s.G..fh.i....
0001010: 536d 562c 0b10 8c77 8e14 7801 e0c0 c4ce  SmV,...w..x.....
0001020: 1768 a539 09c6 2dbb 15c2 89d2 9525 bc01  .h.9..-......%..
0001030: c72a 484a 00e9 1ac2 bdb1 ecdf 7929 f19e  .*HJ........y)..
0001040: 1ae7 1050 5d8e 329b b15c a09d 2952 1ac7  ...P].2..\..)R..
0001050: c669 d645 1e5a 4740 d0bb 5c3c b39f b652  .i.E.ZG@..\<...R
0001060: 82df 8214 2246 1784 fd87 298d 0ee2 ac63  ...."F....)....c
0001070: ed97 1620 5d91 fc64 5ee0 3b02 90cc 0dce  ... ]..d^.;.....
0001080: 05c9 e872 5cb4 17ca c10a ccab e57d fdf9  ...r\........}..
0001090: 62e3 70a2 3dc6 cc5f fb8a 2209 b73b ac6d  b.p.=.._.."..;.m
00010a0: 761c 020a 332d 3f5c a0bb 7a19 10ea 4dc1  v...3-?\..z...M.
00010b0: a9ff 0028 061c 0c96 0954 5a1f 3f83 c03c  ...(.....TZ.?..<
00010c0: be55 1001 d582 5ce8 7167 31c0 3af3 8492  .U....\.qg1.:...
00010d0: 46a9 096d 56f9 870e 451c 10b2 f509 1a76  F..mV...E......v
00010e0: 4c32 6387 368a 3690 706f b70d 7010 5c04  L2c.6.6.po..p.\.
00010f0: aa05 37de bb7e cebd 6a73 0934 a11f b4ce  ..7..~..js.4....
0001100: 674f b85b 48d5 e4ac f2d5 eb36 1903 d6f8  gO.[H......6....
0001110: cef6 4a90 df36 f8e0 e3b1 c056 d50d 53df  ..J..6.....V..S.
0001120: eb2e d237 66da 001a 34ac 9be0 89fd 5c48  ...7f...4.....\H
0001130: 88cd 6f61 db99 4584 303f 1e29 4c57 22b2  ..oa..E.0?.)LW".
0001140: 720e be61 6435 88c8 b018 77b6 38fb 0334  r..ad5....w.8..4
0001150: acd7 8245 1597 594c b92f e032 aad0 4c39  ...E..YL./.2..L9
0001160: 4d7a 9c62 34d6 f09d 374d b16e f22c 2113  Mz.b4...7M.n.,!.
0001170: a92b 8dbc af0a 5d45 84f7 72ff 005d 373f  .+....]E..r..]7?
0001180: fe38 e912 04d6 cc55 0b78 09a5 404c 9b54  .8.....U.x..@L.T
0001190: 4064 3897 1f64 a793 5382 995a 3272 3af5  @d8..d..S..Z2r:.
00011a0: cadb 4eef 247e a528 13c7 dc9c 0462 9285  ..N.$~.(.....b..
00011b0: fb0c 4972 9f3a 7bc4 820f 4fa7 808e eb31  ..Ir.:{...O....1
00011c0: 1019 6680 3778 4200 e0b3 663f 71fb e7eb  ..f.7xB...f?q...
00011d0: c0a8 d609 a24b 7296 2625 07a3 24ee 5651  .....Kr.&%..$.VQ
00011e0: 2494 1771 ae32 c644 e8e2 078e 31c6 38d3  $..q.2.D....1.8.
00011f0: f404 5ab2 df49 25ff 005a 265e dd19 0c55  ..Z..I%..Z&^...U
0001200: 4644 42d2 bb9c 1a72 ab33 000b 2bc7 e230  FDB....r.3..+..0
0001210: 0c38 182c 92a9 b07e 30d3 9459 9902 511e  .8.,...~0..Y..Q.
0001220: 7f38 7fff da00 0c03 0100 0200 0300 0000  .8..............
0001230: 1092 4924 9249 2492 4924 9249 2492 4924  ..I$.I$.I$.I$.I$
0001240: 9249 2492 4924 9249 2492 4924 9249 2492  .I$.I$.I$.I$.I$.
0001250: 4924 9249 2492 4924 9249 2492 4924 9249  I$.I$.I$.I$.I$.I
0001260: 2492 4924 9249 2492 4924 9249 0090 4100  $.I$.I$.I$.I..A.
0001270: 9009 0082 0000 8248 2402 4924 9249 0482  .......H$.I$.I..
0001280: 4104 9201 2092 4000 9009 2090 4924 9249  A... .@... .I$.I
0001290: 2490 4124 9249 2492 4924 9249 2492 4924  $.A$.I$.I$.I$.I$
00012a0: 9249 2490 0104 9008 2402 4924 9249 2492  .I$.....$.I$.I$.
00012b0: 4924 9249 2492 4024 9240 2410 0820 9249  I$.I$.@$.@$.. .I
00012c0: 2492 4924 9249 2492 4924 9249 2492 4924  $.I$.I$.I$.I$.I$
00012d0: 8249 2492 4924 9249 2492 4924 9249 2492  .I$.I$.I$.I$.I$.
00012e0: 4924 9249 2492 4924 9249 2492 4924 9249  I$.I$.I$.I$.I$.I
00012f0: 2492 4924 9249 2492 4924 9249 2492 4924  $.I$.I$.I$.I$.I$
0001300: 9249 2492 4924 9249 2492 4924 9249 2492  .I$.I$.I$.I$.I$.
0001310: 4924 9249 2492 4924 9249 2492 4924 9249  I$.I$.I$.I$.I$.I
0001320: 2492 4924 93ff c400 1411 0100 0000 0000  $.I$............
0001330: 0000 0000 0000 0000 0000 90ff da00 0801  ................
0001340: 0301 013f 1022 bfff c400 1411 0100 0000  ...?."..........
0001350: 0000 0000 0000 0000 0000 0000 90ff da00  ................
0001360: 0801 0201 013f 1022 bfff c400 2210 0101  .....?."...."...
0001370: 0101 0101 0100 0007 0100 0000 0000 0111  ................
0001380: 2100 3141 5120 3050 6170 71f0 81ff da00  !.1AQ 0Papq.....
0001390: 0801 0100 013f 10ff 000d faaa 910f 0ac1  .....?..........
00013a0: 1815 982f 3ac3 0382 0c6e 7c47 f60f 7a18  .../:....n|G..z.
00013b0: 277d d43c 3030 0388 73af 01cc c318 988f  '}.<00..s.......
00013c0: 9c36 16e9 4028 b62c c328 a5ea 08e1 25a0  .6..@(.,.(....%.
00013d0: ae51 33c3 b8f2 388e fd00 0da0 4ac9 71cb  .Q3...8.....J.q.
00013e0: d79b 5067 f3b0 16c7 3856 4c5e c638 b342  ..Pg....8VL^.8.B
00013f0: 2348 e18c 3fbe b589 074f ad92 a5b8 c56b  #H..?....O.....k
0001400: c398 d5f0 8565 e9a3 5cb6 b7b3 2153 6753  .....e..\...!SgS
0001410: a4a0 98be a293 e849 f671 0602 5584 4a4a  .......I.q..U.JJ
0001420: 4cf5 e0bc 3da9 088d 6a72 b108 40e4 0eec  L...=...jr..@...
0001430: 0ba2 09a9 e042 41e7 1314 2c09 54d4 8d24  .....BA...,.T..$
0001440: 4442 0e87 8362 b414 55ea 3c79 38a0 b6bb  DB...b..U.<y8...
0001450: 2000 c9a1 969c 9237 9443 d1e1 594c 08bc   ......7.C..YL..
0001460: 20c7 70c4 bc04 0c14 07a9 9f82 9191 70c7   .p...........p.
0001470: 1505 ece6 dff8 5a7a a920 589e 372e ea03  ......Zz. X.7...
0001480: 773b a3ad d0a5 dcb6 b837 a60c 99c0 4a49  w;.......7....JI
0001490: 6f4c f742 8051 20aa 96a3 1ff3 b3fe 2bfd  oL.B.Q .......+.
00014a0: bf78 f963 2483 1610 7a93 4d3f 7eb1 f370  .x.c$...z.M?~..p
00014b0: 328a 61e3 0bbc d205 e171 f944 306f 1ae1  2.a......q.D0o..
00014c0: 6cd5 9370 495f 0785 3a88 be4b 34df ea65  l..pI_..:..K4..e
00014d0: 6bab 7cff 0023 7d60 4a22 679d 9161 2c32  k.|..#}`J"g..a,2
00014e0: 6010 3236 34f4 4660 92c4 cc2a 1be1 ba70  `.264.F`...*...p
00014f0: c89b 0cc1 a663 09ee 02f6 a93a cc90 5e34  .....c.....:..^4
0001500: 3abe fe49 c67c f3b2 03ff 006c 7741 595f  :..I.|.....lwAY_
0001510: e6f8 bdc0 dd84 703e 6d60 0c5e 7a79 c0f6  ......p>m`.^zy..
0001520: 0258 8905 0a9c aff7 f2b4 8046 c41a a65e  .X.........F...^
0001530: 3cda 1609 6912 61f0 580b 150b e893 f100  <...i.a.X.......
0001540: 5084 4d0e 8d7e eab0 a134 407f 4054 41a0  P.M..~...4@.@TA.
0001550: 65f0 62cc 8171 206b fdb2 93b0 1012 44a9  e.b..q k......D.
0001560: 7adc 6256 86b0 9c1a 2c47 1baa 9442 0644  z.bV....,G...B.D
0001570: 03f1 5de8 7ab9 2118 c546 ccb1 839b 6c8c  ..].z.!..F....l.
0001580: 8208 c196 d2b9 0303 7301 bded 548d 5857  ........s...T.XW
0001590: b19b bfd0 aeee 57a5 af7c 01d9 2ebd 424e  ......W..|....BN
00015a0: 3224 cc79 530d 22d4 01b8 409e 4389 a503  2$.yS."...@.C...
00015b0: 651f cdf0 8676 46ad 5b0b 0601 1663 31d2  e....vF.[....c1.
00015c0: 4bca 4672 c4a0 b811 14b0 643a 5338 3e3e  K.Fr......d:S8>>
00015d0: b4d2 14c8 de24 497e 6830 1104 1b1f ce89  .....$I~h0......
00015e0: 1edc 73b3 8c3e aa72 d1a5 600a 2941 4e94  ..s..>.r..`.)AN.
00015f0: 5453 be7e 0763 b5c9 ff00 000a 201e d116  TS.~.c...... ...
0001600: 8e99 a1b1 7d28 97f5 50ee 493f a82f fb7b  ....}(..P.I?./.{
0001610: ff00 6f31 b0f3 4b8a 5ae0 bdf7 f03b 1da6  ..o1..K.Z....;..
0001620: cff8 0254 16a3 e82a a194 0bf4 020e 79f6  ...T...*......y.
0001630: 0f1b 47fb 6fa3 66e8 04a3 009d 00ae e703  ..G.o.f.........
0001640: ad7a 6a47 d7a1 f739 fb60 5869 c9b3 0faa  .zjG...9.`Xi....
0001650: 5145 3e28 e726 594d 0540 3954 054a 6bde  QE>(.&YM.@9T.Jk.
0001660: b061 784f d55b b257 1888 3774 9a44 a23f  .axO.[.W..7t.D.?
0001670: cf17 b959 242a 20ed 13d0 e650 a381 0291  ...Y$* ....P....
0001680: 6885 4365 1407 a6f2 0018 2542 20fa 7788  h.Ce......%B .w.
0001690: f15a ba58 4f8b 030f e2f2 6a04 c2d4 a015  .Z.XO.....j.....
00016a0: d41e bfd1 cf1d 1c46 8218 63e5 1a8d ea3f  .......F..c....?
00016b0: 96a1 4739 830e 19e0 4e46 bcf3 023a 215a  ..G9....NF...:!Z
00016c0: 341b 4e3c 2412 c035 da11 e80e ac71 45fd  4.N<$..5.....qE.
00016d0: 2fd8 cd2f 2e7f c2b2 c50f 4429 5047 8c6e  /../......D)PG.n
00016e0: 2bdd 81fc 2920 bed8 e399 47a5 8765 54aa  +...) ....G..eT.
00016f0: 3472 ce8f 4774 ca7a 9606 81c7 69f1 0304  4r..Gt.z....i...
0001700: 4978 a08d 606a 72d2 3688 51ea 5f40 a540  Ix..`jr.6.Q._@.@
0001710: 8f2a 6b6c 7036 4918 1741 415d ddb2 93b0  .*klp6I..AA]....
0001720: 1056 40a3 38e3 a7d2 a76c 8759 0330 93f8  .V@.8....l.Y.0..
0001730: 8a47 39c4 0d90 cecc 932d 8cd3 f748 41c5  .G9......-...HA.
0001740: 3a07 f26b e943 8205 90c6 e036 7583 ad51  :..k.C.....6u..Q
0001750: 2050 e949 fd06 566f be1d 20d5 aa25 6430   P.I..Vo.. ..%d0
0001760: 0ec0 569b 98a8 788a 948a d505 f265 48e0  ..V...x......eH.
0001770: 8fe4 8030 7815 bcb0 9f21 83be 6ea2 1c57  ...0x....!..n..W
0001780: a585 f9e0 7147 e593 78cb ca6e c4b8 1474  ....qG..x..n...t
0001790: f040 fb7b a43a d1f8 9a15 1c11 1cfb 5836  .@.{.:........X6
00017a0: 5708 4040 8ca9 b099 3b00 af88 4c32 d794  W.@@....;...L2..
00017b0: 0c2e 9d6b f1c8 54ad 6f13 6964 b64d a35a  ...k..T.o.id.M.Z
00017c0: 1d02 eaa7 c363 eec1 680c 5798 43f9 eb08  .....c..h.W.C...
00017d0: b474 f8db 60c0 0af5 0220 a0b0 2e92 b390  .t..`.... ......
00017e0: db83 3910 0202 8505 383e 886a 7a08 47e2  ..9.....8>.jz.G.
00017f0: 9fab d28d 43d1 5aaa 2115 a693 5fd1 014c  ....C.Z.!..._..L
0001800: a161 bcf0 788e f4d9 4c09 69e0 50ee d1fe  .a..x...L.i.P...
0001810: acd7 2b14 0002 aa07 f51f 26a0 4c25 5801  ..+.......&.L%X.
0001820: 4c43 e9c3 fd59 ae16 2008 1110 4ff3 0fff  LC...Y.. ...O...
0001830: d9"""
    help_text = 'Background text'


@global_preferences_registry.register
class HomeTitle(StringPreference):
    section = 'home'
    name = 'title'
    verbose_name = 'Home Title'
    default = 'Welcome to the CTF-Backend.'
    help_text = 'Home site title (Default: '+default+')'


@global_preferences_registry.register
class HomeLead(LongStringPreference):
    section = 'home'
    name = 'lead'
    verbose_name = 'Home Lead'
    default = ''
    help_text = 'Home site lead text'


@global_preferences_registry.register
class EmailSMTPHost(StringPreference):
    section = 'mail'
    name = 'smtp_host'
    verbose_name = 'SMTP Host'
    default = 'localhost'
    help_text = 'The SMTP Host you wish to send your mails with. ' \
                '(Default: '+default+')'


@global_preferences_registry.register
class EmailSMTPPort(IntegerPreference):
    section = 'mail'
    name = 'smtp_port'
    verbose_name = 'SMTP Port'
    default = 25
    help_text = 'SMTP Port (Default: '+str(default)+')'


@global_preferences_registry.register
class EmailSMTPUser(StringPreference):
    section = 'mail'
    name = 'smtp_user'
    verbose_name = 'SMTP User'
    default = ''
    help_text = 'Username for the SMTP Host (Default: None)'


@global_preferences_registry.register
class EmailSMTPPassword(StringPreference):
    section = 'mail'
    name = 'smtp_password'
    verbose_name = 'SMTP Password'
    default = ''
    help_text = 'Password for the SMTP Host (Default: None)'


@global_preferences_registry.register
class SenderEmail(StringPreference):
    section = 'mail'
    name = 'return_path'
    verbose_name = 'Sender Email Address (Return-Path)'
    default = 'ctf-backend@mailhost.xx'
    help_text = 'Mail address used to send emails. This mail address ' \
                'should exist for real. (Default: '+default+')'


@global_preferences_registry.register
class FromEmail(StringPreference):
    section = 'mail'
    name = 'from'
    verbose_name = 'From Email Address and name'
    default = 'CTF-Backend <ctf-backend@noreply>'
    help_text = 'The Mail address the recipient ' \
                'will see as From address. (Default: '+default+')'


@global_preferences_registry.register
class GoodDomains(LongStringPreference):
    section = 'registration'
    name = 'allowed_domains'
    verbose_name = 'Allowed Domains'
    default = ''
    help_text = 'Comma-separated list of allowed mail domains for registration'


@global_preferences_registry.register
class FlagRegex(StringPreference):
    section = 'ctf'
    name = 'flag_regex'
    verbose_name = 'Flag Format'
    default = '^flag_[a-fA-F0-9]{40}_$'
    help_text = 'Regex for flag format validation'


order = [BackendTitle, HomeTitle, HomeLead, Background, GoodDomains,
         EmailSMTPHost, EmailSMTPPort, EmailSMTPUser, EmailSMTPPassword,
         FromEmail, SenderEmail, FlagRegex]
