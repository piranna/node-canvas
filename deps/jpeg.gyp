{ 

  'includes': [  'common.gyp' , 'locations.gyp'],
  'targets': [
    {
      'target_name': 'libjpeg',
      'type': 'static_library',
      'include_dirs': [ 
            './custom-include/jpeg/',
            '<(jpeg_root)' ,
        ],
      
      'dependencies': [],
      'defines': [],
      'sources': [
   
            #"<(jpeg_root)ansi2knr.c",
            #"<(jpeg_root)cdjpeg.c",
            #"<(jpeg_root)cjpeg.c",
            #"<(jpeg_root)ckconfig.c",
            #"<(jpeg_root)djpeg.c",
            #"<(jpeg_root)example.c",
            
        
            "<(jpeg_root)jcapimin.c",
            "<(jpeg_root)jcapistd.c",
            "<(jpeg_root)jccoefct.c",
            "<(jpeg_root)jccolor.c",
            "<(jpeg_root)jcdctmgr.c",
            "<(jpeg_root)jchuff.c",
            "<(jpeg_root)jchuff.h",
            "<(jpeg_root)jcinit.c",
            "<(jpeg_root)jcmainct.c",
            "<(jpeg_root)jcmarker.c",
            "<(jpeg_root)jcmaster.c",
            "<(jpeg_root)jcomapi.c",
            "./custom-include/jpeg/jconfig.h",
            "<(jpeg_root)jcparam.c",
            "<(jpeg_root)jcphuff.c",
            "<(jpeg_root)jcprepct.c",
            "<(jpeg_root)jcsample.c",
            #"<(jpeg_root)jctrans.c",
            "<(jpeg_root)jdapimin.c",
            "<(jpeg_root)jdapistd.c",
            "<(jpeg_root)jdatadst.c",
            "<(jpeg_root)jdatasrc.c",
            "<(jpeg_root)jdcoefct.c",
            "<(jpeg_root)jdcolor.c",
            "<(jpeg_root)jdct.h",
            "<(jpeg_root)jddctmgr.c",
            "<(jpeg_root)jdhuff.c",
            "<(jpeg_root)jdhuff.h",
            "<(jpeg_root)jdinput.c",
            "<(jpeg_root)jdmainct.c",
            "<(jpeg_root)jdmarker.c",
            "<(jpeg_root)jdmaster.c",
            "<(jpeg_root)jdmerge.c",
            "<(jpeg_root)jdphuff.c",
            "<(jpeg_root)jdpostct.c",
            "<(jpeg_root)jdsample.c",
            #"<(jpeg_root)jdtrans.c",
            "<(jpeg_root)jerror.c",
            "<(jpeg_root)jerror.h",
            "<(jpeg_root)jfdctflt.c",
            "<(jpeg_root)jfdctfst.c",
            "<(jpeg_root)jfdctint.c",
            "<(jpeg_root)jidctflt.c",
            "<(jpeg_root)jidctfst.c",
            "<(jpeg_root)jidctint.c",
            "<(jpeg_root)jinclude.h",
            
            #"<(jpeg_root)jidctred.c",
            
            #"<(jpeg_root)jmemansi.c",
            #"<(jpeg_root)jmemdos.c",
            #"<(jpeg_root)jmemmac.c",
            
            "<(jpeg_root)jmemmgr.c",
            
            #"<(jpeg_root)jmemname.c",
            "<(jpeg_root)jmemnobs.c",
            #"<(jpeg_root)jpegtran.c",
            
            "<(jpeg_root)jquant1.c",
            "<(jpeg_root)jquant2.c",
            
            "<(jpeg_root)jmemsys.h",
            "<(jpeg_root)jmorecfg.h",
            "<(jpeg_root)jpegint.h",
            "<(jpeg_root)jpeglib.h",
            
            "<(jpeg_root)jutils.c",
            "<(jpeg_root)jversion.h",
            
            #"<(jpeg_root)rdbmp.c",
            #"<(jpeg_root)rdcolmap.c",
            #"<(jpeg_root)rdgif.c",
            #"<(jpeg_root)rdjpgcom.c",
            #"<(jpeg_root)rdppm.c",
            #"<(jpeg_root)rdrle.c",
            #"<(jpeg_root)rdswitch.c",
            #"<(jpeg_root)rdtarga.c",
            #"<(jpeg_root)transupp.c",
            #"<(jpeg_root)wrbmp.c",
            #"<(jpeg_root)wrgif.c",
            #"<(jpeg_root)wrjpgcom.c",
            #"<(jpeg_root)wrppm.c",
            #"<(jpeg_root)wrrle.c",
            #"<(jpeg_root)wrtarga.c",
      ],
    },
  ]
} 