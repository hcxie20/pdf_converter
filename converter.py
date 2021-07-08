import os
# from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function

def is_pdf(file_name, file_path):
    return os.path.isfile(os.path.join(file_path, file_name)) and file_name[-4:] == ".pdf"

pdf_dir = "c:\\Users\haochenxie\Desktop\docs\第二医院"
pdf_names = [file_name for file_name in os.listdir(pdf_dir) if is_pdf(file_name, pdf_dir)]

def convert_to_image(file_name, file_path):
    images = convert_from_path(os.path.join(file_path, file_name))

    for i in range(len(images)):
        print(os.path.join(file_path, file_name[-4:]) + '_page_' + ('{0}'.format()).zfill(len(str(len(images)))))
        # images[i].save(os.path.join(file_path, file_name[-4:]) + '_page_' + ('{0}'.format()).zfill(len(str(len(images)))))

for file_name in pdf_names:
    convert_to_image(file_name, pdf_dir)
 