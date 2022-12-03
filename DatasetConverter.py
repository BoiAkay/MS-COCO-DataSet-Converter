import json

InputFilePath = "/Users/akay/Downloads/DataSets/COCO-IMAGES/Captions/captions_val2014.json"
OutputFilePath = "/Users/akay/Downloads/DataSets/COCO-IMAGES/temp.txt"
# loading Json file
with open(InputFilePath,"r") as file:
    InputDict = json.load(file) # it return an python dictionary
# extracting filename and associated ImageID from dictionary
ImageList = [(x['file_name'],x['id']) for x in InputDict['images']]
ImageList.sort() # sorting list
caption_list = [x for x in InputDict['annotations']] #extracting captionsdictionary

i=1
with open(OutputFilePath, 'w') as fp:
    for ImageName,ImageID in ImageList:
        print(f"Processing file # {i}")
        TempCapList=[]
        #extracting caption for asscoiate image by mathing image id
        for xImageName in caption_list:
            if xImageName['image_id']==ImageID:
                TempCapList.append(xImageName['caption'])
        
        TempStr0=ImageName+'#0'+'\t'+TempCapList[0]
        TempStr1=ImageName+'#1'+'\t'+TempCapList[1]
        TempStr2=ImageName+'#2'+'\t'+TempCapList[2]
        TempStr3=ImageName+'#3'+'\t'+TempCapList[3]
        TempStr4=ImageName+'#4'+'\t'+TempCapList[4]
        fp.write("%s\n" % TempStr0)
        fp.write("%s\n" % TempStr1)
        fp.write("%s\n" % TempStr2)
        fp.write("%s\n" % TempStr3)
        fp.write("%s\n" % TempStr4)
        i=i+1
        del TempCapList
    print('File Creation Completed')
file.close()