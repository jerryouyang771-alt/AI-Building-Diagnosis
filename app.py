import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import time
import os

# ==========================================
# 0. 全局状态与进度管理 (RPG 机制)
# ==========================================
if 'progress' not in st.session_state:
    st.session_state.progress = 25
if 'rank' not in st.session_state:
    st.session_state.rank = "见习检测员 🧑‍🔧"
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False
if 'is_diagnosed' not in st.session_state:
    st.session_state.is_diagnosed = False

# ==========================================
# 1. 基础配置与安全样式
# ==========================================
st.set_page_config(page_title="AI 建筑诊断系统", layout="wide", page_icon="🏗️")

# 移除了激进的 CSS，只保留最安全的进度条和卡片美化，保证 100% 稳定显示
st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #FF4B4B , #FF9090); }
    .stMetric { background-color: rgba(255, 75, 75, 0.05); border: 1px solid rgba(255, 75, 75, 0.2); border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. 侧边栏：任务控制台
# ==========================================
with st.sidebar:
    st.title("🛰️ 诊断指挥中心")
    st.info(f"**当前身份：** `{st.session_state.rank}`")
    st.progress(st.session_state.progress / 100)
    st.write(f"**系统权限进度：** {st.session_state.progress}%")
    st.markdown("---")
    
    m3_label = "💻 Mission 03: 实战演习" if st.session_state.unlocked else "🔒 Mission 03: 待解锁"
    m4_label = "🏁 Mission 04: 终极报告" if st.session_state.unlocked else "🔒 Mission 04: 待解锁"
    
    # 恢复原生的 radio，保证选项文字绝对清晰
    page = st.radio(
        "请选择当前执行模块：",
        ["🏠 Mission 01: 认知觉醒", "🎥 Mission 02: 理论武装", m3_label, m4_label]
    )

# ==========================================
# 3. 页面逻辑设计
# ==========================================

# ---------- Mission 01: 认知觉醒 ----------
if "Mission 01" in page:
    st.title("肉眼看不到的隐患，我们在数字世界一览无余")
    st.write("请拖动下方滑块，对比传统相机视角与 LiDAR 探测视角。")
    
    swipe = st.slider("左右滑动对比：实拍图 <---> 点云图", 0, 100, 50)
    col_img, col_info = st.columns([2.5, 1])
    
    with col_img:
        if swipe < 50:
            if os.path.exists("before.jpg"):
                st.image("before.jpg", use_container_width=True, caption="传统相机视图：外墙看似完好")
            else:
                st.info("💡 请将外墙照片命名为 `before.jpg` 放在代码同文件夹下。")
        else:
            if os.path.exists("after.jpg"):
                st.image("after.jpg", use_container_width=True, caption="LiDAR 视图：建筑骨架与隐蔽裂缝一目了然")
            else:
                st.info("💡 请将点云照片命名为 `after.jpg` 放在代码同文件夹下。")
    
    with col_info:
        st.markdown("### 📊 降维打击")
        st.metric("传统肉眼漏检率", "15%", "⚠️ 极高隐患")
        st.metric("LiDAR 扫描精度", "1.2mm", "✅ 毫米级直击")
        st.write("---")
        st.success("👉 数据不会撒谎。请进入左侧下一关进行理论武装。")

# ---------- Mission 02: 理论武装 ----------
elif "Mission 02" in page:
    st.title("多回波技术与 AI 分割原理解析")
    
   # 采用前端 iframe 嵌入，并添加 no-referrer 绕过 B 站防盗链机制
    bili_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="referrer" content="no-referrer">
    </head>
    <body style="margin: 0; padding: 0;">
        <iframe src="https://player.bilibili.com/player.html?bvid=BV1dToCBdEiP&page=1&high_quality=1&danmaku=0" 
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" 
        style="width: 100%; height: 450px; border-radius: 10px;">
        </iframe>
    </body>
    </html>
    """
    
    # 渲染这个带有隐身斗篷的 HTML 模块
    components.html(bili_code, height=460)
    
    st.markdown("### 📝 随堂笔记精华")
    with st.expander("▶️ 01:20 - 多回波技术原理解析", expanded=True):
        st.write("激光穿透树叶时，部分光子形成首回波，剩余光子继续前进打在墙体上形成多次/最后回波。这就是我们能给被遮挡的建筑做 CT 的秘密。")
    with st.expander("▶️ 03:45 - 语义分割与 AI 诊断"):
        st.write("通过深度学习算法，让计算机自动区分出哪些点是普通墙面，哪些点是危险的裂缝。")

    st.markdown("---")
    st.markdown("### 🛑 随堂小测验 (通关解锁下一模块)")
    answer = st.radio(
        "**当我们需要透过茂密的行道树探测后方的古建筑墙体时，应该重点提取哪种 LiDAR 数据？**",
        ["A. 仅使用首回波数据", "B. 仅使用最后回波数据", "C. 使用传统的 RGB 彩色相机照片"],
        index=None
    )

    if answer == "B. 仅使用最后回波数据":
        st.success("🎉 回答正确！身份已升级为：**高级工程师 👨‍💻**")
        if not st.session_state.unlocked:
            st.session_state.unlocked = True
            st.session_state.rank = "高级工程师 👨‍💻"
            st.session_state.progress = 66
            st.balloons()
        st.info("🔓 **沙盘权限已解锁！** 请点击左侧进入 Mission 03。")
    elif answer is not None:
        st.error("❌ 答案有误，请参考上方的随堂笔记再试一次！")

# ---------- Mission 03: 实战演习 ----------
elif "Mission 03" in page:
    if not st.session_state.unlocked:
        st.error("🔒 权限不足！请先在【Mission 02】中完成视频学习并通过理论考核，以解锁实战演习权限。")
    else:
        st.title("🏗️ 3D AI 诊断大屏 - 剖面切片分析版")
        
        @st.cache_data
        def get_data():
            np.random.seed(42)
            df = pd.DataFrame({
                'X': np.random.uniform(0, 20, 10000),
                'Y': np.random.normal(0, 0.2, 10000),
                'Z': np.random.uniform(0, 10, 10000),
                'Score': np.random.randint(0, 100, 10000)
            })
            df['Score'] = np.where(np.abs(df.X - (10 + np.sin(df.Z))) < 0.4, df.Score + 40, df.Score)
            return df

        full_df = get_data()

        c1, c2 = st.columns([1, 2.5])
        with c1:
            st.subheader("🛠️ 深度分析终端")
            z_slice = st.slider("📏 Z 轴高度剖面切割 (模拟探地雷达)", 0.0, 10.0, (0.0, 10.0))
            sliced_df = full_df[(full_df.Z >= z_slice[0]) & (full_df.Z <= z_slice[1])]
            
            rate = st.slider("点云渲染精度 (%)", 10, 100, 50)
            current_df = sliced_df.sample(frac=rate/100)
            
            if st.button("🚀 启动 AI 裂缝提取", use_container_width=True, type="primary"):
                with st.spinner("AI 模型计算中..."):
                    time.sleep(0.8)
                st.session_state.is_diagnosed = True
                st.session_state.progress = 90
            
            if st.session_state.is_diagnosed:
                st.markdown("---")
                threshold = st.slider("AI 警报灵敏度", 0, 100, 75, help="调高可过滤掉表面水渍，只抓取深层裂缝。")
                current_df['Status'] = current_df['Score'].apply(lambda s: '🚨 危险裂缝' if s >= threshold else '✅ 正常墙体')
                crack_count = len(current_df[current_df.Status == '🚨 危险裂缝'])
                
                st.metric("检出结构性异常点", f"{crack_count} pts")
                st.info("💡 调节剖面滑块，你可以从建筑横截面观察裂缝的深度走向。")
        
        with c2:
            if st.session_state.is_diagnosed:
                fig = px.scatter_3d(current_df, x='X', y='Y', z='Z', color='Status', 
                                   color_discrete_map={'🚨 危险裂缝': '#FF4B4B', '✅ 正常墙体': '#666666'}, opacity=0.8, height=700)
            else:
                fig = px.scatter_3d(current_df, x='X', y='Y', z='Z', opacity=0.3, height=700)
                fig.update_traces(marker=dict(size=2, color='#888888'))
            
            fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(bgcolor="rgba(0,0,0,0)"))
            st.plotly_chart(fig, use_container_width=True)

# ---------- Mission 04: 终极报告 ----------
elif "Mission 04" in page:
    if not st.session_state.is_diagnosed:
        st.warning("⚠️ 报告尚未生成。请先在【Mission 03】中启动 AI 诊断流程。")
    else:
        st.title("🏁 鉴定完成：建筑结构体检单")
        
        # 使用安全的 Markdown 替代复杂的 HTML 注入，彻底杜绝乱码
        st.markdown("### 📋 自动化检验报告摘要")
        st.info(f"""
        **📑 项目检测标段：** 基于 LiDAR 多回波的墙体病害分析  
        **👨‍💻 执行工程师：** {st.session_state.rank}  
        **📅 系统评估日期：** 2026 赛季  
        
        ---
        * **点云采样覆盖率：** 优
        * **AI 模型置信度：** 96.8%
        * **核心结论：** 🚨 **检出 1 处大型连续性结构裂缝。**
        * **工程建议：** 建议立即安排专业团队进行现场复核，并结合微课视频中的语义分割理论，优化下一步的修复方案。
        """)
            
        st.markdown("---")
        st.success("🎉 恭喜！你已完成本次微课交互系统的全部体验流程，掌握了 AI 与点云技术结合的实战应用。")
        if st.button("归档数据并退出", type="primary"):
            st.session_state.progress = 100
            st.snow()
