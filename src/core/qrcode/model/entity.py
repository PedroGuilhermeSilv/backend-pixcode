import os
import shutil
from dataclasses import dataclass

import boto3
from dotenv import load_dotenv

from qrcode.constants import (  # noqa
    ERROR_CORRECT_L,
)
from qrcode.main import QRCode as QRCODE

load_dotenv()

@dataclass
class QRCode:
    image_url: str = ""


    def generate_qr_code(self, payload: str, image_name: str)-> str:
        self.clean_tmp()
        qr = QRCODE(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        path_for_save = f"src/core/qrcode/tmp/{image_name}"
        img.save(path_for_save)
        self.save_in_storage(path_file=path_for_save, file_name=image_name)
        return image_name

    def save_in_storage(self, path_file: str, file_name: str):
        s3 = boto3.resource(
        service_name='s3',
        aws_access_key_id=os.getenv('SECRET_ID_TEBI'),
        aws_secret_access_key=os.getenv('SECRET_KEY_TEBI'),
        endpoint_url='https://s3.tebi.io'
        )
        data = open(path_file, 'rb')
        s3.Bucket('aula').put_object(Key=file_name, Body=data, ACL='public-read')
        self.image_url = f"https://aula.s3.tebi.io/{file_name}"
        self.clean_tmp()
            
    def clean_tmp(self):
        folder = 'src/core/qrcode/tmp'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
