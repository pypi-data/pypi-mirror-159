python3 tools/conv_cmap.py -c B5=cp950 -c UniCNS-UTF8=utf-8 pdfminer/cmap Adobe-CNS1 cmaprsrc/cid2code_Adobe_CNS1.txt
python3 tools/conv_cmap.py -c GBK-EUC=cp936 -c UniGB-UTF8=utf-8 pdfminer/cmap Adobe-GB1 cmaprsrc/cid2code_Adobe_GB1.txt
python3 tools/conv_cmap.py -c RKSJ=cp932 -c EUC=euc-jp -c UniJIS-UTF8=utf-8 pdfminer/cmap Adobe-Japan1 cmaprsrc/cid2code_Adobe_Japan1.txt
python3 tools/conv_cmap.py -c KSC-EUC=euc-kr -c KSC-Johab=johab -c KSCms-UHC=cp949 -c UniKS-UTF8=utf-8 pdfminer/cmap Adobe-Korea1 cmaprsrc/cid2code_Adobe_Korea1.txt
