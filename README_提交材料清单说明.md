# 数据新闻比赛提交材料包清单说明
**作品名称：《初婚年龄十年曲线：婚姻推迟背后的城市成本结构》**

本文件夹严格按照比赛提交规范整理，包含**作品正文、数据文件、分析代码、创作说明文档**四大核心模块，具体目录结构如下：

```text
数据新闻作品/
├── README_提交材料清单说明.md                 # 本提交材料结构与使用说明
├── 01_作品正文/
│   ├── index.html                            # 【核心交互作品】单文件独立运行版数据新闻网页（双击即可在浏览器运行）
│   └── 作品正文文稿_初婚年龄十年曲线：婚姻推迟背后的城市成本结构.md  # 作品完整文字稿与核心数据图表论述
├── 02_数据文件/
│   ├── 01_china_marriage_national_trend_2010_2024.csv       # 全国历年结婚登记对数、粗结婚率、周工时与普查初婚年龄（2010-2024）
│   ├── 02_china_31_provinces_marriage_and_female_age.csv    # 全国31省市女性初婚年龄、结婚登记对数、结婚人口与粗结婚率
│   ├── 03_city_marriage_age_and_living_cost.csv             # 10大样本城市初婚年龄、房价收入比、0-17岁育儿成本与房租负担比
│   ├── 04_marriage_age_distribution_2010_2022.csv           # 全国结婚登记人口分年龄段（20-24岁至40岁+）占比演变（2010-2022）
│   ├── 05_education_and_gender_housework_census2020.csv     # 七普分学历初婚年龄 & 16-59岁分性别因家务未工作比例（母职惩罚数据）
│   ├── authoritative_dataset_all.json                       # 前端可视化引擎调用的全量结构化权威数据集（JSON格式）
│   └── 数据信源与统计口径说明书.md                             # 所有数据指标的官方统计年鉴出处与计算口径说明
├── 03_分析代码/
│   ├── data_cleaning_and_analysis.py         # 数据清洗、导出与皮尔逊相关性统计检验脚本（Python 3 标准库即可运行）
│   └── statistical_analysis_report.txt       # 脚本运行自动生成的统计检验与核心极值分析报告
└── 04_创作说明文档/
    └── 创作说明文档_初婚年龄十年曲线.md         # 含：创作思路、AIGC应用情况说明、作品视觉与交互亮点说明
```

## 快速预览方式
1. **交互网页体验**：直接双击打开 `01_作品正文/index.html`（推荐使用 Chrome / Edge / Safari 浏览器，需联网加载字体与中国地图 GeoJSON 底图）。
2. **线上 GitHub 仓库地址**：`https://github.com/GEM-wb-Gloria/marriage-age-datanews`
3. **复现统计分析**：在终端运行 `python3 03_分析代码/data_cleaning_and_analysis.py` 即可重新生成所有 CSV、JSON 数据集与统计检验报告。
