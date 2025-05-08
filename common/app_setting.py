import os
from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class Setting:
    """软件设置"""
    title: str = "Flet-GUI-basic"
    version: str = '0.4.1'
    _app_dir: str = os.getenv('APP_DIR')

    # 运行时文件保存路径
    upload_dir: str = f'{_app_dir}/user_data/uploads'
    download_dir: str = f'{_app_dir}/user_data/downloads'
    temp_dir: str = f'{_app_dir}/user_data/temp'
    notice_message_path: str = f'{_app_dir}/user_data/mes.bin'
    gpt_message_path: str = f'{_app_dir}/user_data/mes2.bin'
    bg_image_192_path: str = f'{_app_dir}/user_data/bg_192.jpg'

    # 设置页面的默认值
    language: str = '0'
    font: str = '1'
    theme: str = '0'
    bg_image_idx: int = 0
    bg_image_path: str = ''
    bg_image_opacity: float = 0.15
    thread: int = 3
    use_gpu: bool = False
    qwen_api_key: str = 'sk-7628caf375354d51a45d9202bb99da5f'
    yuanqi_id: str = 'WfdxtUNUaBUk'
    yuanqi_token: str = 'kR2C1EjEeXP0VSgVbBvYP3JHrhllb7aa'


CONFIG_OBJ = ConfigParser()
CONFIG_OBJ.read('user_data/config.ini', encoding='utf-8')
if not CONFIG_OBJ.has_section('base'):
    CONFIG_OBJ.add_section('base')
if not CONFIG_OBJ.has_section('surface'):
    CONFIG_OBJ.add_section('surface')
if not CONFIG_OBJ.has_section('function'):
    CONFIG_OBJ.add_section('function')
if not CONFIG_OBJ.has_section('shortcut'):
    CONFIG_OBJ.add_section('shortcut')
