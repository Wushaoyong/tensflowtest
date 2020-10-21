import os
import pydicom
import cv2
import numpy as np
import xml
in_path=''
in_path_1_xml=""
out_path=''
files = os.listdir(in_path)
num_sum=0
num=0
for strx in files:
    num_sum=num_sum+1
for strx in files:
    num = num + 1
    filename_in_path = in_path + strx
    if(filename_in_path.find('.dcm')!= -1 and filename_in_path.find('\.')==-1):
        ds = pydicom.read_file(filename_in_path)  #读取.dcm文件
        strx = strx.strip('.dcm')
        filename_out_path=out_path+strx+'.jpg'
        img=np.array
        img = ds.pixel_array  # 提取图像信息
        img_SeriesInstanceUid=ds.SeriesInstanceUID
        img=(((img-np.min(img))/(np.max(img)-np.min(img)))*255).astype('uint8')
cv2.imwrite(filename_out_path,img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
in_path_files = os.listdir(in_path_1_xml)
#######  将路径下的DICOM图片读取出来并转换为JPG，并保存到指定路径 ，匹配出每个病例的DICOM文件所对应的XML文件   #########
for route in in_path_files:
    in_path_2_media = in_path_1_xml + route + '\\'
    if(in_path_2_media.find('._')== -1):
        in_path_2_m = os.listdir(in_path_2_media)
        for in_path_2 in in_path_2_m:
            route_xml = in_path_2_media + in_path_2
            # print(route_xml)
            instead = route_xml
            dom = xml.dom.minidom.parse(instead)
            root = dom.documentElement
       SeriesInstanceUid = root.getElementsByTagName('SeriesInstanceUid')
            if (len(SeriesInstanceUid) != 0):
                for value_series in SeriesInstanceUid:
    if(value_series.firstChild.data==img_SeriesInstanceUid):
          xml_name=route_xml
          flag_find_xml=0
          print(xml_name)
          break
            if(flag_find_xml==0):
                break
        if (flag_find_xml == 0):
            break
############################   匹配出每个病例的DICOM文件所对应的XML文件，  读取XML文件的各项信息，并提取出医生标注的肺结节相关信息，并与DICOM中的图片号匹配起来，保存为TXT文件(new)   ###############################
num=0
instead=xml_name
dom = xml.dom.minidom.parse(instead)
root = dom.documentElement
itemlist3 = root.getElementsByTagName('xCoord')
itemlist4 = root.getElementsByTagName('yCoord')
itemlist5 = root.getElementsByTagName('readingSession')
x_cor=[]
y_cor=[]
tmp = []
i=0
j=0
if os.path.exists(new_txt_root):
    os.remove(new_txt_root)  # 删除文件
if os.path.exists(tmp_root):
    os.remove(tmp_root)  # 删除文件
for itemlist5_1 in itemlist5:
   itemlist5_1_1=itemlist5_1.getElementsByTagName('unblindedReadNodule')
   for itemlist5_1_1_1 in itemlist5_1_1:
itemlist5_1_1_1_maglignance=itemlist5_1_1_1.getElementsByTagName('malignancy')
if len(itemlist5_1_1_1_maglignance)>=1:
      malignancy=itemlist5_1_1_1_maglignance[0]
      if malignancy.firstChild.data !='3':
        ROI_list=itemlist5_1_1_1.getElementsByTagName('roi')
        for ROI in ROI_list:
        inclusion_list=ROI.getElementsByTagName('inclusion')
        imageSOP_UID_list= ROI.getElementsByTagName('imageSOP_UID')
          xCoord_list = ROI.getElementsByTagName('xCoord')
          yCoord_list = ROI.getElementsByTagName('yCoord')
          for imageSOP_UID in imageSOP_UID_list:
              i = 0
              x_cor = []
              y_cor = []
              if inclusion_list[i].firstChild.data=='TRUE':
                  num = 0
                  tmp=[]
                  for strx in files:
                     num = num + 1
                     filename_in_path = in_path + strx
if (filename_in_path.find('.dcm') != -1 and filename_in_path.find('\.')==-1):
    ds = pydicom.read_file(filename_in_path)
    symbol = ds.SOPInstanceUID
    if (imageSOP_UID.firstChild.data == symbol):
         flag_malig_all_3 = 1
         j=j+1
         tmp.append(j)
         tmp.append(strx[0:6])
         tmp.append(str(symbol))
         mp.append(int(malignancy.firstChild.data))
         tmp.append(' ')
         change=" ".join('%s' %id for id in tmp)
         with open(tmp_root,'a') as file:
             file.write(change+'\n')
             tmp=[]