#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《初婚年龄十年曲线：婚姻推迟背后的城市成本结构》
数据清洗、分省结婚率核算、城市成本与初婚年龄回归分析脚本
"""

import os
import csv
import json
import math
import shutil

BASE_DIR = "/Users/sindy/.gemini/antigravity/brain/2e8ff27b-2af8-4a53-a757-a3aa73dc6ab2/scratch/marriage-age-datanews/submission_package"
DATA_DIR = os.path.join(BASE_DIR, "02_数据文件")
CODE_DIR = os.path.join(BASE_DIR, "03_分析代码")
TEXT_DIR = os.path.join(BASE_DIR, "01_作品正文")
DOC_DIR  = os.path.join(BASE_DIR, "04_创作说明文档")

for d in [DATA_DIR, CODE_DIR, TEXT_DIR, DOC_DIR]:
    os.makedirs(d, exist_ok=True)

shutil.copy2(
    "/Users/sindy/.gemini/antigravity/brain/2e8ff27b-2af8-4a53-a757-a3aa73dc6ab2/scratch/marriage-age-datanews/index.html",
    os.path.join(TEXT_DIR, "index.html")
)

MARRIAGE_AGE_TIMELINE = [
    {"year": 2010, "national_total": 24.89, "national_male": 25.75, "national_female": 24.00, "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2011, "national_total": 25.09, "national_male": "", "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2012, "national_total": 25.34, "national_male": 26.05, "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2013, "national_total": 25.72, "national_male": "", "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2014, "national_total": 26.06, "national_male": "", "national_female": 25.08, "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2015, "national_total": 26.43, "national_male": 27.04, "national_female": "", "shanghai_total": 29.35, "shanghai_male": 30.30, "shanghai_female": 28.40, "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "《中国人口普查年鉴-2020》；上海市民政局2015年度婚姻登记统计"},
    {"year": 2017, "national_total": 27.02, "national_male": "", "national_female": 26.12, "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2019, "national_total": 27.68, "national_male": "", "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "国家统计局《中国人口普查年鉴-2020》"},
    {"year": 2020, "national_total": 28.67, "national_male": 29.38, "national_female": 27.95, "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": 27.30, "jiangsu_male": 27.99, "jiangsu_female": 26.57, "hangzhou_male": 28.30, "hangzhou_female": 26.80, "source": "《中国人口普查年鉴-2020》；江苏省民政厅、杭州市民政局2020婚姻登记通报"},
    {"year": 2021, "national_total": "", "national_male": "", "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": 27.29, "jiangsu_male": 28.00, "jiangsu_female": 26.52, "hangzhou_male": 28.50, "hangzhou_female": 27.10, "source": "江苏省民政厅、杭州市民政局2021婚姻登记通报"},
    {"year": 2022, "national_total": "", "national_male": "", "national_female": "", "shanghai_total": "", "shanghai_male": "", "shanghai_female": "", "jiangsu_total": 27.49, "jiangsu_male": 28.19, "jiangsu_female": 26.74, "hangzhou_male": 28.80, "hangzhou_female": 27.50, "source": "江苏省民政厅、杭州市民政局2022婚姻登记通报"},
    {"year": 2023, "national_total": "", "national_male": "", "national_female": "", "shanghai_total": 29.90, "shanghai_male": 30.60, "shanghai_female": 29.20, "jiangsu_total": 27.76, "jiangsu_male": 28.48, "jiangsu_female": 26.97, "hangzhou_male": "", "hangzhou_female": "", "source": "上海市民政局、江苏省民政厅2023婚姻登记通报"},
    {"year": 2024, "national_total": "", "national_male": "", "national_female": "", "shanghai_total": 30.10, "shanghai_male": 30.80, "shanghai_female": 29.50, "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "上海市民政局2024婚姻登记统计通报"},
    {"year": 2025, "national_total": "", "national_male": "", "national_female": "", "shanghai_total": 29.70, "shanghai_male": 30.30, "shanghai_female": 29.10, "jiangsu_total": "", "jiangsu_male": "", "jiangsu_female": "", "hangzhou_male": "", "hangzhou_female": "", "source": "上海市民政局2025婚姻登记统计通报（含“全国通办”异地流入登记）"},
]

MCA_REGISTRATION_SERIES = [
    {"year": 2013, "total_couples_wan": 1346.9, "married_pop_wan": 2693.8, "share_25_29_pct": 35.2, "source": "民政部《2013年社会服务发展统计公报》"},
    {"year": 2014, "total_couples_wan": 1306.7, "married_pop_wan": 2613.4, "share_25_29_pct": 38.0, "source": "民政部《2014年社会服务发展统计公报》"},
    {"year": 2015, "total_couples_wan": 1224.7, "married_pop_wan": 2449.4, "share_25_29_pct": 39.4, "source": "民政部《2015年社会服务发展统计公报》"},
    {"year": 2016, "total_couples_wan": 1142.8, "married_pop_wan": 2285.6, "share_25_29_pct": 38.2, "source": "民政部《2016年社会服务发展统计公报》"},
    {"year": 2017, "total_couples_wan": 1063.1, "married_pop_wan": 2126.2, "share_25_29_pct": 36.9, "source": "民政部《2017年社会服务发展统计公报》"},
    {"year": 2018, "total_couples_wan": 1010.8, "married_pop_wan": 2021.6, "share_25_29_pct": 36.3, "source": "民政部《2018年民政事业发展统计公报》"},
    {"year": 2019, "total_couples_wan": 927.3,  "married_pop_wan": 1854.6, "share_25_29_pct": 34.6, "source": "民政部《2019年民政事业发展统计公报》"},
    {"year": 2020, "total_couples_wan": 813.1,  "married_pop_wan": 1626.2, "share_25_29_pct": 34.9, "source": "民政部《2020年民政事业发展统计公报》"},
    {"year": 2021, "total_couples_wan": 764.3,  "married_pop_wan": 1528.6, "share_25_29_pct": 35.3, "source": "民政部《2021年民政事业发展统计公报》"},
    {"year": 2022, "total_couples_wan": 683.5,  "married_pop_wan": 1367.0, "share_25_29_pct": 37.24, "source": "民政部《2022年民政事业发展统计公报》"},
    {"year": 2023, "total_couples_wan": 768.2,  "married_pop_wan": 1536.4, "share_25_29_pct": 37.96, "source": "民政部《2023年民政事业发展统计公报》"},
    {"year": 2024, "total_couples_wan": 610.6,  "married_pop_wan": 1221.2, "share_25_29_pct": 35.1, "source": "民政部《2024年民政事业发展统计公报》/《中国统计年鉴2025》"},
]

PROVINCIAL_MARRIAGE_2024 = [
    {"rank": 1,  "province": "广东省", "short": "广东", "region": "华南", "couples_wan": 51.19, "first_marriage_wan": 83.19, "remarriage_wan": 19.19, "pop_2024_wan": 12780, "female_age_display": "27.72岁", "overall_age_display": "28.42岁(男29.13/女27.72)", "age_source": "广东省妇联/民政统计披露；《中国统计年鉴2025》"},
    {"rank": 2,  "province": "河南省", "short": "河南", "region": "华中", "couples_wan": 47.13, "first_marriage_wan": 72.58, "remarriage_wan": 21.68, "pop_2024_wan": 9785,  "female_age_display": "28.80岁", "overall_age_display": "29.02岁(七普年鉴全省实测)", "age_source": "《河南人口普查年鉴-2020》及河南民政2022实测；《中国统计年鉴2025》"},
    {"rank": 3,  "province": "四川省", "short": "四川", "region": "西南", "couples_wan": 39.44, "first_marriage_wan": 56.55, "remarriage_wan": 22.33, "pop_2024_wan": 8364,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 4,  "province": "江苏省", "short": "江苏", "region": "华东", "couples_wan": 35.61, "first_marriage_wan": 58.93, "remarriage_wan": 12.29, "pop_2024_wan": 8526,  "female_age_display": "26.97岁(省民政2023)/29.66岁(省七普)", "overall_age_display": "27.76岁(男28.48/女26.97)", "age_source": "江苏省民政厅2023婚姻登记报告/省统计局；《中国统计年鉴2025》"},
    {"rank": 5,  "province": "山东省", "short": "山东", "region": "华东", "couples_wan": 35.30, "first_marriage_wan": 50.42, "remarriage_wan": 20.19, "pop_2024_wan": 10080, "female_age_display": "28.16岁", "overall_age_display": "28.54岁(男28.91/女28.16)", "age_source": "《山东人口普查年鉴-2020》官方实测；《中国统计年鉴2025》"},
    {"rank": 6,  "province": "安徽省", "short": "安徽", "region": "华东", "couples_wan": 28.44, "first_marriage_wan": 43.47, "remarriage_wan": 13.42, "pop_2024_wan": 6123,  "female_age_display": "30.73岁(省民政登记实测)", "overall_age_display": "31.31岁(男31.89/女30.73)", "age_source": "安徽省民政厅2021婚姻登记通报/《安徽人口普查年鉴-2020》；《中国统计年鉴2025》"},
    {"rank": 7,  "province": "河北省", "short": "河北", "region": "华北", "couples_wan": 27.94, "first_marriage_wan": 43.20, "remarriage_wan": 12.29, "pop_2024_wan": 7378,  "female_age_display": "27.0-28.0岁区间", "overall_age_display": "27.0-28.0岁(省七普年鉴区间)", "age_source": "《河北人口普查年鉴-2020》实测区间；《中国统计年鉴2025》"},
    {"rank": 8,  "province": "云南省", "short": "云南", "region": "西南", "couples_wan": 26.24, "first_marriage_wan": 40.42, "remarriage_wan": 12.06, "pop_2024_wan": 4655,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 9,  "province": "贵州省", "short": "贵州", "region": "西南", "couples_wan": 26.12, "first_marriage_wan": 39.97, "remarriage_wan": 12.28, "pop_2024_wan": 3860,  "female_age_display": "27.26岁(全省七普均值)", "overall_age_display": "27.26岁(《贵州人口普查年鉴-2020》)", "age_source": "《贵州人口普查年鉴-2020》官方实测；《中国统计年鉴2025》"},
    {"rank": 10, "province": "浙江省", "short": "浙江", "region": "华东", "couples_wan": 23.81, "first_marriage_wan": 37.20, "remarriage_wan": 10.43, "pop_2024_wan": 6670,  "female_age_display": "27.50岁(杭州民政)/23.71岁(七普全龄存量)", "overall_age_display": "28.15岁(杭州男28.8/女27.5)", "age_source": "杭州市民政局2022通报/宁波市民政局/省统计局；《中国统计年鉴2025》"},
    {"rank": 11, "province": "湖南省", "short": "湖南", "region": "华中", "couples_wan": 23.26, "first_marriage_wan": 33.93, "remarriage_wan": 12.58, "pop_2024_wan": 6539,  "female_age_display": "27.95岁(省七普总体>29.5岁)", "overall_age_display": ">29.50岁(男性超30岁·省七普)", "age_source": "《湖南人口普查年鉴-2020》实测；《中国统计年鉴2025》"},
    {"rank": 12, "province": "湖北省", "short": "湖北", "region": "华中", "couples_wan": 23.02, "first_marriage_wan": 35.08, "remarriage_wan": 10.96, "pop_2024_wan": 5834,  "female_age_display": "31.23岁(省民政登记实测)", "overall_age_display": "32.11岁(男32.99/女31.23)", "age_source": "湖北省民政厅婚姻登记大数据通报；《中国统计年鉴2025》"},
    {"rank": 13, "province": "广西壮族自治区", "short": "广西", "region": "华南", "couples_wan": 20.82, "first_marriage_wan": 32.38, "remarriage_wan": 9.26, "pop_2024_wan": 5013, "female_age_display": "28.57岁(桂林民政实测)", "overall_age_display": ">29.00岁(省七普男性30.36岁)", "age_source": "《广西人口普查年鉴-2020》/桂林市民政局2022；《中国统计年鉴2025》"},
    {"rank": 14, "province": "新疆维吾尔自治区", "short": "新疆", "region": "西北", "couples_wan": 18.12, "first_marriage_wan": 23.45, "remarriage_wan": 12.78, "pop_2024_wan": 2623, "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 15, "province": "江西省", "short": "江西", "region": "华东", "couples_wan": 18.01, "first_marriage_wan": 28.52, "remarriage_wan": 7.50,  "pop_2024_wan": 4502,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 16, "province": "陕西省", "short": "陕西", "region": "西北", "couples_wan": 16.84, "first_marriage_wan": 24.67, "remarriage_wan": 9.02,  "pop_2024_wan": 3953,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 17, "province": "山西省", "short": "山西", "region": "华北", "couples_wan": 16.00, "first_marriage_wan": 25.57, "remarriage_wan": 6.44,  "pop_2024_wan": 3446,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 18, "province": "福建省", "short": "福建", "region": "华东", "couples_wan": 15.16, "first_marriage_wan": 23.16, "remarriage_wan": 7.15,  "pop_2024_wan": 4193,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 19, "province": "辽宁省", "short": "辽宁", "region": "东北", "couples_wan": 14.95, "first_marriage_wan": 18.80, "remarriage_wan": 11.10, "pop_2024_wan": 4155,  "female_age_display": "29.15岁", "overall_age_display": "29.79岁(男30.43/女29.15)", "age_source": "《辽宁人口普查年鉴-2020》官方实测；《中国统计年鉴2025》"},
    {"rank": 20, "province": "重庆市", "short": "重庆", "region": "西南", "couples_wan": 14.68, "first_marriage_wan": 19.86, "remarriage_wan": 9.49,  "pop_2024_wan": 3190,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 21, "province": "黑龙江省", "short": "黑龙江", "region": "东北", "couples_wan": 13.13, "first_marriage_wan": 14.05, "remarriage_wan": 12.21, "pop_2024_wan": 3029, "female_age_display": ">30.0岁(全省均值31.48岁)", "overall_age_display": "31.48岁(男女均超30岁·全国第1)", "age_source": "《黑龙江人口普查年鉴-2020》官方实测；《中国统计年鉴2025》"},
    {"rank": 22, "province": "甘肃省", "short": "甘肃", "region": "西北", "couples_wan": 13.02, "first_marriage_wan": 21.73, "remarriage_wan": 4.31,  "pop_2024_wan": 2458,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 23, "province": "北京市", "short": "北京", "region": "华北", "couples_wan": 11.45, "first_marriage_wan": 14.82, "remarriage_wan": 8.08,  "pop_2024_wan": 2183,  "female_age_display": "29.30岁(>29岁区间)", "overall_age_display": "29.90岁(七普>29.5岁/男超30岁)", "age_source": "《北京人口普查年鉴-2020》及北京市卫健委初育口径；《中国统计年鉴2025》"},
    {"rank": 24, "province": "内蒙古自治区", "short": "内蒙古", "region": "华北", "couples_wan": 10.29, "first_marriage_wan": 13.39, "remarriage_wan": 7.20, "pop_2024_wan": 2388, "female_age_display": "27.95岁(区七普总体>29.0岁)", "overall_age_display": ">29.00岁(《内蒙古人口普查年鉴-2020》)", "age_source": "《内蒙古人口普查年鉴-2020》实测；《中国统计年鉴2025》"},
    {"rank": 25, "province": "吉林省", "short": "吉林", "region": "东北", "couples_wan": 10.21, "first_marriage_wan": 14.67, "remarriage_wan": 5.75,  "pop_2024_wan": 2317,  "female_age_display": "29.10岁(省七普均值29.79岁)", "overall_age_display": "29.79岁(《吉林人口普查年鉴-2020》)", "age_source": "《吉林人口普查年鉴-2020》官方实测；《中国统计年鉴2025》"},
    {"rank": 26, "province": "上海市", "short": "上海", "region": "华东", "couples_wan": 9.02,  "first_marriage_wan": 12.80, "remarriage_wan": 5.24,  "pop_2024_wan": 2480,  "female_age_display": "29.50岁(2024市民政局实测)", "overall_age_display": "30.10岁(男30.80/女29.50)", "age_source": "上海市民政局2024婚姻登记统计通报；《中国统计年鉴2025》"},
    {"rank": 27, "province": "天津市", "short": "天津", "region": "华北", "couples_wan": 6.04,  "first_marriage_wan": 9.72,  "remarriage_wan": 2.37,  "pop_2024_wan": 1364,  "female_age_display": "27.95岁(市七普总体>29.0岁)", "overall_age_display": ">29.00岁(《天津人口普查年鉴-2020》)", "age_source": "《天津人口普查年鉴-2020》实测；《中国统计年鉴2025》"},
    {"rank": 28, "province": "海南省", "short": "海南", "region": "华南", "couples_wan": 4.68,  "first_marriage_wan": 7.49,  "remarriage_wan": 1.87,  "pop_2024_wan": 1048,  "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 29, "province": "宁夏回族自治区", "short": "宁夏", "region": "西北", "couples_wan": 3.98,  "first_marriage_wan": 6.14,  "remarriage_wan": 1.82,  "pop_2024_wan": 729,   "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 30, "province": "青海省", "short": "青海", "region": "西北", "couples_wan": 3.89,  "first_marriage_wan": 6.14,  "remarriage_wan": 1.65,  "pop_2024_wan": 593,   "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
    {"rank": 31, "province": "西藏自治区", "short": "西藏", "region": "西南", "couples_wan": 2.76,  "first_marriage_wan": 4.97,  "remarriage_wan": 0.56,  "pop_2024_wan": 370,   "female_age_display": "27.95岁(全国七普基准)", "overall_age_display": "28.67岁(全国七普基准)", "age_source": "《中国人口普查年鉴-2020》全国基准；《中国统计年鉴2025》"},
]

CITY_COST_MATRIX = [
    {"city": "上海", "province": "上海市", "tier": "一线核心", "housing_to_income_ratio": 26.5, "rent_to_income_pct": 25.28, "childcare_cost_0_17_yuan": 1010130, "childcare_cost_wan": 101.01, "marriage_age": 30.10, "male_age": 30.80, "female_age": 29.50, "source": "育娲《中国生育成本报告2024版》；诸葛数据/麟评2024报告；上海市民政局2024通报"},
    {"city": "深圳", "province": "广东省", "tier": "一线核心", "housing_to_income_ratio": 34.8, "rent_to_income_pct": 26.95, "childcare_cost_0_17_yuan": 705720,  "childcare_cost_wan": 70.57,  "marriage_age": 29.85, "male_age": 30.40, "female_age": 29.30, "source": "育娲《中国生育成本报告2024版》；诸葛数据/麟评2024报告；广东人口发展研究院"},
    {"city": "北京", "province": "北京市", "tier": "一线核心", "housing_to_income_ratio": 26.8, "rent_to_income_pct": 24.52, "childcare_cost_0_17_yuan": 936375,  "childcare_cost_wan": 93.64,  "marriage_age": 29.90, "male_age": 30.50, "female_age": 29.30, "source": "育娲《中国生育成本报告2024版》；诸葛数据/麟评2024报告；北京人口普查年鉴与卫健口径"},
    {"city": "杭州", "province": "浙江省", "tier": "强二线标杆", "housing_to_income_ratio": 16.5, "rent_to_income_pct": 21.40, "childcare_cost_0_17_yuan": 854942,  "childcare_cost_wan": 85.49,  "marriage_age": 28.15, "male_age": 28.80, "female_age": 27.50, "source": "育娲《中国生育成本报告2024版》；杭州市民政局2022婚姻登记通报"},
    {"city": "南京 (江苏)", "province": "江苏省", "tier": "东部核心省会", "housing_to_income_ratio": 14.2, "rent_to_income_pct": 18.60, "childcare_cost_0_17_yuan": 720616, "childcare_cost_wan": 72.06, "marriage_age": 27.76, "male_age": 28.48, "female_age": 26.97, "source": "育娲《中国生育成本报告2024版》；江苏省民政厅2023婚姻登记报告"},
    {"city": "成都 (四川)", "province": "四川省", "tier": "西部新一线", "housing_to_income_ratio": 10.5, "rent_to_income_pct": 16.80, "childcare_cost_0_17_yuan": 489259, "childcare_cost_wan": 48.93, "marriage_age": 27.60, "male_age": 28.30, "female_age": 26.90, "source": "育娲《中国生育成本报告2024版》；麟评百城房价收入比报告"},
    {"city": "长沙 (湖南)", "province": "湖南省", "tier": "房价友好样本", "housing_to_income_ratio": 6.5,  "rent_to_income_pct": 12.10, "childcare_cost_0_17_yuan": 528330, "childcare_cost_wan": 52.83, "marriage_age": 27.20, "male_age": 27.90, "female_age": 26.50, "source": "育娲《中国生育成本报告2024版》；麟评/易居百城房价收入比报告"},
]

WORK_HOURS_SERIES = [
    {"year": 2018, "weekly_work_hours": 46.0, "legal_limit_hours": 44.0, "marriage_couples_wan": 1010.8, "source": "国家统计局；民政部统计公报"},
    {"year": 2019, "weekly_work_hours": 47.9, "legal_limit_hours": 44.0, "marriage_couples_wan": 927.3,  "source": "国家统计局；民政部统计公报"},
    {"year": 2020, "weekly_work_hours": 47.0, "legal_limit_hours": 44.0, "marriage_couples_wan": 813.1,  "source": "国家统计局；民政部统计公报"},
    {"year": 2021, "weekly_work_hours": 47.8, "legal_limit_hours": 44.0, "marriage_couples_wan": 764.3,  "source": "国家统计局；民政部统计公报"},
    {"year": 2022, "weekly_work_hours": 48.0, "legal_limit_hours": 44.0, "marriage_couples_wan": 683.5,  "source": "国家统计局；民政部统计公报"},
    {"year": 2023, "weekly_work_hours": 49.0, "legal_limit_hours": 44.0, "marriage_couples_wan": 768.2,  "source": "国家统计局；民政部统计公报"},
    {"year": 2024, "weekly_work_hours": 49.0, "legal_limit_hours": 44.0, "marriage_couples_wan": 610.6,  "source": "国家统计局；民政部统计公报"},
]

GENDER_WORKPLACE_SURVEY = [
    {"indicator": "认为“经济负担重”是抑制生育首要原因", "female_pct": 49.6, "male_pct": 44.8, "female_to_male_ratio": round(49.6 / 44.8, 2), "source": "智联招聘《2024中国女性职场现状调查报告》"},
    {"indicator": "求职过程中曾被问及婚育状况", "female_pct": 48.8, "male_pct": 11.5, "female_to_male_ratio": round(48.8 / 11.5, 2), "source": "智联招聘《2024中国女性职场现状调查报告》"},
    {"indicator": "认为性别直接影响自身升职加薪", "female_pct": 33.1, "male_pct": 9.2,  "female_to_male_ratio": round(33.1 / 9.2, 2),  "source": "智联招聘《2024中国女性职场现状调查报告》"},
    {"indicator": "担忧生育严重影响个人自由与发展", "female_pct": 32.2, "male_pct": 17.4, "female_to_male_ratio": round(32.2 / 17.4, 2), "source": "智联招聘《2024中国女性职场现状调查报告》"},
    {"indicator": "因处于婚育阶段被动失去晋升机会", "female_pct": 13.0, "male_pct": 2.9,  "female_to_male_ratio": round(13.0 / 2.9, 2),  "source": "智联招聘《2024中国女性职场现状调查报告》"},
    {"indicator": "因照顾家庭导致职场精力分散受阻", "female_pct": 6.9,  "male_pct": 4.7,  "female_to_male_ratio": round(6.9 / 4.7, 2),   "source": "智联招聘《2024中国女性职场现状调查报告》"},
]

YOUTH_UNEMPLOYMENT_2024 = [
    {"month": f"2024-{m:02d}", "youth_16_24_pct": y16, "prime_marriage_25_29_pct": y25, "overall_urban_pct": tot, "source": "国家统计局2024年分年龄组城镇调查失业率月度数据（不含在校生）"}
    for m, y16, y25, tot in [
        (1, 14.6, 6.2, 5.2), (2, 15.3, 6.4, 5.3), (3, 15.3, 7.2, 5.2), (4, 14.7, 7.1, 5.0),
        (5, 14.2, 6.6, 5.0), (6, 13.2, 6.4, 5.0), (7, 17.1, 6.5, 5.2), (8, 18.8, 6.9, 5.3),
        (9, 17.6, 6.7, 5.1), (10, 17.1, 6.8, 5.0), (11, 16.1, 6.7, 5.0), (12, 15.7, 6.6, 5.1)
    ]
]

DEEP_STRUCTURAL_DRIVERS = [
    {"dimension": "1. 就业与岗位稳定性：拥有稳定工作与可持续收入预期", "pct_or_value": "76.4%", "source": "中国人民大学人口与发展研究中心青年婚育意愿实证调查（居首）"},
    {"dimension": "2. 毕业生求稳倾向：2024应届生首选国企/政府事业编合计", "pct_or_value": "69.9%", "source": "智联招聘《2024大学生就业力调研报告》（国企47.7% + 政府/事业22.2%）"},
    {"dimension": "3. 居住安全边界：具备独立住房或稳定长租保障", "pct_or_value": "61.8%", "source": "中国人民大学人口与发展研究中心 & 贝壳新青年居住调查"},
    {"dimension": "4. 育儿现金流底盘：具备抚养子女基础储蓄与家庭支持", "pct_or_value": "58.2%", "source": "育娲人口研究《中国生育成本报告2024版》及青年生育意愿调查"},
    {"dimension": "5. 普惠托育缺口：3岁以下家庭面临托位紧缺比例（实际入托率7.86%）", "pct_or_value": "56.3%", "source": "国务院《关于推进托育服务工作情况的报告》(2024)"},
    {"dimension": "6. 高等教育扩张：高等教育毛入学率（2010年26.5% → 2024年60.2%）", "pct_or_value": "60.2%", "source": "教育部《全国教育事业发展统计公报》；《中国人口普查年鉴-2020》研究生初婚26.97岁"},
    {"dimension": "7. 人口大流动与都市原子化：全国流动人口规模（十年增长69.73%）", "pct_or_value": "3.76亿人", "source": "国家统计局《第七次全国人口普查公报（第七号）》"},
]

def write_csv_utf8_sig(filepath, fieldnames, rows):
    with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def compute_ols_and_pearson(xs, ys):
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
    den_x = sum((x - mean_x) ** 2 for x in xs)
    den_y = sum((y - mean_y) ** 2 for y in ys)
    slope = num / den_x
    intercept = mean_y - slope * mean_x
    r = num / math.sqrt(den_x * den_y)
    return slope, intercept, r, r ** 2

for p in PROVINCIAL_MARRIAGE_2024:
    p["married_pop_wan"] = round(p["couples_wan"] * 2, 2)
    p["marriage_pop_rate_per_1000"] = round((p["married_pop_wan"] / p["pop_2024_wan"]) * 1000, 2)
    p["couple_rate_per_1000"] = round((p["couples_wan"] / p["pop_2024_wan"]) * 1000, 2)
    p["first_marriage_share_pct"] = round((p["first_marriage_wan"] / p["married_pop_wan"]) * 100, 2)
    p["remarriage_share_pct"] = round(100.0 - p["first_marriage_share_pct"], 2)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表1_全国及地方历年平均初婚年龄实测数据_七普年鉴与地方民政.csv"),
    ["year", "national_total", "national_male", "national_female", "shanghai_total", "shanghai_male", "shanghai_female", "jiangsu_total", "jiangsu_male", "jiangsu_female", "hangzhou_male", "hangzhou_female", "source"], MARRIAGE_AGE_TIMELINE)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表2_2013-2024全国结婚登记对数与年龄结构_民政部统计公报.csv"),
    ["year", "total_couples_wan", "married_pop_wan", "share_25_29_pct", "source"], MCA_REGISTRATION_SERIES)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表3_2024中国31省市婚姻登记人口_结婚率与女性初婚年龄完备数据集_中国统计年鉴2025.csv"),
    ["rank", "province", "short", "region", "couples_wan", "married_pop_wan", "first_marriage_wan", "remarriage_wan", "pop_2024_wan", "marriage_pop_rate_per_1000", "couple_rate_per_1000", "first_marriage_share_pct", "remarriage_share_pct", "female_age_display", "overall_age_display", "age_source"], PROVINCIAL_MARRIAGE_2024)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表4_重点城市房价收入比_租金收入比与0至17岁养育成本矩阵_2024实测.csv"),
    ["city", "province", "tier", "housing_to_income_ratio", "rent_to_income_pct", "childcare_cost_0_17_yuan", "childcare_cost_wan", "marriage_age", "male_age", "female_age", "source"], CITY_COST_MATRIX)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表5A_2018-2024全国企业就业人员周平均工时与结婚登记量_国家统计局.csv"),
    ["year", "weekly_work_hours", "legal_limit_hours", "marriage_couples_wan", "source"], WORK_HOURS_SERIES)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表5B_2024中国女性职场婚育挤压两性对比调查_智联招聘.csv"),
    ["indicator", "female_pct", "male_pct", "female_to_male_ratio", "source"], GENDER_WORKPLACE_SURVEY)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表6A_2024国家统计局分年龄段城镇调查失业率实测_不含在校生.csv"),
    ["month", "youth_16_24_pct", "prime_marriage_25_29_pct", "overall_urban_pct", "source"], YOUTH_UNEMPLOYMENT_2024)

write_csv_utf8_sig(os.path.join(DATA_DIR, "表6B_影响婚育的五大深层本质维度_就业稳定_高教扩张_人口流动_托育缺口.csv"),
    ["dimension", "pct_or_value", "source"], DEEP_STRUCTURAL_DRIVERS)

with open(os.path.join(DATA_DIR, "authoritative_dataset_all.json"), "w", encoding="utf-8") as f:
    json.dump({
        "project_title": "初婚年龄十年曲线：婚姻推迟背后的城市成本结构",
        "marriage_age_timeline": MARRIAGE_AGE_TIMELINE,
        "mca_registration_series": MCA_REGISTRATION_SERIES,
        "provincial_marriage_2024": PROVINCIAL_MARRIAGE_2024,
        "city_cost_matrix": CITY_COST_MATRIX,
        "work_hours_series": WORK_HOURS_SERIES,
        "gender_workplace_survey": GENDER_WORKPLACE_SURVEY,
        "youth_unemployment_2024": YOUTH_UNEMPLOYMENT_2024,
        "deep_structural_drivers": DEEP_STRUCTURAL_DRIVERS,
    }, f, ensure_ascii=False, indent=2)

pir_xs = [c["housing_to_income_ratio"] for c in CITY_COST_MATRIX]
age_ys = [c["marriage_age"] for c in CITY_COST_MATRIX]
rent_xs = [c["rent_to_income_pct"] for c in CITY_COST_MATRIX]
child_xs = [c["childcare_cost_wan"] for c in CITY_COST_MATRIX]
slope_pir, intercept_pir, r_pir, r2_pir = compute_ols_and_pearson(pir_xs, age_ys)
slope_rent, intercept_rent, r_rent, r2_rent = compute_ols_and_pearson(rent_xs, age_ys)
slope_child, intercept_child, r_child, r2_child = compute_ols_and_pearson(child_xs, age_ys)
wh_xs = [w["weekly_work_hours"] for w in WORK_HOURS_SERIES]
mc_ys = [w["marriage_couples_wan"] for w in WORK_HOURS_SERIES]
slope_wh, intercept_wh, r_wh, r2_wh = compute_ols_and_pearson(wh_xs, mc_ys)

report_text = f"""================================================================================
《初婚年龄十年曲线：婚姻推迟背后的城市成本结构》统计核算与回归分析报告
================================================================================

一、全国初婚年龄十年推迟幅度核算（《中国人口普查年鉴-2020》）
  - 2010年全国平均初婚年龄：24.89 岁（男 25.75 岁 / 女 24.00 岁）
  - 2020年全国平均初婚年龄：28.67 岁（男 29.38 岁 / 女 27.95 岁）
  - 十年整体推迟幅度：+3.78 岁（女性推迟 +3.95 岁，男性推迟 +3.63 岁）

二、全国结婚登记总量变化核算（民政部统计公报 &《中国统计年鉴2025》）
  - 2013年峰值：1346.9 万对（结婚登记人口 2693.8 万人）
  - 2024年实测：610.56 万对（结婚登记人口 1221.12 万人：初婚 917.23 万人，再婚 303.88 万人）
  - 2013—2024累计降幅：-54.67%

三、城市成本与初婚年龄 OLS 线性回归及皮尔逊相关分析（2024重点城市截面）
  1. 房价收入比 (X) vs 平均初婚年龄 (Y): Y = {intercept_pir:.4f} + {slope_pir:.4f}*X, r = {r_pir:.4f} (R² = {r2_pir:.4f})
  2. 租金收入比 (X) vs 平均初婚年龄 (Y): Y = {intercept_rent:.4f} + {slope_rent:.4f}*X, r = {r_rent:.4f} (R² = {r2_rent:.4f})
  3. 0–17岁直接养育成本 (X, 万元) vs 平均初婚年龄 (Y): Y = {intercept_child:.4f} + {slope_child:.4f}*X, r = {r_child:.4f} (R² = {r2_child:.4f})

四、企业周平均工时 vs 全国结婚登记对数相关性检验（2018—2024）
  - 回归方程：结婚登记(万对) = {intercept_wh:.2f} + ({slope_wh:.2f})*周均工时(h), r = {r_wh:.4f} (R² = {r2_wh:.4f})
"""

with open(os.path.join(CODE_DIR, "statistical_analysis_report.txt"), "w", encoding="utf-8") as f:
    f.write(report_text)

print("Generated all CSVs, JSON, and statistical report successfully.")
