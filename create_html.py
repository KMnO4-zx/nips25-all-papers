#!/usr/bin/env python3
"""
创建包含所有NeurIPS 2025论文核心信息的HTML页面
"""

import json
from html import escape

def create_simple_html_page():
    """创建简洁的HTML页面，包含所有论文的核心信息"""
    
    # 读取论文数据
    with open('./neurips2025_all_papers.json', 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    # 按类型分组论文
    oral_papers = [p for p in papers_data if p['type'] == 'oral']
    spotlight_papers = [p for p in papers_data if p['type'] == 'spotlight']
    poster_papers = [p for p in papers_data if p['type'] == 'poster']
    
    # 创建HTML内容
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeurIPS 2025 论文集 - 全部5275篇论文</title>
    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 24px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
            color: #1a1a2e;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        }}

        .header {{
            text-align: center;
            margin-bottom: 48px;
            padding-bottom: 32px;
            border-bottom: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: -40px -40px 40px -40px;
            padding: 48px 40px 36px;
            border-radius: 16px 16px 0 0;
            color: white;
        }}

        .header h1 {{
            font-size: 2.6rem;
            color: white;
            margin: 0 0 8px 0;
            font-weight: 800;
            letter-spacing: -0.5px;
        }}

        .header .subtitle {{
            font-size: 1.1rem;
            color: rgba(255,255,255,0.85);
            margin-bottom: 8px;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 16px;
            margin: 28px 0 0;
            flex-wrap: wrap;
        }}

        .stat-item {{
            text-align: center;
            padding: 14px 24px;
            background: rgba(255,255,255,0.15);
            border-radius: 12px;
            border-left: none;
            backdrop-filter: blur(4px);
        }}

        .stat-number {{
            font-size: 1.8rem;
            font-weight: 800;
            color: white;
            display: block;
        }}

        .stat-label {{
            font-size: 0.85rem;
            color: rgba(255,255,255,0.8);
            margin-top: 2px;
        }}
        
        .section {{
            margin: 48px 0;
        }}

        .section-title {{
            font-size: 1.4rem;
            color: #1a1a2e;
            margin-bottom: 24px;
            padding-bottom: 12px;
            border-bottom: 2px solid #e8ecf1;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .section-count {{
            color: #8e99a4;
            font-size: 0.95rem;
            font-weight: 400;
        }}

        .paper-card {{
            background: #ffffff;
            border: 1px solid #e8ecf1;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
            transition: box-shadow 0.2s ease, transform 0.2s ease;
            page-break-inside: avoid;
        }}

        .paper-card:hover {{
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            transform: translateY(-1px);
        }}
        
        .paper-type {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.7rem;
            font-weight: 700;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .paper-type.oral {{
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
        }}

        .paper-type.spotlight {{
            background: linear-gradient(135deg, #ffa502, #e67e22);
            color: white;
        }}

        .paper-type.poster {{
            background: linear-gradient(135deg, #2ed573, #20bf6b);
            color: white;
        }}

        .paper-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #1a1a2e;
            margin-bottom: 10px;
            line-height: 1.4;
        }}

        .paper-authors {{
            color: #6c7a89;
            font-size: 0.88rem;
            margin-bottom: 10px;
            font-style: italic;
            line-height: 1.5;
        }}

        .paper-meta {{
            color: #5a6c7d;
            font-size: 0.82rem;
            margin-bottom: 5px;
            padding: 3px 0;
            display: flex;
            align-items: baseline;
            gap: 6px;
            line-height: 1.5;
            font-style: italic;
        }}

        .paper-abstract {{
            color: #3d3d3d;
            font-size: 0.88rem;
            line-height: 1.65;
            margin: 14px 0;
            text-align: justify;
            padding: 12px 16px;
            background: #f8f9fb;
            border-radius: 8px;
            border-left: 3px solid #dde1e7;
        }}
        
        .paper-links {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 14px;
        }}

        .paper-link {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 7px 14px;
            background: #eef1f6;
            color: #4a5568;
            text-decoration: none;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 500;
            transition: all 0.2s ease;
            border: 1px solid transparent;
        }}

        .paper-link:hover {{
            background: #667eea;
            color: white;
            border-color: #667eea;
            transform: translateY(-1px);
        }}
        
        .footer {{
            text-align: center;
            margin-top: 56px;
            padding-top: 32px;
            border-top: 2px solid #e8ecf1;
            color: #8e99a4;
            font-size: 0.9rem;
        }}

        .footer p {{
            margin: 6px 0;
        }}

        .download-section {{
            background: linear-gradient(135deg, #f8f9fb 0%, #eef1f6 100%);
            padding: 28px;
            border-radius: 12px;
            margin: 32px 0;
            text-align: center;
            border: 1px solid #e8ecf1;
        }}

        .download-section h3 {{
            margin: 0 0 8px;
            color: #1a1a2e;
            font-weight: 700;
        }}

        .download-section p {{
            color: #6c7a89;
            margin: 0 0 16px;
            font-size: 0.92rem;
        }}

        .download-btn {{
            display: inline-block;
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin: 5px;
            font-weight: 600;
            font-size: 0.88rem;
            transition: all 0.2s ease;
        }}

        .download-btn:hover {{
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(102,126,234,0.4);
        }}
        
        @media print {{
            body {{
                background: white !important;
                padding: 10px !important;
            }}

            .container {{
                box-shadow: none !important;
                padding: 10px !important;
            }}

            .header {{
                background: #667eea !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .paper-card {{
                break-inside: avoid;
                page-break-inside: avoid;
                margin-bottom: 10px !important;
                padding: 15px !important;
                box-shadow: none !important;
            }}

            .paper-card:hover {{
                transform: none !important;
                box-shadow: none !important;
            }}

            .section {{
                page-break-before: always;
            }}

            .download-section {{
                display: none !important;
            }}
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 12px;
            }}

            .container {{
                padding: 20px;
            }}

            .header {{
                margin: -20px -20px 28px -20px;
                padding: 32px 20px 28px;
            }}

            .header h1 {{
                font-size: 1.8rem;
            }}

            .stats {{
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }}

            .stat-item {{
                width: 100%;
                max-width: 200px;
            }}

            .paper-card {{
                padding: 16px;
            }}

            .paper-links {{
                flex-direction: column;
            }}

            .paper-link {{
                text-align: center;
                justify-content: center;
            }}
        }}
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>NeurIPS 2025</h1>
            <div class="subtitle">第39届 NIPS 会议论文集</div>
            <div class="subtitle">完整收录5,275篇接收论文</div>
            
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">{len(oral_papers)}</span>
                    <span class="stat-label">Oral论文</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(spotlight_papers)}</span>
                    <span class="stat-label">Spotlight论文</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(poster_papers)}</span>
                    <span class="stat-label">Poster论文</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(papers_data)}</span>
                    <span class="stat-label">总论文数</span>
                </div>
            </div>
        </div>

        <div class="download-section">
            <h3>📥 数据下载</h3>
            <p>获取完整的论文数据集和PDF报告</p>
            <a href="neurips2025_all_papers.json" class="download-btn" download>📄 JSON数据集</a>
            <a href="neurips2025_all_papers_complete.csv" class="download-btn" download>📊 CSV数据集</a>
            <a href="README.md" class="download-btn" download>📖 使用说明</a>
        </div>
'''
    
    # 添加Oral论文部分
    html_content += f'''
        <div class="section">
            <h2 class="section-title">
                Oral 论文 <span class="section-count">({len(oral_papers)}篇)</span>
            </h2>
'''
    
    for i, paper in enumerate(oral_papers):
        authors = escape(', '.join(paper['authors']))
        abstract = escape(paper['abstract'])
        title = escape(paper['title'])
        area = escape(paper['primary_area'])
        keywords = escape(', '.join(paper['keywords']))

        html_content += f'''
            <div class="paper-card">
                <div class="paper-type oral">Oral</div>
                <div class="paper-title">{i+1}. {title}</div>
                <div class="paper-authors">作者: {authors}</div>
                <div class="paper-meta">领域: {area}</div>
                <div class="paper-meta">关键词: {keywords}</div>
                <div class="paper-abstract">{abstract}</div>
                <div class="paper-links">
                    <a href="https://openreview.net/forum?id={paper['paper_id']}" class="paper-link" target="_blank">📄 openreview</a>
                    <a href="https://openreview.net/pdf?id={paper['paper_id']}" class="paper-link" target="_blank">📄 下载PDF</a>
                    <a href="https://paper-online.onrender.com/?id={paper['paper_id']}" class="paper-link" target="_blank">🤖 LLM-Analysis</a>
                </div>
            </div>
'''

    html_content += '''
        </div>
'''

    # 添加Spotlight论文部分
    html_content += f'''
        <div class="section">
            <h2 class="section-title">
                Spotlight 论文 <span class="section-count">({len(spotlight_papers)}篇)</span>
            </h2>
'''
    
    for i, paper in enumerate(spotlight_papers):
        authors = escape(', '.join(paper['authors']))
        abstract = escape(paper['abstract'])
        title = escape(paper['title'])
        area = escape(paper['primary_area'])
        keywords = escape(', '.join(paper['keywords']))

        html_content += f'''
            <div class="paper-card">
                <div class="paper-type spotlight">Spotlight</div>
                <div class="paper-title">{i+1}. {title}</div>
                <div class="paper-authors">作者: {authors}</div>
                <div class="paper-meta">领域: {area}</div>
                <div class="paper-meta">关键词: {keywords}</div>
                <div class="paper-abstract">{abstract}</div>
                <div class="paper-links">
                    <a href="https://openreview.net/forum?id={paper['paper_id']}" class="paper-link" target="_blank">📄 openreview</a>
                    <a href="https://openreview.net/pdf?id={paper['paper_id']}" class="paper-link" target="_blank">📄 下载PDF</a>
                    <a href="https://paper-online.onrender.com/?id={paper['paper_id']}" class="paper-link" target="_blank">🤖 LLM-Analysis</a>
                </div>
            </div>
'''

    html_content += '''
        </div>
'''

    # 添加Poster论文部分
    html_content += f'''
        <div class="section">
            <h2 class="section-title">
                Poster 论文 <span class="section-count">({len(poster_papers)}篇)</span>
            </h2>
'''
    
    for i, paper in enumerate(poster_papers):
        authors = escape(', '.join(paper['authors']))
        abstract = escape(paper['abstract'])
        title = escape(paper['title'])
        area = escape(paper['primary_area'])
        keywords = escape(', '.join(paper['keywords']))

        html_content += f'''
            <div class="paper-card">
                <div class="paper-type poster">Poster</div>
                <div class="paper-title">{i+1}. {title}</div>
                <div class="paper-authors">作者: {authors}</div>
                <div class="paper-meta">领域: {area}</div>
                <div class="paper-meta">关键词: {keywords}</div>
                <div class="paper-abstract">{abstract}</div>
                <div class="paper-links">
                    <a href="https://openreview.net/forum?id={paper['paper_id']}" class="paper-link" target="_blank">📄 openreview</a>
                    <a href="https://openreview.net/pdf?id={paper['paper_id']}" class="paper-link" target="_blank">📄 下载PDF</a>
                    <a href="https://paper-online.onrender.com/?id={paper['paper_id']}" class="paper-link" target="_blank">🤖 LLM-Analysis</a>
                </div>
            </div>
'''

    html_content += '''
        </div>

        <div class="footer">
            <p><strong>NeurIPS 2025 完整论文集</strong></p>
            <p>数据来源: OpenReview官方平台</p>
            <p>会议时间: 2025年12月1-7日 | 地点: 美国圣地亚哥</p>
            <p>数据更新时间: 2025年11月15日</p>
        </div>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            renderMathInElement(document.body, {
                delimiters: [
                    {left: "$$", right: "$$", display: true},
                    {left: "$", right: "$", display: false}
                ],
                throwOnError: false
            });
        });
    </script>
</body>
</html>'''
    
    # 保存HTML文件
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"完整HTML页面已创建")
    print(f"页面包含 {len(papers_data)} 篇论文的完整信息")
    
    return 'index.html'

if __name__ == "__main__":
    create_simple_html_page()