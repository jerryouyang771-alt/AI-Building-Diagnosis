import streamlit as st
from streamlit_image_comparison import image_comparison
import pandas as pd
import numpy as np
import plotly.express as px
import time
import os

# ==========================================
# 0. 全局状态与进度管理
# ==========================================
if 'progress' not in st.session_state:
    st.session_state.progress = 25
if 'rank' not in st.session_state:
    st.session_state.rank = "见习检测员 🧑‍🔧"
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False
if 'is_diagnosed' not in st.session_state:
    st.session_state.is_diagnosed = False
if 'active_page' not in st.session_state:
    st.session_state.active_page = "00. 首页"

# 极简且绝对安全的路由切换函数
def nav_to(page_name):
    st.session_state.active_page = page_name

# ==========================================
# 1. 基础配置与安全样式
# ==========================================
st.set_page_config(page_title="AI 建筑诊断系统", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #FF4B4B , #FF9090); }
    .stMetric { background-color: rgba(255, 75, 75, 0.05); border: 1px solid rgba(255, 75, 75, 0.2); border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. 侧边栏：任务控制台 (全宽按钮交互版)
# ==========================================
with st.sidebar:
    st.title("🛰️ 诊断指挥中心")
    st.info(f"**当前身份：** `{st.session_state.rank}`")
    st.progress(st.session_state.progress / 100)
    st.write(f"**系统权限进度：** {st.session_state.progress}%")
    st.markdown("---")
    
    # 🌍 第一篇章
    st.markdown("### 🌍 第一篇章：接入系统")
    st.button(
        "🏠 00. 首页与先导片", 
        use_container_width=True, 
        type="primary" if st.session_state.active_page == "00. 首页" else "secondary",
        on_click=nav_to, args=("00. 首页",)
    )

    # 🛠️ 第二篇章
    st.markdown("### 🛠️ 第二篇章：核心探究")
    st.button(
        "👁️ Mission 01: 认知觉醒", 
        use_container_width=True, 
        type="primary" if st.session_state.active_page == "Mission 01" else "secondary",
        on_click=nav_to, args=("Mission 01",)
    )
    st.button(
        "🎥 Mission 02: 理论武装", 
        use_container_width=True, 
        type="primary" if st.session_state.active_page == "Mission 02" else "secondary",
        on_click=nav_to, args=("Mission 02",)
    )
    
    # 锁定逻辑
    if st.session_state.unlocked:
        st.button(
            "💻 Mission 03: 虚拟实操", 
            use_container_width=True, 
            type="primary" if st.session_state.active_page == "Mission 03" else "secondary",
            on_click=nav_to, args=("Mission 03",)
        )
        st.button(
            "🏁 Mission 04: AI 诊断", 
            use_container_width=True, 
            type="primary" if st.session_state.active_page == "Mission 04" else "secondary",
            on_click=nav_to, args=("Mission 04",)
        )
    else:
        st.button("🔒 Mission 03: 待理论通关解锁", use_container_width=True, disabled=True)
        st.button("🔒 Mission 04: 待实操完成后解锁", use_container_width=True, disabled=True)

    # 🚀 第三篇章
    st.markdown("### 🚀 第三篇章：星辰大海")
    st.button(
        "🌌 Mission 05: 拓展与未来", 
        use_container_width=True, 
        type="primary" if st.session_state.active_page == "Mission 05" else "secondary",
        on_click=nav_to, args=("Mission 05",)
    )

# 提取当前激活的页面
page = st.session_state.active_page

# ==========================================
# 3. 主页面渲染逻辑
# ==========================================

# ---------- 00. 首页与先导片 ----------
if page == "00. 首页":
    if os.path.exists("banner.jpg"):
        st.image("banner.jpg", use_container_width=True)
    else:
        st.warning("🖼️ 提示：请在文件夹中放入一张名为 `banner.jpg` 的长图作为头图。")
        
    st.title("欢迎接入“AI之眼”数字文化遗产保护系统")
    st.markdown("#### —— 配合《多回波 LiDAR 与 AI 语义分割》微课程专属实操平台")
    
    st.info("""
    **👋 同学你好，欢迎来到微观的数字世界！**
    
    在肉眼看不见的地方，岁月正在悄悄侵蚀我们的历史建筑。今天，你将化身为一名**数字保护工程师**。
    在这里，我们将结合武汉大学真实的雷达扫描数据，运用你在微课中学到的知识，揪出隐藏在墙体内部的结构性隐患。
    """)
    
    st.markdown("---")
    st.markdown("### 🎬 系统先导片 (微课原片)")
    st.write("在开始硬核探究之前，别忘了通过复习我们团队制作的微课视频来了解本次任务的背景原理哦：")
    
    st.markdown("""
        <iframe src="//player.bilibili.com/player.html?bvid=BV1dToCBdEiP&page=1&high_quality=1&danmaku=0" 
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" 
        style="width:100%; height:450px; border-radius: 10px;">
        </iframe>
        """, unsafe_allow_html=True)

# ---------- Mission 01: 认知觉醒 ----------
elif page == "Mission 01":
    st.title("肉眼看不到的隐患，我们在数字世界一览无余")
    
    # 【改动1】：增强 Mission 01 的保姆级指示语和情境引入
    st.info("""
    🎯 **任务目标**：了解 LiDAR（激光雷达）如何突破肉眼和传统相机的局限，发现建筑表层下隐藏的结构性病害。  
    💡 **操作指南**：请**按住并在左右拖动**下方的分割线。左侧代表传统可见光相机的常规视觉，右侧代表 LiDAR 多回波穿透后的微观点云视觉。观察同一面墙体在不同视角下的巨大差异！
    """)

    col_img, col_info = st.columns([2, 1])
    
    with col_img:
        image_comparison(
            img1="before.jpg",
            img2="after.jpg",
            label1="常规视觉 (被掩盖的真相)",
            label2="LiDAR 穿透 (结构性裂缝)",
            width=700,
            starting_position=50,
            show_labels=True,
            make_responsive=True,
            in_memory=True
        )
        
    with col_info:
        st.markdown("### 📊 降维打击")
        st.metric("传统肉眼漏检率", "15%", "⚠️ 极高隐患")
        st.metric("LiDAR 扫描精度", "1.2mm", "✅ 毫米级直击")
        st.write("---")
        # 增加了一个直接跳转到下一关的快捷按钮
        st.write("👉 数据不会撒谎。请进入下一关进行理论武装。")
        st.button("🚀 前往 Mission 02: 理论武装", type="primary", on_click=nav_to, args=("Mission 02",))
        
# ---------- Mission 02: 理论武装 ----------
elif page == "Mission 02":
    st.title("多回波技术与 AI 分割原理解析")
    
    st.info("💡 **实操受阻？理论告急？** \n\n 请点击左侧菜单回到 **【🏠 00. 首页与先导片】**，重新回顾咱们团队制作的微课主视频，复习 LiDAR 的多次回波与 AI 语义分割原理后再来进行测验！")
    
    st.markdown("### 📝 随堂笔记精华")
    with st.expander("▶️ 核心原理回顾 - 多回波技术", expanded=True):
        st.write("激光穿透树叶时，部分光子形成首回波，剩余光子继续前进打在墙体上形成多次/最后回波。这就是我们能给被遮挡的建筑做 CT 的秘密。")
    with st.expander("▶️ 核心原理回顾 - 语义分割"):
        st.write("通过深度学习算法，让计算机自动区分出哪些点是普通墙面，哪些点是危险的裂缝。")

    st.markdown("---")
    st.markdown("### 🛑 工程师资格认证 (需全对以解锁沙盘)")
    st.write("请结合所学知识，完成以下三项研判测试：")

    st.markdown("#### 1️⃣ 穿透障碍物的数据提取")
    q1 = st.radio(
        "当我们需要透过茂密的行道树探测后方的古建筑墙体时，应该重点提取哪种 LiDAR 数据？",
        ["A. 仅使用首回波数据", "B. 仅使用最后回波数据", "C. 使用传统的 RGB 彩色相机照片"],
        index=None,
        key="q1"
    )

    st.markdown("#### 2️⃣ AI 语义分割的核心作用")
    q2 = st.radio(
        "在我们的数字诊断系统中，引入深度学习（AI）的主要目的是什么？",
        ["A. 让网页运行得更快", "B. 自动生成建筑的美化渲染图", "C. 自动识别并分类点云，将危险裂缝从普通墙体中“揪出”"],
        index=None,
        key="q2"
    )

    st.markdown("#### 3️⃣ LiDAR 技术的降维打击点")
    q3 = st.radio(
        "相比传统的人工肉眼巡检，LiDAR（激光雷达）技术在结构检测上最大的优势在于？",
        ["A. 具有极高的色彩还原度", "B. 纯粹为了增加项目的科技感", "C. 能实现不受光照影响的毫米级精度扫描，并获取三维空间坐标"],
        index=None,
        key="q3"
    )

    st.markdown("---")
    if q1 and q2 and q3:
        if q1.startswith("B") and q2.startswith("C") and q3.startswith("C"):
            st.success("🎉 全回答正确！理论知识满分！")
            if not st.session_state.unlocked:
                st.session_state.unlocked = True
                st.session_state.rank = "高级工程师 👨‍💻"
                st.session_state.progress = 66
                st.balloons()
            
            # 【改动2】：通关后直接出现一键跳转按钮，彻底解决刷新Bug
            st.info("🔓 **沙盘权限已彻底解锁！**")
            st.button("🚀 立即进入 Mission 03: 虚拟实操", use_container_width=True, type="primary", on_click=nav_to, args=("Mission 03",))
        else:
            st.error("❌ 哎呀，有题目答错了哦。请再次核对随堂笔记，或回首页复习视频！")

# ---------- Mission 03: 实战演习 ----------
elif page == "Mission 03":
    if not st.session_state.unlocked:
        st.error("🔒 权限不足！请先在【Mission 02】中完成理论考核，以解锁实战演习权限。")
        st.button("🔙 返回 Mission 02", on_click=nav_to, args=("Mission 02",))
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
                st.warning("👨‍🏫 **实操指引：** 请拖动下方【警报灵敏度】滑块至 100，观察 AI 算法如何精准提取肉眼无法分辨的结构性裂缝！")
                threshold = st.slider("AI 警报灵敏度", 0, 100, 75, help="调高可过滤掉表面水渍，只抓取深层裂缝。")
                current_df['Status'] = current_df['Score'].apply(lambda s: '🚨 危险裂缝' if s >= threshold else '✅ 正常墙体')
                crack_count = len(current_df[current_df.Status == '🚨 危险裂缝'])
                
                st.metric("检出结构性异常点", f"{crack_count} pts")
                st.info("💡 调节上方剖面滑块，你可以从建筑横截面观察裂缝的深度走向。")
                
                # 诊断完成后，底部出现生成报告的按钮
                st.markdown("---")
                st.button("📝 生成终极诊断报告", use_container_width=True, on_click=nav_to, args=("Mission 04",))
        
        with c2:
            if st.session_state.is_diagnosed:
                fig = px.scatter_3d(current_df, x='X', y='Y', z='Z', color='Status', 
                                   color_discrete_map={'🚨 危险裂缝': '#FF4B4B', '✅ 正常墙体': '#666666'}, opacity=0.8, height=700)
            else:
                fig = px.scatter_3d(current_df, x='X', y='Y', z='Z', opacity=0.3, height=700)
                fig.update_traces(marker=dict(size=2, color='#888888'))
            
            fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(bgcolor="rgba(0,0,0,0)"))
            st.plotly_chart(fig, use_container_width=True)

# ---------- Mission 04: AI 诊断 ----------
elif page == "Mission 04":
    if not st.session_state.is_diagnosed:
        st.warning("⚠️ 报告尚未生成。请先在【Mission 03】中启动 AI 诊断流程。")
        st.button("🔙 返回 Mission 03", on_click=nav_to, args=("Mission 03",))
    else:
        st.title("🏁 鉴定完成：建筑结构体检单")
        
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
        st.success("🎉 恭喜！你已完成核心勘测任务。请进入最后一个模块，看看这项技术的星辰大海。")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 归档数据并结束", use_container_width=True):
                st.session_state.progress = 100
                st.snow()
        with col2:
            st.button("🌌 探索更多技术应用 (拓展)", use_container_width=True, type="primary", on_click=nav_to, args=("Mission 05",))

# ---------- Mission 05: 拓展与未来 ----------
elif page == "Mission 05":
    st.title("🌌 星辰大海：不止于裂缝，洞见被折叠的文明与未来")
    st.write("在科技的赋能下，LiDAR 与 AI 的结合，不仅能保护脆弱的历史遗产，更在现代工业和复杂基建中发挥着“火眼金睛”的作用。")
    
    st.markdown("### 🏛️ 案例：拨开雨林，重构玛雅古城")
    st.write("考古学家曾认为玛雅遗址已经被茂密的热带雨林彻底吞噬。但在多回波 LiDAR 的“X光”扫射下，算法自动剥离了上亿棵树木的数据点，让一座沉睡千年的宏伟古城骨架直接显现在屏幕上。")
    
    if os.path.exists("expand_before.jpg") and os.path.exists("expand_after.jpg"):
        image_comparison(
            img1="expand_before.jpg",
            img2="expand_after.jpg",
            label1="茂密的雨林地表",
            label2="褪去植被后的城市骨架",
            width=800,
            starting_position=30,
            show_labels=True,
            make_responsive=True,
            in_memory=True
        )
    else:
        st.warning("🖼️ 提示：请放入 `expand_before.jpg` 和 `expand_after.jpg` 以激活此处的交互透视效果。")
        
    st.markdown("---")
    st.markdown("### 🌉 深入现代基建与工业质检")
    
    # 【改动3】：将拓展模块升级为两行两列，加入工业检测内容，格局拉满
    c1, c2 = st.columns(2)
    with c1:
        if os.path.exists("expand_1.jpg"):
            st.image("expand_1.jpg", use_container_width=True)
        st.info("**跨海大桥的毫米级体检**\n\n受风浪影响，跨海大桥的底部和桥墩极难进行人工巡检。搭载 LiDAR 的无人机可以定期扫描桥体应变，预防灾难性坍塌。")
        
    with c2:
        if os.path.exists("expand_4.jpg"):
            st.image("expand_4.jpg", use_container_width=True)
        st.error("**工业设施高危病害排查**\n\n在核电站冷却塔、大型风电叶片、超高压输电塔等极端工业场景下，三维点云提取裂缝技术能实现全自动非接触式安全巡检，将工业事故扼杀在摇篮中。")

    st.markdown("<br>", unsafe_allow_html=True) # 增加点行距

    c3, c4 = st.columns(2)
    with c3:
        if os.path.exists("expand_2.jpg"):
            st.image("expand_2.jpg", use_container_width=True)
        st.success("**古建木构件的无损拆解**\n\n面对极其复杂的古建，不开一枪一炮，在数字世界里彻底透视内部的榫卯结构，完成数字存档和修复指导。")
        
    with c4:
        if os.path.exists("expand_3.jpg"):
            st.image("expand_3.jpg", use_container_width=True)
        st.warning("**灾区救援的三维重建**\n\n地震后，快速飞过灾区上空生成废墟高精度三维模型，智能识别出结构仍稳定的“生命三角区”，指导救援通道开挖。")
        
    st.markdown("---")
    st.markdown("<h4 style='text-align: center; color: gray;'>科技不仅能让被掩盖的文明重见天日，更能守护现代社会的安全命脉。</h4>", unsafe_allow_html=True)
