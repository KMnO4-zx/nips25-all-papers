# NeurIPS 2025 Papers Crawler

## 简介
这是一个用于从 OpenReview API 获取 NeurIPS 2025 会议论文的 Python 爬虫脚本，支持 Poster、Oral 和 Spotlight 三种论文类型。

## 功能特点

- ✅ 自动分页获取所有论文（Poster/Oral/Spotlight）
- ✅ 提取论文标题、作者、摘要、PDF链接等完整元数据
- ✅ 支持 JSON 和 CSV 两种输出格式
- ✅ 显示进度条，实时监控获取进度
- ✅ 支持断点续传（重新运行会自动跳过已获取的论文）
- ✅ 错误处理和网络异常恢复
- ✅ 遵守 API 请求的礼貌性延迟
- ✅ 输出文件名自动根据论文类型调整

## 提取的字段

每篇论文包含以下信息：
- `paper_id`: 论文唯一标识符
- `title`: 论文标题
- `authors`: 作者列表
- `abstract`: 论文摘要
- `keywords`: 关键词列表
- `primary_area`: 研究领域/类别
- `venue`: 会议场馆 (如 "NeurIPS 2025 poster")
- `tldr`: 简要总结（如果有）
- `pdf_url`: PDF 下载链接
  - 使用 `https://openreview.net/attachment?id={paper_id}&name=pdf` 格式
- `forum_url`: 论文页面链接
- `submission_date`: 提交日期
- `reply_count`: 回复/评论数量

## API 信息

- **API 端点**: `https://api2.openreview.net/notes`
- **查询参数**:
  - `content.venue=NeurIPS 2025 poster` (或 `oral`, `spotlight`)
  - `details=replyCount,presentation,writable`
  - `domain=NeurIPS.cc/2025/Conference`
  - `invitation=NeurIPS.cc/2025/Conference/-/Submission`
  - `limit=25`: 每页 25 篇论文
- **论文数量参考**（基于 NeurIPS 历史数据估算）:
  - Poster 论文: 4515 篇（主要论文类型，数量最多）
  - Oral 论文: 77 篇（高质量口头报告，会议亮点，录取率极低）
  - Spotlight 论文: 683 篇（优秀论文快速展示，录取率低）
  - **注**: 具体数量请以 OpenReview 官网为准，会随会议最终确定而变化
- **分页**: 根据论文总数自动计算页数

## 使用方法

### 基本使用

```bash
# 安装依赖
pip install tqdm requests

# 运行脚本（获取 Poster 论文）
python request_nips25.py
```

#### 获取不同类型的论文

修改脚本中的 `PAPER_VENUE` 变量来获取不同类型的论文：

```python
# 在 request_nips25.py 中修改此行：
PAPER_VENUE = "NeurIPS 2025 poster"    # Poster 论文（数量最多）
# PAPER_VENUE = "NeurIPS 2025 oral"    # Oral 论文（高质量口头报告）
# PAPER_VENUE = "NeurIPS 2025 spotlight" # Spotlight 论文（亮点论文）
```

每次修改后重新运行脚本即可：
```bash
python request_nips25.py
```

### 自定义配置

可以在脚本开头修改以下配置参数：

```python
LIMIT = 25              # 每页论文数量（不建议修改）
INITIAL_DELAY = 0.8     # 请求延迟（秒）
OUTPUT_FORMAT = "json"  # 输出格式: "json" 或 "csv"

# 选择要获取的论文类型
PAPER_VENUE = "NeurIPS 2025 poster"  # 可改为: "NeurIPS 2025 oral" 或 "NeurIPS 2025 spotlight"
```

#### 支持的论文类型

修改 `PAPER_VENUE` 变量来获取不同类型的论文：

- **Poster 论文** (数量最多): `"NeurIPS 2025 poster"`
- **Oral 论文** (高质量口头报告): `"NeurIPS 2025 oral"`
- **Spotlight 论文** (亮点论文): `"NeurIPS 2025 spotlight"`

示例：
```python
# 获取 Oral 论文
PAPER_VENUE = "NeurIPS 2025 oral"

# 获取 Spotlight 论文
PAPER_VENUE = "NeurIPS 2025 spotlight"
```

### 输出文件

脚本会生成以下文件之一（文件名会根据论文类型自动调整）：

- **Poster 论文**: `nips25_poster_papers.json` 或 `nips25_poster_papers.csv`
- **Oral 论文**: `nips25_oral_papers.json` 或 `nips25_oral_papers.csv`
- **Spotlight 论文**: `nips25_spotlight_papers.json` 或 `nips25_spotlight_papers.csv`

示例（以 Poster 论文为例）：
- `nips25_poster_papers.json` - JSON 格式（推荐，保留完整结构）
- `nips25_poster_papers.csv` - CSV 格式（适合 Excel）

## PDF 链接说明

NeurIPS 2025 的 PDF 链接支持两种格式：
1. `https://openreview.net/pdf?id={paper_id}`
2. `https://openreview.net/attachment?id={paper_id}&name=pdf`

脚本优先使用 API 返回的 pdf 路径，如果不可用则使用第二种格式。

## 示例输出

### JSON 格式

```json
[
  {
    "paper_id": "RxWILaXuhb",
    "number": 1,
    "title": "Paper Title",
    "authors": ["Author Name 1", "Author Name 2"],
    "abstract": "Paper abstract...",
    "keywords": ["keyword1", "keyword2"],
    "primary_area": "deep learning",
    "pdf_url": "https://openreview.net/attachment?id=RxWILaXuhb&name=pdf",
    "forum_url": "https://openreview.net/forum?id=RxWILaXuhb",
    "submission_date": "2025-05-15 10:30:00",
    "reply_count": 5
  }
]
```

### CSV 格式

```csv
paper_id,number,version,title,authors,abstract,keywords,primary_area,venue,...,pdf_url,forum_url,submission_date,reply_count
RxWILaXuhb,1,1,Paper Title,"Author Name 1; Author Name 2",Paper abstract...,"keyword1; keyword2",deep learning,NeurIPS 2025 (poster/oral/spotlight),...,https://openreview.net/attachment?id=RxWILaXuhb&name=pdf,https://openreview.net/forum?id=RxWILaXuhb,2025-05-15 10:30:00,5
```

## 注意事项

1. **API 限制**: 脚本默认每页 25 篇论文，符合 OpenReview API 的限制
2. **请求延迟**: 每次请求之间有 0.8 秒的延迟，以减轻对 API 服务器的压力
3. **预计时间**: 根据论文数量不同，获取时间也不同：
   - Poster 论文（~4,000-5,000 篇）: 约 3-5 分钟
   - Oral 论文（~50-100 篇）: 约 10-20 秒
   - Spotlight 论文（~100-200 篇）: 约 20-30 秒
4. **网络中断**: 如果网络中断，可以重新运行脚本，它会从上次中断的地方继续
5. **文件名**: 输出文件名会根据 `PAPER_VENUE` 自动调整，方便区分不同类型的论文：
   - Poster 论文 → `nips25_poster_papers.{json|csv}`
   - Oral 论文 → `nips25_oral_papers.{json|csv}`
   - Spotlight 论文 → `nips25_spotlight_papers.{json|csv}`

## 技术要求

- Python 3.6+
- 依赖库:
  - `requests` - HTTP 请求库
  - `tqdm` - 进度条库

## 故障排除

### 连接超时或网络错误
- 检查网络连接
- 增加 `INITIAL_DELAY` 的值（例如改为 1.5）
- 重新运行脚本

### 权限错误（Windows）
- 确保有足够的权限写入当前目录
- 或以管理员身份运行

### JSON/CSV 解析错误
- 确保已安装所有依赖库
- 重新安装依赖: `pip install --upgrade requests tqdm`

## 许可证

Apache License 2.0

## 更新日志

- 2025-11-15: 初始版本发布
